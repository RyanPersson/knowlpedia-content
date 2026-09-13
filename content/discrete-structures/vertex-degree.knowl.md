+++
id = "discrete-structures/vertex-degree"
title = "Vertex degree"
kind = "definition"
summary = "The number of neighbors of a vertex in a simple undirected graph."
aliases = ["graph degree", "bounded-degree graph", "bounded degree"]
domains = ["discrete-structures"]
section_mode = "progressive"
prerequisites = ["discrete-structures/graph-vertex-edge", "shared-foundations/cardinality"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **degree** of a vertex \(v\) in a simple undirected [[discrete-structures/graph-vertex-edge|graph]] \(G=(V,E)\) is
\[
\deg_G(v)=\bigl|\{w\in V:\{v,w\}\in E\}\bigr|.
\]
It counts the neighbors of \(v\). The degree may be infinite.

## Bounded degree

The graph has **degree bounded by \(\Delta\)** if \(\deg_G(v)\le\Delta\) for every vertex, where \(\Delta\) is a fixed nonnegative integer. A graph can have infinitely many vertices and bounded degree. Requiring each degree to be finite is weaker than requiring one finite bound for all vertices.
