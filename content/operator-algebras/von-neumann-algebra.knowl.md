+++
id = "operator-algebras/von-neumann-algebra"
title = "Von Neumann algebra"
kind = "definition"
summary = "A unital self-adjoint algebra of bounded Hilbert-space operators that is closed in the weak operator topology."
aliases = ["W*-algebra", "concrete von Neumann algebra"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(H\) be a [[linear-algebra/hilbert-space|Hilbert space]]. A **von Neumann
algebra** on \(H\) is a unital \(*\)-subalgebra
\(M\subseteq B(H)\), the algebra of
[[operator-algebras/bounded-operator-cstar-algebra|bounded operators]], that is
closed in the [[operator-algebras/weak-operator-topology|weak operator topology]]. Equivalently, \(M\) is closed in the
[[operator-algebras/strong-operator-topology|strong operator topology]] or satisfies
\[
M=M'',
\]
where \(M''\) is its [[operator-algebras/bicommutant|bicommutant]]. An abstract
**\(W^*\)-algebra** is a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]
that is the dual [[linear-algebra/banach-space|Banach space]] of a Banach-space predual. Every abstract
\(W^*\)-algebra has a faithful representation as a concrete von Neumann
algebra.

## Closure and the bicommutant theorem

For a unital self-adjoint subalgebra \(A\subseteq B(H)\), the von Neumann
bicommutant theorem identifies its weak-operator closure, strong-operator
closure, and [[operator-algebras/bicommutant|double commutant]] \(A''\).
The hypotheses matter: an arbitrary weakly closed nonself-adjoint operator
algebra is not a von Neumann algebra. Norm closure alone produces only a
\(C^*\)-algebra and is generally smaller.

## The predual and normality

The predual \(M_*\) of a von Neumann algebra is unique up to isometric
isomorphism. Its elements are the normal bounded linear functionals, and the
[[functional-analysis/weak-star-topology|weak-star topology]] \(\sigma(M,M_*)\) agrees with the ultraweak topology in a
concrete faithful representation. This predual is extra analytic structure
not carried by an arbitrary \(C^*\)-algebra; it supports [[operator-algebras/normal-state|normal states]],
normal maps, and monotone convergence.

## Examples and scope

The full algebra \(B(H)\), every [[operator-algebras/commutant|commutant]]
\(S'\subseteq B(H)\), and \(L^\infty(X,\mu)\) acting by multiplication on
\(L^2(X,\mu)\) are von Neumann algebras. A norm-closed algebra such as
\(C([0,1])\) in its multiplication representation is usually not weakly
closed. Calling a \(W^*\)-algebra a von Neumann algebra suppresses the choice
of faithful concrete representation but is standard when no confusion can
result.

## References

1. Masamichi Takesaki, Theory of Operator Algebras I, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter III on von Neumann algebras, bicommutants, preduals, and normal functionals.
2. Shôichirô Sakai, \(C^*\)-Algebras and \(W^*\)-Algebras, Springer, 1971; Classics in Mathematics reprint, 1998. [Publisher record](https://doi.org/10.1007/978-3-642-61993-9). Relevant: Chapter 1 on the abstract predual characterization.
