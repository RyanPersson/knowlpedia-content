+++
id = "mathematical-physics/semiclassical-measure"
title = "Semiclassical measure"
kind = "definition"
summary = "A weak-star limit in phase space of quadratic observables evaluated on a bounded family of high-frequency states."
aliases = ["defect measure", "microlocal defect measure", "quantum limit"]
domains = ["mathematical-physics", "microlocal-analysis", "quantum-chaos"]
prerequisites = ["differential-geometry/classical-phase-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(u_h\) be an \(L^2\)-bounded family on a manifold as \(h\to0\). A
**semiclassical measure** is a Radon measure \(\mu\) on [[differential-geometry/classical-phase-space|phase space]] obtained
along a subsequence from
\[
\langle \operatorname{Op}_h(a)u_h,u_h\rangle
\longrightarrow \int a\,d\mu
\]
for every compactly supported smooth symbol \(a\), where
\(\operatorname{Op}_h(a)\) is a fixed semiclassical quantization.

## Dependence and invariance

The measure may depend on the chosen subsequence, but standard quantizations
give the same limit. If \(u_h\) solves a semiclassical eigenvalue equation,
\(\mu\) is supported on the corresponding characteristic energy surface and
is invariant under the classical [[differential-geometry/hamiltonian-flow|Hamiltonian flow]].

## Full support

For [[mathematical-physics/laplace-beltrami-eigenfunction|Laplace
eigenfunctions]] on a [[mathematical-physics/compact-hyperbolic-surface|compact hyperbolic surface]], every semiclassical measure
has full support. The stronger uniform statement is the
[[mathematical-physics/uniform-eigenfunction-mass-lower-bound|eigenfunction
mass lower bound]].

## References

1. Maciej Zworski, *Semiclassical Analysis*, AMS, 2012. [Publisher record](https://bookstore.ams.org/gsm-138/).
