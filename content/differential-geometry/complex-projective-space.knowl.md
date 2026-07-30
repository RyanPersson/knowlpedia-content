+++
id = "differential-geometry/complex-projective-space"
title = "Complex projective space"
kind = "definition"
summary = "The compact complex manifold of complex lines in complex Euclidean space."
aliases = ["CPn", "complex projective n-space", "complex projective manifold"]
domains = ["differential-geometry", "algebraic-geometry-foundations", "complex-analysis"]
section_mode = "progressive"
+++

For \(n\ge0\), **complex projective \(n\)-space** is the set of one-dimensional complex linear subspaces of \(\mathbb C^{n+1}\):
\[
\mathbb{CP}^n=\mathbb P(\mathbb C^{n+1}).
\]
This is the complex-analytic manifold associated with the
[[algebraic-geometry-foundations/projective-space|scheme-theoretic projective
space]] \(\mathbb P_{\mathbb C}^n\). Its affine projective charts have
holomorphic transition maps, making it a
[[differential-geometry/complex-manifold|complex manifold]] of complex
dimension \(n\) and underlying real dimension \(2n\).

## Quotient and homogeneous-space descriptions

Scalar multiplication gives
\[
\mathbb{CP}^n\cong
(\mathbb C^{n+1}\setminus\{0\})/\mathbb C^\times.
\]
Every complex line meets the unit sphere in a circle, so there is also the Hopf quotient
\[
\mathbb{CP}^n\cong S^{2n+1}/U(1).
\]
The unitary group acts transitively on complex lines, with stabilizer \(U(1)\times U(n)\), yielding
\[
\mathbb{CP}^n\cong U(n+1)/(U(1)\times U(n)).
\]
These descriptions exhibit \(\mathbb{CP}^n\) as a compact connected smooth [[lie-groups/homogeneous-space|homogeneous space]].

## Complex, symplectic, and Kähler structure

The [[differential-geometry/fubini-study-metric|Fubini–Study metric]] is invariant under the projective unitary action, and its fundamental two-form is closed. Consequently \(\mathbb{CP}^n\) is a [[differential-geometry/kahler-manifold|Kähler manifold]]. Its Kähler class lies on the positive ray through the canonical integral generator of \(H^2(\mathbb{CP}^n;\mathbb Z)\).
With the normalization
\(\omega_{\mathrm{FS}}=i\partial\bar\partial\log(1+\lVert z\rVert^2)\),
the integral generator is \([\omega_{\mathrm{FS}}/(2\pi)]\).

The group \(\operatorname{PGL}_{n+1}(\mathbb C)\) acts transitively by holomorphic transformations, but it does not preserve a chosen Fubini–Study metric in general; the projective unitary subgroup does. Thus the holomorphic and isometric symmetry groups should not be conflated.

## Important low-dimensional case

The complex projective line \(\mathbb{CP}^1\) is the [[complex-analysis/riemann-sphere|Riemann sphere]]. It is diffeomorphic to \(S^2\), while for higher \(n\), \(\mathbb{CP}^n\) is not a sphere.

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Publisher record](https://doi.org/10.1007/b137952). Relevant: Chapter 1, projective space as a complex manifold, and Chapter 3, the Fubini–Study Kähler form.
2. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [Publisher record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: quotient manifolds and homogeneous spaces.
