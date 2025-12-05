
def read_input(filename: str) -> tuple[list[tuple[int, int]], list[int]]:
    ranges, ingredients = [], []

    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            if "-" in line:
                parts = line.split("-")
                ranges.append(
                    (
                        int(parts[0]),
                        int(parts[1]),
                    )
                )
            else:
                ingredients.append(int(line))

    return ranges, ingredients

def p1(filename: str):
    ranges, ingredients = read_input(filename)
    fresh = 0

    for num in ingredients:
        
        for low, high in ranges:
            if num >= low and num <= high:
                fresh += 1
                break
    
    print(fresh)

def overlap(l1: int, h1: int, l2: int, h2: int) -> bool:
    return h1>=l2 and h2>=l1

def p2(filename: str):
    ranges, _ = read_input(filename)
    distinct_ranges = []

    # sort ranges so that we make sure to combine all overlapping ranges
    ranges.sort()

    for l1, h1 in ranges:
        for i in range(len(distinct_ranges)):
            l2, h2 = distinct_ranges[i]
            if overlap(l1, h1, l2, h2):
                distinct_ranges[i] = (
                    min(l1, l2),
                    max(h1, h2),
                )
                l1, h1 = -1, -1
                break
            
        # new range
        if l1!=-1 and h1!=-1:
            distinct_ranges.append((l1, h1))
    
    fresh = sum([high - low + 1 for low, high in distinct_ranges])
    print(fresh)

if __name__=="__main__":
    p1("data/d5_test.txt")
    p1("data/d5_real.txt")

    p2("data/d5_test.txt")
    p2("data/d5_real.txt")