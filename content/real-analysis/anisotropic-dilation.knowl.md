+++
id = "real-analysis/anisotropic-dilation"
title = "Anisotropic dilation"
kind = "definition"
summary = "A coordinate dilation with a separate scaling exponent in each direction."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/real-power", "linear-algebra/euclidean-space", "real-analysis/jacobian-determinant"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For fixed [[real-analysis/real-power|real exponents]] \(b_1,\ldots,b_d\) and \(\lambda>0\), the **anisotropic dilation** is
\[
D_\lambda(y_1,\ldots,y_d)=(\lambda^{b_1}y_1,\ldots,\lambda^{b_d}y_d).
\]
It satisfies \(D_\lambda D_\mu=D_{\lambda\mu}\), \(D_\lambda^{-1}=D_{1/\lambda}\), and has [[real-analysis/jacobian-determinant|Jacobian determinant]] \(\lambda^{b_1+\cdots+b_d}\). The dilation is isotropic when the exponents are equal.

## Homogeneous functions

A scalar function is homogeneous of degree \(a\) for this dilation if \(f(D_\lambda y)=\lambda^a f(y)\). Homogeneity is relative to the chosen exponents. In particular, the same function can have different degrees for different dilations.
