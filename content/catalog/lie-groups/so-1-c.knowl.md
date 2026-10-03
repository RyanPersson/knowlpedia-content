+++
id = "catalog/lie-groups/so-1-c"
title = "SO(1,C)"
kind = "definition"
summary = "SO(1,C) as a separately identified complex Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/special-orthogonal-group", "linear-algebra/bilinear-form"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\operatorname{SO}(1,\mathbb C)\) is the [[lie-groups/special-orthogonal-group|special orthogonal group]]
\[ \operatorname{SO}(1,\mathbb C)=\{A\in M_{1}(\mathbb C):A^{\mathsf T}A=I,\ \det A=1\}, \]
with matrix multiplication. The preserved form is the complex [[linear-algebra/bilinear-form|bilinear form]] \(\sum_j x_jy_j\); transpose here does not include complex conjugation.

## Dimensions and structure

This group has real dimension \(0\), complex dimension \(0\). Its tangent algebra consists of skew-symmetric matrices, \(X^{\mathsf T}+X=0\). The determinant-one subgroup is trivial. A Hermitian form would instead lead to a real unitary group; the complex [[lie-groups/orthogonal-group|orthogonal group]] uses a bilinear form.

Its [[lie-groups/complex-lie-group|complex Lie group]] structure uses holomorphic multiplication and inversion. Forgetting the complex structure gives the [[lie-groups/underlying-real-lie-group|underlying real Lie group]]; real and holomorphic homomorphisms belong to different categories.

The determinant-one subgroup includes by the identity on matrices. See [[catalog/lie-groups/o-1-c|\(\operatorname{O}(1,\mathbb C)\)]].

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
