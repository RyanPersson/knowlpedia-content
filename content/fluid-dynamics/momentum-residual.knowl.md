+++
id = "fluid-dynamics/momentum-residual"
title = "Navier–Stokes momentum residual"
kind = "definition"
summary = "The defect obtained by evaluating the momentum equation on a trial velocity and pressure."
aliases = ["momentum equation defect"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/navier-stokes-equations", "fluid-dynamics/transport-operator", "real-analysis/gradient", "real-analysis/laplacian"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For sufficiently differentiable trial fields \(u,p\), fixed viscosity \(\nu>0\), and prescribed force \(f\), the **momentum residual** is
\[
\mathcal R_\nu(u,p;f)
=\partial_tu+(u\cdot\nabla)u+\nabla p-\nu\Delta u-f.
\]
It vanishes precisely when the momentum equation in [[fluid-dynamics/navier-stokes-equations|Navier–Stokes]] holds. The additional condition \(\nabla\cdot u=0\), initial data, and boundary conditions are separate constraints.

## Exact correction identity

For increments \(w,\pi\),
\[
\mathcal R_\nu(u+w,p+\pi;f)=\mathcal R_\nu(u,p;f)
+\partial_tw+(u\cdot\nabla)w+(w\cdot\nabla)u
+\nabla\pi-\nu\Delta w+(w\cdot\nabla)w.
\]
The last term is the quadratic error after a linear correction. This sign convention includes \(-f\); defining an effective force instead requires stating the corresponding sign explicitly.
