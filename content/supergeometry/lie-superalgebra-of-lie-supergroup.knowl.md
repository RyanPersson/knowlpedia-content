+++
id = "supergeometry/lie-superalgebra-of-lie-supergroup"
title = "Lie superalgebra of a Lie supergroup"
kind = "construction"
summary = "The tangent superspace at the identity of a Lie supergroup, with bracket induced by invariant vector fields."
aliases = ["Lie functor for Lie supergroups", "tangent Lie superalgebra"]
domains = ["supergeometry", "lie-groups"]
prerequisites = ["supergeometry/lie-supergroup", "supergeometry/super-vector-space", "lie-groups/left-invariant-vector-field", "supergeometry/lie-superalgebra", "lie-groups/lie-algebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[supergeometry/lie-supergroup|Lie supergroup]] with identity
\(e\). Its **Lie superalgebra** is the tangent [[supergeometry/super-vector-space|super vector space]]
\[
\operatorname{Lie}(G)=T_eG.
\]
Left translation identifies \(T_eG\) with the [[lie-groups/left-invariant-vector-field|left-invariant vector fields]]
on \(G\). Transporting the supercommutator of derivations through this
identification gives a [[supergeometry/lie-superalgebra|Lie superbracket]]
on \(T_eG\).

The even part is canonically the ordinary [[lie-groups/lie-algebra|Lie algebra]] of the reduced group:
\[
\operatorname{Lie}(G)_{\bar 0}
\cong \operatorname{Lie}(G_{\mathrm{red}}).
\]
The odd tangent space supplies the genuinely new infinitesimal directions,
and its symmetric odd–odd bracket can have values in the even Lie algebra.

## Functoriality

A homomorphism of Lie supergroups \(F:G\to H\) differentiates at the identity
to an even Lie-superalgebra homomorphism
\[
dF_e:\operatorname{Lie}(G)\to\operatorname{Lie}(H).
\]
This defines a Lie functor from smooth real Lie supergroups to finite-dimensional
real Lie superalgebras. Unlike the ordinary simply-connected integration
statement, a Lie superalgebra alone does not record the chosen global reduced
Lie group; the missing global data is organized by a
[[supergeometry/super-harish-chandra-pair|super Harish–Chandra pair]].

## References

1. B. Kostant, “Graded manifolds, graded Lie theory, and prequantization,” in *Differential Geometrical Methods in Mathematical Physics*, Lecture Notes in Mathematics 570, Springer, 1977, 177–306. [Chapter](https://doi.org/10.1007/BFb0087787).
2. V. S. Varadarajan, *Supersymmetry for Mathematicians: An Introduction*, Courant Lecture Notes 11, American Mathematical Society, 2004. [Publisher record](https://doi.org/10.1090/cln/011). Relevant: Chapter 7.
