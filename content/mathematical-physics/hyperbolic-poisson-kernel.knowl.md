+++
id = "mathematical-physics/hyperbolic-poisson-kernel"
title = "Hyperbolic Poisson kernel on the disk"
kind = "definition"
summary = "The positive kernel comparing a point in the Poincaré disk with a point on its ideal boundary."
aliases = ["Poincaré-disk Poisson kernel", "hyperbolic Poisson kernel"]
domains = ["mathematical-physics", "harmonic-analysis", "hyperbolic-geometry"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For \(z\in\mathbb D\) and \(b\in S^1=\partial\mathbb D\), the **hyperbolic
Poisson kernel** is
\[
P_b(z)=\frac{1-|z|^2}{|z-b|^2}.
\]
For fixed \(b\), it is positive and tends to infinity as \(z\) approaches
\(b\) non-tangentially.

## Boundary representation

If \(F\) is suitable boundary data on \(S^1\), its harmonic extension to the
disk is obtained by integrating \(F(b)P_b(z)\) against normalized angular
measure. This is the disk-model analogue of the
[[harmonic-analysis/poisson-kernel-upper-half-plane|upper-half-plane Poisson
kernel]].

## Spectral powers

Complex powers \(P_b(z)^{1/2+ir}\) are
[[mathematical-physics/hyperbolic-plane-wave|hyperbolic plane waves]] and solve
the Laplace eigenvalue equation with spectral parameter \(r\).

## References

1. Sigurdur Helgason, *Groups and Geometric Analysis*, AMS, 2000. [Publisher record](https://bookstore.ams.org/surv-83/).
