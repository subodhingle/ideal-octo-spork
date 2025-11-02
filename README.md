Euler Tour & Hamiltonian Cycle 

This repository contains:

An analysis of pairs of easy vs hard graph/combinatorial problems (e.g. Euler tour vs Hamiltonian cycle), discussing why the hard versions are hard.

Implementations of two algorithms from scratch (no graph libraries):

Euler tour (Hierholzer's algorithm) — finds an Eulerian trail/circuit when one exists.

Hamiltonian cycle (backtracking / DFS with pruning) — attempts to find a Hamiltonian cycle (NP-hard problem; approach is exponential in the worst case).

The goal is both theoretical (understand complexity differences) and practical (implement graph data structures and algorithms from the ground up).

Motivation: easy vs hard problem pairs

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
