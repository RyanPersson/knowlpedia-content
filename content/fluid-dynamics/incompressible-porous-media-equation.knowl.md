+++
id = "fluid-dynamics/incompressible-porous-media-equation"
title = "Incompressible porous media equation"
kind = "definition"
summary = "Density transport coupled to a Darcy velocity and zero divergence."
aliases = ["IPM", "incompressible porous medium equation"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/active-scalar-equation", "real-analysis/gradient", "real-analysis/divergence", "fluid-dynamics/leray-projection"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

In a normalized two-dimensional convention, the **incompressible porous media equation (IPM)** is
\[
\partial_t\rho+u\cdot\nabla\rho=F,\qquad
u=-\nabla p-\rho e_2,\qquad \operatorname{div}u=0,
\quad e_2=(0,1).
\]
Here \(\rho\) is density, \(p\) is pressure, and the second relation is the normalized Darcy law. The [[real-analysis/gradient|gradient]] and [[real-analysis/divergence|divergence]] act in space. When Euclidean \(L^2\) projection is applicable, \(u=-\mathbb P(\rho e_2)\) with the [[fluid-dynamics/leray-projection|Leray projector]], making this an [[fluid-dynamics/active-scalar-equation|active scalar equation]].

## Model conventions

Positive physical constants can be included for permeability, viscosity, and gravity before normalization. Gravity direction fixes the density sign. Domain and boundary conditions matter when recovering pressure. A sourced equation allows \(F\ne0\); the unforced model sets \(F=0\).

## References

- [Córdoba and Martínez-Zoroa, Finite time singularities of smooth solutions for the 2D IPM equation with a smooth source](https://arxiv.org/abs/2410.22920).
