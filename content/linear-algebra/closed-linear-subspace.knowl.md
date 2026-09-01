+++
id = "linear-algebra/closed-linear-subspace"
title = "Closed linear subspace"
kind = "knowl"
summary = "A linear subspace that is closed in the topology induced by the ambient norm."
aliases = ["closed subspace", "closed linear subspace"]
domains = ["linear-algebra", "topology"]
prerequisites = ["convex-analysis/linear-subspace", "linear-algebra/normed-vector-space", "linear-algebra/banach-space", "linear-algebra/hilbert-space", "linear-algebra/orthogonal-complement"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
+++

A [[convex-analysis/linear-subspace|linear subspace]] \(M\) of a [[linear-algebra/normed-vector-space|normed vector space]] \(E\) is **closed** if it contains the limit of every convergent sequence of points of \(M\). Equivalently, its complement is open in the subspace topology inherited from \(E\).

A closed linear subspace of a [[linear-algebra/banach-space|Banach space]] is again a Banach space. In a [[linear-algebra/hilbert-space|Hilbert space]], every closed subspace \(M\) has an [[linear-algebra/orthogonal-complement|orthogonal complement]] and every vector decomposes uniquely as \(x=m+m^\perp\).
