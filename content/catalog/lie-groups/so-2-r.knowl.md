+++
id = "catalog/lie-groups/so-2-r"
title = "SO(2,R)"
kind = "definition"
summary = "SO(2,R) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/special-orthogonal-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\operatorname{SO}(2,\mathbb R)\) is the [[lie-groups/special-orthogonal-group|special orthogonal group]]
\[ \operatorname{SO}(2,\mathbb R)=\{A\in M_{2}(\mathbb R):A^{\mathsf T}A=I,\ \det A=1\}, \]
with matrix multiplication. The preserved form is the positive-definite real Euclidean form.

## Dimensions and structure

This group has real dimension \(1\). Its tangent algebra consists of skew-symmetric matrices, \(X^{\mathsf T}+X=0\). It is connected.

The determinant-one subgroup includes by the identity on matrices. See [[catalog/lie-groups/o-2-r|\(\operatorname{O}(2,\mathbb R)\)]].

The map \(\left(\begin{smallmatrix}a&-b\\b&a\end{smallmatrix}\right)\mapsto a+ib\) is a real [[fiber-bundles/lie-group|Lie group]] isomorphism. See [[lie-groups/example-u1-circle|\(\operatorname{U}(1)\)]].

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
