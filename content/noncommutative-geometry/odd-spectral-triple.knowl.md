+++
id = "noncommutative-geometry/odd-spectral-triple"
title = "Odd spectral triple"
kind = "definition"
summary = "An ungraded spectral triple representing the odd parity of analytic K-homology."
aliases = ["ungraded spectral triple", "odd K-cycle"]
domains = ["noncommutative-geometry", "operator-algebras"]
prerequisites = ["noncommutative-geometry/spectral-triple", "operator-algebras/involutive-algebra", "linear-algebra/hilbert-space", "noncommutative-geometry/analytic-k-homology", "noncommutative-geometry/even-spectral-triple"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

An **odd spectral triple** is a [[noncommutative-geometry/spectral-triple|spectral triple]] \((\mathcal A,H,D)\) regarded without a compatible \(\mathbb Z/2\)-grading: the data are the represented [[operator-algebras/involutive-algebra|involutive algebra]] \(\mathcal A\), [[linear-algebra/hilbert-space|Hilbert space]] \(H\), and self-adjoint operator \(D\), subject to the compactness and bounded-commutator axioms of a spectral triple. “Odd” names its parity in [[noncommutative-geometry/analytic-k-homology|analytic K-homology]]; it does not mean that \(D\) has odd degree on an unstated grading. If a grading \(\Gamma\) commuting with \(\mathcal A\) and anticommuting with \(D\) is included, the resulting object is instead an [[noncommutative-geometry/even-spectral-triple|even spectral triple]].

## Example: the circle

For the circle, take
\[
\mathcal A=C^\infty(S^1),\qquad
H=L^2(S^1),\qquad
D=-i\frac{d}{d\theta}
\]
with periodic domain \(H^1(S^1)\). Multiplication by \(f\in C^\infty(S^1)\) preserves the domain, and
\[
[D,f]=-i\,f'
\]
is bounded multiplication. The Fourier basis diagonalizes \(D\), and its eigenvalues tend to both positive and negative infinity, so \(D\) has compact resolvent. This is the basic odd spectral triple associated with a one-dimensional closed spin manifold.

## Bounded transform

The bounded transform
\[
F=D(1+D^2)^{-1/2}
\]
is self-adjoint and bounded. Under the spectral-triple hypotheses, it satisfies the compactness relations used in an odd bounded [[noncommutative-geometry/fredholm-module|Fredholm module]]. This construction connects the unbounded geometric cycle with an odd K-homology class. It does not say that \(D\) itself is bounded or Fredholm in the bounded-operator sense.

## Parity convention

Many texts define an odd cycle simply by omitting grading data. This does not assert that no compatible grading could possibly exist; it asserts that none is part of the odd cycle. Conversely, forgetting the grading from an even triple loses essential parity data and is not a neutral identification of its K-homology class.

## References

- [Alain Connes, *Noncommutative Geometry*, Parts IV and VI (Academic Press, 1994)](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf)
- [Nigel Higson and John Roe, *Analytic K-Homology* (Oxford University Press, 2000)](https://doi.org/10.1093/oso/9780198511762.001.0001)
