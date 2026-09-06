+++
id = "supergeometry/supercommutative-algebra"
title = "Supercommutative algebra"
kind = "definition"
summary = "A superalgebra whose homogeneous elements commute with the Koszul sign."
aliases = ["graded-commutative superalgebra", "commutative superalgebra"]
domains = ["supergeometry", "algebra-commutative"]
prerequisites = ["supergeometry/superalgebra", "algebra-category-theory/algebra-object", "supergeometry/category-of-super-vector-spaces"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(k\) be a field of characteristic different from \(2\). A
[[supergeometry/superalgebra|superalgebra]] \(A\) is
**supercommutative** when its homogeneous elements satisfy
\[
ab=(-1)^{|a||b|}ba.
\]
Equivalently, its multiplication is unchanged by the Koszul braiding in
\(\mathbf{SuperVect}_k\), so \(A\) is a commutative [[algebra-category-theory/algebra-object|algebra object]] in the
[[supergeometry/category-of-super-vector-spaces|category of super vector
spaces]].

## Consequence for odd elements

If \(a\) is odd, supercommutativity gives \(a^2=-a^2\). Because \(2\) is
invertible in \(k\), every odd element therefore satisfies
\[
a^2=0.
\]
This conclusion need not follow in characteristic \(2\); definitions intended
for that setting commonly impose additional conditions on odd squares.

## Basic examples

The [[algebra-modules/exterior-algebra|exterior algebra]] \(\Lambda W\), graded
by exterior degree modulo \(2\), is supercommutative. More generally,
\[
\operatorname{Sym}(U)\otimes\Lambda(W)
\]
is supercommutative when \(U\) is even and \(W\) is odd. These algebras are the
local coordinate models in smooth and algebraic supergeometry.

By contrast, a [[differential-geometry/clifford-algebra|Clifford algebra]] is
naturally a superalgebra but is generally not supercommutative: its odd
generators can have nonzero squares.

## Terminology warning

“Graded-commutative” is also used for \(\mathbb Z\)-graded algebras with sign
\((-1)^{ij}\). Reducing a \(\mathbb Z\)-grading modulo \(2\) gives the present
rule, but it forgets the integer degree.

## References

1. C. Carmeli, L. Caston, and R. Fioresi, *Mathematical Foundations of
   Supersymmetry*, European Mathematical Society, 2011. [DOI
   record](https://doi.org/10.4171/097). Relevant: Chapter 1.
2. Y. I. Manin, *Gauge Field Theory and Complex Geometry*, second edition,
   Springer, 1997. [DOI
   record](https://doi.org/10.1007/978-3-662-07386-5). Relevant: Chapter 4.
