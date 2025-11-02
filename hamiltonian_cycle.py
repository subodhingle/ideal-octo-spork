
def read_graph(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    N = int(lines[0])
    E = int(lines[1])
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    for line in lines[2:]:
        u, v = map(int, line.split(','))
        adj[u][v] = 1
        adj[v][u] = 1
    return adj, N


def is_safe(v, pos, path, adj):
    if adj[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True


def ham_cycle_util(adj, path, pos, N):
    if pos == N:
        if adj[path[pos - 1]][path[0]] == 1:
            return True
        return False

    for v in range(2, N + 1):
        if is_safe(v, pos, path, adj):
            path[pos] = v
            if ham_cycle_util(adj, path, pos + 1, N):
                return True
            path[pos] = -1
    return False


def find_hamiltonian_cycle(adj, N):
    path = [-1] * N
    path[0] = 1  # start from vertex 1
    if not ham_cycle_util(adj, path, 1, N):
        print("No Hamiltonian cycle exists")
    else:
        print("Hamiltonian Cycle:", " -> ".join(map(str, path + [path[0]])))


if __name__ == "__main__":
    filename = input("Enter graph input file: ").strip()
    adj, N = read_graph(filename)
    find_hamiltonian_cycle(adj, N)
