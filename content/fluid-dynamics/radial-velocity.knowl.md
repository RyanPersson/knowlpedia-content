+++
id = "fluid-dynamics/radial-velocity"
title = "Radial velocity in cylindrical coordinates"
kind = "definition"
summary = "The component of velocity pointing away from the chosen symmetry axis."
aliases = ["radial inflow", "radial outflow"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/velocity-field", "real-analysis/cylindrical-coordinates", "linear-algebra/inner-product"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Away from the \(z\)-axis, the **radial velocity** is \(u_r=u\cdot e_r\), where \(e_r\) is the outward radial unit vector in [[real-analysis/cylindrical-coordinates|cylindrical coordinates]]. Along a particle trajectory,
\[
\frac{dr}{dt}=u_r(t,X(t)).
\]
Thus \(u_r<0\) describes radial inflow toward the axis, and \(u_r>0\) describes radial outflow.

## Cylindrical versus spherical radius

Here \(r=\sqrt{x^2+y^2}\) is distance from the axis. It is not distance from the origin in \(\mathbb R^3\). A flow can move toward the axis while moving away from the origin in the axial direction.
