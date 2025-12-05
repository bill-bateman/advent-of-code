
def read_input(filename: str) -> list[tuple[int, int]]:
    with open(filename, 'r') as f:
        return [
            (
                int(ids.split("-")[0]),
                int(ids.split("-")[1]),
            )
            for line in f.readlines()
            for ids in line.split(",")
        ]

def next_invalid(num: int) -> int:
    num_s = str(num)

    if len(num_s) % 2 == 0:
        # divisible by 2
        h1 = num_s[:len(num_s)//2]

        if int(h1 + h1) > num:
            return int(h1 + h1)
        
        # next h1
        # if h1 ends in 9, it will still work fine
        h1 = str(int(h1) + 1)
        return int(h1 + h1)
    
    # not divisible by 2
    h1 = "1" + "0" * (len(num_s)//2)
    return int(h1 + h1)

def p1(filename: str):
    ans = 0
    for (start, end) in read_input(filename):
        i = start-1
        i = next_invalid(i)
        while i<=end:
            ans += i
            i = next_invalid(i)
    print(ans)

def is_invalid_pt2(num: int) -> bool:
    s = str(num)
    for l in range(1, 1 + len(s)//2):
        if len(s) % l == 0:
            if s == (s[:l]) * (len(s)//l):
                return True
    return False


def p2(filename: str):
    ans = 0
    for (start, end) in read_input(filename):
        for i in range(start, end+1):
            if is_invalid_pt2(i):
                ans += i
    print(ans)


if __name__=="__main__":
    p1("data/d2_test.txt")
    p1("data/d2_real.txt")

    p2("data/d2_test.txt")
    p2("data/d2_real.txt")
