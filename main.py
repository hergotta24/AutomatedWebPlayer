import tkinter as tk
from ttkbootstrap import Style
from pages.Page1 import Page1
from pages.Page2 import Page2

class MultiPageApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Multi-Page Tkinter App")
        self.style = Style(theme="solar")  # Change 'yeti' to your preferred ttkbootstrap theme
        self.master.geometry("800x600")

        self.pages = {}

        self.create_page(Page1, "Page 1")
        self.create_page(Page2, "Page 2")

        self.create_navigation()

        self.show_page("Page 1")

    def create_page(self, page_class, page_name):
        page = page_class(self.master, self.style, self)
        self.pages[page_name] = page

    def create_navigation(self):
        navigation_frame = tk.Frame(self.master)
        navigation_frame.pack(side="top", fill="x")

        for page_name in self.pages:
            tk.Button(navigation_frame, text=page_name, command=lambda name=page_name: self.show_page(name)).pack(side="left", padx=10)

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.show()
        for other_page_name, other_page in self.pages.items():
            if other_page_name != page_name:
                other_page.hide()

def main():
    root = tk.Tk()
    app = MultiPageApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()