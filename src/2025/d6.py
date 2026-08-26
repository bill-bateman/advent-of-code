import math

def read_input(filename: str) -> tuple[list[list[int]], list[str]]:
    operations = []
    problems = []

    with open(filename, "r") as f:
        for line in f.readlines():
            for i, p in enumerate(line.strip().split()):
                if p == '+' or p == '*':
                    operations.append(p)
                else:
                    if len(problems)<=i:
                        problems.append([])
                    problems[i].append(int(p))
    
    return problems, operations

def p1(filename: str):
    problems, operations = read_input(filename)

    grand_total = 0
    for numbers, op in zip(problems, operations, strict=True):
        if op=='+':
            grand_total += sum(numbers)
        if op=='*':
            grand_total += math.prod(numbers)
    print(grand_total)

def read_input_2(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line for line in f.readlines()]

def p2(filename: str):
    lines = read_input_2(filename)
    grand_total = 0

    for i, op in enumerate(lines[-1]):
        if op != '*' and op != '+':
            continue # blank line
        
        # i gives the start position of a problem
        # find the end
        i2 = i+1
        while i2<len(lines[-1]) and lines[-1][i2]==' ':
            i2 += 1
        if i2!=len(lines[-1]):
            i2 -= 1

        #[i, i2] is the range of the problem
        inputs = [line[i:i2] for line in lines[:-1]]
        transposed = map(list, zip(*inputs))
        numbers = [
            int(''.join(c for c in num_str if c!=' '))
            for num_str in transposed
        ]

        if op=='+':
            grand_total += sum(numbers)
        if op=='*':
            grand_total += math.prod(numbers)
    print(grand_total)


if __name__=="__main__":
    p1("data/d6_test.txt")
    p1("data/d6_real.txt")

    p2("data/d6_test.txt")
    p2("data/d6_real.txt")
