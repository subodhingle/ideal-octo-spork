def read_graph(filename):
    f = open(filename, 'r')
    lines = [line.strip() for line in f.readlines() if line.strip() and not line.strip().startswith('#')]
    f.close()
    if len(lines) < 2:
        raise ValueError("Input must contain at least N and E")
    N = int(lines[0])
    E = int(lines[1])
    edges = []
    for i in range(2, 2 + E):
        if i >= len(lines):
            raise ValueError("Not enough edge lines")
        s = lines[i].replace(',', ' ').split()
        if len(s) < 2:
            raise ValueError("Invalid edge line: " + lines[i])
        u, v = int(s[0]), int(s[1])
        edges.append((u, v))
    return N, E, edges

def euler_tour(N, edges):
    adj = {}
    used_edge = [False] * len(edges)
    for idx in range(len(edges)):
        u, v = edges[idx]
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    nonzero = [node for node in range(1, N + 1) if node in adj and len(adj[node]) > 0]
    if not nonzero:
        return []
    start = nonzero[0]
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node in adj:
                for y, _ in adj[node]:
                    if y not in visited:
                        stack.append(y)
    for node in nonzero:
        if node not in visited:
            return None
    for node in nonzero:
        if len(adj[node]) % 2 == 1:
            return None
    stack = [start]
    path = []
    while len(stack) > 0:
        v = stack[-1]
        while v in adj and len(adj[v]) > 0 and used_edge[adj[v][-1][1]]:
            adj[v].pop()
        if v not in adj or len(adj[v]) == 0:
            path.append(stack.pop())
        else:
            to, eid = adj[v].pop()
            if used_edge[eid]:
                continue
            used_edge[eid] = True
            stack.append(to)
    path.reverse()
    tour_edges = []
    for i in range(1, len(path)):
        tour_edges.append((path[i - 1], path[i]))
    return tour_edges

def hamiltonian_cycle(N, edges):
    adjset = [[] for _ in range(N + 1)]
    for u, v in edges:
        if 1 <= u <= N and 1 <= v <= N:
            if v not in adjset[u]:
                adjset[u].append(v)
            if u not in adjset[v]:
                adjset[v].append(u)
    if N == 0:
        return None
    for start in range(1, N + 1):
        if len(adjset[start]) == 0 and N > 1:
            continue
        path = [start]
        used = [False] * (N + 1)
        used[start] = True
        def backtrack():
            if len(path) == N:
                return path[0] in adjset[path[-1]]
            for nbr in adjset[path[-1]]:
                if not used[nbr]:
                    used[nbr] = True
                    path.append(nbr)
                    if backtrack():
                        return True
                    path.pop()
                    used[nbr] = False
            return False
        if backtrack():
            return path + [path[0]]
    return None

def main():
    args = input("Enter mode and input file name (e.g., euler input.txt): ").strip().split()
    if len(args) < 2:
        print("Usage: euler|hamiltonian input.txt")
        return
    mode = args[0].lower()
    fname = args[1]
    N, E, edges = read_graph(fname)
    if mode == 'euler':
        tour_edges = euler_tour(N, edges)
        if tour_edges is None:
            print("No Euler circuit exists.")
        elif not tour_edges:
            print("Empty Euler tour.")
        else:
            print("Euler circuit:")
            for u, v in tour_edges:
                print(u, "->", v)
    elif mode == 'hamiltonian':
        cycle = hamiltonian_cycle(N, edges)
        if cycle is None:
            print("No Hamiltonian cycle found.")
        else:
            print("Hamiltonian cycle:")
            print(" -> ".join(str(x) for x in cycle))
    else:
        print("Unknown mode.")

if __name__ == "__main__":
    main()
