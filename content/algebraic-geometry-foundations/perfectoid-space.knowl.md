+++
id = "algebraic-geometry-foundations/perfectoid-space"
title = "Perfectoid space"
kind = "definition"
summary = "An adic space locally modeled on perfectoid affinoid algebras."
aliases = ["perfectoid adic space", "affinoid perfectoid space"]
domains = ["algebraic-geometry-foundations", "number-theory", "langlands"]
section_mode = "progressive"
+++

Let \(K\) be a
[[algebraic-geometry-foundations/perfectoid-field|perfectoid field]]. A Banach
\(K\)-algebra \(R\) is
**perfectoid** if it is uniform and Frobenius is surjective on
\(R^\circ/p\).  An affinoid perfectoid space is an
[[algebraic-geometry-foundations/adic-space|adic space]]

\[
\operatorname{Spa}(R,R^+)
\]

for a perfectoid \(K\)-algebra \(R\) and an open integrally closed
\(R^+\subseteq R^\circ\).  A **perfectoid space** is an adic space locally of
this form.

Equivalent definitions replace \(p\) by a pseudo-uniformizer whose \(p\)th
power divides \(p\); this is useful over general perfectoid bases.

## Tilting equivalence

[[algebraic-geometry-foundations/tilt-and-untilt|Tilting]] sends a perfectoid
space \(X/K\) to a perfectoid space
\(X^\flat/K^\flat\) with the same underlying
[[topology/topological-space|topological space]]. It identifies
étale sites and finite étale covers, although it does not identify the
structure sheaves as ordinary rings.

## Role in local Langlands geometry

Perfectoid spaces underlie diamonds, the
[[algebraic-geometry-foundations/v-stack|v-topology]], the
[[langlands/fargues-fontaine-curve|Fargues–Fontaine curve]], and infinite-level
[[langlands/local-shimura-variety|local Shimura varieties]]. They allow towers
with increasingly fine \(p\)-adic
level structure to acquire a geometric limit.

## References

1. Peter Scholze, “Perfectoid spaces,” *Publications Mathématiques de l'IHÉS*
   116 (2012), 245–313. [arXiv](https://arxiv.org/abs/1111.4914).
2. Peter Scholze and Jared Weinstein, *Berkeley Lectures on \(p\)-adic
   Geometry*, Annals of Mathematics Studies 207, Princeton University Press,
   2020, Chapters 6–7.
