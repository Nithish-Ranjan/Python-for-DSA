"""Presentation-only colors and widget styling for the desktop interface."""

from tkinter import ttk

COLORS = {"cream": "#FFF9F1", "surface": "#FFFFFF", "surface_alt": "#FFF2E3", "sidebar": "#3A2418", "sidebar_hover": "#5B3825", "ink": "#2D1B12", "muted": "#8A7062", "terracotta": "#C65D3B", "terracotta_hover": "#A9472A", "gold": "#E3A842", "sage": "#557A62", "rose": "#B94D4D", "border": "#EAD9C8"}

def button_kwargs(kind="primary"):
    palettes = {"primary": (COLORS["terracotta"], COLORS["terracotta_hover"], "#FFFFFF"), "secondary": (COLORS["surface_alt"], "#F5E3D1", COLORS["ink"]), "danger": (COLORS["rose"], "#983737", "#FFFFFF")}
    fg, hover, text = palettes[kind]
    return {"fg_color": fg, "hover_color": hover, "text_color": text, "corner_radius": 10}

def option_menu_kwargs():
    """Option menus use different CustomTkinter option names than buttons."""
    return {
        "fg_color": COLORS["surface_alt"],
        "button_color": COLORS["terracotta"],
        "button_hover_color": COLORS["terracotta_hover"],
        "text_color": COLORS["ink"],
        "dropdown_fg_color": COLORS["surface"],
        "dropdown_hover_color": "#F5E3D1",
        "corner_radius": 10,
    }

def configure_treeview():
    style = ttk.Style(); style.theme_use("clam")
    style.configure("Warm.Treeview", background=COLORS["surface"], foreground=COLORS["ink"], fieldbackground=COLORS["surface"], borderwidth=0, rowheight=36, font=("Segoe UI", 10))
    style.configure("Warm.Treeview.Heading", background=COLORS["surface_alt"], foreground=COLORS["muted"], relief="flat", borderwidth=0, font=("Segoe UI Semibold", 9), padding=(12, 10))
    style.map("Warm.Treeview", background=[("selected", "#F4C7A1")], foreground=[("selected", COLORS["ink"])])
    style.map("Warm.Treeview.Heading", background=[("active", "#F5E3D1")])
