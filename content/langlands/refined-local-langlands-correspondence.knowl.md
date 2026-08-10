+++
id = "langlands/refined-local-langlands-correspondence"
title = "Refined local Langlands correspondence"
kind = "knowl"
summary = "The internal parametrization of local L-packets, simultaneously across rigid inner forms, by representations of a parameter centralizer."
aliases = ["refined LLC", "internal parametrization of L-packets", "enhanced local Langlands correspondence"]
domains = ["langlands", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(G^*\) be a quasi-split connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over a local field,
choose a [[langlands/whittaker-datum|Whittaker datum]] \(\mathfrak w\), and
let \(\varphi:L_F\to{}^LG^*\) be a relevant parameter. The **refined local
Langlands correspondence** predicts a canonical internal parametrization of
the compound packet of \(\varphi\) by [[algebra-representation-theory/irreducible-representation|irreducible representations]] of the
refined centralizer group:

\[
\Pi_\varphi
\;\longleftrightarrow\;
\operatorname{Irr}\!\left(\pi_0(S_\varphi^+)\right).
\]

Here the left side ranges over appropriately rigidified inner forms of
\(G^*\); on the right, the central character of an irreducible representation
records the inner form on which the corresponding packet member lives.

## Quasi-split fiber

Restricting to \(G^*(F)\) gives a parametrization by the appropriate
center-quotiented [[langlands/component-group-of-l-parameter|component
group]]. For tempered \(\varphi\), the conjecturally unique
\(\mathfrak w\)-generic member corresponds to the trivial representation.

## Why rigidification is present

An ordinary inner twist does not retain enough cohomological information to
normalize [[langlands/transfer-factor|transfer factors]] and distinguish all packet members functorially.
Pure inner twists suffice in some settings; rigid inner twists give a uniform
framework for general connected reductive groups. The older notions of inner
and pure inner forms are reviewed in
[[langlands-letter/knowls/galois-descent-forms|Galois descent and forms]].

## Character identities

The parametrization is characterized not just as a bijection but through
stable and endoscopic character identities. The trivial component-group
element gives a stable packet distribution, while other elements select
[[langlands/endoscopic-transfer|endoscopic transfers]]. Dependence on the Whittaker datum and rigidifying
cocycle is governed by explicit character twists.

## Status

Refined correspondences are theorems for archimedean groups and many important
nonarchimedean families, including broad classes of classical groups. The
uniform statement above remains conjectural for a general reductive group.

## References

1. Tasho Kaletha, “Representations of reductive groups over local fields,”
   §§2.2–2.3, 2022. [arXiv](https://arxiv.org/abs/2201.07741).
2. Tasho Kaletha, “Rigid inner forms of real and \(p\)-adic groups,” *Annals
   of Mathematics* 184 (2016), 559–632.
   [DOI](https://doi.org/10.4007/annals.2016.184.2.6).
