import tkinter as tk
from tkinter import filedialog

class NotepadApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notepad")
        self.geometry("800x600")

        self.create_menu()
        self.create_text_area()

        self.protocol("WM_DELETE_WINDOW", self.exit_app)

        # Open file.txt on launch
        self.open_file("file.txt")

    def create_menu(self):
        menu_bar = tk.Menu(self)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)

        menu_bar.add_cascade(label="File", menu=file_menu)

        self.config(menu=menu_bar)

    def create_text_area(self):
        self.text_area = tk.Text(self)
        self.text_area.pack(expand=True, fill=tk.BOTH)

    def open_file(self, filename=None):
        if not filename:
            filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if filename:
            with open(filename, "r") as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self, filename="file.txt"):
        with open(filename, "w") as file:
            content = self.text_area.get("1.0", tk.END)
            file.write(content)

    def exit_app(self):
        self.save_file()
        self.destroy()

if __name__ == "__main__":
    app = NotepadApp()
    app.mainloop()
