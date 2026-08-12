import customtkinter as ctk
from .theme import COLORS, button_kwargs


class LoginFrame(ctk.CTkFrame):
    """Presentation layer for sign-in; authentication is supplied by the app."""

    def __init__(self, master, authenticate):
        ctk.set_appearance_mode("Light")
        master.configure(fg_color=COLORS["cream"])
        super().__init__(master, corner_radius=0, fg_color=COLORS["cream"])
        self.authenticate = authenticate
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(0, weight=1)

        self._build_welcome_panel()
        self._build_signin_panel()

    def _build_welcome_panel(self):
        panel = ctk.CTkFrame(self, corner_radius=0, fg_color=COLORS["sidebar"])
        panel.grid(row=0, column=0, sticky="nsew")
        panel.grid_columnconfigure(0, weight=1)
        panel.grid_rowconfigure(1, weight=1)

        brand = ctk.CTkFrame(panel, fg_color="transparent")
        brand.grid(row=0, column=0, sticky="ew", padx=52, pady=(48, 0))
        ctk.CTkLabel(brand, text="SC", width=42, height=42, corner_radius=12, fg_color=COLORS["terracotta"], font=ctk.CTkFont(size=17, weight="bold")).pack(side="left")
        ctk.CTkLabel(brand, text="Smart Complaints", text_color="#FFF8F0", font=ctk.CTkFont(size=18, weight="bold")).pack(side="left", padx=12)

        copy = ctk.CTkFrame(panel, fg_color="transparent")
        copy.grid(row=1, column=0, sticky="nsew", padx=52)
        ctk.CTkLabel(copy, text="Resolve more.\nWorry less.", text_color="#FFF8F0", justify="left", anchor="w", font=ctk.CTkFont(size=38, weight="bold")).pack(anchor="w", pady=(0, 14))
        ctk.CTkLabel(copy, text="One thoughtful workspace for every campus service request, from first report to resolution.", text_color="#DCC5B4", justify="left", anchor="w", wraplength=380, font=ctk.CTkFont(size=15)).pack(anchor="w")

        points = ctk.CTkFrame(copy, fg_color="#4C2F20", corner_radius=18)
        points.pack(fill="x", pady=(36, 0))
        for text in ("Clear priorities, at a glance", "Simple handoffs for every team", "Live progress you can trust"):
            ctk.CTkLabel(points, text="  " + text, text_color="#F7E9DE", anchor="w", font=ctk.CTkFont(size=13)).pack(fill="x", padx=15, pady=8)

        ctk.CTkLabel(panel, text="CAMPUS OPERATIONS  |  SECURE WORKSPACE", text_color="#B99176", font=ctk.CTkFont(size=10, weight="bold")).grid(row=2, column=0, sticky="w", padx=52, pady=42)

    def _build_signin_panel(self):
        pane = ctk.CTkFrame(self, corner_radius=0, fg_color=COLORS["cream"])
        pane.grid(row=0, column=1, sticky="nsew")
        pane.grid_columnconfigure(0, weight=1)
        pane.grid_rowconfigure(0, weight=1)

        form = ctk.CTkFrame(pane, width=410, fg_color="transparent")
        form.grid(row=0, column=0, padx=48, pady=30)
        form.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(form, text="WELCOME BACK", font=ctk.CTkFont(size=11, weight="bold"), text_color=COLORS["terracotta"]).grid(row=0, column=0, sticky="w", pady=(0, 7))
        ctk.CTkLabel(form, text="Sign in to your\nworkspace", justify="left", anchor="w", font=ctk.CTkFont(size=31, weight="bold"), text_color=COLORS["ink"]).grid(row=1, column=0, sticky="w")
        ctk.CTkLabel(form, text="Use your account details to continue.", text_color=COLORS["muted"], font=ctk.CTkFont(size=14)).grid(row=2, column=0, sticky="w", pady=(10, 30))
        ctk.CTkLabel(form, text="USERNAME", text_color=COLORS["muted"], font=ctk.CTkFont(size=10, weight="bold")).grid(row=3, column=0, sticky="w", pady=(0, 5))
        self.username = ctk.CTkEntry(form, placeholder_text="Enter your username", height=46, corner_radius=10, border_color=COLORS["border"], fg_color=COLORS["surface"], text_color=COLORS["ink"])
        self.username.grid(row=4, column=0, sticky="ew", pady=(0, 17))
        ctk.CTkLabel(form, text="PASSWORD", text_color=COLORS["muted"], font=ctk.CTkFont(size=10, weight="bold")).grid(row=5, column=0, sticky="w", pady=(0, 5))
        self.password = ctk.CTkEntry(form, placeholder_text="Enter your password", show="*", height=46, corner_radius=10, border_color=COLORS["border"], fg_color=COLORS["surface"], text_color=COLORS["ink"])
        self.password.grid(row=6, column=0, sticky="ew", pady=(0, 12))
        self.message = ctk.CTkLabel(form, text="Demo: admin / admin123", text_color=COLORS["muted"], anchor="w")
        self.message.grid(row=7, column=0, sticky="w", pady=(0, 14))
        ctk.CTkButton(form, text="Sign in", height=48, command=self._login, font=ctk.CTkFont(size=14, weight="bold"), **button_kwargs()).grid(row=8, column=0, sticky="ew")
        self.password.bind("<Return>", lambda _: self._login())
        self.username.focus_set()

    def _login(self):
        user = self.authenticate(self.username.get().strip(), self.password.get())
        if user:
            self.master.open_app(user)
        else:
            self.message.configure(text="Invalid username or password. Please try again.", text_color=COLORS["rose"])
