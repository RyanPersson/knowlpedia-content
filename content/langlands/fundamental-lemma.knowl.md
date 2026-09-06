+++
id = "langlands/fundamental-lemma"
title = "Fundamental lemma of endoscopy"
kind = "knowl"
summary = "The theorem that unramified unit Hecke functions have matching endoscopic orbital integrals."
aliases = ["fundamental lemma", "Langlands-Shelstad fundamental lemma", "endoscopic fundamental lemma"]
domains = ["langlands", "harmonic-analysis", "algebraic-geometry"]
prerequisites = ["algebra-fields-galois/nonarchimedean-local-field", "algebraic-geometry-foundations/unramified-reductive-group", "langlands/endoscopic-datum", "langlands-letter/knowls/maximal-compact-hyperspecial", "langlands/endoscopic-transfer", "langlands/strongly-regular-semisimple-element", "langlands/orbital-integral"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F\) be a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]], let \(G\) be an
[[algebraic-geometry-foundations/unramified-reductive-group|unramified
reductive group]], and let \(H\) be an unramified
[[langlands/endoscopic-datum|endoscopic group]]. Choose
[[langlands-letter/knowls/maximal-compact-hyperspecial|hyperspecial
subgroups]] \(K\subset G(F)\) and \(K_H\subset H(F)\), with
volume \(1\). The **fundamental lemma** states that the unit functions

\[
\mathbf 1_K
\quad\text{and}\quad
\mathbf 1_{K_H}
\]

are matching functions under [[langlands/endoscopic-transfer|endoscopic
transfer]]. Equivalently, their matching [[langlands/strongly-regular-semisimple-element|strongly regular semisimple]]
[[langlands/orbital-integral|orbital integrals]] satisfy the transfer-factor identity.

## Hecke-algebra form

More generally, the transfer homomorphism between unramified spherical
[[harmonic-analysis/hecke-algebra-locally-compact-group-pair|Hecke algebras]],
defined through the
[[langlands-letter/knowls/spherical-hecke-algebra-satake|Satake isomorphism]],
sends a spherical
Hecke function on \(G\) to a function on \(H\) with matching stable orbital
integrals. The unit-element statement is the historically central case.

## Why “lemma” is misleading

The statement is a deep theorem. Langlands and Shelstad formulated it as the
local identity needed to stabilize the trace formula. Ngô Bảo Châu proved
the [[lie-groups/lie-algebra|Lie algebra]] fundamental lemma by interpreting the relevant orbital
integrals through the geometry of the
[[langlands/hitchin-fibration|Hitchin fibration]]. Reduction and
transfer results of Waldspurger, Hales, Cluckers–Loeser, and others connect
the Lie algebra, group, and characteristic-zero formulations.

## Geometric content

Over a function field, orbital integrals become weighted point counts on
fibers related to
[[langlands/affine-springer-fiber|affine Springer fibers]]. Globally, the
Hitchin fibration
organizes these fibers. A support theorem and comparison of endoscopic
summands in its \(\ell\)-adic cohomology yield the required identities.

## Variants

The standard fundamental lemma must be distinguished from:

- the weighted fundamental lemma needed for the full trace formula;
- twisted fundamental lemmas;
- the nonstandard fundamental lemma for groups with related [[lie-groups/root-system|root systems]];
- relative fundamental lemmas for relative trace formulas.

Each has its own matching data and hypotheses.

## References

1. Ngô Bảo Châu, “Le lemme fondamental pour les algèbres de Lie,”
   *Publications Mathématiques de l'IHÉS* 111 (2010), 1–169.
   [arXiv](https://arxiv.org/abs/0801.0446).
2. Ngô Bảo Châu, “Survey on the fundamental lemma.”
   [PDF](https://math.uchicago.edu/~ngo/survey.pdf).
