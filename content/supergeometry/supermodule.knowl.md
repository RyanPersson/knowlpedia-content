+++
id = "supergeometry/supermodule"
title = "Supermodule"
kind = "definition"
summary = "A graded module over a superalgebra with degree-preserving action."
aliases = ["graded module over a superalgebra", "superalgebra module"]
domains = ["supergeometry", "algebra-modules"]
section_mode = "progressive"
prerequisites = ["supergeometry/superalgebra", "supergeometry/super-vector-space", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A=A_{\bar0}\oplus A_{\bar1}\) be a
[[supergeometry/superalgebra|superalgebra]]. A **left supermodule** over \(A\)
is a [[supergeometry/super-vector-space|super vector space]]
\(M=M_{\bar0}\oplus M_{\bar1}\) with a unital associative action satisfying
\[
A_{\bar i}M_{\bar j}\subseteq M_{\bar i+\bar j}.
\]
Equivalently, the action \(A\otimes M\to M\) is an even map in
\(\mathbf{SuperVect}\).

## Morphisms and internal maps

Morphisms of supermodules are usually even \(A\)-linear maps. A homogeneous
linear map \(f:M\to N\) of parity \(\epsilon\) is internally \(A\)-linear when
\[
f(am)=(-1)^{\epsilon|a|}a\,f(m)
\]
for homogeneous \(a\in A\). Thus degree-zero internal maps are precisely the
ordinary morphisms, while degree-one internal maps are odd module maps.

## Left and right modules

Koszul signs enter when one converts a left action into a right action. If
\(A\) is supercommutative and \(M\) is a left \(A\)-supermodule, the compatible
right action is
\[
m a=(-1)^{|m||a|}a m
\]
on homogeneous elements. Omitting this sign generally breaks associativity
with the super symmetry.

## Clifford modules

Because a [[differential-geometry/clifford-algebra|Clifford algebra]] is
\(\mathbb Z/2\)-graded, a graded
[[differential-geometry/clifford-module|Clifford module]] is exactly a
supermodule over that superalgebra. An ungraded Clifford module instead
forgets the parity information.

## References

1. V. S. Varadarajan, *Supersymmetry for Mathematicians: An Introduction*,
   American Mathematical Society, 2004. [DOI
   record](https://doi.org/10.1090/cour/011). Relevant: Chapter 1.
2. I. M. Musson, *Lie Superalgebras and Enveloping Algebras*, American
   Mathematical Society, 2012. [DOI
   record](https://doi.org/10.1090/gsm/131). Relevant: Chapter 1.
