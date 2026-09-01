+++
id = "operator-algebras/commutative-von-neumann-algebra"
title = "Commutative von Neumann algebra"
kind = "definition"
summary = "A von Neumann algebra whose elements commute, modeled by an algebra of essentially bounded functions."
aliases = ["abelian von Neumann algebra", "L-infinity algebra"]
domains = ["operator-algebras", "measure-theory"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/center-of-von-neumann-algebra", "measure-theory/measure-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A **commutative von Neumann algebra** is a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\) in which
\(xy=yx\) for all \(x,y\in M\). Equivalently, \(M\) equals its
[[operator-algebras/center-of-von-neumann-algebra|center]]. The fundamental
concrete model is \(L^\infty(X,\mu)\), acting on \(L^2(X,\mu)\) by
multiplication:
\[
(M_f\xi)(x)=f(x)\xi(x).
\]
For suitable localizable [[measure-theory/measure-space|measure spaces]],
every commutative von Neumann algebra is isomorphic as a von Neumann algebra
to such an \(L^\infty\) algebra. The measure model is determined by the
associated measure algebra, not by a preferred point-set presentation of
\(X\).

## Projections and measure

The projections in \(L^\infty(X,\mu)\) are the [[shared-foundations/equivalence-class|equivalence classes]] of
[[measure-theory/indicator-function|indicator functions]] \(1_E\) of
[[measure-theory/measurable-set|measurable sets]], where sets differing by a [[measure-theory/null-set|null
set]] define the same projection. Joins, meets, and complements of
projections correspond to the Boolean operations on measurable sets modulo
[[measure-theory/null-set|null sets]]. This complete projection lattice is the measure-theoretic skeleton
of the algebra.

## Atomic and diffuse parts

A commutative von Neumann algebra is atomic when every nonzero projection
dominates a [[operator-algebras/minimal-projection|minimal projection]];
typical examples are \(\ell^\infty(I)\).
It is diffuse when it has no nonzero minimal projections, as for
\(L^\infty([0,1])\) with [[measure-theory/lebesgue-measure|Lebesgue measure]]. In general the algebra decomposes
canonically into central atomic and diffuse summands.

## Contrast with commutative C*-algebras

A commutative \(C^*\)-algebra is described by continuous functions on a
[[topology/locally-compact-space|locally compact space]], whereas a commutative von Neumann algebra is governed
by essentially bounded [[measure-theory/measurable-function|measurable functions]] and is monotone complete. Its
natural topology is the weak-star topology coming from its predual, not the
uniform topology alone. This
[[functional-analysis/weak-star-topology|weak-star topology]] and the extra
order structure record measure classes and normal integration.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 2002. [Publisher record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter III, §1 on commutative von Neumann algebras and measure representations.
2. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, American Mathematical Society, 1997. [Publisher record](https://bookstore.ams.org/GSM/16/). Relevant: the representation and projection theory of abelian von Neumann algebras.
