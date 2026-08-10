+++
id = "langlands/fundamental-lemma"
title = "Fundamental lemma of endoscopy"
kind = "knowl"
summary = "The theorem that unramified unit Hecke functions have matching endoscopic orbital integrals."
aliases = ["fundamental lemma", "Langlands-Shelstad fundamental lemma", "endoscopic fundamental lemma"]
domains = ["langlands", "harmonic-analysis", "algebraic-geometry"]
section_mode = "progressive"
+++

Let \(F\) be a nonarchimedean local field, let \(G\) be an unramified
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]], and let \(H\) be an unramified endoscopic group. Choose
hyperspecial subgroups \(K\subset G(F)\) and \(K_H\subset H(F)\), with
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
Hecke algebras, defined through the Satake isomorphism, sends a spherical
Hecke function on \(G\) to a function on \(H\) with matching stable orbital
integrals. The unit-element statement is the historically central case.

## Why “lemma” is misleading

The statement is a deep theorem. Langlands and Shelstad formulated it as the
local identity needed to stabilize the trace formula. Ngô Bảo Châu proved
the [[lie-groups/lie-algebra|Lie algebra]] fundamental lemma by interpreting the relevant orbital
integrals through the geometry of the Hitchin fibration. Reduction and
transfer results of Waldspurger, Hales, Cluckers–Loeser, and others connect
the Lie algebra, group, and characteristic-zero formulations.

## Geometric content

Over a function field, orbital integrals become weighted point counts on
fibers related to affine Springer fibers. Globally, the Hitchin fibration
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
