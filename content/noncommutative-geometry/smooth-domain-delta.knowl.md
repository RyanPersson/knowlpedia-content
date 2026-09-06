+++
id = "noncommutative-geometry/smooth-domain-delta"
title = "Smooth domain of the Dirac derivation"
kind = "definition"
summary = "The algebra of bounded operators lying in the domain of every iterated commutator with the absolute Dirac operator."
aliases = ["OP-zero", "intersection of domains of delta powers", "smooth operators"]
domains = ["noncommutative-geometry", "functional-analysis"]
prerequisites = ["noncommutative-geometry/delta-derivation", "noncommutative-geometry/spectral-triple"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\delta(T)=[|D|,T]\) be the [[noncommutative-geometry/delta-derivation|Dirac derivation]] on \(B(H)\). Its **smooth domain** is
\[
\operatorname{Dom}\delta^\infty
=\bigcap_{k\geq1}\operatorname{Dom}\delta^k.
\]
Thus a bounded operator \(T\) lies in \(\operatorname{Dom}\delta^\infty\) precisely when every iterated commutator
\[
\delta^k(T)=[|D|,[|D|,\ldots,[|D|,T]\ldots]]
\]
initially defined on the appropriate common domain, extends to a bounded operator on \(H\). The notation \(\mathrm{OP}^0\) is often used for this same smooth operator algebra in the pseudodifferential calculus associated with a [[noncommutative-geometry/spectral-triple|spectral triple]]. Membership is an all-orders regularity condition, not merely boundedness of the first commutator.

## Fréchet algebra structure

The seminorms
\[
q_k(T)=\|\delta^k(T)\|,\qquad k=0,1,2,\ldots,
\]
where \(\delta^0(T)=T\), define a complete locally convex topology on the
smooth domain. The Leibniz rule expresses \(\delta^k(ST)\) as a finite sum of
products of iterated derivatives of \(S\) and \(T\), so
\(\operatorname{Dom}\delta^\infty\) is an algebra. It is also closed under
adjoints because \(\delta(T^*)=-\delta(T)^*\).

## Role in spectral regularity

A spectral triple is regular exactly when its represented algebra and all
basic commutators \([D,a]\) lie in this smooth domain. This hypothesis permits
repeated commutator expansions and serves as the order-zero coefficient
algebra for the local-index pseudodifferential calculus.

## Conventions and scope

**Warning.** The symbol \(\mathrm{OP}^0\) is calculus-dependent. Some authors
define it using commutators with \(\langle D\rangle=(1+D^2)^{1/2}\), or reserve
it for operators satisfying additional domain conditions. The displayed
intersection is the smooth domain of the specific derivation \(\delta\), and
any identification with another order-zero class must be checked in that
author's framework.

## References

1. A. Connes and H. Moscovici, “The Local Index Formula in Noncommutative Geometry,” *Geometric and Functional Analysis* 5 (1995), 174–243. [DOI record](https://doi.org/10.1007/BF01895667). Relevant: §II on the smooth domain of \(\delta\) and abstract pseudodifferential operators.
2. N. Higson, “The Local Index Formula in Noncommutative Geometry,” in *Contemporary Developments in Algebraic K-Theory*, ICTP Lecture Notes 15, 2004. [Author-hosted manuscript](https://nigel.higson.ca/uploads/1/2/1/4/121496570/higson_-_2004_-_the_local_index_formula_in_noncommutative_geometry.pdf). Relevant: §§3–4 on regularity and differential operator algebras.
