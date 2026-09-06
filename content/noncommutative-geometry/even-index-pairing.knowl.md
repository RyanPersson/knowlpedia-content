+++
id = "noncommutative-geometry/even-index-pairing"
title = "Even K-theory/K-homology index pairing"
kind = "definition"
summary = "The integer obtained by compressing the off-diagonal operator of an even Fredholm module by a K-zero projection."
aliases = ["even index pairing", "K0 index pairing", "projection index pairing"]
domains = ["noncommutative-geometry", "operator-algebras"]
prerequisites = ["noncommutative-geometry/even-fredholm-module", "operator-algebras/projection-cstar-algebra", "operator-algebras/k0-cstar-algebra", "functional-analysis/fredholm-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a unital complex \(C^*\)-algebra, let \((H^+\oplus H^-,\pi,F)\) be a normalized [[noncommutative-geometry/even-fredholm-module|even Fredholm module]], and write \(F^+:H^+\to H^-\) for its positive-to-negative part. For a [[operator-algebras/projection-cstar-algebra|projection]] \(p\in M_n(A)\) representing a [[operator-algebras/k0-cstar-algebra|\(K_0(A)\)-class]], put \(p^\pm=\pi_n^\pm(p)\). The compression
\[
p^-F_n^+p^+:p^+H^{+n}\longrightarrow p^-H^{-n}
\]
is [[functional-analysis/fredholm-operator|Fredholm]], and the **even index pairing** is
\[
\langle[p],[H,\pi,F]\rangle=\operatorname{ind}(p^-F_n^+p^+).
\]
It extends additively to differences of projections, giving a bilinear pairing \(K_0(A)\times K^0(A)\to\mathbb Z\).

## Why the compression is Fredholm

Because \([F,\pi(a)]\) is compact, \(p^-F_n^+p^+\) has \(p^+F_n^-p^-\) as an inverse modulo [[linear-algebra/compact-operator|compact operators]]. The compressed operator is therefore Fredholm by Atkinson's characterization. Its index is unchanged under stabilization of \(p\), homotopy of the projection, compact perturbation of \(F\), and stable homotopy of the [[noncommutative-geometry/fredholm-module|Fredholm module]]. These facts make the formula descend to [[operator-algebras/k0-cstar-algebra|\(K_0(A)\)]] and [[noncommutative-geometry/analytic-k-homology|analytic K-homology]].

For a class \([p]-[q]\), the value is
\[
\operatorname{ind}(p^-F_n^+p^+)-\operatorname{ind}(q^-F_m^+q^+).
\]
This subtraction is essential: the pairing is defined on the Grothendieck group, not only on individual projections.

## Geometric example

Let \(M\) be a closed even-dimensional spin manifold and take the even Fredholm module obtained from its [[noncommutative-geometry/dirac-operator|Dirac operator]]. A projection \(p\in M_n(C^\infty(M))\) determines a [[fiber-bundles/vector-bundle|vector bundle]] \(E\). The compression represents the Dirac operator twisted by \(E\), so the pairing is its Fredholm index. This is the operator-theoretic bridge from a \(K_0\)-class to an integer index.

For \(A=\mathbb C\), pairing the class of a finite-rank projection with an even cycle scales the cycle's basic index by the rank.

## Conventions and scope

For nonunital \(A\), projections are taken in matrix algebras over the [[operator-algebras/unitization|unitization]], with the scalar projection subtracted so that the class lies in \(K_0(A)\). An unnormalized Fredholm module may be normalized or handled directly modulo compact operators before compression.

Switching which grading summand is called positive, or replacing the Fredholm-index convention \(\dim\ker T-\dim\ker T^*\) by its negative, reverses the displayed sign. The displayed formula fixes the convention used here.

## References

1. [Alain Connes, *Noncommutative Geometry*, Chapter IV, Section 1, Proposition 2(a), Academic Press, 1994](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).
2. [Nigel Higson and John Roe, *Analytic K-Homology*, Chapters 8–10, Oxford University Press, 2000](https://doi.org/10.1093/oso/9780198511762.001.0001).
