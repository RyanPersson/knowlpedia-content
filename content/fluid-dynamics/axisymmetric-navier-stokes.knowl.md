+++
id = "fluid-dynamics/axisymmetric-navier-stokes"
title = "Axisymmetric Navier–Stokes component equations"
kind = "identity"
summary = "The incompressible momentum equations for radial, azimuthal, and axial velocity components independent of angle."
aliases = ["axisymmetric momentum equations"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/navier-stokes-equations", "fluid-dynamics/axisymmetric-field", "real-analysis/cylindrical-coordinates", "real-analysis/laplacian", "fluid-dynamics/material-derivative"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For an axisymmetric velocity, pressure, and force, define the scalar operators on \(r>0\)
\[
\mathcal D=\partial_t+u_r\partial_r+u_z\partial_z,
\qquad \Delta_0=\partial_r^2+\frac1r\partial_r+\partial_z^2.
\]
Then the [[fluid-dynamics/navier-stokes-equations|Navier–Stokes equations]] are
\[
\begin{aligned}
\mathcal D u_r-\frac{u_\theta^2}{r}+\partial_rp
 &=\nu(\Delta_0-r^{-2})u_r+f_r,\\
\mathcal D u_\theta+\frac{u_ru_\theta}{r}
 &=\nu(\Delta_0-r^{-2})u_\theta+f_\theta,\\
\mathcal D u_z+\partial_zp&=\nu\Delta_0u_z+f_z,\\
\partial_r u_r+\frac{u_r}{r}+\partial_z u_z&=0.
\end{aligned}
\]

## Geometric terms

Differentiating the moving cylindrical basis produces \(-u_\theta^2/r\) and \(u_ru_\theta/r\) in material acceleration. The vector Laplacian produces the terms \(-u_r/r^2\) and \(-u_\theta/r^2\); applying only the scalar Laplacian to cylindrical components would omit them.

## Axis and inviscid versions

These formulas hold directly for \(r>0\). A smooth solution containing the axis must also obey [[real-analysis/cylindrical-axis-regularity|Cartesian axis regularity]]. The axisymmetric Euler equations follow by setting \(\nu=0\).
