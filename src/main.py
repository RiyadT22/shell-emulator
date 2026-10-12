"""Точка входа: запускает окно эмулятора."""

import sys
import tkinter as tk

from commands import new_state
from config import debug_lines, parse_args, vfs_name
from gui import ShellWindow


def main(argv=None):
    """Разбирает параметры, создаёт окно и запускает цикл событий."""
    args = parse_args(argv)
    lines = debug_lines(args)
    print("\n".join(lines))
    state = new_state(vfs_name(args.vfs))
    root = tk.Tk()
    root.geometry("800x500")
    window = ShellWindow(root, state)
    window.write_lines(lines)
    if args.script:
        root.after(0, window.run_startup, args.script)
    root.mainloop()
    return state["exit_code"]


if __name__ == "__main__":
    sys.exit(main())
