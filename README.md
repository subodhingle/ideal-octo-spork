An analysis of pairs of easy vs hard graph/combinatorial problems (e.g. Euler tour vs Hamiltonian cycle), discussing why the hard versions are hard.
Implementations of two algorithms from scratch (no graph libraries):
Euler tour (Hierholzer's algorithm) — finds an Eulerian trail/circuit when one exists.
Hamiltonian cycle (backtracking / DFS with pruning) — attempts to find a Hamiltonian cycle (NP-hard problem; approach is exponential in the worst case).
The goal is both theoretical (understand complexity differences) and practical (implement graph data structures and algorithms from the ground up).
This project studies these pairs of problems:
Euler tour vs Hamiltonian cycle
Shortest path vs Longest path
2-CNF (2-SAT) vs 3-CNF (3-SAT)
Minimum Spanning Tree (MST) vs Traveling Salesman Problem (TSP)
Why the hard problems are harder (intuitive summary)
Structure vs. global constraints. The easy variants usually rely on local structural properties that can be checked or constructed greedily or using dynamic programming (e.g., MST, shortest paths, Euler tour). Hard variants usually require satisfying global constraints simultaneously (Hamiltonian cycle, TSP, 3-SAT), producing a combinatorial explosion of possibilities.
Algebraic / matroid properties. Problems like MST benefit from matroid or greedy-optimality properties that guarantee local choices lead to global optimality. Hard problems typically lack such structure.
Existence vs. optimization. Euler tour and 2-SAT are existence problems with polynomial-time decision procedures (2-SAT via implication graph SCCs). Hamiltonian cycle and 3-SAT are NP-complete: verifying a given solution is easy, but finding one requires searching a huge solution space in the worst case.
Reduction hardness. Many hard problems are proven hard because classic NP-complete problems can be reduced to them (e.g., 3-SAT → Hamiltonian Cycle). This gives a formal basis for believing no poly-time algorithm exists (unless P = NP).
Summary: the hard problems force one to combine many local choices so they satisfy a global constraint; there is no known efficient procedure (no greedy matroid-like property or simple DP) that always avoids exponential search.
Repository structure
README.md                    # this file
src/
  euler_tour.[c|cpp|py|java]  # Hierholzer implementation (one file per language variant)
  hamiltonian.[c|cpp|py|java] # Backtracking implementation for Hamiltonian cycle
  graph.[c|cpp|py|java]       # Graph data structure used by both algorithms
examples/
  sample_graph.txt            # sample input file
  euler_example.txt
  hamiltonian_example.txt
docs/
  analysis.md                 # Deeper write-up about easy vs hard problems
LICENSE
Input file format
Programs read a text file with the following exact format (no external graph libraries used):
N
E
Ns1, Ne1
Ns2, Ne2
...
NsE, NeE
N — number of nodes (positive integer). Nodes are assumed to be labeled 1..N (or 0..N-1 depending on implementation; check the program's README header or command-line flag).
E — number of edges (positive integer).
Each of the next E lines contains the start and end node of an edge separated by a comma (and optional spaces), e.g. 1, 2.
Notes:
The graph may be interpreted as undirected or directed depending on which program you run. By default the Euler Tour implementation assumes the input is undirected unless the program's command-line flag sets --directed.
Multiple edges and self-loops are allowed if the implementation supports them (Euler tour implementation must handle multiple edges correctly).
Algorithmic notes
Euler tour — Hierholzer's algorithm (used in euler_tour.*)
Complexity: O(V + E) using adjacency lists.
Works for undirected graphs when all vertices with non-zero degree belong to a single connected component and each vertex has even degree for an Euler circuit (or exactly 0 or 2 odd-degree vertices for an Euler trail).
Implementation details: adjacency lists + multiset handling for multiple edges. Maintain an explicit stack for current path and build final path by edge-removal.
Hamiltonian cycle — Backtracking (used in hamiltonian.*)
Complexity: worst-case O(N!) but with pruning and heuristics can handle small graphs.
Implementation details: simple DFS/backtracking that keeps visited flags and builds a path; backtracks when no unvisited neighbors remain. Useful heuristics: degree ordering, early stopping when remaining vertices can't possibly close a cycle.
The Hamiltonian Cycle decision problem is NP-complete; this implementation is intended for studying and small experiments, not large-scale graphs.
Sample input (undirected graph)
5
6
1, 2
2, 3
3, 4
4, 1
1, 3
3, 5
Use this file to test both programs — one may choose the graph that has an Eulerian circuit (if degrees are even) or a Hamiltonian cycle (if it exists).
Testing and validation
Unit tests (recommended): small graphs covering cases such as:
Euler: disconnected graph, graph with odd degrees, graphs with parallel edges and loops, and a valid Eulerian circuit.
Hamiltonian: small graphs with known Hamiltonian cycles and graphs with no Hamiltonian cycle.
Compare outputs against known answers and visualize small graphs using any graph viewer.
