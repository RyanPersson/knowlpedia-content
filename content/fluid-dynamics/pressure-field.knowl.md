+++
id = "fluid-dynamics/pressure-field"
title = "Pressure in incompressible flow"
kind = "definition"
summary = "The scalar field whose negative spatial gradient supplies the pressure force per unit mass."
aliases = ["pressure field", "normalized pressure", "pressure gradient"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["real-analysis/gradient", "shared-foundations/function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

In the constant-density incompressible equations, the **normalized pressure** \(p(t,x)\) is the physical pressure divided by the constant density. Its contribution to acceleration is
\[
-\nabla_xp.
\]
Pressure is a scalar field; its [[real-analysis/gradient|spatial gradient]] is a vector field. In the evolution problem, pressure is an unknown enforcing compatibility with the incompressibility constraint.

## Additive freedom

Replacing \(p(t,x)\) by \(p(t,x)+c(t)\) leaves its spatial gradient unchanged. A normalization, such as zero spatial mean on a periodic domain, fixes this freedom. On a disconnected domain there can be one additive function of time on each component.

## Regularity and reconstruction

To speak of a classical pressure gradient, the necessary spatial derivatives must exist. Pressure can instead be interpreted distributionally in weaker formulations. Taking the divergence of the momentum equation leads to a pressure Poisson equation, developed with the harmonic-analysis prerequisites.

## References

- [Lenya Ryzhik, Lecture Notes for Math 256B (2024), Sections 1–3](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).
- [Charles L. Fefferman, Existence and Smoothness of the Navier–Stokes Equation](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).
