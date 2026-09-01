+++
id = "harmonic-analysis/parabolic-modulus-character"
title = "Parabolic modulus character"
kind = "definition"
summary = "The positive character measuring how a parabolic Levi acts on its unipotent radical."
aliases = ["modulus character of a parabolic", "modular character delta_P", "delta_P"]
domains = ["harmonic-analysis", "langlands", "lie-groups"]
prerequisites = ["algebra-fields-galois/local-field", "algebraic-geometry-foundations/reductive-algebraic-group", "algebraic-geometry-foundations/parabolic-subgroup", "algebraic-geometry-foundations/unipotent-radical", "algebra-representation-theory/character", "lie-groups/lie-algebra", "algebraic-geometry-foundations/levi-subgroup", "harmonic-analysis/modular-function"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(F\) be a
[[algebra-fields-galois/local-field|local field]], let
\(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(F\)-group]], and let \(P=MN\) be a
[[algebraic-geometry-foundations/parabolic-subgroup|parabolic subgroup]] with
[[algebraic-geometry-foundations/unipotent-radical|unipotent radical]]
\(N\). The **parabolic modulus character** is the positive
[[algebra-representation-theory/character|character]]

\[
\delta_P(p)=
\left|\det\!\left(\operatorname{Ad}(p)
\bigm|\operatorname{Lie}N\right)\right|_F,
\qquad p\in P(F).
\]

Here \(\operatorname{Lie}N\) is the
[[lie-groups/lie-algebra|Lie algebra]] of \(N\). The character is trivial on
\(N(F)\), so it may be regarded as a character of the
[[algebraic-geometry-foundations/levi-subgroup|Levi subgroup]] \(M(F)\).
It is also the restriction to \(P(F)\) of the
[[harmonic-analysis/modular-function|modular function]] appropriate to the
quotient \(G(F)/P(F)\).

## Normalization convention

For nonarchimedean \(F\),
[[harmonic-analysis/normalized-parabolic-induction-p-adic-group|normalized
parabolic induction]] uses \(\delta_P^{1/2}\sigma\), while the normalized
[[harmonic-analysis/jacquet-module|Jacquet module]] uses
\(\delta_P^{-1/2}\). These half-powers make
[[harmonic-analysis/unitary-induced-representation|unitary induction]] unitary and
produce symmetric formulas for
[[langlands-letter/knowls/contragredient-representation|contragredients]]
and adjunction.

Some sources call \(\delta_P^{-1}\) the modulus.  A formula involving
\(\rho_P\), normalized induction, or a
[[langlands/satake-parameter|Satake parameter]] should therefore be
checked against the author's convention.

## Example

For the upper-triangular Borel \(B\subset\operatorname{GL}_n(F)\),

\[
\delta_B(\operatorname{diag}(a_1,\ldots,a_n))
=\prod_{i<j}|a_i/a_j|_F.
\]

## References

1. Armand Borel, “Automorphic \(L\)-functions,” in *Automorphic Forms,
   Representations and \(L\)-Functions*, Proceedings of Symposia in Pure
   Mathematics 33, part 2, 1979, §3.
2. I. N. Bernstein and A. V. Zelevinsky, “Induced representations of
   reductive \(p\)-adic groups. I,” *Annales scientifiques de l'École Normale
   Supérieure* 10 (1977), 441–472.
   [Numdam](https://www.numdam.org/articles/10.24033/asens.1333/).
