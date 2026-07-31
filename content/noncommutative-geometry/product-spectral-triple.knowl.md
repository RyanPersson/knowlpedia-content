+++
id = "noncommutative-geometry/product-spectral-triple"
title = "Product of spectral triples"
kind = "definition"
summary = "The graded tensor product combines spectral triples using the Dirac operator D1 tensor 1 plus Gamma1 tensor D2."
aliases = ["tensor product of spectral triples", "graded product triple"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
+++

Let \((\mathcal A_i,H_i,D_i,\Gamma_i)\), \(i=1,2\), be
[[noncommutative-geometry/even-spectral-triple|even spectral triples]] over
complex [[linear-algebra/hilbert-space|Hilbert spaces]]. Their **product
spectral triple** has
\[
\mathcal A=\mathcal A_1\odot\mathcal A_2,\qquad
H=H_1\widehat\otimes H_2,\qquad
D=\overline{D_1\otimes1+\Gamma_1\otimes D_2},
\qquad \Gamma=\Gamma_1\otimes\Gamma_2.
\]
The algebraic [[algebra-modules/tensor-product-algebras|tensor product algebra]]
acts on the Hilbert tensor product in the evident way, and the bar denotes the
self-adjoint closure from the natural tensor-product core. The grading makes
the two unbounded summands anticommute, so \(D^2=D_1^2\otimes1+1\otimes D_2^2\)
on that core.

## Why the formula works

For \(a_i\in\mathcal A_i\),
\[
[D,a_1\otimes a_2]
=[D_1,a_1]\otimes a_2
 +\Gamma_1a_1\otimes[D_2,a_2],
\]
which is bounded. The anticommutation in the square combines compact
resolvents to give [[functional-analysis/compact-resolvent|compact resolvent]]
for \(D\) under the standard compact spectral-triple hypotheses. These signs
are precisely the
[[operator-algebras/graded-operator|graded-operator]] signs; omitting
\(\Gamma_1\) generally destroys the simple square formula
[Connes, Part VI.3].

## Geometric example

For closed even-dimensional spin manifolds \(M_1\) and \(M_2\), the product of
their canonical spin spectral triples is unitarily equivalent to the
canonical triple of \(M_1\times M_2\), after the standard identification of
product spinors. The displayed Dirac formula becomes the familiar product
formula for [[noncommutative-geometry/dirac-operator|spin Dirac operators]].

## Parity and conventions

If only the first factor is even, the same operator formula defines the
even–odd product, which is odd and has no product grading. Odd–odd products
require an auxiliary two-dimensional
[[differential-geometry/clifford-module|Clifford module]] or an equivalent
matrix convention. Different choices are unitarily equivalent after the
convention is fixed, but writing \(D_1\otimes1+1\otimes D_2\) without a
grading sign is not the graded product.

For \(C^*\)-completions of \(\mathcal A_1\odot\mathcal A_2\), the intended
tensor norm must be specified separately; the spectral-triple axioms are
imposed on the chosen dense star-subalgebra.

## References

1. Alain Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-hosted book](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Part VI.3 on products in spectral geometry.
2. Walter D. van Suijlekom, *Noncommutative Geometry and Particle Physics*, Springer, 2015. [Publisher record](https://doi.org/10.1007/978-94-017-9162-5). Relevant: the product construction used in the chapter “Almost-Commutative Manifolds and Gauge Theories,” pp. 137–158.
