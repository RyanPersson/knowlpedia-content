+++
id = "discrete-structures/greedy-coloring-bounded-degree"
title = "Greedy coloring of a countable bounded-degree graph"
kind = "theorem"
summary = "A countable graph of degree at most Delta has a proper coloring with Delta plus one colors."
aliases = []
domains = ["discrete-structures"]
section_mode = "progressive"
prerequisites = ["discrete-structures/countable-graph", "discrete-structures/vertex-degree", "discrete-structures/proper-graph-coloring", "shared-foundations/mathematical-induction"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Every [[discrete-structures/countable-graph|countable graph]] with degree at most \(\Delta<\infty\) has a proper \((\Delta+1)\)-coloring.

## Greedy proof

Enumerate the vertices. At step \(j\), at most \(\Delta\) previously colored neighbors of \(v_j\) can forbid colors. Choose any of the \(\Delta+1\) colors that remains. Induction defines a color at every step. For an edge, the later endpoint receives a color different from the earlier endpoint, proving properness. A finite graph uses the same argument with a finite enumeration.

The bound uses the degree, not the number of vertices. No limiting recoloring argument is needed for a countably infinite graph.

## References

- [Tait, Introduction to Combinatorics, Proposition 3.1.10 (greedy coloring)](https://www.math.cmu.edu/users/math/mtait/301/Notes.pdf).
