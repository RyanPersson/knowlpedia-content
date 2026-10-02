+++
id = "discrete-structures/ramanujan-graph"
title = "Ramanujan graph"
kind = "definition"
summary = "A finite connected regular graph whose nontrivial adjacency eigenvalues lie in the tree spectral interval."
aliases = ["Ramanujan graphs", "bipartite Ramanujan graph"]
domains = ["discrete-structures"]
section_mode = "progressive"
prerequisites = ["discrete-structures/finite-graph", "discrete-structures/vertex-degree", "linear-algebra/eigenvalue"]
dependency_heuristic = "transcript-connections-semantic-v1"
dependency_review_count = 1
+++
A finite connected undirected simple [[discrete-structures/finite-graph|graph]] of constant [[discrete-structures/vertex-degree|degree]] \(d\ge2\) is a **Ramanujan graph** if every [[linear-algebra/eigenvalue|eigenvalue]] \(\lambda\) of its adjacency matrix other than the trivial eigenvalues satisfies
\[
|\lambda|\le2\sqrt{d-1}.
\]
The adjacency matrix has entry \(1\) at adjacent vertex pairs and \(0\) elsewhere. The trivial eigenvalue is \(d\), together with \(-d\) when the graph is bipartite. Here bipartite means that the vertices split into two sets with every edge joining the two sets.

## Bipartite convention

The negative eigenvalue \(-d\) is excluded in the bipartite case. Consequently bipartite graphs can be Ramanujan; imposing the displayed bound on \(-d\) would rule them out for \(d>2\).

## Quaternionic constructions

The Lubotzky–Phillips–Sarnak construction produces arithmetic families of [[discrete-structures/cayley-graph|Cayley graphs]] from quaternionic data. The spectral estimate is a theorem about those constructions, not a property of an arbitrary Cayley graph.

## References

1. Adam W. Marcus, Daniel A. Spielman, and Nikhil Srivastava, *Interlacing Families I: Bipartite Ramanujan Graphs of All Degrees*, [author-hosted paper](https://www.cs.yale.edu/homes/spielman/PAPERS/lifts.pdf), §2.1, p. 2.
