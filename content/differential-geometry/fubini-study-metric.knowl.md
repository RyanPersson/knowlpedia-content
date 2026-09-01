+++
id = "differential-geometry/fubini-study-metric"
title = "Fubini–Study metric"
kind = "definition"
summary = "The canonical unitary-invariant Kähler metric on complex projective space."
aliases = ["Fubini Study metric", "Fubini–Study Kähler form"]
domains = ["differential-geometry"]
prerequisites = ["algebraic-geometry-foundations/projective-space", "differential-geometry/kahler-metric", "differential-geometry/kahler-form"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

On [[algebraic-geometry-foundations/projective-space|complex projective space]] \(\mathbb{CP}^n\), the **Fubini–Study metric** is the [[differential-geometry/kahler-metric|Kähler metric]] whose [[differential-geometry/kahler-form|Kähler form]] on the affine chart \(Z_0\neq0\), with \(z_j=Z_j/Z_0\), is
\[
\omega_{\mathrm{FS}}=i\,\partial\bar\partial\log(1+\lVert z\rVert^2).
\]
Equivalently, its Hermitian coefficients are
\[
(g_{j\bar k})=
\frac{(1+\lVert z\rVert^2)\delta_{jk}-\bar z_jz_k}
{(1+\lVert z\rVert^2)^2}.
\]
These local formulas agree on chart overlaps and define a smooth positive form. This normalization is fixed in the core; authors also multiply the form by \(1/2\), \(1/2\pi\), or another positive constant.

## Global construction and invariance

The [[differential-geometry/local-kahler-potential|local potential]] \(\log(1+\lVert z\rVert^2)\) is the chart expression of \(\log\lVert Z\rVert^2\) in homogeneous coordinates. Changing a homogeneous representative adds the logarithm of the squared modulus of a nowhere-zero holomorphic function, whose \(i\partial\bar\partial\) vanishes. Hence the forms glue globally. The resulting metric is invariant under the projective action of \(U(n+1)\).

## Geometry and normalization

The Fubini–Study metric has positive constant holomorphic sectional curvature, with the numerical value depending on normalization. Its [[differential-geometry/kahler-class|Kähler class]] generates \(H^2(\mathbb{CP}^n;\mathbb Z)\) after the standard integral normalization \([\omega_{\mathrm{FS}}/(2\pi)]\). On \(\mathbb{CP}^1\), it is a constant multiple of the round metric under the identification with the two-sphere.

The metric is also obtained by Kähler reduction of the unit sphere in \(\mathbb C^{n+1}\) by the scalar \(S^1\)-action.

## References

1. Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry*, Wiley, 1978. [Wiley DOI record](https://doi.org/10.1002/9781118032527). Relevant: Chapter 0, §5.
2. Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*, 2012. [Author-hosted text](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf). Relevant: Chapter VI, §4, Example 4.4.
