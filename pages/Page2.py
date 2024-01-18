import tkinter as tk
from tkinter import ttk
from pages.BasePage import BasePage

class Page2(BasePage):
    def __init__(self, master, style, app, *args, **kwargs):
        super().__init__(master, style, app, *args, **kwargs)
        ttk.Label(self, text="Page 2 Content", style="TLabel").pack(pady=10)