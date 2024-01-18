import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import pyautogui


class BasePage(tk.Frame):
    def __init__(self, master, style, app, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.style = style
        self.app = app

    def show(self):
        self.pack(fill="both", expand=True)
        self.lift()

    def hide(self):
        self.pack_forget()
