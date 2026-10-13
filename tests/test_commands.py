from commands import (
    STATUS_ERROR, STATUS_NOT_FOUND, STATUS_OK, execute, new_state, parse,
)

EXIT_CODE = 3


def test_parse_splits_by_spaces():
    assert parse("ls  -l   /home") == ("ls", ["-l", "/home"])


def test_parse_empty_line():
    assert parse("   ") == (None, [])


def test_empty_line_gives_no_output():
    assert execute("", new_state()) == ""


def test_unknown_command():
    assert execute("nope 1", new_state()) == "nope: command not found"


def test_ls_stub_prints_args():
    assert execute("ls -l /home", new_state()) == "ls -l /home"


def test_ls_stub_without_args():
    assert execute("ls", new_state()) == "ls"


def test_cd_stub_prints_args():
    assert execute("cd /tmp", new_state()) == "cd /tmp"


def test_cd_too_many_args():
    assert execute("cd a b", new_state()) == "cd: too many arguments"


def test_exit_stops_shell():
    state = new_state()
    assert execute("exit", state) == ""
    assert state["running"] is False
    assert state["exit_code"] == STATUS_OK


def test_exit_with_code():
    state = new_state()
    execute(f"exit {EXIT_CODE}", state)
    assert state["exit_code"] == EXIT_CODE


def test_exit_bad_code():
    state = new_state()
    result = execute("exit abc", state)
    assert result == "exit: abc: numeric argument required"
    assert state["running"] is True


def test_exit_too_many_args():
    state = new_state()
    assert execute("exit 1 2", state) == "exit: too many arguments"
    assert state["running"] is True


def test_vfs_name_in_state():
    assert new_state("myfs")["vfs_name"] == "myfs"


def test_status_ok():
    state = new_state()
    execute("ls", state)
    assert state["status"] == STATUS_OK


def test_status_error():
    state = new_state()
    execute("cd a b", state)
    assert state["status"] == STATUS_ERROR


def test_status_not_found():
    state = new_state()
    execute("nope", state)
    assert state["status"] == STATUS_NOT_FOUND
