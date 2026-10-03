+++
id = "catalog/lie-groups/o-n-r"
title = "O(n,R)"
kind = "definition"
summary = "O(n,R) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/orthogonal-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

For every integer \(n\ge1\), \(\operatorname{O}(n,\mathbb R)\) is the [[lie-groups/orthogonal-group|orthogonal group]]
\[ \operatorname{O}(n,\mathbb R)=\{A\in M_{n}(\mathbb R):A^{\mathsf T}A=I\}, \]
with matrix multiplication. The preserved form is the positive-definite real Euclidean form.

## Dimensions and structure

This group has real dimension \(n(n-1)/2\). Its tangent algebra consists of skew-symmetric matrices, \(X^{\mathsf T}+X=0\). It has two [[topology/connected-component|connected components]] distinguished by determinant.

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
