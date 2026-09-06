+++
id = "algebra-fields-galois/inertia-subgroup"
title = "Inertia subgroup"
kind = "definition"
summary = "The kernel of the residue-field action of a decomposition group."
aliases = ["inertia group", "inertia subgroup at a place", "I_F", "I_w"]
domains = ["algebra-fields-galois", "langlands"]
section_mode = "progressive"
prerequisites = ["langlands-letter/knowls/galois-extension-and-group", "algebra-fields-galois/nonarchimedean-local-field", "algebra-commutative/residue-field", "algebra-fields-galois/decomposition-group", "algebra-groups/exact-sequence-groups"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(L_w/K_v\) be a finite
[[langlands-letter/knowls/galois-extension-and-group|Galois extension]] of
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local fields]].
The **inertia subgroup** is

\[
I_w=\ker\!\left(
\operatorname{Gal}(L_w/K_v)\longrightarrow
\operatorname{Gal}(k_w/k_v)
\right).
\]

Equivalently, it consists of the automorphisms acting trivially on the
[[algebra-commutative/residue-field|residue field]]. In the global situation
it is the kernel of the residue-field action
of the [[algebra-fields-galois/decomposition-group|decomposition group]].

For a nonarchimedean local field \(F\), let \(F^{\mathrm s}\) be the
separable closure inside a fixed
[[algebra-fields-galois/algebraic-closure|algebraic closure]]. Then
passing through all finite
[[algebra-fields-galois/galois-extension|Galois extensions]] gives an
[[algebra-groups/exact-sequence-groups|exact sequence]]

\[
1\longrightarrow I_F\longrightarrow
\operatorname{Gal}(F^{\mathrm s}/F)\longrightarrow
\operatorname{Gal}(\overline{k}_F/k_F)\simeq\widehat{\mathbb Z}
\longrightarrow1.
\]

Here \(\operatorname{Gal}(F^{\mathrm s}/F)\) is the
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]]
of \(F\).

## Tame and wild inertia

If the residue characteristic is \(p\), inertia contains a distinguished
pro-\(p\) subgroup \(P_F\), the [[langlands/wild-ramification|wild inertia
group]].  The quotient \(I_F/P_F\) is tame inertia; after compatible choices
it is isomorphic to
\(\prod_{\ell\ne p}\mathbb Z_\ell(1)\).  A representation is
[[langlands/tame-ramification|tamely ramified]] when \(P_F\) acts trivially and
unramified when all of \(I_F\) acts trivially.

The local [[langlands/weil-group|Weil group]] contains the same \(I_F\) as an
open compact subgroup.  This is why “trivial on inertia” is the common
unramified condition for Galois, Weil, and
[[langlands/local-l-parameter|Langlands parameters]].

## References

1. Jean-Pierre Serre, *Local Fields*, Graduate Texts in Mathematics 67,
   Springer, 1979, Chapter IV.
2. The Stacks Project Authors, “Fundamental Groups of Schemes,” §58.13,
   “Ramification theory.” [Stacks Project](https://stacks.math.columbia.edu/tag/0BSD).
