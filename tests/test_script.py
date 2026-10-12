from commands import new_state
from script import run_script, strip_comment


def write(tmp_path, text):
    path = tmp_path / "start.txt"
    path.write_text(text, encoding="utf-8")
    return path


def test_strip_comment():
    assert strip_comment("ls -l  # list") == "ls -l"
    assert strip_comment("# only comment") == ""
    assert strip_comment("   ") == ""


def test_dialog_shows_input_and_output(tmp_path):
    path = write(tmp_path, "# comment\n\nls -l\ncd /tmp  # go\n")
    assert run_script(path, new_state()) == [
        "$ ls -l", "ls -l", "$ cd /tmp", "cd /tmp",
    ]


def test_error_has_line_number_and_script_goes_on(tmp_path):
    path = write(tmp_path, "ls\nnope\ncd a b\nls after\n")
    assert run_script(path, new_state()) == [
        "$ ls", "ls",
        "$ nope", "script: line 2: nope: command not found",
        "$ cd a b", "script: line 3: cd: too many arguments",
        "$ ls after", "ls after",
    ]


def test_exit_stops_script(tmp_path):
    path = write(tmp_path, "exit 2\nls\n")
    state = new_state()
    assert run_script(path, state) == ["$ exit 2"]
    assert state["running"] is False
    assert state["exit_code"] == 2


def test_missing_script(tmp_path):
    path = tmp_path / "missing.txt"
    assert run_script(path, new_state()) == [
        f"script: {path}: No such file or directory",
    ]


def test_script_is_directory(tmp_path):
    [message] = run_script(tmp_path, new_state())
    assert message.startswith(f"script: {tmp_path}: ")
