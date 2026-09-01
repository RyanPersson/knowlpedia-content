+++
id = "mathematical-physics/uniform-eigenfunction-mass-lower-bound"
title = "Uniform mass lower bound for hyperbolic-surface eigenfunctions"
kind = "theorem"
summary = "Every normalized Laplace eigenfunction on a compact hyperbolic surface has a uniformly positive amount of L2 mass in each fixed nonempty open set."
aliases = ["Dyatlov–Jin eigenfunction mass theorem", "full support of semiclassical measures on hyperbolic surfaces"]
domains = ["mathematical-physics", "spectral-theory", "quantum-chaos"]
prerequisites = ["mathematical-physics/compact-hyperbolic-surface", "mathematical-physics/laplace-beltrami-eigenfunction", "differential-geometry/laplace-beltrami-operator"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(M\) be a [[mathematical-physics/compact-hyperbolic-surface|compact
hyperbolic surface]] and \(U\subset M\) a nonempty open set. There is
\(c_U>0\) such that every \(L^2\)-normalized
[[mathematical-physics/laplace-beltrami-eigenfunction|eigenfunction]]
\(\psi_k\) of the [[differential-geometry/laplace-beltrami-operator|Laplace–Beltrami operator]] satisfies
\[
\|\psi_k\mathbf1_U\|_{L^2(M)}\ge c_U.
\]
The constant depends on \(U\) and \(M\), but not on the eigenvalue.

## Semiclassical interpretation

Writing a high eigenvalue as \(h^{-2}\), the theorem rules out a sequence of
eigenfunctions whose mass in \(U\) tends to zero as \(h\to0\). Equivalently,
every [[mathematical-physics/semiclassical-measure|semiclassical measure]]
arising from eigenfunctions has full support.

## Role of fractal uncertainty

Boundary data giving incoming and outgoing
[[mathematical-physics/hyperbolic-plane-wave|hyperbolic plane-wave]]
representations would both have to concentrate near the porous set of geodesic
endpoints avoiding \(U\). Their oscillatory relation and the
[[harmonic-analysis/fractal-uncertainty-principle|fractal uncertainty
principle]] exclude simultaneous concentration.

## References

1. Semyon Dyatlov and Long Jin, “Semiclassical measures on hyperbolic surfaces have full support,” *Acta Mathematica* 220 (2018), 297–339. [DOI record](https://doi.org/10.4310/ACTA.2018.v220.n2.a2).
