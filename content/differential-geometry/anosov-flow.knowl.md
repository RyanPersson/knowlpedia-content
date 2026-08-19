+++
id = "differential-geometry/anosov-flow"
title = "Anosov flow"
kind = "definition"
summary = "A flow whose tangent dynamics split uniformly into flow, exponentially contracting, and exponentially expanding directions."
aliases = ["uniformly hyperbolic flow"]
domains = ["differential-geometry", "dynamical-systems", "quantum-chaos"]
section_mode = "progressive"
+++

A \(C^1\) flow \(\varphi_t:N\to N\) on a compact manifold is an **Anosov
flow** if there is a continuous invariant splitting
\[
TN=E^s\oplus E^0\oplus E^u,
\]
where \(E^0\) is the flow direction, and constants \(C,\lambda>0\) satisfy
\[
\|D\varphi_t v^s\|\le Ce^{-\lambda t}\|v^s\|,
\qquad
\|D\varphi_{-t}v^u\|\le Ce^{-\lambda t}\|v^u\|
\]
for all \(t\ge0\), \(v^s\in E^s\), and \(v^u\in E^u\).

## Invariance

The splitting is invariant:
\(D\varphi_t(E^\bullet_x)=E^\bullet_{\varphi_t(x)}\). Vectors in \(E^s\)
contract forward in time, while vectors in \(E^u\) contract backward in time.

## Principal example

The [[differential-geometry/geodesic-flow|geodesic flow]] on the unit tangent
bundle of a compact negatively curved manifold is Anosov. Its hyperbolic
splitting supports symbolic descriptions and stable/unstable fractal sets.

## References

1. Dmitry Anosov, *Geodesic Flows on Closed Riemannian Manifolds with Negative Curvature*, AMS, 1969. [DOI record](https://doi.org/10.1090/chel/100).
