+++
id = "langlands-letter/knowls/contragredient-representation"
title = "Contragredient representation"
kind = "knowl"
summary = "The inverse-transpose action on an algebraic dual, or on the smooth dual for a locally profinite group."
aliases = ["contragredient-representation", "Contragredient (Dual) Representation"]
domains = ["langlands-letter"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "langlands-letter/knowls/contragredient-representation.md"
section_mode = "progressive"
+++

For a finite-dimensional representation \((\pi,V)\) of a group \(G\), the
**contragredient representation** on
\(V^*=\operatorname{Hom}_{\mathbb C}(V,\mathbb C)\) is

\[
(\pi^\vee(g)\ell)(v)=\ell(\pi(g^{-1})v).
\]

In a basis, \(\pi^\vee(g)\) is the transpose of
\(\pi(g)^{-1}\).

## Smooth representations

If \(G\) is [[topology/locally-profinite-group|locally profinite]] and \(V\)
is a
[[harmonic-analysis/smooth-representation-totally-disconnected-group|smooth
representation]], the
correct contragredient space is the **smooth dual**

\[
V^\vee
=
\{\ell\in V^*:\ell\text{ is fixed by some compact open subgroup}\},
\]

not generally the entire algebraic dual. If \(V\) is
[[harmonic-analysis/admissible-representation-p-adic-group|admissible]],
then \(V^\vee\) is admissible and the natural map
\(V\to(V^\vee)^\vee\) is an
isomorphism.

## Unitary distinction

For a unitary Hilbert representation, the Hilbert-space contragredient is
naturally related to the conjugate [[linear-algebra/hilbert-space|Hilbert space]]. Passing among the
algebraic, smooth, and Hilbert categories requires specifying which dual is
being used.

## Langlands compatibility

The [[langlands/local-langlands-correspondence|local Langlands
correspondence]] is expected, and known in established cases, to carry
contragredients to the Chevalley-dual parameter. This compatibility is
listed separately in
[[langlands/local-langlands-compatibilities|local Langlands
compatibilities]].

## Relation to the letter

The letter denotes this operation by \(\pi^e\). Its finite-dimensional
dual-group representations use the ordinary algebraic dual; modern
[[langlands/automorphic-representation|automorphic representations]] require the smooth local formulation above.

## References

1. Joseph Bernstein and Andrei Zelevinsky, “Induced representations of
   reductive \(p\)-adic groups I,” *Annales scientifiques de l'ÉNS* 10
   (1977), 441–472.
   [Numdam](https://www.numdam.org/item/ASENS_1977_4_10_4_441_0/).
