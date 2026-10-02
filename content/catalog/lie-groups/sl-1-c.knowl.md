+++
id = "catalog/lie-groups/sl-1-c"
title = "SL(1,C)"
kind = "definition"
summary = "SL(1,C) as a separately identified complex Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/complex-lie-group", "lie-groups/special-linear-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\operatorname{SL}(1,\mathbb C)\) is the determinant-one [[lie-groups/special-linear-group|special linear group]]
\[ \operatorname{SL}(1,\mathbb C)=\{A\in M_{1}(\mathbb C):\det A=1\}, \]
with matrix multiplication and the inherited [[lie-groups/complex-lie-group|complex Lie group]] structure.

## Dimensions and structure

This group has real dimension \(0\), complex dimension \(0\). Differentiating the determinant at the identity gives the trace-zero tangent algebra. The center consists of scalar matrices \(\lambda I\) with \(\lambda^{1}=1\). In size one the defining equation forces the sole matrix to be 1, so this is the trivial group.

Its complex Lie group structure uses holomorphic multiplication and inversion. Forgetting the complex structure gives the [[lie-groups/underlying-real-lie-group|underlying real Lie group]]; real and holomorphic homomorphisms belong to different categories.

The inclusion sends a determinant-one matrix to the same invertible matrix; it is injective and smooth and holomorphic. See [[catalog/lie-groups/gl-1-c|\(\operatorname{GL}(1,\mathbb C)\)]].

The scalar-center quotient has kernel \(\{\lambda I:\lambda^{1}=1\}\). See [[catalog/lie-groups/psl-1-c|\(\operatorname{PSL}(1,\mathbb C)\)]].

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
