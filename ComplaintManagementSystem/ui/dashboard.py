import customtkinter as ctk
from tkinter import ttk, messagebox, filedialog
from collections import Counter
import shutil

from .theme import COLORS, button_kwargs, configure_treeview, option_menu_kwargs


class ApplicationFrame(ctk.CTkFrame):
    NAV = [("Overview", "Dashboard"), ("Requests", "Complaints"), ("People", "Technicians"), ("Insights", "Reports"), ("Preferences", "Settings")]

    def __init__(self, master, user, manager, database, analyzer, reporter):
        super().__init__(master, corner_radius=0, fg_color=COLORS["cream"])
        self.user, self.manager, self.db = user, manager, database
        self.analyzer, self.reporter, self.current = analyzer, reporter, None
        self.nav_buttons = {}
        self.grid_columnconfigure(1, weight=1); self.grid_rowconfigure(0, weight=1)
        configure_treeview(); self._build_sidebar(); self.show("Dashboard")

    def _build_sidebar(self):
        bar = ctk.CTkFrame(self, width=238, corner_radius=0, fg_color=COLORS["sidebar"])
        bar.grid(row=0, column=0, sticky="nsew"); bar.grid_propagate(False)
        ctk.CTkLabel(bar, text="SC", width=42, height=42, corner_radius=12, fg_color=COLORS["terracotta"], font=ctk.CTkFont(size=17, weight="bold")).pack(anchor="w", padx=24, pady=(30, 10))
        ctk.CTkLabel(bar, text="Smart Complaints", font=ctk.CTkFont(size=19, weight="bold"), text_color="#FFF7EF").pack(anchor="w", padx=24)
        ctk.CTkLabel(bar, text="CAMPUS OPERATIONS", font=ctk.CTkFont(size=10, weight="bold"), text_color="#CFAE96").pack(anchor="w", padx=24, pady=(3, 28))
        for label, name in self.NAV:
            if self.user["role"] == "Technician" and name in ("Reports", "Settings"): continue
            button = ctk.CTkButton(bar, text=label, anchor="w", height=42, fg_color="transparent", hover_color=COLORS["sidebar_hover"], text_color="#F7E9DE", corner_radius=10, command=lambda n=name: self.show(n))
            button.pack(fill="x", padx=14, pady=3)
            self.nav_buttons[name] = button
        identity = ctk.CTkFrame(bar, fg_color="#4C2F20", corner_radius=14)
        identity.pack(side="bottom", fill="x", padx=16, pady=20)
        ctk.CTkLabel(identity, text=self.user["name"], font=ctk.CTkFont(size=13, weight="bold"), text_color="#FFF7EF").pack(anchor="w", padx=14, pady=(12, 1))
        ctk.CTkLabel(identity, text=self.user["role"], text_color="#DABDA7").pack(anchor="w", padx=14, pady=(0, 12))

    def _clear(self):
        if self.current: self.current.destroy()
        self.current = ctk.CTkFrame(self, fg_color="transparent")
        self.current.grid(row=0, column=1, sticky="nsew", padx=34, pady=28)
        self.current.grid_columnconfigure(0, weight=1)

    def show(self, page):
        for name, button in self.nav_buttons.items():
            active = name == page
            button.configure(fg_color=COLORS["terracotta"] if active else "transparent", hover_color=COLORS["terracotta_hover"] if active else COLORS["sidebar_hover"])
        self._clear(); getattr(self, f"_show_{page.lower()}")()

    def _title(self, title, subtitle=""):
        top = ctk.CTkFrame(self.current, fg_color="transparent"); top.grid(row=0, column=0, sticky="ew", pady=(0, 20)); top.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(top, text=title, font=ctk.CTkFont(size=30, weight="bold"), text_color=COLORS["ink"]).grid(row=0, column=0, sticky="w")
        ctk.CTkLabel(top, text=subtitle, text_color=COLORS["muted"], font=ctk.CTkFont(size=13)).grid(row=1, column=0, sticky="w", pady=(3, 0))
        return top

    def _card(self, parent, title, value, accent):
        card = ctk.CTkFrame(parent, fg_color=COLORS["surface"], corner_radius=16, border_width=1, border_color=COLORS["border"])
        ctk.CTkFrame(card, height=4, fg_color=accent, corner_radius=4).pack(fill="x", padx=15, pady=(14, 10))
        ctk.CTkLabel(card, text=title.upper(), text_color=COLORS["muted"], font=ctk.CTkFont(size=10, weight="bold")).pack(anchor="w", padx=18)
        ctk.CTkLabel(card, text=str(value), text_color=COLORS["ink"], font=ctk.CTkFont(size=29, weight="bold")).pack(anchor="w", padx=18, pady=(2, 16))
        return card

    def _show_dashboard(self):
        self._title("Good day, " + self.user["name"].split()[0], "Here is the latest picture across your service requests.")
        rows = self.db.get_complaints(technician_only=self.user["name"] if self.user["role"] == "Technician" else None)
        counts, priorities = Counter(r["status"] for r in rows), Counter(r["priority"] for r in rows)
        grid = ctk.CTkFrame(self.current, fg_color="transparent"); grid.grid(row=1, column=0, sticky="ew"); [grid.grid_columnconfigure(i, weight=1) for i in range(4)]
        cards = [("All requests", len(rows), COLORS["terracotta"]), ("Awaiting action", counts["Pending"], COLORS["gold"]), ("In progress", counts["In Progress"], "#7896A6"), ("Resolved", counts["Resolved"], COLORS["sage"])]
        for i, item in enumerate(cards): self._card(grid, *item).grid(row=0, column=i, sticky="ew", padx=5)
        urgency = ctk.CTkFrame(self.current, fg_color="#F9E5D7", corner_radius=16)
        urgency.grid(row=2, column=0, sticky="ew", pady=(20, 10)); urgency.grid_columnconfigure(0, weight=1)
        urgent = self.manager.queue.next_urgent()
        ctk.CTkLabel(urgency, text="NEXT UP", text_color=COLORS["terracotta"], font=ctk.CTkFont(size=10, weight="bold")).grid(row=0, column=0, sticky="w", padx=20, pady=(14, 2))
        ctk.CTkLabel(urgency, text=(urgent["title"] if urgent else "Your priority queue is clear"), text_color=COLORS["ink"], font=ctk.CTkFont(size=16, weight="bold")).grid(row=1, column=0, sticky="w", padx=20, pady=(0, 14))
        ctk.CTkLabel(urgency, text=("Review request " + str(urgent["id"]) if urgent else "No pending requests need immediate action."), text_color=COLORS["muted"]).grid(row=1, column=1, sticky="e", padx=20)
        section = ctk.CTkFrame(self.current, fg_color=COLORS["surface"], corner_radius=18, border_width=1, border_color=COLORS["border"])
        section.grid(row=3, column=0, sticky="nsew", pady=(0, 20)); self.current.grid_rowconfigure(3, weight=1); section.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(section, text="Priority queue", font=ctk.CTkFont(size=18, weight="bold"), text_color=COLORS["ink"]).grid(row=0, column=0, sticky="w", padx=22, pady=(19, 2))
        ctk.CTkLabel(section, text="The requests that need attention first", text_color=COLORS["muted"]).grid(row=1, column=0, sticky="w", padx=22, pady=(0, 12))
        if rows:
            for i, row in enumerate(rows[:6], 2):
                item = ctk.CTkFrame(section, fg_color=COLORS["cream"], corner_radius=10)
                item.grid(row=i, column=0, sticky="ew", padx=18, pady=3); item.grid_columnconfigure(1, weight=1)
                priority_color = {"Critical": COLORS["rose"], "High": COLORS["terracotta"], "Medium": COLORS["gold"], "Low": COLORS["sage"]}.get(row["priority"], COLORS["muted"])
                ctk.CTkLabel(item, text=row["priority"].upper(), text_color=priority_color, font=ctk.CTkFont(size=10, weight="bold"), width=70).grid(row=0, column=0, padx=(12, 6), pady=11)
                ctk.CTkLabel(item, text=row["title"], text_color=COLORS["ink"], anchor="w").grid(row=0, column=1, sticky="ew")
                ctk.CTkLabel(item, text=row["status"], text_color=COLORS["muted"]).grid(row=0, column=2, padx=12)
        else:
            ctk.CTkLabel(section, text="No requests to prioritise yet.", text_color=COLORS["muted"]).grid(row=2, column=0, sticky="w", padx=22, pady=22)

    def _show_complaints(self):
        top = self._title("Requests", "Search, filter and manage every service request.")
        if self.user["role"] == "Admin": ctk.CTkButton(top, text="New request", command=lambda: self._dialog(), **button_kwargs()).grid(row=0, column=1, rowspan=2, padx=5)
        ctk.CTkButton(top, text="Undo", width=76, command=self._undo, **button_kwargs("secondary")).grid(row=0, column=2, rowspan=2, padx=5)
        controls = ctk.CTkFrame(self.current, fg_color=COLORS["surface"], corner_radius=14, border_width=1, border_color=COLORS["border"]); controls.grid(row=1, column=0, sticky="ew", pady=(0, 12)); controls.grid_columnconfigure(0, weight=1)
        self.search = ctk.CTkEntry(controls, placeholder_text="Search by request, department, category, technician or status", height=38, fg_color=COLORS["cream"], border_color=COLORS["border"], text_color=COLORS["ink"]); self.search.grid(row=0, column=0, sticky="ew", padx=12, pady=11); self.search.bind("<KeyRelease>", lambda _: self._load_table())
        self.filter_priority = ctk.CTkOptionMenu(controls, values=["All", "Critical", "High", "Medium", "Low"], command=lambda _: self._load_table(), **option_menu_kwargs()); self.filter_priority.grid(row=0, column=1, padx=4)
        self.filter_status = ctk.CTkOptionMenu(controls, values=["All", "Pending", "In Progress", "Resolved"], command=lambda _: self._load_table(), **option_menu_kwargs()); self.filter_status.grid(row=0, column=2, padx=(4, 12))
        wrap = ctk.CTkFrame(self.current, fg_color=COLORS["surface"], corner_radius=16, border_width=1, border_color=COLORS["border"]); wrap.grid(row=2, column=0, sticky="nsew"); self.current.grid_rowconfigure(2, weight=1)
        cols = ("id", "title", "department", "priority", "status", "technician", "date"); self.tree = ttk.Treeview(wrap, columns=cols, show="headings", height=16, style="Warm.Treeview")
        for col, width in zip(cols, [82, 250, 110, 75, 110, 125, 125]): self.tree.heading(col, text=col.replace("_", " ").title()); self.tree.column(col, width=width, anchor="w")
        self.tree.pack(fill="both", expand=True, padx=8, pady=8); self.tree.bind("<Double-1>", lambda _: self._edit_selected())
        actions = ctk.CTkFrame(self.current, fg_color="transparent"); actions.grid(row=3, column=0, sticky="w", pady=12)
        for label, command, kind in [("View / edit", self._edit_selected, "secondary"), ("Assign", self._assign, "secondary"), ("Resolve", self._resolve, "primary"), ("Delete", self._delete, "danger")]:
            if self.user["role"] == "Admin" or label in ("View / edit", "Resolve"): ctk.CTkButton(actions, text=label, width=104, command=command, **button_kwargs(kind)).pack(side="left", padx=(0, 6))
        self._load_table()

    def _load_table(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        filters = {"priority": self.filter_priority.get(), "status": self.filter_status.get()}
        rows = self.db.get_complaints(self.search.get(), filters, self.user["name"] if self.user["role"] == "Technician" else None); self._rows = {r["id"]: r for r in rows}
        for r in rows: self.tree.insert("", "end", iid=r["id"], values=tuple(r[x] for x in ("id", "title", "department", "priority", "status", "technician", "date")))

    def _selected(self):
        selected = self.tree.selection(); return self._rows.get(selected[0]) if selected else None

    def _dialog(self, row=None):
        row = row or {}; win = ctk.CTkToplevel(self); win.title("Request details"); win.geometry("760x650"); win.configure(fg_color=COLORS["cream"]); win.grab_set(); win.grid_columnconfigure(1, weight=1)
        fields = [("student_name", "Student name"), ("usn", "USN"), ("title", "Request title"), ("location", "Location"), ("department", "Department"), ("category", "Category"), ("priority", "Priority"), ("expected_time", "Expected resolution"), ("technician", "Assigned technician"), ("status", "Status"), ("description", "Description"), ("remarks", "Remarks")]; entries = {}
        choices = {"department": self.db.departments(), "category": self.db.categories(), "priority": ["Critical", "High", "Medium", "Low"], "technician": ["Unassigned"] + [x["name"] for x in self.db.technicians()], "status": ["Pending", "In Progress", "Resolved"]}
        for i, (key, label) in enumerate(fields):
            ctk.CTkLabel(win, text=label, text_color=COLORS["ink"]).grid(row=i, column=0, sticky="w", padx=24, pady=6)
            if key in choices:
                widget = ctk.CTkOptionMenu(win, values=choices[key], **option_menu_kwargs()); widget.set(row.get(key, choices[key][0]))
            elif key in ("description", "remarks"):
                widget = ctk.CTkTextbox(win, height=48, fg_color=COLORS["surface"], border_width=1, border_color=COLORS["border"], text_color=COLORS["ink"]); widget.insert("1.0", row.get(key, ""))
            else:
                widget = ctk.CTkEntry(win, fg_color=COLORS["surface"], border_color=COLORS["border"], text_color=COLORS["ink"]); widget.insert(0, row.get(key, ""))
            widget.grid(row=i, column=1, sticky="ew", padx=24, pady=6); entries[key] = widget
        def save():
            data = {k: (w.get("1.0", "end").strip() if isinstance(w, ctk.CTkTextbox) else w.get()) for k, w in entries.items()}
            if not data["title"]: messagebox.showwarning("Required", "A title is required."); return
            if row: self.manager.update(row["id"], data, self.user["name"])
            else: self.manager.create(data, self.user["name"])
            win.destroy(); self._load_table()
        ctk.CTkButton(win, text="Save request", command=save, **button_kwargs()).grid(row=len(fields), column=1, sticky="e", padx=24, pady=18)

    def _edit_selected(self):
        row = self._selected()
        if row: self._dialog(row)
        else: messagebox.showinfo("Select request", "Select a request first.")
    def _assign(self):
        row = self._selected()
        if not row: return
        name = ctk.CTkInputDialog(text="Enter technician name:\n" + ", ".join(x["name"] for x in self.db.technicians()), title="Assign technician").get_input()
        if name: self.manager.update(row["id"], {"technician": name, "status": "In Progress"}, self.user["name"]); self._load_table()
    def _resolve(self):
        row = self._selected()
        if row: self.manager.update(row["id"], {"status": "Resolved"}, self.user["name"]); self._load_table()
    def _delete(self):
        row = self._selected()
        if row and messagebox.askyesno("Delete request", "Delete this request? You can undo immediately."): self.manager.delete(row["id"]); self._load_table()
    def _undo(self):
        if self.manager.undo(self.user["name"]): self._load_table()
        else: messagebox.showinfo("Undo", "There is no recent action to undo.")

    def _show_technicians(self):
        self._title("People & workload", "A clear view of capacity, ownership and service performance.")
        rows, techs = self.db.get_complaints(), self.db.technicians()
        total_active = sum(r["status"] != "Resolved" and r["technician"] != "Unassigned" for r in rows)
        total_resolved = sum(r["status"] == "Resolved" for r in rows)
        summary = ctk.CTkFrame(self.current, fg_color="transparent")
        summary.grid(row=1, column=0, sticky="ew", pady=(0, 18))
        for index in range(3): summary.grid_columnconfigure(index, weight=1)
        for index, item in enumerate((("Team members", len(techs), COLORS["terracotta"]), ("Active assignments", total_active, COLORS["gold"]), ("Requests resolved", total_resolved, COLORS["sage"]))):
            self._card(summary, *item).grid(row=0, column=index, sticky="ew", padx=5)

        frame = ctk.CTkFrame(self.current, fg_color="transparent")
        frame.grid(row=2, column=0, sticky="nsew"); self.current.grid_rowconfigure(2, weight=1)
        frame.grid_columnconfigure(0, weight=1); frame.grid_columnconfigure(1, weight=1)
        for index, tech in enumerate(techs):
            assigned = [row for row in rows if row["technician"] == tech["name"]]
            active = sum(row["status"] != "Resolved" for row in assigned)
            resolved = sum(row["status"] == "Resolved" for row in assigned)
            resolution_rate = round((resolved / len(assigned)) * 100) if assigned else 0
            load_label, load_color = ("Available", COLORS["sage"]) if active == 0 else (("Balanced", COLORS["gold"]) if active < 4 else ("At capacity", COLORS["rose"]))
            card = ctk.CTkFrame(frame, fg_color=COLORS["surface"], corner_radius=18, border_width=1, border_color=COLORS["border"])
            card.grid(row=index // 2, column=index % 2, sticky="nsew", padx=6, pady=6)
            card.grid_columnconfigure(0, weight=1)
            top = ctk.CTkFrame(card, fg_color="transparent"); top.grid(row=0, column=0, sticky="ew", padx=20, pady=(18, 3)); top.grid_columnconfigure(0, weight=1)
            ctk.CTkLabel(top, text=tech["name"], font=ctk.CTkFont(size=18, weight="bold"), text_color=COLORS["ink"]).grid(row=0, column=0, sticky="w")
            ctk.CTkLabel(top, text=load_label.upper(), text_color=load_color, font=ctk.CTkFont(size=10, weight="bold")).grid(row=0, column=1, sticky="e")
            ctk.CTkLabel(card, text=tech["specialty"], text_color=COLORS["terracotta"], font=ctk.CTkFont(size=12, weight="bold")).grid(row=1, column=0, sticky="w", padx=20)
            ctk.CTkLabel(card, text=tech["email"], text_color=COLORS["muted"], font=ctk.CTkFont(size=12)).grid(row=2, column=0, sticky="w", padx=20, pady=(2, 15))
            metrics = ctk.CTkFrame(card, fg_color=COLORS["cream"], corner_radius=12); metrics.grid(row=3, column=0, sticky="ew", padx=18); metrics.grid_columnconfigure((0, 1, 2), weight=1)
            for metric_index, (value, label) in enumerate(((active, "ACTIVE"), (resolved, "RESOLVED"), (f"{resolution_rate}%", "SUCCESS RATE"))):
                cell = ctk.CTkFrame(metrics, fg_color="transparent"); cell.grid(row=0, column=metric_index, pady=12)
                ctk.CTkLabel(cell, text=str(value), text_color=COLORS["ink"], font=ctk.CTkFont(size=17, weight="bold")).pack()
                ctk.CTkLabel(cell, text=label, text_color=COLORS["muted"], font=ctk.CTkFont(size=9, weight="bold")).pack()
            ctk.CTkLabel(card, text=f"Workload: {active} active request{'s' if active != 1 else ''}", text_color=COLORS["muted"], font=ctk.CTkFont(size=12)).grid(row=4, column=0, sticky="w", padx=20, pady=(13, 4))
            workload_bar = ctk.CTkProgressBar(card, height=7, progress_color=load_color, fg_color=COLORS["surface_alt"])
            workload_bar.grid(row=5, column=0, sticky="ew", padx=20, pady=(0, 20))
            workload_bar.set(min(active / 6, 1))

    def _show_reports(self):
        self._title("Insights & exports", "Bring a clear view of service operations into every review.")
        actions = ctk.CTkFrame(self.current, fg_color=COLORS["surface"], corner_radius=16, border_width=1, border_color=COLORS["border"]); actions.grid(row=1, column=0, sticky="ew")
        ctk.CTkLabel(actions, text="Export your data", font=ctk.CTkFont(size=18, weight="bold"), text_color=COLORS["ink"]).pack(anchor="w", padx=20, pady=(18, 2)); ctk.CTkLabel(actions, text="Create a shareable snapshot in the format you need.", text_color=COLORS["muted"]).pack(anchor="w", padx=20, pady=(0, 12))
        buttons = ctk.CTkFrame(actions, fg_color="transparent"); buttons.pack(anchor="w", padx=16, pady=(0, 18))
        for label, fn in [("Export CSV", self.reporter.csv), ("Export Excel", self.reporter.excel), ("Export PDF", self.reporter.pdf)]: ctk.CTkButton(buttons, text=label, command=lambda f=fn: self._export(f), **button_kwargs("secondary")).pack(side="left", padx=4)
        rows = self.db.get_complaints(); priorities, categories = Counter(x["priority"] for x in rows), Counter(x["category"] for x in rows)
        stats = ctk.CTkFrame(self.current, fg_color=COLORS["surface"], corner_radius=16, border_width=1, border_color=COLORS["border"]); stats.grid(row=2, column=0, sticky="ew", pady=16); stats.grid_columnconfigure((0, 1), weight=1)
        ctk.CTkLabel(stats, text="BY PRIORITY\n\n" + "\n".join(f"{x:<10} {priorities[x]}" for x in ["Critical", "High", "Medium", "Low"]), justify="left", text_color=COLORS["ink"], font=ctk.CTkFont(size=14)).grid(row=0, column=0, sticky="nw", padx=26, pady=22)
        ctk.CTkLabel(stats, text="TOP CATEGORIES\n\n" + "\n".join(f"{x:<18} {n}" for x, n in categories.most_common()), justify="left", text_color=COLORS["ink"], font=ctk.CTkFont(size=14)).grid(row=0, column=1, sticky="nw", padx=26, pady=22)

    def _export(self, func):
        try: path = func(); messagebox.showinfo("Report created", f"Saved to:\n{path}")
        except ImportError: messagebox.showerror("Library missing", "Install requirements.txt to enable this export.")
        except Exception as exc: messagebox.showerror("Export failed", str(exc))

    def _show_settings(self):
        self._title("Preferences", "Personalise the workspace and manage the local application data.")
        box = ctk.CTkFrame(self.current, fg_color=COLORS["surface"], corner_radius=16, border_width=1, border_color=COLORS["border"]); box.grid(row=1, column=0, sticky="ew")
        ctk.CTkLabel(box, text="Appearance", font=ctk.CTkFont(size=18, weight="bold"), text_color=COLORS["ink"]).pack(anchor="w", padx=22, pady=(20, 6)); mode = ctk.CTkOptionMenu(box, values=["Light", "Dark", "System"], command=ctk.set_appearance_mode, **option_menu_kwargs()); mode.set("Light"); mode.pack(anchor="w", padx=22, pady=(0, 20))
        ctk.CTkLabel(box, text="Data tools", font=ctk.CTkFont(size=18, weight="bold"), text_color=COLORS["ink"]).pack(anchor="w", padx=22, pady=(2, 6)); tools = ctk.CTkFrame(box, fg_color="transparent"); tools.pack(anchor="w", padx=18, pady=(0, 22))
        for label, command in [("Backup database", self._backup), ("Restore database", self._restore), ("Analyse with AI", self._ai_dialog)]: ctk.CTkButton(tools, text=label, command=command, **button_kwargs("secondary")).pack(side="left", padx=4)

    def _backup(self):
        path = filedialog.asksaveasfilename(defaultextension=".db", filetypes=[("SQLite database", "*.db")])
        if path: self.db.backup(path); messagebox.showinfo("Backup created", f"Database backup saved to:\n{path}")
    def _restore(self):
        path = filedialog.askopenfilename(filetypes=[("SQLite database", "*.db")])
        if path and messagebox.askyesno("Restore database", "Replace current data with this backup? The app will need to restart."):
            try: shutil.copy2(path, self.db.db_path); messagebox.showinfo("Restored", "Database restored. Please restart the application.")
            except Exception as exc: messagebox.showerror("Restore failed", str(exc))
    def _ai_dialog(self):
        win = ctk.CTkToplevel(self); win.title("AI request analyser"); win.geometry("620x450"); win.configure(fg_color=COLORS["cream"]); win.grab_set()
        ctk.CTkLabel(win, text="AI request analyser", font=ctk.CTkFont(size=21, weight="bold"), text_color=COLORS["ink"]).pack(anchor="w", padx=24, pady=(24, 4)); ctk.CTkLabel(win, text="Describe the issue and get a suggested route.", text_color=COLORS["muted"]).pack(anchor="w", padx=24, pady=(0, 12))
        text = ctk.CTkTextbox(win, height=130, fg_color=COLORS["surface"], border_width=1, border_color=COLORS["border"], text_color=COLORS["ink"]); text.pack(fill="x", padx=24); text.insert("1.0", "There is a water leakage in hostel block A and electricity is exposed.")
        result = ctk.CTkLabel(win, text="", justify="left", anchor="w", text_color=COLORS["ink"]); result.pack(fill="both", expand=True, padx=24, pady=12)
        def analyze():
            data = self.analyzer.analyze(text.get("1.0", "end").strip()); result.configure(text=f"Category: {data['category']}\nPriority: {data['priority']}\nDepartment: {data['department']}\nExpected resolution: {data['expected_time']}\nSuggested technician: {data['technician']}\nConfidence: {data['confidence']:.0%}\n\nSummary: {data['summary']}")
        ctk.CTkButton(win, text="Analyse request", command=analyze, **button_kwargs()).pack(pady=(0, 20))
