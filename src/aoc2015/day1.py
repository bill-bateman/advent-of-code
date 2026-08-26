from utils.filestuff import load_file

def part1(data: str) -> int:
	ans = 0

	for ch in data:
		if ch=='(':
			ans += 1
		if ch==')':
			ans -= 1

	return ans

def main():
	print(part1(load_file("data/1_real.txt")))

if __name__=="__main__":
	main()