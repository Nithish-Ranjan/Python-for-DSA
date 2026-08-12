from pathlib import Path
from datetime import datetime
import csv


class ReportManager:
    def __init__(self, database, reports_dir): self.db=database; self.directory=Path(reports_dir); self.directory.mkdir(exist_ok=True)
    def _rows(self): return self.db.get_complaints()
    def csv(self):
        path=self.directory / f"complaints_{datetime.now():%Y%m%d_%H%M}.csv"; rows=self._rows()
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer=csv.DictWriter(f, fieldnames=rows[0].keys() if rows else ["id"]); writer.writeheader(); writer.writerows(rows)
        return path
    def excel(self):
        from openpyxl import Workbook
        path=self.directory / f"complaints_{datetime.now():%Y%m%d_%H%M}.xlsx"; rows=self._rows(); book=Workbook(); ws=book.active; ws.title="Complaints"
        if rows:
            ws.append(list(rows[0].keys()))
            for row in rows: ws.append(list(row.values()))
            ws.freeze_panes="A2"; ws.auto_filter.ref=ws.dimensions
            for col in ws.columns: ws.column_dimensions[col[0].column_letter].width=18
        book.save(path); return path
    def pdf(self):
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import landscape, A4
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet
        path=self.directory / f"complaints_{datetime.now():%Y%m%d_%H%M}.pdf"; rows=self._rows(); styles=getSampleStyleSheet()
        data=[["ID","Title","Priority","Status","Technician"]]+[[r["id"], r["title"][:32], r["priority"], r["status"], r["technician"]] for r in rows]
        table=Table(data, colWidths=[65,250,70,70,110]); table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#1F6AA5")),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),.25,colors.grey),("FONTSIZE",(0,0),(-1,-1),8),("VALIGN",(0,0),(-1,-1),"MIDDLE")]))
        SimpleDocTemplate(str(path), pagesize=landscape(A4)).build([Paragraph("Smart Complaint Management Report", styles["Title"]), Spacer(1,12), table]); return path
