
def read_input(filename: str) -> list[list[bool]]:
    with open(filename, "r") as f:
        return [
            [c=="@" for c in line]
            for line in f.readlines()
        ]

def check(grid: list[list[bool]], x: int, y: int) -> int:
    if x>=0 and x<len(grid) and y>=0 and y<len(grid[x]):
        return int(grid[x][y])
    return 0

def p1(filename: str):
    grid = read_input(filename)
    ans1 = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y]:
                num = (
                    check(grid, x-1, y-1)
                    + check(grid, x-1, y)
                    + check(grid, x-1, y+1)
                    + check(grid, x, y-1)
                    + check(grid, x, y+1)
                    + check(grid, x+1, y-1)
                    + check(grid, x+1, y)
                    + check(grid, x+1, y+1)
                )
                if num<4:
                    ans1 += 1
    print(ans1)

def p2(filename: str):
    grid = read_input(filename)
    ans2 = 0
    old_ans2=-1
    while ans2 > old_ans2:
        old_ans2 = ans2
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y]:
                    num = (
                        check(grid, x-1, y-1)
                        + check(grid, x-1, y)
                        + check(grid, x-1, y+1)
                        + check(grid, x, y-1)
                        + check(grid, x, y+1)
                        + check(grid, x+1, y-1)
                        + check(grid, x+1, y)
                        + check(grid, x+1, y+1)
                    )
                    if num<4:
                        ans2 += 1
                        grid[x][y] = False
    print(ans2)

if __name__=="__main__":
    p1("data/d4_test.txt")
    p1("data/d4_real.txt")

    p2("data/d4_test.txt")
    p2("data/d4_real.txt")