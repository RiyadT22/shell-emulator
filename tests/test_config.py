from config import NOT_SET, debug_lines, parse_args, vfs_name


def test_no_args():
    args = parse_args([])
    assert args.vfs is None
    assert args.script is None


def test_all_args():
    args = parse_args(["--vfs", "data/myfs", "--script", "start.txt"])
    assert args.vfs == "data/myfs"
    assert args.script == "start.txt"


def test_vfs_name_from_path():
    assert vfs_name("data/myfs") == "myfs"
    assert vfs_name("data/myfs/") == "myfs"


def test_vfs_name_default():
    assert vfs_name(None) == "vfs"


def test_debug_lines():
    args = parse_args(["--vfs", "data/myfs"])
    assert debug_lines(args) == ["vfs: data/myfs", f"script: {NOT_SET}"]
