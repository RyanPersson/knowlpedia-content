+++
id = "noncommutative-geometry/spectral-triple"
title = "Spectral triple"
kind = "definition"
summary = "An algebra represented on a Hilbert space together with a self-adjoint operator having compact resolvent and bounded algebra commutators."
aliases = ["unbounded Fredholm module", "compact spectral triple", "K-cycle"]
domains = ["noncommutative-geometry", "operator-algebras"]
prerequisites = ["operator-algebras/involutive-algebra", "linear-algebra/hilbert-space", "operator-algebras/bounded-star-representation", "functional-analysis/self-adjoint-unbounded-operator", "functional-analysis/compact-resolvent", "functional-analysis/bounded-commutator"]
dependency_review_count = 1
section_mode = "progressive"
+++

A **compact spectral triple** \((\mathcal A,H,D)\) consists of a unital
[[operator-algebras/involutive-algebra|involutive algebra]] \(\mathcal A\), a [[linear-algebra/hilbert-space|Hilbert space]] \(H\) carrying a
[[operator-algebras/bounded-star-representation|bounded star-representation]]
of \(\mathcal A\), and a densely defined
[[functional-analysis/self-adjoint-unbounded-operator|self-adjoint operator]]
\(D\). The operator has
[[functional-analysis/compact-resolvent|compact resolvent]], and every
\(a\in\mathcal A\) preserves \(\operatorname{Dom}(D)\), with the commutator
there extending to a
[[functional-analysis/bounded-commutator|bounded operator]] on \(H\). The
representation is usually suppressed, so \(a\) denotes its represented
operator. It is often required to be faithful, or \(\mathcal A\) is replaced
by its represented quotient.

## What the axioms encode

The algebra \(\mathcal A\) plays the role of a smooth algebra of functions, while \(H\) is the space on which geometry is represented. The operator \(D\) supplies metric and differential information. Compact resolvent gives discrete spectral behavior analogous to an elliptic operator on a compact manifold. Boundedness of
\[
[D,a]=Da-aD
\]
is the abstract first-order regularity condition: multiplication by a smooth function changes a first-order differential operator only by an operator of order zero.

The adjective “spectral” does not mean that the spectrum alone determines every aspect of the triple. The representation of \(\mathcal A\) and its commutators with \(D\) are part of the data.

## Canonical commutative example

Let \(M\) be a closed Riemannian spin manifold, let \(\mathcal A=C^\infty(M)\), let \(H=L^2(M,S)\) be the square-integrable sections of its [[differential-geometry/spinor-bundle|spinor bundle]], and let \(D\) be the spin [[noncommutative-geometry/dirac-operator|Dirac operator]]. Functions act by multiplication. Ellipticity and compactness of \(M\) give compact resolvent, while
\[
[D,f]=c(df)
\]
is bounded Clifford multiplication by the differential of \(f\). Thus \((C^\infty(M),L^2(M,S),D)\) is a spectral triple.

## Parity

An [[noncommutative-geometry/even-spectral-triple|even spectral triple]] includes a compatible grading on \(H\) for which the algebra acts evenly and \(D\) acts oddly. An [[noncommutative-geometry/odd-spectral-triple|odd spectral triple]] is ungraded. Parity is additional structure and is separate from summability, regularity, reality, and first-order axioms that may be imposed in more elaborate versions.

## Nonunital and locally compact variants

For a nonunital algebra, compact resolvent is generally too strong. A common locally compact convention replaces it by
\[
a(1+D^2)^{-1/2}\in K(H)
\qquad\text{for every }a\in\mathcal A.
\]
For unital \(\mathcal A\), taking \(a=1\) recovers compactness of \((1+D^2)^{-1/2}\), hence compact resolvent. Semifinite, real, twisted, and graded-algebra spectral triples modify other parts of the definition; hypotheses from one variant should not be presumed in another.

## References

- [Alain Connes, *Noncommutative Geometry*, Parts IV and VI (Academic Press, 1994)](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf)
- [Alain Connes and Henri Moscovici, “The local index formula in noncommutative geometry,” *Geometric and Functional Analysis* 5 (1995), 174–243](https://doi.org/10.1007/BF01895667)
- [José M. Gracia-Bondía, Joseph C. Várilly, and Héctor Figueroa, *Elements of Noncommutative Geometry*, Section 10.1 (Birkhäuser, 2001)](https://doi.org/10.1007/978-1-4612-0005-5)
