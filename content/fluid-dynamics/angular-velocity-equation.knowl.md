+++
id = "fluid-dynamics/angular-velocity-equation"
title = "Angular-velocity equation in axisymmetric flow"
kind = "identity"
summary = "The swirl equation after dividing azimuthal velocity by radius, with the radial heat operator of four transverse dimensions."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/axisymmetric-navier-stokes", "fluid-dynamics/angular-velocity", "real-analysis/product-rule"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a smooth axisymmetric solution with \(r>0\), write \(u_\theta=r\Omega\). The azimuthal equation is equivalent to
\[
\left(\partial_t+u_r\partial_r+u_z\partial_z\right)\Omega
+\frac{2u_r}{r}\Omega
=\nu\left(\partial_r^2+\frac3r\partial_r+\partial_z^2\right)\Omega
+\frac{f_\theta}{r}.
\]

## Derivation

The [[real-analysis/product-rule|product rule]] gives \(\mathcal D(r\Omega)=r\mathcal D\Omega+u_r\Omega\). The additional curvature term \(u_ru_\theta/r\) gives another \(u_r\Omega\). On the diffusion side,
\[
(\Delta_0-r^{-2})(r\Omega)
=r\left(\partial_r^2+\frac3r\partial_r+\partial_z^2\right)\Omega.
\]
Dividing the resulting equation by \(r\) proves the formula.

## Radial interpretation

The operator \(\partial_r^2+3r^{-1}\partial_r\) is the radial Laplacian in four Euclidean dimensions. This algebraic reformulation is useful for heat-profile constructions; it does not change the physical fluid's three-dimensional domain.
