+++
id = "catalog/lie-groups/so-1-1-r"
title = "SO(1,1)"
kind = "definition"
summary = "SO(1,1) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\operatorname{SO}(1,1)\) is the real [[fiber-bundles/lie-group|Lie group]]
\[ \operatorname{SO}(1,1)=\{A\in\mathrm{GL}(2,\mathbb R):A^{\mathsf T}I_{1,1}A=I_{1,1},\ \det A=1\},\qquad I_{1,1}=\operatorname{diag}(-I_{1},I_{1}). \]
The first parameter counts negative directions. The form is real symmetric bilinear.

## Dimensions and structure

This group has real dimension \(1\). The definition specifies the full matrix group. When both signature entries are positive it has two components; its [[lie-groups/identity-component-of-a-lie-group|identity component]] is written SO⁺(p,q). Determinant one alone does not impose [[differential-geometry/time-orientation|time orientation]].

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
