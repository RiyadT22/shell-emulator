"""Точка входа: запускает окно эмулятора."""

import sys
import tkinter as tk

from commands import new_state
from gui import ShellWindow


def main():
    """Создаёт окно и запускает цикл событий."""
    state = new_state()
    root = tk.Tk()
    root.geometry("800x500")
    ShellWindow(root, state)
    root.mainloop()
    return state["exit_code"]


if __name__ == "__main__":
    sys.exit(main())
