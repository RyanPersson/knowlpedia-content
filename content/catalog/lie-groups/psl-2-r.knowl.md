+++
id = "catalog/lie-groups/psl-2-r"
title = "PSL(2,R)"
kind = "definition"
summary = "PSL(2,R) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/projective-special-linear-lie-group", "lie-groups/quotient-lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\operatorname{PSL}(2,\mathbb R)\) is the [[lie-groups/projective-special-linear-lie-group|projective special linear Lie group]]
\[ \operatorname{PSL}(2,\mathbb R)=\operatorname{SL}(2,\mathbb R)/\{\lambda I:\lambda\in \mathbb R^\times,\ \lambda^{2}=1\}, \]
with the [[lie-groups/quotient-lie-group|quotient Lie group]] structure.

## Dimensions and structure

This group has real dimension \(3\). It acts on [[algebraic-geometry-foundations/projective-space|projective space]] by applying a representative matrix to a line. For odd matrix size, a real determinant has a real root of that degree and PSL equals PGL. For even matrix size, PSL is the [[lie-groups/identity-component-of-a-lie-group|identity component]] of PGL and PGL has two components. The real scalar quotient is taken on real matrices; replacing it by a statement about complex points changes the object.

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.1, pp. 38–39; Proposition 6.3 and Exercise 6.5.
