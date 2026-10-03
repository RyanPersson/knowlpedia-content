+++
id = "catalog/lie-groups/heisenberg-3-r"
title = "Heisenberg H_7(R)"
kind = "definition"
summary = "Heisenberg H_7(R) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/heisenberg-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

the [[lie-groups/heisenberg-group|Heisenberg group]] \(H_{7}(\mathbb R)\) has underlying manifold \(\mathbb R^{3}\times \mathbb R^{3}\times \mathbb R\) and multiplication
\[ (x,y,z)(x^{\prime},y^{\prime},z^{\prime})=\bigl(x+x^{\prime},y+y^{\prime},z+z^{\prime}+\tfrac12(x\cdot y^{\prime}-y\cdot x^{\prime})\bigr). \]
The dot product is bilinear \(x\cdot y=\sum_jx_jy_j\) (no complex conjugation). The subscript denotes dimension over the displayed field, while the catalogue parameter counts pairs of noncentral coordinates.

## Dimensions and structure

This group has real dimension \(7\). The inverse is \((-x,-y,-z)\) and the commutator is \((0,0,x\cdot y^{\prime}-y\cdot x^{\prime})\). Thus the center and [[algebra-groups/commutator-subgroup|commutator subgroup]] are exactly the last coordinate, and the group is two-step nilpotent. Bilinearity of the central term verifies associativity. The underlying affine space makes the group connected and [[topology/simply-connected-space|simply connected]].

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §49.1, Example 49.2, p. 266; general-coordinate associativity and commutator verified directly.
