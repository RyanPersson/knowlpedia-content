+++
id = "fluid-dynamics/specific-angular-momentum"
title = "Specific angular momentum about an axis"
kind = "definition"
summary = "The axial component of position cross velocity, equal to r times the azimuthal velocity."
aliases = ["angular momentum about an axis", "cylindrical angular momentum"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/swirl", "linear-algebra/cross-product", "real-analysis/cylindrical-coordinates"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **specific angular momentum about the \(z\)-axis** is
\[
\Gamma=(x\times u)\cdot e_z=x_1u_2-x_2u_1=r u_\theta.
\]
“Specific” means per unit mass. It differs from the angular velocity \(u_\theta/r\) by the factor \(r^2\).

## Axisymmetric evolution

For a smooth axisymmetric Navier–Stokes solution, axisymmetric pressure and force, and \(r>0\), the azimuthal momentum equation yields
\[
(\partial_t+u_r\partial_r+u_z\partial_z)\Gamma
=\nu\left(\partial_r^2-\frac1r\partial_r+\partial_z^2\right)\Gamma+r f_\theta.
\]
Multiply the [[fluid-dynamics/axisymmetric-navier-stokes|azimuthal component equation]] by \(r\) and use \(D_t r=u_r\) to derive this identity. With \(\nu=0\) and no azimuthal forcing, \(\Gamma\) is transported by the meridional motion.

## Total angular momentum

When the integral converges, total axial angular momentum at density one is \(\int\Gamma\,dx\). Its conservation requires suitable force, boundary, and integrability assumptions; it is not part of the definition of \(\Gamma\).
