+++
id = "fluid-dynamics/local-energy-inequality"
title = "Local energy inequality"
kind = "definition"
summary = "The distributional kinetic-energy balance with a nonnegative dissipation defect."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/weak-navier-stokes-solution", "fluid-dynamics/local-kinetic-energy-balance", "functional-analysis/test-function-space", "measure-theory/locally-integrable-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a [[fluid-dynamics/weak-navier-stokes-solution|weak velocity-pressure pair]], write \(e=|u|^2/2\). Assume \(\nabla u\in L^2_{\rm loc}\) and \(e,eu,pu,f\cdot u\) are [[measure-theory/locally-integrable-function|locally integrable]]. The **local energy inequality** is
\[
\partial_t e+\operatorname{div}((e+p)u)-\nu\Delta e
 +\nu|\nabla u|^2\leq f\cdot u
\]
in distributions. Explicitly, every nonnegative [[functional-analysis/test-function-space|test function]] \(\phi\in C_c^\infty(Q)\) satisfies
\[
\nu\int_Q|\nabla u|^2\phi\leq\int_Q
e(\partial_t\phi+\nu\Delta\phi)+(e+p)u\cdot\nabla\phi+f\cdot u\,\phi.
\]
It permits extra energy loss relative to the [[fluid-dynamics/local-kinetic-energy-balance|smooth local balance]].

## Local and global statements

Tests have compact support inside space-time. Obtaining a global energy inequality requires cutoff limits and endpoint information; the two definitions are not interchangeable without those arguments.
