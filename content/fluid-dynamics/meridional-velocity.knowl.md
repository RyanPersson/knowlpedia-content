+++
id = "fluid-dynamics/meridional-velocity"
title = "Meridional velocity"
kind = "definition"
summary = "The radial and axial components of a cylindrical velocity field, excluding its azimuthal component."
aliases = ["meridional flow"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/radial-velocity", "fluid-dynamics/axial-velocity", "real-analysis/cylindrical-coordinates"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **meridional velocity** relative to a chosen axis is
\[
u_{\mathrm{mer}}=u_r e_r+u_z e_z.
\]
It is often represented by the ordered pair \((u_r,u_z)\) on the \((r,z)\) half-plane. A meridional plane contains the symmetry axis; its radial and axial directions span this part of the velocity.

## Axisymmetric incompressible representation

For an axisymmetric divergence-free velocity, a [[real-analysis/stokes-streamfunction|Stokes streamfunction]] \(S\) locally represents these components by
\[
u_r=-\frac1r\partial_z S,\qquad
u_z=\frac1r\partial_r S.
\]
The swirl component can be prescribed separately, subject to the fluid equations and axis regularity. The pair \((u_r,u_z)\) satisfies the weighted divergence relation \(\partial_r(ru_r)+\partial_z(ru_z)=0\).
