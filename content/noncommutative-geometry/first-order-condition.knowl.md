+++
id = "noncommutative-geometry/first-order-condition"
title = "First-order condition for a real spectral triple"
kind = "definition"
summary = "The double-commutator axiom requiring Dirac commutators to be linear for the opposite-algebra action."
aliases = ["order-one condition", "first order axiom"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
+++

Let \((\mathcal A,H,D,J)\) satisfy the [[noncommutative-geometry/order-zero-condition|order-zero condition]] and write \(b^\circ=Jb^*J^{-1}\). The **first-order condition** is
\[
\bigl[\, [D,a],b^\circ\,\bigr]=0
\qquad\text{for every }a,b\in\mathcal A,
\]
where each \([D,a]\), initially defined on \(\operatorname{Dom}(D)\), is replaced by its [[functional-analysis/bounded-commutator|bounded extension]]. Equivalently, the derivation
\[
a\longmapsto [D,a]
\]
takes values in bounded operators that are right \(\mathcal A\)-linear for the opposite action. The axiom is strictly stronger than order zero: order zero concerns \(a\) itself, while first order concerns its differential \([D,a]\).

## Differential meaning

For a first-order differential operator, commuting once with multiplication by a function removes the derivative and leaves an order-zero operator. Such an operator commutes with multiplication by a second function. The double commutator is the operator-algebraic form of this property.

More generally, the axiom ensures that represented one-forms
\[
\sum_j a_j[D,b_j]
\]
are compatible with the right \(\mathcal A\)-module structure. This is the reason the condition is separated from the bimodule-producing order-zero axiom [Connes and Marcolli, equation (1.473)](https://doi.org/10.1090/coll/055).

## Example and near miss

For the [[noncommutative-geometry/dirac-operator|Dirac operator]] \(\not D\) on a closed spin manifold,
\[
[\not D,f]=c(df),
\]
Clifford multiplication by \(df\). This is a bundle endomorphism and therefore commutes with right multiplication by every function \(g\), so first order holds.

The Laplace operator is a decisive near miss: although functions commute with
the opposite action, \(\bigl[\, [\Delta,f],g\,\bigr]\) is generally
multiplication by a nonzero multiple of the metric pairing of \(df\) and
\(dg\). It therefore fails the first-order axiom.

## References

1. A. Connes, “Noncommutative Geometry and Reality,” *Journal of Mathematical Physics* 36 (1995), 6194–6231. [DOI record](https://doi.org/10.1063/1.531241). Relevant: §2 on the order-one relation.
2. A. Connes and M. Marcolli, *Noncommutative Geometry, Quantum Fields and Motives*, American Mathematical Society, 2008. [DOI record](https://doi.org/10.1090/coll/055). Relevant: Definition 1.124, equation (1.473).
3. S. Lord, A. Rennie, and J. C. Várilly, “Riemannian Manifolds in Noncommutative Geometry,” *Journal of Geometry and Physics* 62 (2012), 1611–1638. [DOI record](https://doi.org/10.1016/j.geomphys.2012.03.004). Relevant: §§2–3 on bimodules and first-order conditions.
