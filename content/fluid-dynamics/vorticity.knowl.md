+++
id = "fluid-dynamics/vorticity"
title = "Vorticity of a velocity field"
kind = "definition"
summary = "The curl of a three-dimensional velocity field."
aliases = ["fluid vorticity"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/velocity-field", "real-analysis/curl"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **vorticity** of a differentiable three-dimensional velocity field is
\[
\omega=\nabla\times u.
\]
It is a vector field obtained by applying [[real-analysis/curl|curl]] to the spatial variable at each fixed time. For twice continuously differentiable velocity, \(\nabla\cdot\omega=0\).

## Two-dimensional convention

For \(u=(u_1(x_1,x_2),u_2(x_1,x_2),0)\), the vorticity points in the third direction. It is commonly identified with the scalar \(\omega=\partial_1u_2-\partial_2u_1\).

## Rotation and vortex terminology

Rigid rotation \(u=(-\Omega x_2,\Omega x_1,0)\) has \(\omega=(0,0,2\Omega)\). A “vortex” denotes a flow structure and is not synonymous with the vorticity vector at a point; circular particle motion and local vorticity must be distinguished.

## References

- [Lenya Ryzhik, Lecture Notes for Math 256B (2024), Sections 1–3](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).

## Axisymmetric cylindrical formula

For [[fluid-dynamics/axisymmetric-field|axisymmetric velocity]],
\[
\omega_r=-\partial_z u_\theta,\qquad
\omega_\theta=\partial_z u_r-\partial_r u_z,\qquad
\omega_z=\frac1r\partial_r(ru_\theta).
\]
These identities follow from the cylindrical curl formula and hold directly for \(r>0\).
