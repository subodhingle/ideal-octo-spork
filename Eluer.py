def read_graph(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    N = int(lines[0])
    E = int(lines[1])
    adj = {i: [] for i in range(1, N + 1)}
    for line in lines[2:]:
        u, v = map(int, line.split(','))
        adj[u].append(v)
        adj[v].append(u)
    return adj, N, E


def is_eulerian(adj):
    odd = [v for v in adj if len(adj[v]) % 2 != 0]
    if len(odd) == 0:
        return "circuit"
    elif len(odd) == 2:
        return "trail"
    else:
        return "none"


def find_euler_tour(adj):
    graph = {u: adj[u][:] for u in adj}  # copy
    start = next((v for v in graph if len(graph[v]) > 0), None)
    if not start:
        return []
    stack, path = [start], []
    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v].pop()
            graph[u].remove(v)
            stack.append(u)
        else:
            path.append(stack.pop())
    return path[::-1]


if __name__ == "__main__":
    filename = input("Enter graph input file: ").strip()
    adj, N, E = read_graph(filename)
    euler_type = is_eulerian(adj)

    print(f"Euler Type: {euler_type}")
    if euler_type == "none":
        print("No Euler tour or trail exists for this graph.")
    else:
        tour = find_euler_tour(adj)
        print("Euler Tour/Trail:", " -> ".join(map(str, tour)))
