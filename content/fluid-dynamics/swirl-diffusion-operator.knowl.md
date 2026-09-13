+++
id = "fluid-dynamics/swirl-diffusion-operator"
title = "Cylindrical swirl diffusion operator"
kind = "definition"
summary = "The radial diffusion of an azimuthal vector component includes a negative inverse-square term."
aliases = ["radial swirl Laplacian", "swirl heat operator"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/axisymmetric-field", "real-analysis/cylindrical-coordinates", "real-analysis/laplacian", "real-analysis/radial-laplacian", "fluid-dynamics/swirl"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For an axisymmetric vector field \(u=K(r,z)e_\theta\), its vector Laplacian is
\[
\Delta u=\left(K_{rr}+\frac1rK_r-\frac1{r^2}K+K_{zz}\right)e_\theta.
\]
The **radial swirl diffusion operator** is therefore \(L_\theta=\partial_r^2+r^{-1}\partial_r-r^{-2}\), rather than the [[real-analysis/radial-laplacian|scalar radial Laplacian]]. The formula holds for \(r>0\).

## Origin of the extra term

In Cartesian components, the angular basis satisfies \(\partial_\theta^2e_\theta=-e_\theta\), producing \(-K/r^2\). Writing \(K=r\Omega\) gives
\[
L_\theta(r\Omega)=r\left(\Omega_{rr}+\frac3r\Omega_r\right).
\]
The bracket is the radial scalar Laplacian in four dimensions. Smoothness across the axis still requires the corresponding Cartesian regularity of the swirl field.
