+++
id = "mathematical-physics/hyperbolic-plane-wave"
title = "Hyperbolic plane wave"
kind = "definition"
summary = "A generalized Laplace eigenfunction on the Poincaré disk obtained from a boundary Poisson kernel raised to a complex power."
aliases = ["incoming hyperbolic wave", "outgoing hyperbolic wave", "Helgason plane wave"]
domains = ["mathematical-physics", "harmonic-analysis", "quantum-chaos"]
section_mode = "progressive"
prerequisites = ["mathematical-physics/hyperbolic-poisson-kernel"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1

[[issues]]
id = "3b5995e5-b613-43c1-9076-a6bbe710cee7"
status = "open"
summary = "Reported missing knowl links, including Poincaré disk"
reported_at = "2026-09-07T03:41:20Z"
updated_at = "2026-09-07T03:41:52Z"
report = "Flagging some missing knowl links in this one including poincare disk."
assessment = "Confirmed that the core mentions Poincaré disk without a knowl link. A corpus search found mentions in compact-hyperbolic-surface and hyperbolic-poisson-kernel, but no dedicated Poincaré disk definition target. A subsequent Request change should establish a canonical disk-model knowl and link the first mention here. The unlinked Laplacian is another candidate: differential-geometry/laplace-beltrami-operator exists, but its nonnegative Delta convention must be reconciled with this source’s displayed -Delta before choosing link wording. The broader missing-link concern remains open; no body corrections were made."
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
