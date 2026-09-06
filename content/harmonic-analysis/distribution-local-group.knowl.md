+++
id = "harmonic-analysis/distribution-local-group"
title = "Distribution on a local group"
kind = "definition"
summary = "A continuous linear functional on the archimedean or nonarchimedean test-function space of a local group."
aliases = ["local-group distribution", "distribution on a p-adic group", "invariant distribution on a local group"]
domains = ["harmonic-analysis", "langlands", "functional-analysis"]
prerequisites = ["algebra-fields-galois/local-field", "harmonic-analysis/test-function-space-local-group"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F\) be a
[[algebra-fields-galois/local-field|local field]], let
\(G(F)\) be a local group, and let
\(\mathcal D(G(F))\) be its
[[harmonic-analysis/test-function-space-local-group|test-function space]]. A
**distribution on \(G(F)\)** is a continuous linear functional

\[
D:\mathcal D(G(F))\longrightarrow\mathbb C.
\]

Thus continuity is measured using smooth compactly supported functions in the
archimedean case and locally constant compactly supported functions in the
nonarchimedean case.

The distribution is **conjugation-invariant** if

\[
D(f^x)=D(f),
\qquad
f^x(g)=f(x^{-1}gx),
\]

for every \(x\in G(F)\). Invariant distributions are the natural common
language for orbital integrals and representation characters.

## Functions and orbital measures

After choosing a [[harmonic-analysis/haar-measure|Haar measure]], a locally
integrable function \(\Theta\) defines a distribution by

\[
f\longmapsto\int_{G(F)}f(g)\Theta(g)\,dg.
\]

Not every distribution is represented by a function. In particular, an
[[langlands/orbital-integral|orbital integral]] is naturally a distribution
supported on a conjugacy orbit, while a Harish–Chandra character is first
defined distributionally and only then represented by a function on a regular
locus.

## Stable distributions

For a
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]], a
[[langlands/stable-distribution|stable distribution]] is an invariant
distribution satisfying an additional factorization condition through stable
orbital-integral data. “Invariant” and “stable” are therefore not synonyms.

## Scope warning

This definition is the local-group analogue of a
[[functional-analysis/distribution|Schwartz distribution]] on an open subset
of [[linear-algebra/euclidean-space|Euclidean space]]. The test-function
categories differ, so the Euclidean page should not be used as the direct
definition of a distribution on a nonarchimedean group.

## References

1. François Bruhat, “Distributions sur un groupe localement compact et
   applications à l'étude des représentations des groupes \(p\)-adiques,”
   *Bulletin de la Société Mathématique de France* 89 (1961), 43–75.
   [Numdam](https://www.numdam.org/item/BSMF_1961__89__43_0/).
2. Harish-Chandra, “Admissible invariant distributions on reductive
   \(p\)-adic groups,” in *Lie Theories and Their Applications*, Queen's
   Papers in Pure and Applied Mathematics 48, 1978.
