+++
id = "supergeometry/universal-enveloping-algebra-of-lie-superalgebra"
title = "Universal enveloping algebra of a Lie superalgebra"
kind = "definition"
summary = "The associative superalgebra universally realizing a Lie superalgebra bracket as a supercommutator."
aliases = ["super universal enveloping algebra", "enveloping superalgebra"]
domains = ["supergeometry", "algebra-rings"]
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
The canonical map \(\mathfrak g\to U(\mathfrak g)\) sends the Lie bracket to
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

## Super PBW theorem

Filter \(U(\mathfrak g)\) by tensor degree. The super
Poincaré–Birkhoff–Witt theorem gives a canonical graded-superalgebra
isomorphism
\[
\operatorname{gr}U(\mathfrak g)
\cong
\operatorname{Sym}_{\mathrm s}(\mathfrak g).
\]
After choosing ordered homogeneous bases, PBW monomials use arbitrary
nonnegative powers of even basis elements and exponent \(0\) or \(1\) for odd
basis elements. Thus, as a vector space,
\[
U(\mathfrak g)
\cong U(\mathfrak g_{\bar0})\otimes
\Lambda(\mathfrak g_{\bar1}),
\]
although this displayed vector-space decomposition is not generally an
algebra decomposition.

## Clifford quotient

A [[differential-geometry/clifford-algebra|Clifford algebra]] can be recovered
from the enveloping algebra of a two-step Lie superalgebra by fixing a central
even generator. This makes precise the way a quadratic odd bracket deforms an
exterior algebra.

## References

1. I. M. Musson, *Lie Superalgebras and Enveloping Algebras*, American
   Mathematical Society, 2012. [DOI
   record](https://doi.org/10.1090/gsm/131). Relevant: Chapters 6–7.
2. M. Scheunert, *The Theory of Lie Superalgebras*, Lecture Notes in
   Mathematics 716, Springer, 1979. [DOI
   record](https://doi.org/10.1007/BFb0073442). Relevant: Chapter 2.
