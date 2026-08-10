+++
id = "langlands-letter/knowls/split-reductive-group"
title = "Split reductive algebraic group"
kind = "knowl"
summary = "A connected reductive group possessing a maximal torus split over the base field."
aliases = ["split-reductive-group", "Split Reductive Algebraic Group"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/split-reductive-group.md"
section_mode = "progressive"
+++

A **connected reductive algebraic group** over a field \(k\) is a smooth
connected affine \(k\)-group \(G\) whose geometric unipotent radical is
trivial. It is **split over \(k\)** if it contains a maximal torus

\[
T\simeq\mathbb G_m^r
\]

split over \(k\).

## Root datum over the base field

For split \(G\), the character and cocharacter lattices of \(T\), roots,
coroots, and a choice of Borel are defined without extending the base field.
A split connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] is classified up to isomorphism by its
root datum.

Examples include \(\operatorname{GL}_n\), \(\operatorname{SL}_n\), and
\(\operatorname{Sp}_{2n}\) in their standard forms over \(k\).

## Integral models

A split root datum defines a Chevalley–Demazure reductive group scheme over
\(\mathbb Z\). Over a nonarchimedean local field this provides a
hyperspecial subgroup after [[algebraic-geometry-foundations/base-change|base change]] to the valuation ring. For a
nonsplit but unramified group, a reductive integral model can still exist
even though the group is not split over the local field itself.

## Duality and descent

For split \(G\), the Galois action on the based root datum is trivial, so
the [[langlands/l-group|\(L\)-group]] has trivial Weil action on
\(\widehat G\). For a nonsplit group, the dual group can be the same
abstract complex group while the Weil action differs; this extra action is
essential data.

## Relation to the letter

The letter begins with split root data and then applies Galois descent and
inner twisting. This cleanly separates the combinatorial dual group from
the arithmetic \(F\)-form.

## References

1. Michel Demazure and Alexander Grothendieck, eds., *Schémas en groupes
   (SGA 3)*.
2. A. Borel, *Linear Algebraic Groups*, second edition, Springer, 1991.
