+++
id = "noncommutative-geometry/odd-fredholm-module"
title = "Odd Fredholm module"
kind = "definition"
summary = "An ungraded Fredholm module representing an odd analytic K-homology class."
aliases = ["ungraded Fredholm module", "odd bounded K-cycle"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
prerequisites = ["noncommutative-geometry/fredholm-module", "linear-algebra/hilbert-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) be a complex \(C^*\)-algebra. An **odd Fredholm module over \(A\)** is a [[noncommutative-geometry/fredholm-module|Fredholm module]] \((H,\pi,F)\) regarded without a \(\mathbb Z/2\)-grading: \(H\) is a complex [[linear-algebra/hilbert-space|Hilbert space]], \(\pi:A\to\mathcal B(H)\) is a representation, and the commutator and local self-adjointness and involutivity defects of \(F\) are compact. In the normalized convention this says
\[
F=F^*,\qquad F^2=I,\qquad [F,\pi(a)]\ \text{is compact for all }a\in A.
\]
“Odd” records K-homological degree, not that \(F\) is odd relative to an omitted grading.

## Projection picture

For a normalized odd module,
\[
P=\frac{I+F}{2}
\]
is an [[linear-algebra/orthogonal-projection|orthogonal projection]]. Compactness of \([F,\pi(a)]\) is equivalent to compactness of \([P,\pi(a)]\). Consequently \(P\pi(a)P\) is multiplicative modulo [[linear-algebra/compact-operator|compact operators]], which is the Toeplitz-type mechanism behind the [[noncommutative-geometry/odd-index-pairing|odd index pairing]].

For an unnormalized module over a unital algebra represented unitally, the image of \((I+F)/2\) in the Calkin algebra is a projection. In the nonunital convention the corresponding assertion is only local relative to the represented algebra. One can avoid this distinction by first passing to a normalized representative.

## Structure and consequences

Odd modules represent degree-one classes in [[noncommutative-geometry/analytic-k-homology|analytic K-homology]]. Their direct sum is addition, and stable homotopy identifies cycles that carry the same class. The terminology differs from graded algebra: there is no operator whose degree is being measured inside the ungraded Hilbert space.

An [[noncommutative-geometry/odd-spectral-triple|odd spectral triple]] has no grading compatible with its algebra and [[noncommutative-geometry/dirac-operator|Dirac operator]]. Its bounded transform is therefore an odd Fredholm module, provided the spectral-triple compactness and commutator hypotheses hold.

## Examples and non-examples

On \(H=L^2(S^1)\), let \(P\) project onto the Hardy space and put \(F=2P-I\). Multiplication by \(C(S^1)\) has compact commutators with \(P\), so this gives the fundamental odd Fredholm module of the circle. Compressing the coordinate unitary produces the unilateral shift and detects a nonzero index.

A normalized Fredholm module equipped with a compatible grading that commutes with the representation and anticommutes with \(F\) is an [[noncommutative-geometry/even-fredholm-module|even Fredholm module]], not an odd one under the standard parity convention.

## References

1. [Alain Connes, *Noncommutative Geometry*, Chapter IV, Section 1, Definition 1 and Proposition 2, Academic Press, 1994](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).
2. [Nigel Higson and John Roe, *Analytic K-Homology*, Chapter 8, Oxford University Press, 2000](https://doi.org/10.1093/oso/9780198511762.001.0001).
