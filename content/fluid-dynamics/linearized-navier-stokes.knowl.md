+++
id = "fluid-dynamics/linearized-navier-stokes"
title = "Linearized Navier–Stokes operator"
kind = "definition"
summary = "The first variation of the momentum residual with respect to velocity and pressure."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/momentum-residual", "real-analysis/linearization", "real-analysis/divergence"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

At a smooth reference velocity \(u\), the **linearized Navier–Stokes momentum operator** acting on a velocity-pressure increment \((w,\pi)\) is
\[
\mathcal L_u(w,\pi)=\partial_tw+(u\cdot\nabla)w
+(w\cdot\nabla)u+\nabla\pi-\nu\Delta w.
\]
It is the coefficient of \(\varepsilon\) in the [[fluid-dynamics/momentum-residual|residual]] of \((u+\varepsilon w,p+\varepsilon\pi)\) with the force held fixed. For an incompressible perturbation one also imposes \(\nabla\cdot w=0\).

## Exact remainder and spaces

The remainder is \(\varepsilon^2(w\cdot\nabla)w\). Thus linearizing about a non-solution still leaves its original residual as an inhomogeneous term. To regard \(\mathcal L_u\) as a bounded derivative between function spaces, choose source norms controlling the displayed time and spatial derivatives and a target norm in which the products are bounded; the algebraic formula alone does not specify such spaces.
