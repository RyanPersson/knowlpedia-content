+++
id = "noncommutative-geometry/fredholm-module"
title = "Fredholm module"
kind = "definition"
summary = "A representation of a complex C*-algebra equipped with an operator whose commutators and local self-adjointness and involutivity defects are compact."
aliases = ["bounded Fredholm module", "bounded K-cycle"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
prerequisites = ["linear-algebra/hilbert-space", "operator-algebras/cstar-representation", "linear-algebra/compact-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) be a complex \(C^*\)-algebra. A **Fredholm module over \(A\)** is a complex [[linear-algebra/hilbert-space|Hilbert space]] \(H\), a [[operator-algebras/cstar-representation|representation]] \(\pi:A\to\mathcal B(H)\), and a bounded operator \(F\in\mathcal B(H)\) such that, for every \(a\in A\),
\[
[F,\pi(a)],\qquad (F^2-I)\pi(a),\qquad (F-F^*)\pi(a)
\]
are [[linear-algebra/compact-operator|compact operators]]. This is the locally compact, Kasparov-cycle convention. A module is **normalized** when \(F=F^*\) and \(F^2=I\), leaving only compactness of the commutators. It is **degenerate** when all three displayed expressions vanish. Parity is supplied by an additional grading or by declaring the module ungraded.

## Normalized and unnormalized conventions

Connes's bounded convention begins with a self-adjoint involution \(F\) and requires \([F,\pi(a)]\) to be compact. The more flexible Kasparov convention used in the core permits self-adjointness and involutivity to fail locally by compact operators. These conventions give the same K-homological cycles after the standard normalization and stabilization procedures; one should nevertheless say which convention a formula assumes.

Nondegeneracy of \(\pi\) is commonly imposed for \(C^*\)-algebras. A degenerate zero summand can be removed, so allowing arbitrary representations does not change the resulting stable theory.

## Structure and consequences

For a unital algebra represented unitally, the compactness conditions say that the image of \(F\) in the Calkin algebra is a self-adjoint involution commuting with the image of \(A\). In the general nonunital convention, self-adjointness and involutivity hold only locally after multiplication by \(\pi(a)\); the defects of \(F\) need not themselves be compact. Thus a Fredholm module is not merely a [[functional-analysis/fredholm-operator|Fredholm operator]]: it is a Fredholm-type operator together with an algebra action that it intertwines modulo compact error.

Direct sums of modules are formed componentwise. Unitary equivalence, norm-continuous operator homotopy, and addition or removal of degenerate modules generate the stable equivalence used in [[noncommutative-geometry/analytic-k-homology|analytic K-homology]]. Under these operations, the index pairings remain unchanged.

## Examples and non-examples

For a compact [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\), an order-zero elliptic pseudodifferential operator between Hermitian bundles gives, after adjoining a parametrix in the opposite direction, an [[noncommutative-geometry/even-fredholm-module|even Fredholm module]] over \(C(M)\). Compactness of the commutators with multiplication operators is the analytic shadow of pseudolocality.

By contrast, a self-adjoint involution \(F\) and a representation \(\pi\) do not form a Fredholm module when some \([F,\pi(a)]\) is noncompact. The failed axiom is compatibility of the operator with the algebra action modulo compact operators.

## References

1. [Alain Connes, *Noncommutative Geometry*, Chapter IV, Section 1 and Appendix A, Academic Press, 1994](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).
2. [Nigel Higson and John Roe, *Analytic K-Homology*, Chapter 8, Oxford University Press, 2000](https://doi.org/10.1093/oso/9780198511762.001.0001).
