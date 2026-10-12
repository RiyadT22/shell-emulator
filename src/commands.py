"""Разбор ввода и команды эмулятора."""

DEFAULT_VFS_NAME = "vfs"
MAX_CD_ARGS = 1
MAX_EXIT_ARGS = 1


class ShellError(Exception):
    """Ошибка выполнения команды, текст уходит пользователю."""


def new_state(vfs_name=DEFAULT_VFS_NAME):
    """Создаёт начальное состояние эмулятора."""
    return {"vfs_name": vfs_name, "running": True, "exit_code": 0}


def parse(line):
    """Делит строку по пробелам на имя команды и аргументы."""
    parts = line.split()
    if not parts:
        return None, []
    return parts[0], parts[1:]


def cmd_ls(args, state):
    """Заглушка ls: выводит имя команды и аргументы."""
    return " ".join(["ls"] + args)


def cmd_cd(args, state):
    """Заглушка cd: выводит имя команды и аргументы."""
    if len(args) > MAX_CD_ARGS:
        raise ShellError("cd: too many arguments")
    return " ".join(["cd"] + args)


def cmd_exit(args, state):
    """Завершает работу эмулятора с кодом из аргумента."""
    if len(args) > MAX_EXIT_ARGS:
        raise ShellError("exit: too many arguments")
    code = 0
    if args:
        try:
            code = int(args[0])
        except ValueError:
            raise ShellError(
                f"exit: {args[0]}: numeric argument required"
            ) from None
    state["running"] = False
    state["exit_code"] = code
    return ""


COMMANDS = {
    "ls": cmd_ls,
    "cd": cmd_cd,
    "exit": cmd_exit,
}


def execute(line, state):
    """Выполняет одну строку ввода и возвращает текст для вывода."""
    name, args = parse(line)
    if name is None:
        return ""
    command = COMMANDS.get(name)
    if command is None:
        return f"{name}: command not found"
    try:
        return command(args, state)
    except ShellError as error:
        return str(error)
