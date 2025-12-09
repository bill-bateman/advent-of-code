import heapq
from collections import Counter
from math import prod

def read_input(filename: str) -> list[tuple[int, int, int]]:
    with open(filename, 'r') as f:
        return [
            tuple(map(int, [x for x in line.strip().split(",")]))
            for line in f.readlines()
        ]

def dist_sq(box1, box2):
    x1, y1, z1 = box1
    x2, y2, z2 = box2
    return (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2

def p1(filename: str, num: int):
    boxes = read_input(filename)

    distances = []
    for i, b1 in enumerate(boxes):
        for j, b2 in enumerate(boxes[i+1:]):
            d = dist_sq(b1, b2)
            i2 = i+1+j

            if len(distances)==num:
                _ = heapq.heappushpop(distances, (-d, i, i2))
            else:
                heapq.heappush(distances, (-d, i, i2))
    
    i_to_cct = {
        i: i for i in range(len(boxes))
    }
    for d, i1, i2 in distances:
        # connect i1 and i2
        old_val = i_to_cct[i2]
        new_val = i_to_cct[i1]

        for i in range(len(boxes)):
            if i_to_cct[i] == old_val:
                i_to_cct[i] = new_val
    
    cct_to_size = Counter(i_to_cct.values())
    sizes = sorted(cct_to_size.values(), reverse=True)
    print(prod(sizes[:3]))

def p2(filename):
    boxes = read_input(filename)
    distances = []
    for i, b1 in enumerate(boxes):
        for j, b2 in enumerate(boxes[i+1:]):
            d = dist_sq(b1, b2)
            i2 = i+1+j

            heapq.heappush(distances, (d, i, i2))
    
    i_to_cct = {
        i: i for i in range(len(boxes))
    }
    while True:
        d, i1, i2 = heapq.heappop(distances)
        # connect i1 and i2
        old_val = i_to_cct[i2]
        new_val = i_to_cct[i1]

        if old_val == new_val:
            continue

        num_in_this_cct = 0

        for i in range(len(boxes)):
            if i_to_cct[i] == old_val:
                i_to_cct[i] = new_val
            if i_to_cct[i] == new_val:
                num_in_this_cct += 1
        
        if num_in_this_cct == len(boxes):
            print(boxes[i1][0] * boxes[i2][0])
            return


if __name__=="__main__":
    p1("data/d8_test.txt", 10)
    p1("data/d8_real.txt", 1000)

    p2("data/d8_test.txt")
    p2("data/d8_real.txt")