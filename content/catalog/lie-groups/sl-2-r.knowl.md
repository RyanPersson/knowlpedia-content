+++
id = "catalog/lie-groups/sl-2-r"
title = "SL(2,R)"
kind = "definition"
summary = "SL(2,R) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group", "lie-groups/special-linear-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\operatorname{SL}(2,\mathbb R)\) is the determinant-one [[lie-groups/special-linear-group|special linear group]]
\[ \operatorname{SL}(2,\mathbb R)=\{A\in M_{2}(\mathbb R):\det A=1\}, \]
with matrix multiplication and the inherited real [[fiber-bundles/lie-group|Lie group]] structure.

## Dimensions and structure

This group has real dimension \(3\). Differentiating the determinant at the identity gives the trace-zero tangent algebra. The center consists of scalar matrices \(\lambda I\) with \(\lambda^{2}=1\). It is connected but is not [[topology/simply-connected-space|simply connected]] for matrix size at least two; its noncompactness distinguishes it from the compact [[lie-groups/special-unitary-group|special unitary group]].

The inclusion sends a determinant-one matrix to the same invertible matrix; it is injective and smooth. See [[catalog/lie-groups/gl-2-r|\(\operatorname{GL}(2,\mathbb R)\)]].

The scalar-center quotient has kernel \(\{\lambda I:\lambda^{2}=1\}\). See [[catalog/lie-groups/psl-2-r|\(\operatorname{PSL}(2,\mathbb R)\)]].

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
