+++
id = "catalog/lie-groups/sp-6-r"
title = "Sp(6,R)"
kind = "definition"
summary = "Sp(6,R) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/symplectic-group", "linear-algebra/bilinear-form"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\mathrm{Sp}(6,\mathbb R)\) is the [[lie-groups/symplectic-group|symplectic group]]
\[ \mathrm{Sp}(6,\mathbb R)=\{A\in\mathrm{GL}(6,\mathbb R):A^{\mathsf T}JA=J\},\qquad J=\begin{pmatrix}0&I_{3}\\-I_{3}&0\end{pmatrix}. \]
It preserves the displayed nondegenerate alternating [[linear-algebra/bilinear-form|bilinear form]].

## Dimensions and structure

This group has real dimension \(21\). The parameter \(3\) is the number of symplectic pairs, while the matrix size is \(6\). Its tangent matrices have block form \(\left(\begin{smallmatrix}P&Q\\R&-P^{\mathsf T}\end{smallmatrix}\right)\) with \(Q=Q^{\mathsf T}\) and \(R=R^{\mathsf T}\). Counting these blocks gives the dimension. This is the noncompact split real form, distinct from compact quaternionic Sp(3).

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
