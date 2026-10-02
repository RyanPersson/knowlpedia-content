+++
id = "catalog/lie-groups/gl-3-c"
title = "GL(3,C)"
kind = "definition"
summary = "GL(3,C) as a separately identified complex Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/general-linear-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\operatorname{GL}(3,\mathbb C)\) is the [[lie-groups/general-linear-group|general linear group]]
\[ \operatorname{GL}(3,\mathbb C)=\{A\in M_{3}(\mathbb C):\det A\ne0\}, \]
with matrix multiplication and its usual complex analytic manifold structure.

## Dimensions and structure

This group has real dimension \(18\), complex dimension \(9\). It is open in the space of all matrices. Its tangent algebra consists of all matrices with the commutator bracket. It is connected; its [[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]] is the unitary group of the same matrix size.

Its [[lie-groups/complex-lie-group|complex Lie group]] structure uses holomorphic multiplication and inversion. Forgetting the complex structure gives the [[lie-groups/underlying-real-lie-group|underlying real Lie group]]; real and holomorphic homomorphisms belong to different categories.

The projectivization map has kernel all nonzero scalar matrices. See [[catalog/lie-groups/pgl-3-c|\(\operatorname{PGL}(3,\mathbb C)\)]].

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
