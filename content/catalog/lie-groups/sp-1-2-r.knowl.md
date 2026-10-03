+++
id = "catalog/lie-groups/sp-1-2-r"
title = "Sp(1,2)"
kind = "definition"
summary = "Sp(1,2) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\operatorname{Sp}(1,2)\) is the real [[fiber-bundles/lie-group|Lie group]]
\[ \operatorname{Sp}(1,2)=\{A\in\mathrm{GL}(3,\mathbb H):A^*I_{1,2}A=I_{1,2}\},\qquad I_{1,2}=\operatorname{diag}(-I_{1},I_{2}). \]
The first parameter counts negative directions. The adjoint is conjugate transpose, so the form is Hermitian.

## Dimensions and structure

This group has real dimension \(21\). The definition specifies the full matrix group. It is connected. The parameters count quaternionic directions, and no quaternionic determinant condition is imposed.

The scalar field of its matrix entries does not assign a [[lie-groups/complex-lie-group|complex Lie group]] structure to this real Lie group. In particular, a [[algebra-groups/group-homomorphism|group homomorphism]] is not called linear merely because the group has a matrix representation.

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.2, Proposition 6.7 and Corollary 6.8; §6.3, Lemma 6.10, pp. 40–43.
