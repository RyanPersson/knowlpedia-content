+++
id = "fluid-dynamics/axisymmetric-field"
title = "Axisymmetric vector field"
kind = "definition"
summary = "A vector field equivariant under rotations about a fixed axis, equivalently with angle-independent cylindrical components."
aliases = ["axisymmetry", "axisymmetric velocity"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["real-analysis/cylindrical-coordinates", "fluid-dynamics/velocity-field"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A vector field on a rotation-invariant domain in \(\mathbb R^3\) is **axisymmetric about the \(z\)-axis** if
\[
u(t,R_\phi x)=R_\phi u(t,x)
\]
for every rotation \(R_\phi\) about that axis. Away from the axis this is equivalent to writing
\[
u=u_r(t,r,z)e_r+u_\theta(t,r,z)e_\theta+u_z(t,r,z)e_z
\]
with all three [[real-analysis/cylindrical-coordinates|cylindrical components]] independent of \(\theta\). The basis vectors \(e_r,e_\theta\) themselves still depend on \(\theta\).

## Scalar fields and incompressibility

A scalar is axisymmetric when \(a(t,R_\phi x)=a(t,x)\). For a differentiable axisymmetric velocity, incompressibility becomes
\[
\frac1r\partial_r(ru_r)+\partial_z u_z=0\qquad(r>0).
\]

## The symmetry axis

The cylindrical description is singular at \(r=0\). [[real-analysis/cylindrical-axis-regularity|Cartesian regularity at the axis]] imposes additional behavior on the components. Axisymmetry permits a nonzero azimuthal component; it does not mean absence of swirl.

## References

- [Ben Pineau, Notes for Beale–Kato–Majda Blowup Criterion and Some Applications, axisymmetric Euler section](https://math.berkeley.edu/~sjoh/2020-spring-rs/pdfs/pineau_fluid_presentation.pdf).
