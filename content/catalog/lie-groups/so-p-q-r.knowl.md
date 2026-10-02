+++
id = "catalog/lie-groups/so-p-q-r"
title = "SO(p,q)"
kind = "definition"
summary = "SO(p,q) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

For nonnegative integers \(p,q\) with \(p+q\ge1\), \(\operatorname{SO}(p,q)\) is the real [[fiber-bundles/lie-group|Lie group]]
\[ \operatorname{SO}(p,q)=\{A\in\mathrm{GL}(p+q,\mathbb R):A^{\mathsf T}I_{p,q}A=I_{p,q},\ \det A=1\},\qquad I_{p,q}=\operatorname{diag}(-I_{p},I_{q}). \]
The first parameter counts negative directions. The form is real symmetric bilinear.

## Dimensions and structure

This group has real dimension \((p+q)(p+q-1)/2\). The definition specifies the full matrix group. When both signature entries are positive it has two components; its [[lie-groups/identity-component-of-a-lie-group|identity component]] is written SO⁺(p,q). Determinant one alone does not impose [[differential-geometry/time-orientation|time orientation]].

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
