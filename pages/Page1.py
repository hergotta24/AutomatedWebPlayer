import tkinter as tk
from tkinter import ttk
from pages.BasePage import BasePage
from tkinter import messagebox  # Import messagebox for displaying alerts
from pages.Page2 import Page2

class Page1(BasePage):
    def __init__(self, master, style, app, *args, **kwargs):
        super().__init__(master, style, app, *args, **kwargs)
        ttk.Label(self, text="Login Page", style="TLabel").pack(pady=10)

        # Entry widgets for username and password
        self.username_entry = ttk.Entry(self, width=20)
        self.password_entry = ttk.Entry(self, width=20, show='*')  # Mask the password with '*'

        ttk.Label(self, text="Username:").pack(pady=5)
        self.username_entry.pack(pady=5)
        ttk.Label(self, text="Password:").pack(pady=5)
        self.password_entry.pack(pady=5)

        # Button for login
        login_button = ttk.Button(self, text="Login", command=self.login)
        login_button.pack(pady=10)

    def login(self):
        # For simplicity, using hardcoded credentials
        valid_username = "user"
        valid_password = "password"

        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        if entered_username == valid_username and entered_password == valid_password:
            # Successful login, switch to the dashboard (Page2)
            self.app.show_page("Page 2")
        else:
            # Display an error message for unsuccessful login
            messagebox.showerror("Login Error", "Invalid username or password. Please try again.")