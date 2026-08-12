import customtkinter as ctk
from database import DatabaseManager
from ai_engine import AIAnalyzer
from managers import ComplaintManager, ReportManager
from ui import LoginFrame, ApplicationFrame
from pathlib import Path

class SmartComplaintApplication(ctk.CTk):
    """Composition root. No module-level mutable application state."""
    def __init__(self):
        super().__init__(); self.title("AI-Powered Smart Complaint Prioritization"); self.geometry("1250x760"); self.minsize(1040,650)
        ctk.set_appearance_mode("System"); ctk.set_default_color_theme("blue")
        self.database=DatabaseManager(); self.manager=ComplaintManager(self.database); self.analyzer=AIAnalyzer(); self.reporter=ReportManager(self.database,Path(__file__).parent / "reports")
        self.login=LoginFrame(self,self.database.authenticate); self.login.pack(fill="both",expand=True)
    def open_app(self,user):
        self.login.destroy(); self.app=ApplicationFrame(self,user,self.manager,self.database,self.analyzer,self.reporter); self.app.pack(fill="both",expand=True)


if __name__ == "__main__": SmartComplaintApplication().mainloop()
