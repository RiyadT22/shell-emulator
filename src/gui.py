"""Окно эмулятора на tkinter."""

import tkinter as tk

from commands import execute

PROMPT = "$ "
FONT = ("Consolas", 11)


class ShellWindow:
    """Окно с областью вывода и строкой ввода."""

    def __init__(self, root, state):
        self.root = root
        self.state = state
        root.title(f"{state['vfs_name']} - shell emulator")

        self.output = tk.Text(root, font=FONT, bg="black", fg="white",
                              state="disabled", wrap="word")
        self.output.pack(fill="both", expand=True)

        self.entry = tk.Entry(root, font=FONT, bg="black", fg="white",
                              insertbackground="white")
        self.entry.pack(fill="x")
        self.entry.bind("<Return>", self.on_enter)
        self.entry.focus_set()

    def write(self, text):
        """Добавляет текст в конец области вывода."""
        self.output.configure(state="normal")
        self.output.insert("end", text)
        self.output.see("end")
        self.output.configure(state="disabled")

    def on_enter(self, event):
        """Обрабатывает введённую строку."""
        line = self.entry.get()
        self.entry.delete(0, "end")
        self.write(PROMPT + line + "\n")
        result = execute(line, self.state)
        if result:
            self.write(result + "\n")
        if not self.state["running"]:
            self.root.destroy()
