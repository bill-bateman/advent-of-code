import scipy
import itertools

import scipy.optimize

def read_file(filename: str) -> list[tuple[int, list[int], list[int]]]:
    data = []

    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()

            light = 0
            buttons = []
            joltage = []

            for word in line.split():
                less = word[1:-1]
                start = word[0]

                if start=="[":
                    # light sequence
                    for i, c in enumerate(less):
                        if c == '#': # on
                            light += (1 << i)
                
                if start=="(":
                    val = 0
                    for n in less.split(","):
                        val += (1 << int(n))
                    buttons.append(val)
                
                if start=="{":
                    for n in less.split(","):
                        joltage.append(int(n))
            data.append((light, buttons, joltage))
    return data

def p1(filename: str):
    data = read_file(filename)
    ans = 0
    for light, buttons, _ in data:
        min_push = None
        for subset in itertools.chain.from_iterable(itertools.combinations(buttons, r) for r in range(len(buttons)+1)):
            if min_push and len(subset) >= min_push:
                continue
            # all combinations of all acceptable lengths
            val = 0
            for b in subset:
                val ^= b
            if val == light:
                min_push = len(subset)
        if not min_push:
            print(f"no min found {light} | {buttons}")
        else:
            ans += min_push
    print(ans)

def pushes_to_get_to_state(
    state: tuple[int],
    buttons: list[int],
    memo: dict[tuple[int], int],
) -> int | None:
    if state in memo:
        return memo[state]
    
    if all([s==0 for s in state]):
        # base case
        return 0
    
    # push each button once
    min_pushes = None
    for b in buttons:
        state2 = list(state)
        for i in range(len(state2)):
            if b & (1<<i) > 0:
                state2[i] -= 1
        if any([s<0 for s in state2]):
            continue

        val = pushes_to_get_to_state(tuple(state2), buttons, memo)
        if val is None:
            continue
        val += 1
        if not min_pushes or val < min_pushes:
            min_pushes = val
    
    memo[state] = min_pushes
    return min_pushes


def p2(filename: str):
    data = read_file(filename)
    ans = 0
    for _, buttons, joltage in data:
        # print(f"current ans: {ans}")

        A = [[] for _ in range(len(joltage))]
        for b in buttons:
            # each button is a row
            for i in range(len(joltage)):
                if b & (1<<i) > 0:
                    A[i].append(1)
                else:
                    A[i].append(0)

        result = scipy.optimize.linprog(
            # minimize the sum of all button presses
            c=[1]*len(buttons),
            # matrix representation of the buttons
            A_eq=A,
            # the joltage requirement
            b_eq=joltage,
            # integers only
            integrality=1, 
        )

        ans += sum(result.x)
    print(ans)


if __name__=="__main__":
    p1("data/d10_test.txt")
    p1("data/d10_real.txt")

    p2("data/d10_test.txt")
    p2("data/d10_real.txt")
            
