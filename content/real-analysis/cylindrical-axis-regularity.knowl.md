+++
id = "real-analysis/cylindrical-axis-regularity"
title = "A sufficient criterion for smoothness at a cylindrical axis"
kind = "proposition"
summary = "Smooth dependence on r squared with the correct component factors yields smooth Cartesian fields."
aliases = ["Cartesian axis regularity", "axis regularity"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/cylindrical-coordinates", "real-analysis/class-ck-map", "real-analysis/chain-rule-multivariable"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(a(s,z),b(s,z),c(s,z)\) be [[real-analysis/class-ck-map|smooth]] on an open neighborhood of the relevant points with \(s\ge0\). An axisymmetric field on \(r>0\) with
\[
u_r=r\,a(r^2,z),\qquad
u_\theta=r\,b(r^2,z),\qquad
u_z=c(r^2,z)
\]
extends smoothly through the axis.

## Cartesian verification

Putting \(s=x^2+y^2\), its Cartesian components are
\[
u_x=x\,a(s,z)-y\,b(s,z),\qquad
u_y=y\,a(s,z)+x\,b(s,z),\qquad
u_z=c(s,z).
\]
These are compositions and products of smooth functions. This proves the stated sufficient criterion directly, including parameter-dependent versions when \(a,b,c\) are jointly smooth in those parameters.

## Why radial smoothness alone is insufficient

The field \(e_r=(x/r,y/r,0)\) has constant cylindrical radial component but no continuous extension at zero. Even a scalar \(f(r)=r\), smooth on the radial half-line in its one-sided sense, becomes \(\sqrt{x^2+y^2}\), which is not differentiable at the axis.
