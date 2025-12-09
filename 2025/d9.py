def read_input(filename: str) -> list[tuple[int, int]]:
    with open(filename, 'r') as f:
        return [
            tuple(map(int, line.strip().split(",")))
            for line in f.readlines()
        ]

def calc_area(x1, y1, x2, y2):
    return (abs(x1-x2)+1) * (abs(y1-y2)+1)

def p1(filename: str):
    tiles = read_input(filename)
    area = 0

    for i, (x1, y1) in enumerate(tiles):
        for x2, y2 in tiles[i+1:]:
            area = max(area, calc_area(x1, y1, x2, y2))
    
    print(area)

def p2(filename: str):
    red_tiles = read_input(filename)

    (min_x, some_y) = min(red_tiles)

    max_x = max([x for (x, _) in red_tiles]) + 1
    max_y = max([y for (_, y) in red_tiles]) + 1

    border = set()
    outside = set()

    prev_x, prev_y = red_tiles[-1]
    for x, y in red_tiles:
        for xi in range(min(x, prev_x), max(x, prev_x)+1):
            for yi in range(min(y, prev_y), max(y, prev_y)+1):
                border.add((xi, yi))
        prev_x, prev_y = x, y

    # set all outside tiles to -1
    print("setting outside")
    queue = []
    queue.append((min_x - 1, some_y))
    while queue:
        x, y = queue.pop()
        if (
            (x, y) in border # on the border
            or (x, y) in outside # already seen
            or not ( # too far from border
                (x+1, y) in border
                or (x-1, y) in border
                or (x+1, y+1) in border
                or (x, y+1) in border
                or (x-1, y+1) in border
                or (x+1, y-1) in border
                or (x, y-1) in border
                or (x-1, y-1) in border
            )
        ):
            continue

        outside.add((x,y))
        queue.append((x+1, y))
        queue.append((x-1, y))
        queue.append((x, y+1))
        queue.append((x, y-1))

    print("finding area")
    area = 0
    for i, (x1, y1) in enumerate(red_tiles):
        print(i, len(red_tiles), area)
        for x2, y2 in red_tiles[i+1:]:
            new_area = calc_area(x1, y1, x2, y2)
            if new_area > area:
                # check that all tiles along the perimeter are not outside
                good = True
                for x in range(min(x1, x2), max(x1, x2)+1):
                    if (x, y1) in outside or (x, y2) in outside:
                        good = False
                        break
                if good:
                    for y in range(min(y1, y2), max(y1, y2)+1):
                        if (x1, y) in outside or (x2, y) in outside:
                            good = False
                            break
                if good:
                    area = new_area
    print(area)


if __name__=="__main__":
    p1("data/d9_test.txt")
    p1("data/d9_real.txt")

    p2("data/d9_test.txt")
    p2("data/d9_real.txt")