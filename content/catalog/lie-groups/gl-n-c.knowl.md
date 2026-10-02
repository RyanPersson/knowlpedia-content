+++
id = "catalog/lie-groups/gl-n-c"
title = "GL(n,C)"
kind = "definition"
summary = "GL(n,C) as a separately identified complex Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/general-linear-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

For every integer \(n\ge1\), \(\operatorname{GL}(n,\mathbb C)\) is the [[lie-groups/general-linear-group|general linear group]]
\[ \operatorname{GL}(n,\mathbb C)=\{A\in M_{n}(\mathbb C):\det A\ne0\}, \]
with matrix multiplication and its usual complex analytic manifold structure.

## Dimensions and structure

This group has real dimension \(2(n^2)\), complex dimension \(n^2\). It is open in the space of all matrices. Its tangent algebra consists of all matrices with the commutator bracket. It is connected; its [[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]] is the unitary group of the same matrix size.

Its [[lie-groups/complex-lie-group|complex Lie group]] structure uses holomorphic multiplication and inversion. Forgetting the complex structure gives the [[lie-groups/underlying-real-lie-group|underlying real Lie group]]; real and holomorphic homomorphisms belong to different categories.

The projectivization map has kernel all nonzero scalar matrices. See [[catalog/lie-groups/pgl-n-c|\(\operatorname{PGL}(n,\mathbb C)\)]].

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
