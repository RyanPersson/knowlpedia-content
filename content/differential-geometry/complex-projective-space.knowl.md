+++
id = "differential-geometry/complex-projective-space"
title = "Complex projective space"
kind = "definition"
summary = "The compact complex manifold of complex lines in complex Euclidean space."
aliases = ["CPn", "complex projective n-space", "complex projective manifold"]
domains = ["differential-geometry", "algebraic-geometry-foundations", "complex-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/vector-space", "shared-foundations/complex-numbers-c", "topology/quotient-topology", "differential-geometry/complex-manifold"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

For \(n\ge0\), **complex projective \(n\)-space** is the quotient
\[
\mathbb{CP}^n=(\mathbb C^{n+1}\setminus\{0\})/\mathbb C^\times,
\]
where \(\mathbb C^\times\) acts by scalar multiplication and the quotient
has the [[topology/quotient-topology|quotient topology]]. Equivalently, its
points are one-dimensional complex linear subspaces of \(\mathbb C^{n+1}\).
For each \(i\), the sets \(U_i=\{[z_0:\cdots:z_n]:z_i\ne0\}\) are identified
with \(\mathbb C^n\) by the coordinate ratios \(z_j/z_i\) for \(j\ne i\).
On overlaps these ratios give holomorphic transition maps, so the charts
define a [[differential-geometry/complex-manifold|complex manifold]] of
complex dimension \(n\) and real dimension \(2n\).

## Comparison with algebraic geometry

This complex manifold is also the analytification associated with the
[[algebraic-geometry-foundations/projective-space|scheme-theoretic projective space]] \(\mathbb P^n_{\mathbb C}\), via the usual complex points and their analytic structure.

## Quotient and homogeneous-space descriptions

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

The [[differential-geometry/fubini-study-metric|Fubini–Study metric]] is invariant under the projective unitary action, and its fundamental two-form is closed. Consequently \(\mathbb{CP}^n\) is a [[differential-geometry/kahler-manifold|Kähler manifold]]. Its [[differential-geometry/kahler-class|Kähler class]] lies on the positive ray through the canonical integral generator of \(H^2(\mathbb{CP}^n;\mathbb Z)\).
With the normalization
\(\omega_{\mathrm{FS}}=i\partial\bar\partial\log(1+\lVert z\rVert^2)\),
the integral generator is \([\omega_{\mathrm{FS}}/(2\pi)]\).

The group \(\operatorname{PGL}_{n+1}(\mathbb C)\) acts transitively by holomorphic transformations, but it does not preserve a chosen Fubini–Study metric in general; the projective unitary subgroup does. Thus the holomorphic and isometric symmetry groups should not be conflated.

## Important low-dimensional case

The complex projective line \(\mathbb{CP}^1\) is the [[complex-analysis/riemann-sphere|Riemann sphere]]. It is diffeomorphic to \(S^2\), while for higher \(n\), \(\mathbb{CP}^n\) is not a sphere.

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Publisher record](https://doi.org/10.1007/b137952). Relevant: Chapter 1, projective space as a complex manifold, and Chapter 3, the Fubini–Study Kähler form.
2. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [Publisher record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: quotient manifolds and homogeneous spaces.
