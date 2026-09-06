+++
id = "mathematical-physics/wave-equation"
title = "Wave equation"
kind = "definition"
summary = "The massless hyperbolic field equation determined by a Lorentzian metric."
aliases = ["scalar wave equation", "homogeneous wave equation", "d'Alembert equation"]
domains = ["mathematical-physics", "partial-differential-equations"]
prerequisites = ["differential-geometry/lorentzian-manifold", "mathematical-physics/dalembert-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

On a [[differential-geometry/lorentzian-manifold|Lorentzian manifold]] \((M,g)\), the **scalar wave equation** for a smooth real- or complex-valued field \(\phi\) is
\[
\Box_g\phi=0,
\]
where \(\Box_g\) is the [[mathematical-physics/dalembert-operator|d’Alembert operator]]. The inhomogeneous equation is \(\Box_g\phi=f\) for a prescribed source \(f\).

## Flat-spacetime form

On [[mathematical-physics/minkowski-spacetime|Minkowski spacetime]], this convention gives
\[
\partial_t^2\phi-\sum_{j=1}^{n-1}\partial_{x_j}^2\phi=0.
\]
Plane waves \(e^{-i\omega t+i k\cdot x}\) solve the equation precisely when \(\omega^2=|k|^2\), so their frequency covector is null.

## Initial-value formulation

The wave equation is an initial-value problem rather than an elliptic boundary-value problem. The precise global existence, uniqueness, and finite-propagation statement is the [[mathematical-physics/cauchy-problem-for-normally-hyperbolic-operators|Cauchy theorem for normally hyperbolic operators]].

## Variants

For a field valued in a vector bundle, the scalar operator is replaced by a [[mathematical-physics/normally-hyperbolic-operator|normally hyperbolic operator]]. Adding a mass term produces the [[mathematical-physics/klein-gordon-equation|Klein–Gordon equation]]. Nonlinear wave equations add terms depending nonlinearly on \(\phi\) or its derivatives and require separate well-posedness analysis.

## References

1. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: Chapter 3.
2. Lars Hörmander, *Lectures on Nonlinear Hyperbolic Differential Equations*, Springer, 1997. [Publisher record](https://doi.org/10.1007/978-3-642-57796-1). Relevant: Chapters 1–2.
