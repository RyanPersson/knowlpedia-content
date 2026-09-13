+++
id = "fluid-dynamics/local-kinetic-energy-balance"
title = "Local kinetic-energy balance for smooth incompressible flow"
kind = "theorem"
summary = "The pointwise energy equation includes transport, pressure flux, diffusion, dissipation and forcing."
aliases = ["local energy identity"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/navier-stokes-equations", "fluid-dynamics/kinetic-energy", "fluid-dynamics/viscous-dissipation", "real-analysis/product-rule", "real-analysis/divergence", "real-analysis/laplacian"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For a smooth solution of the [[fluid-dynamics/navier-stokes-equations|incompressible Navier–Stokes equations]], set \(e=|u|^2/2\). The **local kinetic-energy balance** is
\[
\partial_t e+\nabla\cdot((e+p)u)=\nu\Delta e-\nu|\nabla u|^2+f\cdot u.
\]
Here pressure and force are normalized by the constant density.

## Derivation

Take the scalar product of the momentum equation with \(u\). The identities \(u\cdot\partial_tu=\partial_te\), \(u\cdot(u\cdot\nabla)u=\nabla\cdot(eu)\), \(u\cdot\nabla p=\nabla\cdot(pu)\), and \(u\cdot\Delta u=\Delta e-|\nabla u|^2\) give the equation. The divergence identities use \(\nabla\cdot u=0\).

For a rough distributional solution, these multiplications require justification; this smooth equality does not automatically persist.
