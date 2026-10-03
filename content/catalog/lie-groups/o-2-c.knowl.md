+++
id = "catalog/lie-groups/o-2-c"
title = "O(2,C)"
kind = "definition"
summary = "O(2,C) as a separately identified complex Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/orthogonal-group", "linear-algebra/bilinear-form"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\operatorname{O}(2,\mathbb C)\) is the [[lie-groups/orthogonal-group|orthogonal group]]
\[ \operatorname{O}(2,\mathbb C)=\{A\in M_{2}(\mathbb C):A^{\mathsf T}A=I\}, \]
with matrix multiplication. The preserved form is the complex [[linear-algebra/bilinear-form|bilinear form]] \(\sum_j x_jy_j\); transpose here does not include complex conjugation.

## Dimensions and structure

This group has real dimension \(2\), complex dimension \(1\). Its tangent algebra consists of skew-symmetric matrices, \(X^{\mathsf T}+X=0\). It has two [[topology/connected-component|connected components]] distinguished by determinant. A Hermitian form would instead lead to a real unitary group; the complex orthogonal group uses a bilinear form.

Its [[lie-groups/complex-lie-group|complex Lie group]] structure uses holomorphic multiplication and inversion. Forgetting the complex structure gives the [[lie-groups/underlying-real-lie-group|underlying real Lie group]]; real and holomorphic homomorphisms belong to different categories.

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
