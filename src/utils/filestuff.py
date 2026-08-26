import os


def load_file(file: str, filename: str) -> str:
    with open(os.path.dirname(os.path.realpath(file)) + "/" + filename, "r") as f:
        return f.read()
