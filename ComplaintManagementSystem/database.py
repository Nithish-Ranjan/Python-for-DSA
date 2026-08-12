import sqlite3
from pathlib import Path
from datetime import datetime, timedelta
import uuid


class DatabaseManager:
    """Owns SQLite persistence; callers receive dictionaries, never raw cursors."""
    def __init__(self, db_path=None):
        self.db_path = Path(db_path or Path(__file__).parent / "database" / "complaint.db")
        self.db_path.parent.mkdir(exist_ok=True)
        self._initialize()

    def _connect(self):
        conn = sqlite3.connect(self.db_path); conn.row_factory = sqlite3.Row; return conn

    def _initialize(self):
        with self._connect() as c:
            c.executescript('''
            CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT, name TEXT, role TEXT, email TEXT);
            CREATE TABLE IF NOT EXISTS departments (id INTEGER PRIMARY KEY, name TEXT UNIQUE, contact TEXT);
            CREATE TABLE IF NOT EXISTS technicians (id INTEGER PRIMARY KEY, name TEXT UNIQUE, email TEXT, specialty TEXT, active INTEGER DEFAULT 1);
            CREATE TABLE IF NOT EXISTS complaints (
              id TEXT PRIMARY KEY, student_name TEXT, usn TEXT, department TEXT, category TEXT, title TEXT, description TEXT, location TEXT,
              date TEXT, status TEXT, priority TEXT, technician TEXT, expected_time TEXT, remarks TEXT, resolved_at TEXT);
            CREATE TABLE IF NOT EXISTS complaint_history (id INTEGER PRIMARY KEY, complaint_id TEXT, action TEXT, actor TEXT, timestamp TEXT);
            CREATE TABLE IF NOT EXISTS activity_logs (id INTEGER PRIMARY KEY, message TEXT, timestamp TEXT);
            ''')
            if not c.execute("SELECT 1 FROM users LIMIT 1").fetchone(): self._seed(c)

    def _seed(self, c):
        c.executemany("INSERT INTO users(username,password,name,role,email) VALUES(?,?,?,?,?)", [
            ("admin", "admin123", "System Administrator", "Admin", "admin@campus.edu"),
            ("tech1", "tech123", "Arun Kumar", "Technician", "arun@campus.edu")])
        c.executemany("INSERT INTO departments(name,contact) VALUES(?,?)", [(x, "Campus Office") for x in ["Electrical", "IT", "Maintenance", "Housekeeping", "Administration"]])
        c.executemany("INSERT INTO technicians(name,email,specialty) VALUES(?,?,?)", [
            ("Arun Kumar", "arun@campus.edu", "Electrical"), ("Priya Shah", "priya@campus.edu", "IT / Network"), ("Ravi Das", "ravi@campus.edu", "Maintenance")])
        today = datetime.now()
        samples = [("Water leakage near exposed wire", "There is water leakage in hostel block A and electricity is exposed.", "Electrical", "Maintenance", "Critical", "Arun Kumar", "Hostel Block A", "Immediate"),
                   ("WiFi slow in CSE Lab", "Internet is very slow during lab sessions.", "IT", "Network", "Medium", "Priya Shah", "CSE Lab 2", "24 hours"),
                   ("Broken classroom projector", "Projector is flickering and not usable.", "Maintenance", "Equipment", "High", "Ravi Das", "Room 301", "8 hours"),
                   ("Cleaning needed", "Corridor needs cleaning.", "Housekeeping", "Cleaning", "Low", "Unassigned", "Block C", "48 hours")]
        for i, s in enumerate(samples):
            c.execute("INSERT INTO complaints VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (str(uuid.uuid4())[:8].upper(), f"Student {i+1}", f"1CS2{i:03}", s[2], s[3], s[0], s[1], s[6], (today-timedelta(days=i*3)).isoformat(timespec='seconds'), "Pending" if i != 2 else "Resolved", s[4], s[5], s[7], "", (today-timedelta(days=1)).isoformat() if i == 2 else None))
        self.log("Sample data created", c)

    def authenticate(self, username, password):
        with self._connect() as c:
            row = c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password)).fetchone()
            return dict(row) if row else None

    def log(self, message, conn=None):
        target = conn or self._connect(); target.execute("INSERT INTO activity_logs(message,timestamp) VALUES(?,?)", (message, datetime.now().isoformat(timespec='seconds')))
        if conn is None: target.commit(); target.close()

    def get_complaints(self, search="", filters=None, technician_only=None):
        filters = filters or {}; sql, params = "SELECT * FROM complaints WHERE 1=1", []
        if technician_only: sql += " AND technician=?"; params.append(technician_only)
        if search:
            sql += " AND (id LIKE ? OR student_name LIKE ? OR usn LIKE ? OR department LIKE ? OR category LIKE ? OR technician LIKE ? OR status LIKE ?)"; params += [f"%{search}%"]*7
        for field in ("priority", "status", "department", "category"):
            value = filters.get(field)
            if value and value != "All": sql += f" AND {field}=?"; params.append(value)
        sql += " ORDER BY CASE priority WHEN 'Critical' THEN 1 WHEN 'High' THEN 2 WHEN 'Medium' THEN 3 ELSE 4 END, date DESC"
        with self._connect() as c: return [dict(x) for x in c.execute(sql, params).fetchall()]

    def add_complaint(self, data, actor="Admin"):
        record = {**data, "id": str(uuid.uuid4())[:8].upper(), "date": datetime.now().isoformat(timespec="seconds"), "status": data.get("status", "Pending"), "technician": data.get("technician", "Unassigned"), "remarks": data.get("remarks", ""), "resolved_at": None}
        fields = ["id","student_name","usn","department","category","title","description","location","date","status","priority","technician","expected_time","remarks","resolved_at"]
        with self._connect() as c:
            c.execute(f"INSERT INTO complaints({','.join(fields)}) VALUES({','.join('?'*len(fields))})", [record[x] for x in fields]); self._history(c, record['id'], "Complaint created", actor); self.log(f"Complaint {record['id']} created", c)
        return record["id"]

    def update_complaint(self, complaint_id, changes, actor="Admin"):
        allowed = {k:v for k,v in changes.items() if k in {"student_name","usn","department","category","title","description","location","status","priority","technician","expected_time","remarks"}}
        if changes.get("status") == "Resolved": allowed["resolved_at"] = datetime.now().isoformat(timespec="seconds")
        if not allowed: return
        with self._connect() as c:
            c.execute("UPDATE complaints SET " + ",".join(f"{x}=?" for x in allowed) + " WHERE id=?", [*allowed.values(), complaint_id]); self._history(c, complaint_id, "Updated: " + ", ".join(allowed), actor); self.log(f"Complaint {complaint_id} updated", c)

    def delete_complaint(self, complaint_id):
        with self._connect() as c:
            row=c.execute("SELECT * FROM complaints WHERE id=?", (complaint_id,)).fetchone(); c.execute("DELETE FROM complaints WHERE id=?", (complaint_id,)); self.log(f"Complaint {complaint_id} deleted", c); return dict(row) if row else None

    def _history(self, c, cid, action, actor): c.execute("INSERT INTO complaint_history(complaint_id,action,actor,timestamp) VALUES(?,?,?,?)", (cid,action,actor,datetime.now().isoformat(timespec="seconds")))
    def history(self, cid):
        with self._connect() as c: return [dict(x) for x in c.execute("SELECT * FROM complaint_history WHERE complaint_id=? ORDER BY timestamp DESC", (cid,))]
    def technicians(self):
        with self._connect() as c: return [dict(x) for x in c.execute("SELECT * FROM technicians WHERE active=1 ORDER BY name")]
    def categories(self): return ["Maintenance", "Network", "Equipment", "Cleaning", "Medical", "Safety", "Other"]
    def departments(self):
        with self._connect() as c: return [x[0] for x in c.execute("SELECT name FROM departments ORDER BY name")]
    def backup(self, destination):
        import shutil; shutil.copy2(self.db_path, destination)
