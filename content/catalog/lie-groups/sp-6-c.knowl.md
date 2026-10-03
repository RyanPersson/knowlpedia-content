+++
id = "catalog/lie-groups/sp-6-c"
title = "Sp(6,C)"
kind = "definition"
summary = "Sp(6,C) as a separately identified complex Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/symplectic-group", "linear-algebra/bilinear-form"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\mathrm{Sp}(6,\mathbb C)\) is the [[lie-groups/symplectic-group|symplectic group]]
\[ \mathrm{Sp}(6,\mathbb C)=\{A\in\mathrm{GL}(6,\mathbb C):A^{\mathsf T}JA=J\},\qquad J=\begin{pmatrix}0&I_{3}\\-I_{3}&0\end{pmatrix}. \]
It preserves the displayed nondegenerate alternating [[linear-algebra/bilinear-form|bilinear form]].

## Dimensions and structure

This group has real dimension \(42\), complex dimension \(21\). The parameter \(3\) is the number of symplectic pairs, while the matrix size is \(6\). Its tangent matrices have block form \(\left(\begin{smallmatrix}P&Q\\R&-P^{\mathsf T}\end{smallmatrix}\right)\) with \(Q=Q^{\mathsf T}\) and \(R=R^{\mathsf T}\). Counting these blocks gives the dimension. This is a connected [[topology/simply-connected-space|simply connected]] [[lie-groups/complex-lie-group|complex Lie group]].

Its complex Lie group structure uses holomorphic multiplication and inversion. Forgetting the complex structure gives the [[lie-groups/underlying-real-lie-group|underlying real Lie group]]; real and holomorphic homomorphisms belong to different categories.

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
