+++
id = "fluid-dynamics/pure-swirl-heat-solution"
title = "Pure swirl solution from a radial heat flow"
kind = "theorem"
summary = "A radial swirl heat profile together with its centrifugal pressure gives an exact unforced Navier–Stokes field away from the axis."
aliases = ["exact radial swirl heat exterior"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/axisymmetric-navier-stokes", "fluid-dynamics/swirl-diffusion-operator", "fluid-dynamics/pressure-field", "real-analysis/fundamental-theorem-of-calculus-i", "measure-theory/differentiation-under-integral"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Suppose a smooth \(K(r,t)\) on \(r>0\) satisfies \(K_t=\nu L_\theta K\), and assume the following pressure integral and its needed derivatives converge locally uniformly. Define
\[
u=K(r,t)e_\theta,\qquad
p(r,t)=-\int_r^\infty\frac{K(s,t)^2}{s}\,ds.
\]
Then \((u,p)\) solves the unforced [[fluid-dynamics/axisymmetric-navier-stokes|Navier–Stokes equations]] for \(r>0\).

## Component check

The field is divergence-free and has no radial or axial velocity. Its radial advection is \(-K^2/r\), canceled by \(p_r=K^2/r\). Its azimuthal equation is exactly the swirl heat equation, and its axial equation vanishes by independence of \(z\).

An exterior profile with suitable power decay supplies a convergent pressure integral. This construction is independent of the axial coordinate, so a nonzero such field on all of \(\mathbb R^3\) does not have finite kinetic energy. Using it only in an exterior region requires a separate joining construction.
