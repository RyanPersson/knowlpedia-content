+++
id = "catalog/lie-groups/su-p-q-r"
title = "SU(p,q)"
kind = "definition"
summary = "SU(p,q) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

For nonnegative integers \(p,q\) with \(p+q\ge1\), \(\operatorname{SU}(p,q)\) is the real [[fiber-bundles/lie-group|Lie group]]
\[ \operatorname{SU}(p,q)=\{A\in\mathrm{GL}(p+q,\mathbb C):A^*I_{p,q}A=I_{p,q},\ \det A=1\},\qquad I_{p,q}=\operatorname{diag}(-I_{p},I_{q}). \]
The first parameter counts negative directions. The adjoint is conjugate transpose, so the form is Hermitian.

## Dimensions and structure

This group has real dimension \((p+q)^2-1\). The definition specifies the full matrix group. It is connected.

The scalar field of its matrix entries does not assign a [[lie-groups/complex-lie-group|complex Lie group]] structure to this real Lie group. In particular, a [[algebra-groups/group-homomorphism|group homomorphism]] is not called linear merely because the group has a matrix representation.

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
