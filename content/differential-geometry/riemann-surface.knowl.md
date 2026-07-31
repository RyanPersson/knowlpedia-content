+++
id = "differential-geometry/riemann-surface"
title = "Riemann surface"
kind = "definition"
summary = "A connected complex manifold of complex dimension one."
aliases = ["complex curve", "one-dimensional complex manifold"]
domains = ["differential-geometry", "complex-analysis"]
section_mode = "progressive"
+++

A **Riemann surface** is a connected [[differential-geometry/complex-manifold|complex manifold]] of complex dimension \(1\). Explicitly, it is a connected Hausdorff, second-countable space \(X\) with an atlas of homeomorphisms \(z_\alpha:U_\alpha\to V_\alpha\subseteq\mathbb C\) whose transition maps \(z_\beta\circ z_\alpha^{-1}\) are [[differential-geometry/holomorphic-map|holomorphic]] wherever defined. Thus \(X\) is an underlying real [[fiber-bundles/smooth-manifold|smooth manifold]] of dimension \(2\), while its [[differential-geometry/complex-coordinate-chart|complex charts]] specify which local complex-valued functions and maps are holomorphic.

## Holomorphic structure

A function \(f:X\to\mathbb C\) is holomorphic precisely when \(f\circ z_\alpha^{-1}\) is holomorphic in one complex variable in every chart. These functions form the [[differential-geometry/sheaf-of-holomorphic-functions|sheaf of holomorphic functions]] \(\mathcal O_X\). A map between Riemann surfaces is holomorphic when its coordinate expressions are holomorphic. Every bijective holomorphic map between Riemann surfaces is automatically biholomorphic: injectivity rules out a zero local derivative, so the holomorphic inverse function theorem applies in charts.

## Underlying orientation

Every Riemann surface has a canonical orientation as a real surface. Indeed, a holomorphic transition map with nonzero complex derivative has positive real [[real-analysis/jacobian-determinant|Jacobian determinant]] \(\lvert f'(z)\rvert^2\), so its complex charts are orientation-compatible. This orientation is part of the structure induced by the [[differential-geometry/complex-atlas|complex atlas]], not extra data chosen afterward. The basic manifold and mapping conventions are presented in [Forster, §§1–2](https://doi.org/10.1007/978-1-4612-5961-9).

## Examples and conventions

Connected open subsets of \(\mathbb C\), the Riemann sphere
\(\mathbb P^1(\mathbb C)\), complex tori \(\mathbb C/\Lambda\), and connected
nonsingular complex plane curves are standard examples. More generally, each
connected component of a nonsingular complex curve is a Riemann surface. A
topological surface alone is not a Riemann surface until a complex structure
is specified. Some authors allow a Riemann surface to be disconnected; here
connectedness is part of the definition. “Complex curve” may also mean a
singular analytic space or an algebraic curve, whereas this knowl uses it only
for a nonsingular one-dimensional complex manifold.

## References

1. Otto Forster, *Lectures on Riemann Surfaces*, Graduate Texts in Mathematics 81, Springer, 1981. [Publisher record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: Chapter 1, §§1–2 and §6.
