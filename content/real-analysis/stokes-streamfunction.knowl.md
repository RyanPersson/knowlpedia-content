+++
id = "real-analysis/stokes-streamfunction"
title = "Stokes streamfunction for an axisymmetric meridional field"
kind = "definition"
summary = "A scalar S representing u_r=-S_z/r and u_z=S_r/r in cylindrical coordinates."
aliases = ["axisymmetric streamfunction", "Stokes stream function"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/cylindrical-coordinates", "real-analysis/divergence", "real-analysis/vector-potential", "real-analysis/schwarz-clairaut-theorem"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For an axisymmetric field with radial and axial components depending only on \((r,z)\), a **Stokes streamfunction** \(S\) uses the convention
\[
u_r=-\frac1r\partial_z S,\qquad
u_z=\frac1r\partial_r S,\qquad r>0.
\]
Substitution in the [[real-analysis/divergence|cylindrical divergence formula]] shows that the meridional field \(u_re_r+u_ze_z\) is divergence-free. The swirl component \(u_\theta e_\theta\) is separate and, if axisymmetric, also has zero divergence.

## Potential and axis

The azimuthal potential \(A=(S/r)e_\theta\) has curl \(u_re_r+u_ze_z\). If \(S=r^2a(r^2,z)\) with \(a\) smooth on a neighborhood of the relevant half-plane, then
\[
A=(-y\,a(x^2+y^2,z),\ x\,a(x^2+y^2,z),\ 0)
\]
is smooth at the axis, so its curl is smooth there too. An arbitrary smooth function of \((r,z)\) need not have this property. Authors sometimes choose the opposite sign for \(S\); the component formulas fix the convention.
