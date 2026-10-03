+++
id = "catalog/lie-groups/gl-n-r"
title = "GL(n,R)"
kind = "definition"
summary = "GL(n,R) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/smooth-structure", "lie-groups/general-linear-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

For every integer \(n\ge1\), \(\operatorname{GL}(n,\mathbb R)\) is the [[lie-groups/general-linear-group|general linear group]]
\[ \operatorname{GL}(n,\mathbb R)=\{A\in M_{n}(\mathbb R):\det A\ne0\}, \]
with matrix multiplication and its usual real [[fiber-bundles/smooth-structure|smooth manifold structure]].

## Dimensions and structure

This group has real dimension \(n^2\). It is open in the space of all matrices. Its tangent algebra consists of all matrices with the commutator bracket. The sign of the determinant distinguishes its two [[topology/connected-component|connected components]].

The projectivization map has kernel all nonzero scalar matrices. See [[catalog/lie-groups/pgl-n-r|\(\operatorname{PGL}(n,\mathbb R)\)]].

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
