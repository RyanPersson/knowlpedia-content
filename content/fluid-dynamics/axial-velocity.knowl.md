+++
id = "fluid-dynamics/axial-velocity"
title = "Axial velocity"
kind = "definition"
summary = "The velocity component parallel to a chosen axis."
aliases = ["axial flow", "axial outflow"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/velocity-field", "real-analysis/cylindrical-coordinates", "linear-algebra/inner-product"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Relative to the \(z\)-axis, the **axial velocity** is the scalar \(u_z=u\cdot e_z\); its vector contribution is \(u_z e_z\). Along a particle trajectory, \(dz/dt=u_z(t,X(t))\).

## Axial flow

A purely axial flow has \(u=u_z e_z\), while a general flow can have axial motion together with radial motion and swirl. “Axial outflow” describes motion away from a specified central region along the axis; its sign can differ on the two sides of that region.

For a purely axial differentiable flow, incompressibility requires \(\partial_z u_z=0\). Radial components can balance a nonzero axial derivative in a general incompressible flow.
