+++
id = "catalog/lie-groups/sl-1-h"
title = "SL(1,H)"
kind = "definition"
summary = "SL(1,H) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\mathrm{SL}(1,\mathbb H)\) is the real [[fiber-bundles/lie-group|Lie group]] of quaternionic-linear invertible maps of the right module \(\mathbb H^{1}\) with \(\det_{\mathbb C}\rho(A)=1\), with composition as multiplication. Here a choice \(\mathbb C\subset\mathbb H\) identifies \(\mathbb H^{1}\) with \(\mathbb C^{2}\) and gives \(\rho(A)\).

## Dimensions and structure

This group has real dimension \(3\). The complex determinant of this realization is positive real for every invertible quaternionic matrix. The determinant-one equation means reduced norm one; it is not the naive Leibniz determinant of a noncommutative matrix. In size one this is the unit-quaternion group Sp(1).

The scalar field of its matrix entries does not assign a [[lie-groups/complex-lie-group|complex Lie group]] structure to this real Lie group. In particular, a [[algebra-groups/group-homomorphism|group homomorphism]] is not called linear merely because the group has a matrix representation.

For a single quaternion, the determinant of its complex realization is its squared norm. The determinant-one group is precisely the unit quaternions. See [[catalog/lie-groups/sp-1|\(\operatorname{Sp}(1)\)]].

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.2, Proposition 6.7 and Corollary 6.8; §6.3, Lemma 6.10, pp. 40–43.
