from utils.filestuff import load_file


def test_load_file():
    assert (
        load_file(__file__, "data.txt")
        == """abc
def
123
456"""
    )
