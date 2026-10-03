+++
id = "catalog/lie-groups/so-6-c"
title = "SO(6,C)"
kind = "definition"
summary = "SO(6,C) as a separately identified complex Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/special-orthogonal-group", "linear-algebra/bilinear-form"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\operatorname{SO}(6,\mathbb C)\) is the [[lie-groups/special-orthogonal-group|special orthogonal group]] of \(\mathbb C^{6}\) for the [[linear-algebra/bilinear-form|bilinear form]] \(\sum_jx_jy_j\):
\[ \operatorname{SO}(6,\mathbb C)=\{A\in M_{6}(\mathbb C):A^{\mathsf T}A=I,\ \det A=1\}. \]
Over the complex numbers transpose does not mean conjugate transpose.

## Dimensions and structure

This group has real dimension \(30\), complex dimension \(15\). Its tangent algebra is the skew-symmetric \(6\times6\) matrices. The spin covering has kernel {±1}, so this group is not [[topology/simply-connected-space|simply connected]].

Its [[lie-groups/complex-lie-group|complex Lie group]] structure uses holomorphic multiplication and inversion. Forgetting the complex structure gives the [[lie-groups/underlying-real-lie-group|underlying real Lie group]]; real and holomorphic homomorphisms belong to different categories.

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §31.2, Example 31.3 and Proposition 31.4; §31.3, Example 31.10, pp. 166–168.
