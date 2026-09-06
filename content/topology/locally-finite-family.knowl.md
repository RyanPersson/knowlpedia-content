+++
id = "topology/locally-finite-family"
title = "Locally finite family"
kind = "definition"
summary = "A family of subsets for which every point has a neighborhood meeting only finitely many members."
aliases = ["locally finite collection", "local finiteness of a family"]
domains = ["topology"]
prerequisites = ["topology/topological-space", "shared-foundations/indexed-family-of-sets"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A family \(\{A_i\}_{i\in I}\) of subsets of a topological space \(X\) is
**locally finite** if every point \(x\in X\) has a neighborhood that meets
only finitely many of the sets \(A_i\).

## Consequences

If \(\{A_i\}\) is locally finite, then its subfamilies are locally finite and
the union of the closures satisfies

\[
\overline{\bigcup_i A_i}=\bigcup_i\overline{A_i}.
\]

Local finiteness lets constructions indexed by \(I\) reduce to finite ones
near each point. In particular, a partition of unity is locally a finite sum
because the family of supports of its functions is locally finite.

## Distinction from point finiteness

Point finiteness requires each point to belong to only finitely many \(A_i\).
Local finiteness is stronger: a whole neighborhood must meet only finitely
many members.

## References

1. James R. Munkres, *Topology*, 2nd ed., Prentice Hall, 2000. Relevant: locally finite families and partitions of unity.
