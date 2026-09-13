+++
id = "fluid-dynamics/external-force"
title = "External force in a normalized fluid equation"
kind = "definition"
summary = "A prescribed vector-valued source representing acceleration due to forces outside the modeled internal stresses."
aliases = ["external forcing", "force per unit mass"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["real-analysis/euclidean-vector-field", "shared-foundations/cartesian-product"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An **external force per unit mass** is a prescribed [[real-analysis/euclidean-vector-field|vector field]] \(f(t,x)\) entering the momentum equation as an additive acceleration source. If a physical force density \(F\) is given and the constant mass density is \(\rho\), the normalized forcing is \(f=F/\rho\).

## Forced and unforced equations

A problem with \(f=0\) is unforced. Nonzero forcing is separate from the initial velocity and can generate motion from zero initial data. Smoothness, support, and time dependence of \(f\) must be stated when they matter.

## Gradient forces

If \(f=\nabla\phi\), it can be absorbed algebraically into normalized pressure: \(-\nabla p+\nabla\phi=-\nabla(p-\phi)\). Boundary or pressure-normalization conditions may still affect how this representation is used.

## References

- [Charles L. Fefferman, Existence and Smoothness of the Navier–Stokes Equation](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).
