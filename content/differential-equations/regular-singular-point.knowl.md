+++
id = "differential-equations/regular-singular-point"
title = "Regular singular point of a second-order linear ODE"
kind = "definition"
summary = "A point where the first- and zeroth-order coefficients have at most first- and second-order poles after normalization."
aliases = ["Fuchsian singular point", "regular singular radial equation"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/linear-ode", "differential-geometry/holomorphic-map", "complex-analysis/order-of-zero-or-pole"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(y''+p(z)y'+q(z)y=0\) on a punctured disc about zero, the origin is a **regular singular point** if \(zp(z)\) and \(z^2q(z)\) extend [[differential-geometry/holomorphic-map|holomorphically]] to zero. Equivalently, the equation has the form
\[
z^2y''+zP(z)y'+Q(z)y=0
\]
with \(P,Q\) holomorphic near zero. An ordinary point, where \(p,q\) themselves extend, is included in some conventions and excluded in others.

## Leading powers

Substitution of \(y=z^r\) into the lowest-order terms gives the indicial equation
\(r(r-1)+P(0)r+Q(0)=0\).
The Frobenius method seeks a power times a convergent series; resonances can require logarithmic terms. A regular singular equation need not have every solution smooth at zero. A particular regular branch must be selected by its boundary or normalization condition.
