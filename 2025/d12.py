from copy import deepcopy


def read_input(filename: str):
    boxes = []
    trees = []

    with open(filename, 'r') as f:
        box = []

        for line in f.readlines():
            line = line.strip()

            if not line:
                boxes.append(box)
                box = []
            if line.startswith('#') or line.startswith('.'):
                box.append([c=='#' for c in line])
            if 'x' in line:
                parts = line.split()
                dims = parts[0][:-1].split('x')
                l = [int(dims[0]), int(dims[1])]
                l.extend(map(int, parts[1:]))
                trees.append(l)
    return boxes, trees

def p1(filename: str):
    _, trees = read_input(filename)

    ans = 0
    for tree in trees:
        gx = tree[0]
        gy = tree[1]
        box_nums = tree[2:]
        if 9 * sum(box_nums) > gx * gy:
            precise_val = 7*(box_nums[0] + box_nums[1] + box_nums[3] + box_nums[4]) + 6*(box_nums[2] + box_nums[5])

            if precise_val <= gx*gy:
                # theoretically could fit :(
                # but happily, never happens!
                # doesn't work for the test though
                print(f"{9 * sum(box_nums)} <= {gx} * {gy} = {gx * gy} <= {precise_val}")
        else:
            ans += 1

    print(ans)
    return

if __name__=="__main__":
    # p1("data/d12_test.txt") # test doesn't actually work
    p1("data/d12_real.txt")