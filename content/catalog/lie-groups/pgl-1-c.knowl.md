+++
id = "catalog/lie-groups/pgl-1-c"
title = "PGL(1,C)"
kind = "definition"
summary = "PGL(1,C) as a separately identified complex Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/projective-general-linear-lie-group", "lie-groups/quotient-lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\operatorname{PGL}(1,\mathbb C)\) is the [[lie-groups/projective-general-linear-lie-group|projective general linear Lie group]]
\[ \operatorname{PGL}(1,\mathbb C)=\operatorname{GL}(1,\mathbb C)/\{\lambda I:\lambda\in \mathbb C^\times\}, \]
with the [[lie-groups/quotient-lie-group|quotient Lie group]] structure.

## Dimensions and structure

This group has real dimension \(0\), complex dimension \(0\). It acts on [[algebraic-geometry-foundations/projective-space|projective space]] by applying a representative matrix to a line. In size one both numerator and scalar subgroup coincide (or are trivial), so the projective group is trivial.

Its [[lie-groups/complex-lie-group|complex Lie group]] structure uses holomorphic multiplication and inversion. Forgetting the complex structure gives the [[lie-groups/underlying-real-lie-group|underlying real Lie group]]; real and holomorphic homomorphisms belong to different categories.

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
