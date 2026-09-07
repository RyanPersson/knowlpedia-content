+++
id = "linear-algebra/closed-linear-subspace"
title = "Closed linear subspace"
kind = "knowl"
summary = "A linear subspace that is closed in the topology induced by the ambient norm."
aliases = ["closed subspace", "closed linear subspace"]
domains = ["linear-algebra", "topology"]
prerequisites = ["convex-analysis/linear-subspace", "linear-algebra/normed-vector-space", "topology/closed-set"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

A [[convex-analysis/linear-subspace|linear subspace]] \(M\) of a [[linear-algebra/normed-vector-space|normed vector space]] \(E\) is a **closed linear subspace** if it is a [[topology/closed-set|closed subset]] of \(E\) in the norm topology.

## Equivalent characterization and properties

Equivalently, if a sequence of points of \(M\) converges to \(x\in E\), then \(x\in M\).

A closed linear subspace of a [[linear-algebra/banach-space|Banach space]] is again a Banach space. In a [[linear-algebra/hilbert-space|Hilbert space]], every closed subspace \(M\) has an [[linear-algebra/orthogonal-complement|orthogonal complement]] and every vector decomposes uniquely as \(x=m+m^\perp\).
