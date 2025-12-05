def load_input(filename: str) -> list[tuple[str, int]]:
    with open(filename, 'r') as f:
        return [
            (line[0], int(line[1:]))
            for line in f.readlines()
        ]

class State:
    val: int
    ans1: int
    ans2: int

    def __init__(self):
        self.val = 50
        self.ans1 = 0
        self.ans2 = 0
    
    def __repr__(self) -> str:
        return f"p1={self.ans1}, p2={self.ans2}"

def do_step(s: State, d: str, num: int):
    if d=="R":
        s.val += num
    else:
        if s.val == 0:
            # special case for 0 so we don't double count things for part 2
            s.val = 100 - num
        else:
            s.val -= num

    # keep us within [0, 99]
    while s.val > 99:
        if s.val != 100: # special case for 100 so we don't double count things for part 2
            s.ans2 += 1
        s.val -= 100
    while s.val < 0:
        s.ans2 += 1
        s.val += 100
    
    if s.val == 0:
        s.ans1 += 1
        s.ans2 += 1

def main(filename: str):
    s = State()
    for d, num in load_input(filename):
        # naive solution that was much easier to get right for part 2
        # for _ in range(num):
        #     do_step(s, d, 1)
        do_step(s, d, num)
    
    print(f"{filename} - {s}")

if __name__=="__main__":
    main("data/d1_test.txt")
    main("data/d1_real.txt")