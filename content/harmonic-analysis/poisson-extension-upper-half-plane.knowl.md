+++
id = "harmonic-analysis/poisson-extension-upper-half-plane"
title = "Poisson extension to the upper half-plane"
kind = "construction"
summary = "Boundary data on the real line convolved with the Poisson kernel to produce a harmonic function on the upper half-plane."
aliases = ["harmonic Poisson extension", "Poisson integral"]
domains = ["harmonic-analysis", "complex-analysis", "partial-differential-equations"]
prerequisites = ["harmonic-analysis/poisson-kernel-upper-half-plane", "complex-analysis/harmonic-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For suitable boundary data \(f:\mathbb R\to\mathbb C\), its **Poisson
extension** to \(\mathbb H=\{x+iy:y>0\}\) is
\[
u(x+iy)=(P_y*f)(x)
=\frac1\pi\int_{\mathbb R}f(x-t)\frac{y}{t^2+y^2}\,dt,
\]
where \(P_y\) is the
[[harmonic-analysis/poisson-kernel-upper-half-plane|Poisson kernel]]. The
function \(u\) is [[complex-analysis/harmonic-function|harmonic]] in
\(\mathbb H\) and approaches \(f\) at the boundary
in the topology guaranteed by the hypotheses on \(f\).

## Dirichlet problem

For bounded continuous boundary data, the Poisson extension is the unique
bounded harmonic solution of the upper-half-plane Dirichlet problem. Uniqueness
follows from the
[[complex-analysis/harmonic-maximum-principle|maximum principle]] after
controlling behavior at infinity.

## Normal derivative

When \(f\) is sufficiently regular, its boundary normal derivative is
described by the
[[harmonic-analysis/dirichlet-to-neumann-upper-half-plane|Dirichlet-to-Neumann
operator]], equivalently a [[harmonic-analysis/hilbert-transform|Hilbert transform]] of (f').

## References

1. Elias M. Stein and Rami Shakarchi, *Complex Analysis*, Princeton University Press, 2003. [DOI record](https://doi.org/10.1515/9781400831159).
