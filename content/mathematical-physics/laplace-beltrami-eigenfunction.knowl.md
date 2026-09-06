+++
id = "mathematical-physics/laplace-beltrami-eigenfunction"
title = "Laplace–Beltrami eigenfunction"
kind = "definition"
summary = "A nonzero function transformed into a scalar multiple of itself by the Laplace–Beltrami operator."
aliases = ["Laplace eigenfunction", "Riemannian Laplacian eigenfunction"]
domains = ["mathematical-physics", "spectral-theory", "differential-geometry"]
prerequisites = ["differential-geometry/riemannian-manifold", "differential-geometry/laplace-beltrami-operator"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,g)\) be a [[differential-geometry/riemannian-manifold|Riemannian manifold]]. A nonzero smooth function
\(\psi:M\to\mathbb C\) is a **Laplace–Beltrami eigenfunction** with eigenvalue
\(\lambda\) if
\[
-\Delta_g\psi=\lambda\psi,
\]
where \(\Delta_g\) is the
[[differential-geometry/laplace-beltrami-operator|Laplace–Beltrami operator]].
The minus sign makes \(\lambda\ge0\) on a compact manifold.

## Compact case

On a compact connected manifold without boundary, the spectrum is discrete,
each eigenspace is finite-dimensional, and the eigenfunctions form an
[[linear-algebra/orthonormal-basis|orthonormal basis]] of \(L^2(M)\). The zero eigenspace consists of constant
functions.

## High-frequency scale

For large eigenvalue one often writes \(\lambda=h^{-2}\), where \(h\to0\) is
the semiclassical parameter. The spatial and phase-space distributions of
\(L^2\)-normalized eigenfunctions are central objects in quantum chaos.

## References

1. Isaac Chavel, *Eigenvalues in Riemannian Geometry*, Academic Press, 1984. [DOI record](https://doi.org/10.1016/C2013-0-11074-8).
