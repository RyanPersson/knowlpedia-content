+++
id = "partial-differential-equations/directional-diffusion"
title = "Diffusion in a fixed direction"
kind = "definition"
summary = "The second directional derivative multiplied by a positive diffusivity."
aliases = ["axial diffusion"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["real-analysis/directional-derivative", "linear-algebra/unit-vector", "real-analysis/hessian-matrix", "partial-differential-equations/heat-equation", "real-analysis/higher-derivatives"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For a fixed [[linear-algebra/unit-vector|unit vector]] \(v\) and \(\nu>0\), **diffusion in direction \(v\)** is the operator
\[
\nu D_v^2f=\nu(v\cdot\nabla)^2f
=\nu\sum_{i,j}v_iv_j\partial_i\partial_jf.
\]
The direction is constant in space; a varying vector field would also contribute derivatives of its coefficients.

## Axial diffusion

For the axial direction \(v=e_z\), the term is \(\nu\partial_z^2f\). Under \(z=L_zZ\), it becomes \(\nu L_z^{-2}\partial_Z^2f\). Comparing it with radial diffusion therefore requires the two length scales and the radial operator, including any coordinate-basis terms.
