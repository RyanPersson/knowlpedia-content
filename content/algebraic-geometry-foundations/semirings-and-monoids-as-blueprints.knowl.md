+++
id = "algebraic-geometry-foundations/semirings-and-monoids-as-blueprints"
title = "Semirings and monoids as blueprints"
kind = "construction"
summary = "The canonical fully faithful embeddings of commutative semirings and monoids into blueprints."
aliases = ["canonical blueprints of semirings and monoids"]
domains = ["algebraic-geometry-foundations", "algebra-rings", "algebra-groups"]
section_mode = "progressive"
+++

There are canonical fully faithful embeddings of commutative semirings and commutative monoids with zero into [[algebraic-geometry-foundations/blueprint|blueprints]].

For a semiring \(R\), take the multiplicative monoid \(R^\bullet\) and impose every formal additive relation that is true in \(R\):
\[
R^{\mathrm{blpr}}
=R^\bullet/\!/\left\langle
\sum a_i\equiv\sum b_j
\;\middle|\;
\sum a_i=\sum b_j\text{ in }R
\right\rangle.
\]
For a commutative monoid with zero \(A\), take \(A/\!/\langle\varnothing\rangle\), with no nontrivial additive relations beyond the blueprint axioms.

## Why the embeddings are fully faithful

A blueprint morphism between semiring blueprints preserves precisely the sums already represented in the semirings, so it is a semiring homomorphism. Between monoid blueprints there are no added relations to check, so it is exactly a multiplicative map preserving \(0\) and \(1\).

## Do not identify the two constructions

The semiring completion of the monoid blueprint \(A/\!/\langle\varnothing\rangle\) is the free semiring \(\mathbb N[A]\), not \(A\) itself. Conversely, a semiring blueprint remembers all additive equalities of \(R\). Thus monoids and semirings occupy distinct full subcategories of blueprints even when they have the same underlying multiplicative set.

## Reference

Oliver Lorscheid, [*The geometry of blueprints, Part I*, §§1.1–1.2](https://arxiv.org/abs/1103.1745).

