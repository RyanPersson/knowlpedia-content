+++
id = "catalog/lie-groups/psl-n-c"
title = "PSL(n,C)"
kind = "definition"
summary = "PSL(n,C) as a separately identified complex Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/projective-special-linear-lie-group", "lie-groups/quotient-lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

For every integer \(n\ge1\), \(\operatorname{PSL}(n,\mathbb C)\) is the [[lie-groups/projective-special-linear-lie-group|projective special linear Lie group]]
\[ \operatorname{PSL}(n,\mathbb C)=\operatorname{SL}(n,\mathbb C)/\{\lambda I:\lambda\in \mathbb C^\times,\ \lambda^{n}=1\}, \]
with the [[lie-groups/quotient-lie-group|quotient Lie group]] structure.

## Dimensions and structure

This group has real dimension \(2(n^2-1)\), complex dimension \(n^2-1\). It acts on [[algebraic-geometry-foundations/projective-space|projective space]] by applying a representative matrix to a line. Every nonzero complex determinant has an \(n\)th root. Rescaling a representative therefore identifies \(\mathrm{PSL}(n,\mathbb C)\) with \(\mathrm{PGL}(n,\mathbb C)\).

Its [[lie-groups/complex-lie-group|complex Lie group]] structure uses holomorphic multiplication and inversion. Forgetting the complex structure gives the [[lie-groups/underlying-real-lie-group|underlying real Lie group]]; real and holomorphic homomorphisms belong to different categories.

The map induced by inclusion SL→GL is an isomorphism: normalize a representative by a nth root of its determinant. See [[catalog/lie-groups/pgl-n-c|\(\operatorname{PGL}(n,\mathbb C)\)]].

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
