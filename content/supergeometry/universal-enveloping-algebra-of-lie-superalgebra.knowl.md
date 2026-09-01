+++
id = "supergeometry/universal-enveloping-algebra-of-lie-superalgebra"
title = "Universal enveloping algebra of a Lie superalgebra"
kind = "definition"
summary = "The associative superalgebra universally realizing a Lie superalgebra bracket as a supercommutator."
aliases = ["super universal enveloping algebra", "enveloping superalgebra"]
domains = ["supergeometry", "algebra-rings"]
prerequisites = ["supergeometry/lie-superalgebra", "algebra-modules/tensor-algebra", "fiber-bundles/lie-bracket"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(\mathfrak g\) be a [[supergeometry/lie-superalgebra|Lie superalgebra]]
over a field of characteristic \(0\). Its **universal enveloping algebra** is
the superalgebra
\[
U(\mathfrak g)
=T(\mathfrak g)\Big/
\left\langle
x\otimes y-(-1)^{|x||y|}y\otimes x-[x,y]
\right\rangle,
\]
where \(x,y\) range over homogeneous elements and
\(T(\mathfrak g)\) is the [[algebra-modules/tensor-algebra|tensor algebra]].
The canonical map \(\mathfrak g\to U(\mathfrak g)\) sends the [[fiber-bundles/lie-bracket|Lie bracket]] to
the supercommutator.

## Universal property

If \(A\) is an associative [[supergeometry/superalgebra|superalgebra]] and
\(\phi:\mathfrak g\to A\) is a Lie-superalgebra morphism into the
supercommutator Lie superalgebra of \(A\), there is a unique superalgebra
homomorphism
\[
\widetilde\phi:U(\mathfrak g)\longrightarrow A
\]
extending \(\phi\). Consequently, representations of \(\mathfrak g\) are
equivalently supermodules over \(U(\mathfrak g)\), with the same parity
convention on morphisms.

Filtering \(U(\mathfrak g)\) by tensor degree gives the
[[supergeometry/super-pbw-theorem|super PBW theorem]].

## Clifford quotient

The [[differential-geometry/clifford-algebra-as-super-enveloping-quotient|Clifford
algebra as a super-enveloping quotient]] makes precise how fixing a central
even generator turns a quadratic odd bracket into a Clifford relation.

## References

1. I. M. Musson, *Lie Superalgebras and Enveloping Algebras*, American
   Mathematical Society, 2012. [DOI
   record](https://doi.org/10.1090/gsm/131). Relevant: Chapters 6–7.
2. M. Scheunert, *The Theory of Lie Superalgebras*, Lecture Notes in
   Mathematics 716, Springer, 1979. [DOI
   record](https://doi.org/10.1007/BFb0073442). Relevant: Chapter 2.
