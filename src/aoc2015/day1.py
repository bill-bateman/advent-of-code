from utils.filestuff import load_file


def part1(data: str) -> int:
	ans = 0

	for ch in data:
		if ch=='(':
			ans += 1
		if ch==')':
			ans -= 1

	return ans

def part2(data: str) -> int:
	ans = 0
	for i, ch in enumerate(data):
		if ch=='(':
			ans += 1
		if ch==')':
			ans -=1

		if ans == -1:
			return i+1

	raise Exception("Never went into the basement!")

def main():
	data = load_file(__file__, "1_real.txt")
	print(part1(data))
	print(part2(data))

if __name__=="__main__":
	main()