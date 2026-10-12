"""Выполнение стартового скрипта."""

from commands import PROMPT, STATUS_OK, ShellError, execute


def strip_comment(line):
    """Убирает комментарий от # до конца строки и пробелы по краям."""
    return line.split("#", 1)[0].strip()


def read_lines(path):
    """Читает строки скрипта, при ошибке бросает ShellError."""
    try:
        with open(path, encoding="utf-8") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        raise ShellError(
            f"script: {path}: No such file or directory"
        ) from None
    except IsADirectoryError:
        raise ShellError(f"script: {path}: Is a directory") from None
    except (OSError, UnicodeDecodeError):
        raise ShellError(f"script: {path}: cannot read file") from None


def run_script(path, state):
    """Выполняет скрипт и возвращает строки диалога: ввод и вывод.

    Ошибочная команда не останавливает скрипт, к её выводу
    добавляется номер строки.
    """
    try:
        lines = read_lines(path)
    except ShellError as error:
        return [str(error)]
    dialog = []
    for number, raw in enumerate(lines, 1):
        line = strip_comment(raw)
        if not line:
            continue
        dialog.append(PROMPT + line)
        result = execute(line, state)
        if state["status"] != STATUS_OK:
            result = f"script: line {number}: {result}"
        if result:
            dialog.append(result)
        if not state["running"]:
            break
    return dialog
