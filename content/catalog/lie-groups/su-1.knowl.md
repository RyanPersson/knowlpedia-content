+++
id = "catalog/lie-groups/su-1"
title = "SU(1)"
kind = "definition"
summary = "SU(1) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/special-unitary-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\operatorname{SU}(1)\) is the compact [[lie-groups/special-unitary-group|special unitary group]]
\[ \operatorname{SU}(1)=\{A\in M_{1}(\mathbb C):A^*A=I,\ \det A=1\}, \]
where \(A^*=\overline A^{\mathsf T}\). The defining Hermitian form is positive definite.

## Dimensions and structure

This group has real dimension \(0\). The tangent algebra is formed by skew-Hermitian complex matrices of trace zero. The determinant-one condition makes this the trivial group.

The scalar field of its matrix entries does not assign a [[lie-groups/complex-lie-group|complex Lie group]] structure to this real [[fiber-bundles/lie-group|Lie group]]. In particular, a [[algebra-groups/group-homomorphism|group homomorphism]] is not called linear merely because the group has a matrix representation.

Both groups consist of the identity alone. See [[catalog/lie-groups/sl-1-r|\(\operatorname{SL}(1,\mathbb R)\)]].

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
