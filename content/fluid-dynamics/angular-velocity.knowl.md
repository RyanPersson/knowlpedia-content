+++
id = "fluid-dynamics/angular-velocity"
title = "Angular velocity about an axis"
kind = "definition"
summary = "The azimuthal linear velocity divided by the distance from the axis."
aliases = ["rotation rate"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/swirl", "real-analysis/cylindrical-coordinates"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(r>0\), the **angular velocity** of a fluid about the \(z\)-axis is the [[fluid-dynamics/swirl|swirl velocity]] divided by radius:
\[
\Omega(t,r,\theta,z)=\frac{u_\theta(t,r,\theta,z)}r.
\]
Along a particle trajectory away from the axis, \(d\theta/dt=\Omega(t,X(t))\). Its units are inverse time when the angle is measured in radians.

## Rigid and differential rotation

Rigid rotation with rate \(\Omega_0\) has \(u_\theta=r\Omega_0\). When \(\Omega\) varies spatially, different locations rotate at different rates. The angular velocity is not generally half the axial vorticity: for axisymmetric swirl,
\[
\omega_z=\frac1r\partial_r(ru_\theta)
=2\Omega+r\partial_r\Omega.
\]

The quotient at \(r=0\) is interpreted through smooth extension when the Cartesian field has the required axis regularity.
