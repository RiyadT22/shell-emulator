"""Разбор ввода и команды эмулятора."""

DEFAULT_VFS_NAME = "vfs"
PROMPT = "$ "
MAX_CD_ARGS = 1
MAX_EXIT_ARGS = 1
STATUS_OK = 0
STATUS_ERROR = 1
STATUS_NOT_FOUND = 127


class ShellError(Exception):
    """Ошибка выполнения команды, текст уходит пользователю."""


def new_state(vfs_name=DEFAULT_VFS_NAME):
    """Создаёт начальное состояние эмулятора."""
    return {
        "vfs_name": vfs_name,
        "running": True,
        "exit_code": STATUS_OK,
        "status": STATUS_OK,
    }


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
    code = STATUS_OK
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
    """Выполняет строку ввода, ставит state["status"] и возвращает вывод."""
    name, args = parse(line)
    state["status"] = STATUS_OK
    if name is None:
        return ""
    command = COMMANDS.get(name)
    if command is None:
        state["status"] = STATUS_NOT_FOUND
        return f"{name}: command not found"
    try:
        return command(args, state)
    except ShellError as error:
        state["status"] = STATUS_ERROR
        return str(error)
