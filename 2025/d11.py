def read_file(filename: str) -> dict[str, list[str]]:
    graph = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            parts = line.strip().replace(":","").split()
            graph[parts[0]] = parts[1:]
    return graph

def p1(filename: str):
    graph = read_file(filename)

    paths = 0
    queue = ["you"]
    while queue:
        label = queue.pop()
        if label == "out":
            paths += 1
            continue
        queue.extend(graph[label])
    
    print(paths)

def paths_from_state(graph, state, seen):
    if state in seen:
        return seen[state]

    label, seen_dac, seen_fft = state
    if label == 'out':
        if seen_dac and seen_fft:
            return 1
        else:
            return 0
    if label == 'dac':
        seen_dac = True
    if label == 'fft':
        seen_fft = True
    
    paths_from_here = sum([paths_from_state(graph, (l, seen_dac, seen_fft), seen) for l in graph[label]])
    seen[state] = paths_from_here
    return paths_from_here


def p2(filename: str):
    graph = read_file(filename)
    paths = paths_from_state(graph, ("svr", False, False), {})
    print(paths)

if __name__=="__main__":
    p1("data/d11_test.txt")
    p1("data/d11_real.txt")
        
    p2("data/d11_test_2.txt")
    p2("data/d11_real.txt")