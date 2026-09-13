+++
id = "fluid-dynamics/rotating-flow"
title = "Rotating flow about a fixed axis"
kind = "definition"
summary = "A flow with an azimuthal component, which may coexist with radial and axial motion."
aliases = ["differential rotation", "rotating background flow"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/swirl", "fluid-dynamics/angular-velocity"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **rotating flow about a specified axis** has a [[fluid-dynamics/swirl|swirl component]] \(u_\theta=r\Omega\). It may also have radial and axial components. The angular velocity \(\Omega\) describes its local rotation rate around that axis.

## Rigid rotation

The velocity \(u=(-\Omega_0 x_2,\Omega_0 x_1,0)\), with constant \(\Omega_0\), is rigid rotation. It is divergence free, has zero rate of strain, and satisfies both unforced Euler and Navier–Stokes equations with
\[
p=\tfrac12\Omega_0^2(x_1^2+x_2^2),
\]
since the Laplacian of this linear velocity is zero. On the whole space it has infinite kinetic energy.

## Differential rotation

For an axisymmetric field, variation of \(\Omega(r,z)\) with position is differential rotation. Its radial shear contribution satisfies
\[
2D(u)_{r\theta}=\partial_r u_\theta-\frac{u_\theta}{r}
=r\partial_r\Omega.
\]
Consequently a nonzero azimuthal velocity does not by itself imply nonzero shear.
