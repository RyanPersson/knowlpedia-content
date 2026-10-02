+++
id = "catalog/lie-groups/sl-4-c"
title = "SL(4,C)"
kind = "definition"
summary = "SL(4,C) as a separately identified complex Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/special-linear-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

The complex [[lie-groups/special-linear-group|special linear group]] \(\mathrm{SL}(4,\mathbb C)\) consists of the determinant-one matrices in \(M_4(\mathbb C)\), with matrix multiplication.

## Dimensions and structure

This group has real dimension \(30\), complex dimension \(15\). It is connected and [[topology/simply-connected-space|simply connected]]. Its tangent algebra is the trace-zero 4 by 4 matrices; the [[lie-groups/central-quotient-of-a-lie-group|central quotient]] by {±I} gives SO(6,C).

Its [[lie-groups/complex-lie-group|complex Lie group]] structure uses holomorphic multiplication and inversion. Forgetting the complex structure gives the [[lie-groups/underlying-real-lie-group|underlying real Lie group]]; real and holomorphic homomorphisms belong to different categories.

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §31.2, Example 31.3 and Proposition 31.4; §31.3, Example 31.10, pp. 166–168.
