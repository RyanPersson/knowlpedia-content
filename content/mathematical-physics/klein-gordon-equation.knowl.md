+++
id = "mathematical-physics/klein-gordon-equation"
title = "Klein–Gordon equation"
kind = "definition"
summary = "The relativistic field equation for a free massive scalar field."
aliases = ["Klein-Gordon equation", "Klein Gordon equation", "relativistic scalar wave equation"]
domains = ["mathematical-physics", "partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-geometry/lorentzian-manifold", "mathematical-physics/klein-gordon-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

The **Klein–Gordon equation** for a scalar field \(\phi\) of mass \(m\geq0\) on a [[differential-geometry/lorentzian-manifold|Lorentzian manifold]] is
\[
(\Box_g+m^2)\phi=0
\]
in the \((-+\cdots+)\) metric and wave-operator convention of this collection. Equivalently, \(\phi\) lies in the kernel of the [[mathematical-physics/klein-gordon-operator|Klein–Gordon operator]].

## Massive and massless cases

When \(m>0\), flat-spacetime plane waves satisfy \(\omega^2=|k|^2+m^2\). When \(m=0\), the equation reduces to the [[mathematical-physics/wave-equation|wave equation]]. A curvature-coupled scalar field instead satisfies
\[
(\Box_g+m^2+\xi\operatorname{Scal}_g)\phi=0.
\]
Here \(\operatorname{Scal}_g\) is the [[differential-geometry/scalar-curvature|scalar curvature]]. Minimal coupling means \(\xi=0\); [[mathematical-physics/conformal-coupling-of-a-scalar-field|conformal coupling]] uses the dimension-dependent coefficient that makes the massless equation conformally covariant.

## Initial data and propagation

Because the Klein–Gordon operator is [[mathematical-physics/normally-hyperbolic-operator|normally hyperbolic]], its characteristics are null even when \(m>0\). Its global existence, uniqueness, and finite-propagation properties on [[differential-geometry/globally-hyperbolic-spacetime|globally hyperbolic spacetimes]] follow from the [[mathematical-physics/cauchy-problem-for-normally-hyperbolic-operators|Cauchy theorem for normally hyperbolic operators]].

## Relation to the Dirac equation

In flat spacetime the free [[mathematical-physics/dirac-equation|Dirac equation]] factors a Klein–Gordon operator: each component of a free [[differential-geometry/dirac-spinor|Dirac spinor]] satisfies the Klein–Gordon equation. Curvature and gauge coupling add lower-order terms to the corresponding squared Dirac operator, so the flat factorization should not be transferred unchanged to general backgrounds.

## Terminology

The equation is named for Oskar Klein and Walter Gordon. “Klein–Gordan” is a common misspelling, but **Klein–Gordon** is the standard spelling.

## References

1. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: Chapters 3–4.
2. Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory*, Addison-Wesley, 1995. [Publisher record](https://doi.org/10.1201/9780429503559). Relevant: Chapter 2.
