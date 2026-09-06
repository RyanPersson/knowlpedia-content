+++
id = "langlands/local-epsilon-factor"
title = "Local epsilon factor"
kind = "definition"
summary = "The normalization-sensitive local constant in the functional equation of a local L-factor."
aliases = ["epsilon factor", "local epsilon constant", "epsilon(s,V,psi)"]
domains = ["langlands", "number-theory", "harmonic-analysis"]
prerequisites = ["algebra-fields-galois/local-field", "langlands/weil-deligne-representation", "algebra-representation-theory/character", "langlands-letter/knowls/euler-product-and-local-factor", "harmonic-analysis/haar-measure", "langlands/local-gamma-factor", "langlands-letter/knowls/contragredient-representation", "langlands/artin-conductor"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F\) be a
[[algebra-fields-galois/local-field|local field]], let
\(V=(r,N)\) be a finite-dimensional
[[langlands/weil-deligne-representation|Weil–Deligne representation]], and
choose a nontrivial additive
[[algebra-representation-theory/character|character]]
\(\psi:F\to\mathbb C^\times\).  The **local epsilon factor**

\[
\varepsilon(s,V,\psi)
\]

is the nonzero elementary factor that occurs with the
[[langlands-letter/knowls/euler-product-and-local-factor|local
\(L\)-factors]] in the functional equation. With a self-dual
[[harmonic-analysis/haar-measure|Haar measure]] for \(\psi\), the associated
[[langlands/local-gamma-factor|gamma factor]] satisfies

\[
\gamma(s,V,\psi)=
\varepsilon(s,V,\psi)
\frac{L(1-s,V^\vee)}{L(s,V)}.
\]

Here \(V^\vee\) is the
[[langlands-letter/knowls/contragredient-representation|contragredient]]
Weil–Deligne representation. For nonarchimedean \(F\), the epsilon factor is
a nonzero constant times an integral power of \(q_F^{-s}\). The exponent
records the [[langlands/artin-conductor|Artin conductor]].

## Dependence on choices

Unlike the local L-factor, \(\varepsilon(s,V,\psi)\) depends on the additive
character and on the Haar-measure convention.  Replacing \(\psi(x)\) by
\(\psi(ax)\) changes it by an explicit determinant and absolute-value factor.
Every comparison must therefore fix:

- [[langlands-letter/knowls/frobenius-unramified|arithmetic or geometric
  Frobenius]];
- the [[langlands/local-class-field-theory|reciprocity-map]] normalization;
- the additive character; and
- the measure used in Fourier transform.

## Representations of reductive groups

For representations of \(\operatorname{GL}_n(F)\),
[[langlands/local-langlands-correspondence-for-gln|local Langlands]] defines
epsilon factors through the corresponding Weil–Deligne representation and
agrees with the factors constructed analytically.  For a general reductive
group and a representation \(r\) of its
[[langlands/l-group|\(L\)-group]], Langlands–Shahidi and
Rankin–Selberg methods construct factors in many cases.

The unit-modulus normalization at the central point is the
[[langlands/root-number|local root number]].

## References

1. Pierre Deligne, “Les constantes des équations fonctionnelles des fonctions
   \(L\),” in *Modular Functions of One Variable II*, Lecture Notes in
   Mathematics 349, Springer, 1973, 501–597.
2. John Tate, “Number theoretic background,” in *Automorphic Forms,
   Representations and L-Functions*, Proceedings of Symposia in Pure
   Mathematics 33, part 2, 1979.
