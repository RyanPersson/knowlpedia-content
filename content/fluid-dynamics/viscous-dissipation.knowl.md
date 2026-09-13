+++
id = "fluid-dynamics/viscous-dissipation"
title = "Viscous dissipation in the incompressible energy balance"
kind = "definition"
summary = "Viscosity times the spatial square-integral of the velocity gradient."
aliases = ["total dissipation", "dissipation integral"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/viscosity", "real-analysis/jacobian-matrix", "measure-theory/lp-space", "linear-algebra/frobenius-norm", "measure-theory/lebesgue-integral", "shared-foundations/finite-sum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For kinematic viscosity \(\nu>0\), the **viscous dissipation rate** in the unit-density whole-space or periodic energy balance is
\[
D(t)=\nu\int_\Omega|\nabla u(t,x)|^2\,dx,
\qquad |\nabla u|^2=\sum_{i,j}|\partial_j u_i|^2.
\]
The matrix norm here is the [[linear-algebra/frobenius-norm|Frobenius norm]]. Total dissipation over \(I\) is \(\int_I D(t)\,dt\), when finite.

## Strain and gradient conventions

For divergence-free fields with vanishing boundary terms, integration by parts gives \(2\int|\operatorname{sym}\nabla u|^2=\int|\nabla u|^2\). The physical local strain dissipation is \(2\nu|\operatorname{sym}\nabla u|^2\); it need not equal \(\nu|\nabla u|^2\) pointwise. Their integrated equality uses incompressibility and the boundary conditions.
