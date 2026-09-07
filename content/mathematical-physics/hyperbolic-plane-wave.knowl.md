+++
id = "mathematical-physics/hyperbolic-plane-wave"
title = "Hyperbolic plane wave"
kind = "definition"
summary = "A generalized Laplace eigenfunction on the Poincaré disk obtained from a boundary Poisson kernel raised to a complex power."
aliases = ["incoming hyperbolic wave", "outgoing hyperbolic wave", "Helgason plane wave"]
domains = ["mathematical-physics", "harmonic-analysis", "quantum-chaos"]
section_mode = "progressive"
prerequisites = ["mathematical-physics/hyperbolic-poisson-kernel", "differential-geometry/poincare-disk-model", "differential-geometry/laplace-beltrami-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1

[[issues]]
id = "3b5995e5-b613-43c1-9076-a6bbe710cee7"
status = "resolved"
summary = "Reported missing knowl links, including Poincaré disk"
reported_at = "2026-09-07T03:41:20Z"
updated_at = "2026-09-07T06:38:00Z"
report = "Flagging some missing knowl links in this one including poincare disk."
assessment = "The reported missing Poincaré disk dependency was confirmed. A canonical definition now gives the unit-disk metric, curvature normalization, geodesics, and ideal boundary, and the first mention in this knowl links to it. The existing Laplace–Beltrami knowl uses the nonnegative convention, so the eigenvalue statement was corrected to link that operator and write Δψ=(r²+1/4)ψ. The linked Poisson kernel and new disk model provide the complete direct prerequisites."
resolution = "Added and linked differential-geometry/poincare-disk-model, including the curvature-minus-one metric normalization and boundary/geodesic facts checked against Farb and Margalit, A Primer on Mapping Class Groups, §1.1.2, pp. 19–21. Corrected the sign and linked the Laplace–Beltrami operator under the convention declared by its canonical knowl. Parsed front matter and validated all referenced IDs; no unrelated knowls were changed."
+++

Let \(P_b(z)\) be the
[[mathematical-physics/hyperbolic-poisson-kernel|hyperbolic Poisson kernel]] of
the [[differential-geometry/poincare-disk-model|Poincaré disk]], with
\(b\in S^1\) and \(z\in\mathbb D\). For \(r\in\mathbb R\), the **hyperbolic
plane wave** based at \(b\) is
\[
\psi_b^r(z)=P_b(z)^{1/2+ir}.
\]
With the nonnegative [[differential-geometry/laplace-beltrami-operator|Laplace–Beltrami
operator]] convention it satisfies
\[
\Delta\psi_b^r=(r^2+1/4)\psi_b^r.
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
