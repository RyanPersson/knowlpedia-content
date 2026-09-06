+++
id = "operator-algebras/bounded-operator-cstar-algebra"
title = "C*-algebra of bounded operators"
kind = "definition"
summary = "The unital C*-algebra of all bounded linear operators on a Hilbert space."
aliases = ["B(H)", "bounded operator algebra"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/hilbert-space", "functional-analysis/bounded-linear-operator", "linear-algebra/operator-norm"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(H\) be a complex [[linear-algebra/hilbert-space|Hilbert space]]. The
**\(C^*\)-algebra of bounded operators** \(B(H)\) consists of all
[[functional-analysis/bounded-linear-operator|bounded linear operators]]
\(T:H\to H\). Addition and scalar multiplication are pointwise, multiplication
is composition, and the involution is the Hilbert-space adjoint
\(T\mapsto T^*\). With the [[linear-algebra/operator-norm|operator norm]]
\[
\lVert T\rVert=\sup_{\lVert\xi\rVert\leq1}\lVert T\xi\rVert,
\]
\(B(H)\) is a unital [[operator-algebras/concrete-cstar-algebra|concrete
\(C^*\)-algebra]] whose identity is \(I_H\). It is the ambient algebra for
concrete representations of \(C^*\)-algebras and von Neumann algebras.

## Algebraic and norm structure

The defining identity
\[
\lVert T^*T\rVert=\lVert T\rVert^2
\]
follows from Hilbert-space geometry, and completeness follows from completeness
of the operator norm. Every bounded operator has a bounded adjoint, so \(B(H)\)
is closed under its involution. If \(H\) is finite-dimensional, choosing an
[[linear-algebra/orthonormal-basis|orthonormal basis]] identifies \(B(H)\) with a [[operator-algebras/matrix-cstar-algebra|full matrix algebra]]. If \(H\) is
infinite-dimensional, \(B(H)\) is nonseparable in operator norm even when \(H\)
is separable.

## Operator topologies and commutants

Besides its norm topology, \(B(H)\) carries the strong, weak, ultraweak, and
[[operator-algebras/ultrastrong-topology|ultrastrong operator topologies]]. These topologies are generally distinct on
infinite-dimensional \(H\), and none changes the underlying \(C^*\)-algebra
operations. The [[operator-algebras/commutant|commutant]] of a set of
operators is computed inside \(B(H)\); von Neumann algebras are exactly the
unital \(*\)-subalgebras of \(B(H)\) that are closed in the weak operator
topology, equivalently equal to their bicommutant.

## Conventions and nearby spaces

\(B(H,K)\) denotes the [[linear-algebra/banach-space|Banach space]] of bounded operators from \(H\) to another
Hilbert space \(K\). Unless \(H=K\), composition does not make \(B(H,K)\) an
algebra, so it should not be called a bounded-operator \(C^*\)-algebra. Some
authors write \(\mathcal B(H)\) or \(\mathscr L(H)\). When \(H=\{0\}\),
\(B(H)\) is the zero algebra; whether it is called unital depends on the
author's convention for the zero algebra.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §2.1 on bounded operators and concrete \(C^*\)-algebras.
2. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I: Elementary Theory*, American Mathematical Society, 1997. [AMS record](https://doi.org/10.1090/gsm/015). Relevant: Chapter 2 on Hilbert-space operators and operator topologies.
