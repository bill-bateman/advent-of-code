def read_input(filename: str) -> list[list]:
    with open(filename, 'r') as f:
        return [
            [c for c in line.strip()]
            for line in f.readlines()
        ]

def update(line, i, num):
    if isinstance(line[i], int):
        num += line[i]
    line[i] = num

def main(filename: str):
    grid = read_input(filename)
    splits = 0
    
    for i, line in enumerate(grid[1:]):
        prev_line = grid[i]

        for j, c in enumerate(line):
            prev_c = prev_line[j]

            if prev_c == 'S':
                # activate us
                update(line, j, 1)

            elif isinstance(prev_c, int):
                # activate us
                if c == "^":
                    # splitter!
                    if j-1>=0:
                        update(line, j-1, prev_c)
                    if j+1<len(line):
                        update(line, j+1, prev_c)
                    splits += 1
                
                else:
                    # normal
                    update(line, j, prev_c)
    
    print(f"p1: {splits}")
    print(f"p2: {sum([n for n in grid[-1] if isinstance(n, int)])}")

if __name__=="__main__":
    main("data/d7_test.txt")
    main("data/d7_real.txt")