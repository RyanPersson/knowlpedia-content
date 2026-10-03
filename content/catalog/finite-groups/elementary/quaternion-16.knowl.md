+++
id = "catalog/finite-groups/elementary/quaternion-16"
title = "Generalized quaternion group Q_16"
kind = "definition"
summary = "A cyclic subgroup of index two with the generalized quaternion presentation."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/group-presentation"]
dependency_heuristic = "finite-elementary-semantic-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

the **generalized quaternion group \(Q_{16}\)** is the [[algebra-groups/group-presentation|group with presentation]]
\[
Q_{16}=\langle a,b\mid a^{8}=1,\quad b^2=a^{4},\quad bab^{-1}=a^{-1}\rangle.
\]

## Order and nonsimplicity

Every element has a unique form \(a^j\) or \(a^jb\), with \(0\leq j<8\), so the order is \(16\). The element \(a^{4}\) has order two and generates the center. This proper nontrivial [[algebra-groups/normal-subgroup|normal subgroup]] shows that the group is not simple.

## Smallest member

At \(n=3\), the assignments \(a\mapsto i\), \(b\mapsto j\) identify this presentation with the [[algebra-groups/quaternion-group|quaternion group \(Q_8\)]].

## References

- [J. S. Milne, Group Theory, v4.01](https://www.jmilne.org/math/CourseNotes/GT.pdf), §1.18, p. 14; Example 2.7(b), p. 35: generalized quaternion groups.
