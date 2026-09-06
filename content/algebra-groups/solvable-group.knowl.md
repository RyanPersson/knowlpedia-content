+++
id = "algebra-groups/solvable-group"
title = "Solvable Group"
kind = "knowl"
summary = "A group whose derived series terminates at the trivial subgroup"
aliases = ["solvable-group", "Solvable Group"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group", "algebra-groups/derived-series", "algebra-groups/trivial-subgroup", "algebra-groups/commutator-subgroup"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "algebra-groups/solvable-group.md"
+++

A **solvable group** is a [[algebra-groups/group|group]] \(G\) whose [[algebra-groups/derived-series|derived series]] reaches the [[algebra-groups/trivial-subgroup|trivial subgroup]] after finitely many steps. Explicitly, there is an integer \(n\ge 0\) such that \(G^{(n)}=\{e\}\), where
\[
G^{(0)}=G,
\qquad
G^{(k+1)}=[G^{(k)},G^{(k)}].
\]
Here \([G^{(k)},G^{(k)}]\) is the [[algebra-groups/commutator-subgroup|commutator subgroup]] of \(G^{(k)}\).

## Examples

- Every abelian group is solvable: \(G^{(1)}=\{e\}\).
- \(S_3\) is solvable.
- *(Non-example)* \(A_5\) is not solvable.

## Equivalent characterizations

Equivalently, \(G\) is solvable iff it has a finite [[algebra-groups/subnormal-series|subnormal series]] whose successive quotients are [[algebra-groups/abelian-group|abelian]].
