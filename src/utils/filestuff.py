import os

def load_file(__file: str, filename: str) -> str:
	with open(os.path.dirname(os.path.realpath(__file)) + "/" + filename, 'r') as f:
		return f.read()
