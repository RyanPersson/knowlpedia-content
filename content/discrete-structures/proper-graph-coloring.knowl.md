+++
id = "discrete-structures/proper-graph-coloring"
title = "Proper graph coloring"
kind = "definition"
summary = "Assignment of colors to vertices so adjacent vertices receive different colors."
aliases = ["graph coloring", "proper vertex coloring"]
domains = ["discrete-structures"]
section_mode = "progressive"
prerequisites = ["discrete-structures/graph-vertex-edge", "shared-foundations/function", "shared-foundations/finite-set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **proper vertex coloring** of a [[discrete-structures/graph-vertex-edge|graph]] \(G=(V,E)\) by a color set \(C\) is a function \(c:V\to C\) satisfying
\[
\{u,v\}\in E\ \Longrightarrow\ c(u)\ne c(v).
\]
A proper \(k\)-coloring uses \(C=\{1,\ldots,k\}\). Some available colors may be unused.

## Interpretation

Each color class contains no adjacent pair. If adjacency represents two supports that can interact, one color can be reused at vertices whose supports cannot interact. A coloring only encodes the adjacency rule used to construct the graph; it does not establish that the rule captures all relevant interactions.

## References

- [Tait, Introduction to Combinatorics, Proposition 3.1.10 (greedy coloring)](https://www.math.cmu.edu/users/math/mtait/301/Notes.pdf).
