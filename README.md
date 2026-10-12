# Эмулятор командной строки

Практическая работа №1 по конфигурационному управлению, вариант 24.
Программа на Python 3.13 с окном на tkinter, которое ведёт себя похоже на
командную строку UNIX.

Сейчас сделан этап 1: окно с вводом команд, простой парсер и заглушки
команд. Имя VFS показывается в заголовке окна (пока это имя по умолчанию
`vfs`).

## Команды

`ls [args]` и `cd [dir]` пока заглушки: печатают своё имя и аргументы.
`cd` с двумя и более аргументами выдаёт `cd: too many arguments`.

`exit [code]` закрывает окно. Код должен быть числом, иначе будет
`exit: abc: numeric argument required`.

На неизвестную команду выводится `name: command not found`.

## Запуск

Windows:

```
run.bat
```

Linux:

```
sh run.sh
```

## Тесты

```
pip install -r requirements.txt
python -m pytest
```

## Пример

```
$ ls -l /home
ls -l /home
$ cd a b
cd: too many arguments
$ hello
hello: command not found
$ exit abc
exit: abc: numeric argument required
$ exit
```

## Структура

`src/commands.py` содержит парсер и команды, они не зависят от GUI и
проверяются тестами. `src/gui.py` содержит окно, `src/main.py` запускает
программу.
