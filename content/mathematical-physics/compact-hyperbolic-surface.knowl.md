+++
id = "mathematical-physics/compact-hyperbolic-surface"
title = "Compact hyperbolic surface"
kind = "definition"
summary = "A compact connected surface equipped with a complete Riemannian metric of constant curvature minus one."
aliases = ["closed hyperbolic surface", "compact surface of constant negative curvature"]
domains = ["mathematical-physics", "differential-geometry", "quantum-chaos"]
section_mode = "progressive"
prerequisites = ["differential-geometry/riemannian-manifold"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **compact hyperbolic surface** is a compact connected smooth surface \(M\)
with a [[differential-geometry/riemannian-manifold|Riemannian metric]] of constant
sectional curvature \(-1\). Equivalently,
\[
M\cong\Gamma\backslash\mathbb H^2,
\]
where \(\Gamma\) is a torsion-free cocompact discrete group of orientation-
preserving isometries of the hyperbolic plane.

## Disk model

The hyperbolic plane may be represented by the Poincaré disk
\(\mathbb D=\{z\in\mathbb C:|z|<1\}\). Its ideal boundary is \(S^1\), and each
complete geodesic has two endpoints there.

## Dynamical role

The [[differential-geometry/geodesic-flow|geodesic flow]] on the unit
[[fiber-bundles/tangent-bundle|tangent bundle]] of \(M\) is
[[differential-geometry/anosov-flow|Anosov]]. Its stable and
unstable directions create porous sets of boundary endpoints associated with
geodesics avoiding an open observation region, which is how
[[harmonic-analysis/fractal-uncertainty-principle|fractal uncertainty]] enters
quantum chaos.

The [[differential-geometry/horocycle-flow|horocycle flow]] supplies the
recurrence used to prove porosity in the surface application.

## References

1. David Borthwick, *Spectral Theory of Infinite-Area Hyperbolic Surfaces*, 2nd ed., Birkhäuser, 2016. [DOI record](https://doi.org/10.1007/978-3-319-33877-4).
