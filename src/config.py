"""Параметры командной строки."""

import argparse
import os

from commands import DEFAULT_VFS_NAME

NOT_SET = "(not set)"


def parse_args(argv=None):
    """Разбирает параметры командной строки."""
    parser = argparse.ArgumentParser(description="Shell emulator")
    parser.add_argument("--vfs", help="path to VFS directory")
    parser.add_argument("--script", help="path to startup script")
    return parser.parse_args(argv)


def vfs_name(path):
    """Возвращает имя VFS по пути: последнюю часть пути."""
    if not path:
        return DEFAULT_VFS_NAME
    return os.path.basename(os.path.normpath(path)) or DEFAULT_VFS_NAME


def debug_lines(args):
    """Строки отладочного вывода со всеми параметрами."""
    return [
        f"vfs: {args.vfs or NOT_SET}",
        f"script: {args.script or NOT_SET}",
    ]
