+++
id = "catalog/lie-groups/so-8-r"
title = "SO(8,R)"
kind = "definition"
summary = "SO(8,R) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/special-orthogonal-group", "linear-algebra/bilinear-form"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\operatorname{SO}(8,\mathbb R)\) is the [[lie-groups/special-orthogonal-group|special orthogonal group]] of \(\mathbb R^{8}\) for the [[linear-algebra/bilinear-form|bilinear form]] \(\sum_jx_jy_j\):
\[ \operatorname{SO}(8,\mathbb R)=\{A\in M_{8}(\mathbb R):A^{\mathsf T}A=I,\ \det A=1\}. \]

## Dimensions and structure

This group has real dimension \(28\). Its tangent algebra is the skew-symmetric \(8\times8\) matrices. The spin covering has kernel {±1}, so this group is not [[topology/simply-connected-space|simply connected]]. Dimension eight is the setting for [[lie-groups/spin8-triality|triality]]; the vector and two [[lie-groups/half-spin-representation|half-spin representations]] live naturally on the [[lie-groups/spin-group|spin group]].

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §31.2, Example 31.3 and Proposition 31.4; §31.3, Example 31.10, pp. 166–168.
