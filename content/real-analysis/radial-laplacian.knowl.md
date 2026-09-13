+++
id = "real-analysis/radial-laplacian"
title = "Radial Laplacian"
kind = "definition"
summary = "The scalar Euclidean Laplacian of a radial function has a dimension-dependent first-derivative term."
aliases = ["scalar radial diffusion"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/laplacian", "real-analysis/chain-rule-multivariable", "linear-algebra/euclidean-norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(u(x)=F(r)\), \(r=|x|>0\), in \(\mathbb R^n\), the **radial Laplacian** is
\[
\Delta u=F''(r)+\frac{n-1}{r}F'(r).
\]
This is the [[real-analysis/laplacian|scalar Laplacian]] restricted to radial functions.

## Calculation and the origin

Using \(\partial_i r=x_i/r\), differentiate \(\partial_i u=F'(r)x_i/r\) and sum. At \(r=0\), the displayed singular coefficients require the regularity of the underlying Cartesian function. If \(F(r)=H(r^2)\) with smooth \(H\), the formula extends to the origin and has value \(2nH'(0)\). A cylindrical radial scalar independent of its axial coordinate uses the transverse dimension \(n=2\).
