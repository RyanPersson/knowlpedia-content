+++
id = "noncommutative-geometry/real-spectral-triple"
title = "Real spectral triple"
kind = "definition"
summary = "A spectral triple equipped with a KO-dimensional real structure satisfying the order-zero and first-order conditions."
aliases = ["real even spectral triple", "real odd spectral triple", "real K-cycle"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
+++

A **real spectral triple of KO-dimension \(n\)** is a [[noncommutative-geometry/spectral-triple|spectral triple]] \((\mathcal A,H,D)\), even or odd, together with a [[noncommutative-geometry/real-structure-spectral-triple|real structure]] \(J\) having the [[noncommutative-geometry/ko-dimension-signs|signs prescribed by \(n\bmod 8\)]]. Writing
\[
b^\circ=Jb^*J^{-1},
\]
the data must satisfy the [[noncommutative-geometry/order-zero-condition|order-zero condition]]
\[
[a,b^\circ]=0
\]
and the [[noncommutative-geometry/first-order-condition|first-order condition]]
\[
\bigl[\, [D,a],b^\circ\,\bigr]=0
\]
for all \(a,b\in\mathcal A\). In even parity the grading \(\Gamma\) commutes with \(\mathcal A\), anticommutes with \(D\), and obeys the KO-dimensional relation with \(J\). All commutators involving \(D\) use their bounded extensions.

## Bimodule and parity structure

The order-zero condition makes \(H\) an \(\mathcal A\)-bimodule, with \(a\xi b=ab^\circ\xi\). The first-order condition says that each [[functional-analysis/bounded-commutator|bounded commutator]] \([D,a]\) is right \(\mathcal A\)-linear. Together they abstract the fact that a [[noncommutative-geometry/dirac-operator|Dirac operator]] is first-order.

The parity of the spectral triple and its KO-dimension are distinct: parity records whether a grading is present, whereas KO-dimension records the signs of \(J\) with \(D\) and, when present, \(\Gamma\) [Connes and Marcolli, Definition 1.124](https://doi.org/10.1090/coll/055).

## Canonical example and scope

For a closed Riemannian spin manifold \(M\), the data
\[
\bigl(C^\infty(M),L^2(M,S),\not D,J\bigr)
\]
form a real spectral triple, with chirality added in even dimension. Functions act by multiplication, \(J\) is charge conjugation, and \([\not D,f]\) is Clifford multiplication by \(df\); hence it commutes with the right action by functions.

**Warning.** Some authors use “real spectral triple” for the sign relations alone and list the order conditions separately. The definition here follows the package in equations (1.470)–(1.473) of Connes–Marcolli.

## References

1. A. Connes, “Noncommutative Geometry and Reality,” *Journal of Mathematical Physics* 36 (1995), 6194–6231. [DOI record](https://doi.org/10.1063/1.531241). Relevant: §2 on real K-cycles and the opposite action.
2. A. Connes and M. Marcolli, *Noncommutative Geometry, Quantum Fields and Motives*, American Mathematical Society, 2008. [DOI record](https://doi.org/10.1090/coll/055). Relevant: Definition 1.124 and equations (1.470)–(1.473).
