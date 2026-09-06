+++
id = "algebraic-geometry-foundations/lisse-ell-adic-sheaf"
title = "Lisse ell-adic sheaf"
kind = "definition"
summary = "An ell-adic sheaf that is locally a finite free constant sheaf in the étale topology."
aliases = ["lisse ℓ-adic sheaf", "smooth ell-adic sheaf", "ell-adic local system", "lisse Q_l-sheaf"]
domains = ["algebraic-geometry-foundations", "langlands", "algebra-fields-galois"]
prerequisites = ["algebraic-geometry-foundations/scheme", "algebraic-geometry-foundations/small-etale-site"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be a connected [[algebraic-geometry-foundations/scheme|scheme]] on
which the prime \(\ell\) is invertible. A
**lisse \(\mathbb Z_\ell\)-sheaf** is an inverse system

\[
\mathcal F=(\mathcal F_n)_{n\ge1}
\]

in which each \(\mathcal F_n\) is a locally constant constructible sheaf of
finite free \(\mathbb Z/\ell^n\mathbb Z\)-modules on the
[[algebraic-geometry-foundations/small-etale-site|étale site]] and
\(\mathcal F_{n+1}/\ell^n\simeq\mathcal F_n\).  A lisse
\(\mathbb Q_\ell\)-sheaf is obtained by inverting \(\ell\), or equivalently by
using a finite-dimensional \(\mathbb Q_\ell\)-local system in the pro-étale
formalism.

## Monodromy representation

After choosing a geometric point \(\bar x\), taking the fiber gives an
equivalence between lisse \(\mathbb Q_\ell\)-sheaves of rank \(n\) and
continuous
[[algebra-representation-theory/group-representation|representations]]

\[
\pi_1^{\mathrm{ét}}(X,\bar x)
\longrightarrow\operatorname{GL}_n(\mathbb Q_\ell).
\]

Changing \(\bar x\) changes the representation by the usual inner
identification. On a variety over a
[[algebra-fields-galois/finite-field|finite field]], arithmetic or geometric
[[algebra-fields-galois/frobenius-endomorphism|Frobenius]] acts on each
closed-point fiber.

## Lisse versus constructible

A constructible sheaf need only be lisse on each piece of a finite
stratification. Thus “lisse” is the algebro-geometric analogue of a
[[fiber-bundles/local-system|local system]], while constructible sheaves allow
singularities and extension across strata.

## References

1. Alexander Grothendieck, *SGA 4½: Cohomologie étale*, Lecture Notes in
   Mathematics 569, Springer, 1977.
2. The Stacks Project Authors, “Pro-étale Cohomology,” §61.28,
   “Constructible adic sheaves.”
   [Stacks Project](https://stacks.math.columbia.edu/tag/09BS).
