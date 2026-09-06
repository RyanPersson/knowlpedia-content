+++
id = "algebraic-geometry-foundations/isocrystal"
title = "Isocrystal"
kind = "definition"
summary = "A finite-dimensional vector space over a Witt-vector fraction field equipped with a bijective semilinear Frobenius."
aliases = ["F-isocrystal", "isocrystal over a perfect field", "rational Dieudonné module"]
domains = ["algebraic-geometry-foundations", "algebra-fields-galois", "langlands"]
prerequisites = ["algebra-fields-galois/perfect-field", "linear-algebra/vector-space", "linear-algebra/semilinear-map"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(k\) be a [[algebra-fields-galois/perfect-field|perfect field]] of
characteristic \(p\), let
\(K_0=W(k)[1/p]\), and let \(\sigma\) be the Frobenius automorphism of \(K_0\).
An **isocrystal over \(k\)** is a finite-dimensional
[[linear-algebra/vector-space|\(K_0\)-vector space]] \(D\) equipped with a
bijective [[linear-algebra/semilinear-map|\(\sigma\)-semilinear map]]

\[
\varphi:D\longrightarrow D,
\qquad
\varphi(av)=\sigma(a)\varphi(v).
\]

Equivalently, it is an \(F\)-crystal after inverting \(p\); lattices and
\(p\)-power torsion are forgotten.

## Slopes

When \(k\) is
[[algebraic-geometry-foundations/algebraically-closed-field|algebraically
closed]], the Dieudonné–Manin classification
decomposes an isocrystal, up to isomorphism, into isoclinic pieces indexed by
rational **Newton slopes**.  The multiset of slopes, with multiplicities,
forms its Newton polygon.

For example, the one-dimensional isocrystal with
\(\varphi=p^m\sigma\) has slope \(m\).  Rational slopes with nontrivial
denominators occur in higher dimension.

## G-isocrystals

For a
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
\(G\), a \(G\)-isocrystal can be encoded by a tensor
functor from \(\operatorname{Rep}(G)\) to isocrystals.  After a trivialization,
its Frobenius is represented by an element \(b\in G(\breve F)\), and changing
the trivialization changes \(b\) by
[[langlands/twisted-conjugacy|sigma-conjugacy]]. The resulting classes
form the [[langlands/kottwitz-set-b-g|Kottwitz set \(B(G)\)]].

## References

1. Jean Dieudonné, “Groupes de Lie et hyperalgèbres de Lie sur un corps de
   caractéristique \(p>0\),” *Commentarii Mathematici Helvetici* 28 (1954),
   87–118.
2. Robert E. Kottwitz, “Isocrystals with additional structure,” *Compositio
   Mathematica* 56 (1985), 201–220.
   [Numdam](https://www.numdam.org/item/CM_1985__56_2_201_0/).
