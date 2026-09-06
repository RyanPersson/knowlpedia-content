+++
id = "mathematical-physics/hyperbolic-plane-wave"
title = "Hyperbolic plane wave"
kind = "definition"
summary = "A generalized Laplace eigenfunction on the Poincaré disk obtained from a boundary Poisson kernel raised to a complex power."
aliases = ["incoming hyperbolic wave", "outgoing hyperbolic wave", "Helgason plane wave"]
domains = ["mathematical-physics", "harmonic-analysis", "quantum-chaos"]
prerequisites = ["mathematical-physics/hyperbolic-poisson-kernel"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(P_b(z)\) be the
[[mathematical-physics/hyperbolic-poisson-kernel|hyperbolic Poisson kernel]] of
the Poincaré disk, with
\(b\in S^1\) and \(z\in\mathbb D\). For \(r\in\mathbb R\), the **hyperbolic
plane wave** based at \(b\) is
\[
\psi_b^r(z)=P_b(z)^{1/2+ir}.
\]
With the nonnegative Laplacian convention it satisfies
\[
-\Delta\psi_b^r=(r^2+1/4)\psi_b^r.
\]

## Incoming and outgoing conventions

For the displayed phase convention, \(r>0\) is called outgoing and \(r<0\)
incoming. Reversing the time or Fourier sign convention swaps these labels.

## Boundary synthesis

Generalized eigenfunctions can be synthesized by integrating
\(\psi_b^r(z)\) against a boundary distribution in \(b\). Incoming and outgoing
boundary data are related by an
[[harmonic-analysis/oscillatory-integral|oscillatory integral operator]]; at high
frequency this relation is the Fourier-like transform to which a
[[harmonic-analysis/fractal-uncertainty-principle|fractal uncertainty
principle]] applies.

## References

1. Sigurdur Helgason, *Groups and Geometric Analysis*, AMS, 2000. [Publisher record](https://bookstore.ams.org/surv-83/).
2. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: §1.6.
