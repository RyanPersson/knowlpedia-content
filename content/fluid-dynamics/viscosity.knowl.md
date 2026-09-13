+++
id = "fluid-dynamics/viscosity"
title = "Viscosity in the incompressible Newtonian model"
kind = "definition"
summary = "The coefficient relating viscous stress to the rate of strain, with kinematic viscosity obtained by dividing by density."
aliases = ["kinematic viscosity", "dynamic viscosity"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/rate-of-strain", "shared-foundations/real-numbers"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For an incompressible Newtonian fluid, **dynamic viscosity** \(\mu>0\) relates the viscous stress to the [[fluid-dynamics/rate-of-strain|rate of strain]] by
\[
\tau=2\mu D(u).
\]
At constant density \(\rho>0\), the **kinematic viscosity** is \(\nu=\mu/\rho\). With constant \(\mu\) and divergence-free velocity, the viscous force per unit mass is \(\nu\Delta u\).

## Units and normalization

Kinematic viscosity has units of length squared divided by time. Mathematical formulations often take density equal to one and use \(\nu\) directly as the coefficient of the velocity Laplacian. Setting \(\nu=1\) requires a corresponding choice of units or rescaling; it is not an additional physical identity.

The [[fluid-dynamics/euler-equations|inviscid Euler model]] omits this viscous term.

## References

- [Lenya Ryzhik, Lecture Notes for Math 256B (2024), Sections 1–3](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).
