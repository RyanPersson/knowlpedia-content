+++
id = "differential-geometry/geodesic-flow"
title = "Geodesic flow"
kind = "definition"
summary = "The flow on the unit tangent bundle that advances each unit tangent vector along its geodesic."
aliases = ["unit-speed geodesic flow"]
domains = ["differential-geometry", "dynamical-systems", "quantum-chaos"]
prerequisites = ["differential-geometry/riemannian-manifold"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,g)\) be a complete [[differential-geometry/riemannian-manifold|Riemannian manifold]] and \(SM\) its unit tangent
bundle. The **geodesic flow** is the one-parameter family
\[
\varphi_t:SM\to SM,\qquad
\varphi_t(x,v)=(\gamma_{x,v}(t),\dot\gamma_{x,v}(t)),
\]
where \(\gamma_{x,v}\) is the unique geodesic with initial data
\((x,v)\).

## Flow law

Uniqueness for the geodesic equation gives
\(\varphi_0=\operatorname{id}\) and
\(\varphi_{t+s}=\varphi_t\circ\varphi_s\). Completeness ensures that
\(\varphi_t\) is defined for all \(t\in\mathbb R\).

## Negative curvature

On a compact manifold of strictly negative sectional curvature, the geodesic
flow is an [[differential-geometry/anosov-flow|Anosov flow]]. Exponential
stable and unstable behavior is the dynamical source of the fractal sets used
in quantum-chaos uncertainty arguments.

## References

1. Gabriel P. Paternain, *Geodesic Flows*, Birkhäuser, 1999. [DOI record](https://doi.org/10.1007/978-1-4612-1600-1).
