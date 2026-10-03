+++
id = "catalog/lie-groups/gl-2-h"
title = "GL(2,H)"
kind = "definition"
summary = "GL(2,H) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\mathrm{GL}(2,\mathbb H)\) is the real [[fiber-bundles/lie-group|Lie group]] of invertible right-quaternionic-linear maps of \(\mathbb H^{2}\), with composition as multiplication. Here a choice \(\mathbb C\subset\mathbb H\) identifies \(\mathbb H^{2}\) with \(\mathbb C^{4}\) and gives \(\rho(A)\).

## Dimensions and structure

This group has real dimension \(16\). The complex determinant of this realization is positive real for every invertible quaternionic matrix. Invertibility is openness in the underlying real matrix space. Quaternionic polar decomposition gives a deformation retraction onto Sp(2).

The scalar field of its matrix entries does not assign a [[lie-groups/complex-lie-group|complex Lie group]] structure to this real Lie group. In particular, a [[algebra-groups/group-homomorphism|group homomorphism]] is not called linear merely because the group has a matrix representation.

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.2, Proposition 6.7 and Corollary 6.8; §6.3, Lemma 6.10, pp. 40–43.
