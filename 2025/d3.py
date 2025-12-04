
def read_input(filename: str) -> list[list[int]]:
    with open(filename, "r") as f:
        return [
            [int(c) for c in line.strip()]
            for line in f.readlines()
        ]

def get_max_and_index(nums: list[int]):
    m = max(nums)
    for i, num in enumerate(nums):
        if num==m:
            return m, i

def part1(filename: str):
    banks = read_input(filename)
    ans1 = 0
    for bank in banks:
        d1, i1 = get_max_and_index(bank[:-1])
        d2 = max(bank[i1+1:])

        ans1 += d1*10 + d2
    print(ans1)

def part2(filename: str):
    banks = read_input(filename)
    ans2 = 0
    for bank in banks:
        left = 0
        for i in range(12):
            # make sure we leave enough batteries for the later steps
            right = 12 - 1 - i

            if right==0:
                d, di = get_max_and_index(bank[left:])
            else:
                d, di = get_max_and_index(bank[left:-right])
            
            ans2 += d * 10**right

            left = di+left+1
    print(ans2)


if __name__=="__main__":
    part1("data/p3_test.txt")
    part1("data/p3_real.txt")

    part2("data/p3_test.txt")
    part2("data/p3_real.txt")