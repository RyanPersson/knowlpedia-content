+++
id = "fluid-dynamics/phase-transport-defect"
title = "Phase transport defect"
kind = "definition"
summary = "The material derivative of a phase, measuring failure of exact transport by a chosen velocity."
aliases = ["eikonal transport defect"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/material-derivative", "harmonic-analysis/oscillatory-phase", "harmonic-analysis/oscillatory-modulation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a velocity field \(u\) and a smooth phase \(\Phi\), the **phase transport defect** is the [[fluid-dynamics/material-derivative|material derivative]]
\[
E_\Phi=(\partial_t+u\cdot\nabla)\Phi.
\]
It vanishes when \(\Phi\) is transported exactly along the particle trajectories of \(u\). The velocity and the derivatives held fixed are part of this definition.

## Effect on an oscillatory field

Writing \(D_t=\partial_t+u\cdot\nabla\),
\[
D_t(ae^{i\kappa\Phi})=e^{i\kappa\Phi}(D_ta+i\kappa E_\Phi a).
\]
Even a small phase defect is multiplied by the carrier frequency. Moreover, for \(n=\nabla\Phi\),
\[
D_tn=-(\nabla u)^Tn+\nabla E_\Phi,
\]
where \((\nabla u)_{ij}=\partial_j u_i\). Exact transport therefore evolves the phase gradient by the transpose velocity gradient.
