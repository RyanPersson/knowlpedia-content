+++
id = "differential-equations/equation-for-gamma-average"
title = "Differential equation for the Gamma average"
kind = "theorem"
summary = "An integration-by-parts identity gives a second-order equation for the normalized Gamma integral profile."
aliases = []
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["real-analysis/gamma-average-profile", "real-analysis/smooth-endpoint-of-gamma-average", "real-analysis/integration-by-parts", "differential-equations/linear-ode"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The [[real-analysis/gamma-average-profile|profile]] \(F=F_{a,b}\), \(a,b>0\), satisfies
\[
z^2F''+[1+(a+b+1)z]F'+abF=0
\qquad(z\ge0),
\]
where derivatives at zero are one-sided.

## Integral proof

Insert the differentiated integral formulas into the left side. The result is
\[
\frac b{\Gamma(a)}\int_0^\infty
\frac{d}{dv}\left[e^{-v}v^a(1+zv)^{-b-1}\right]dv.
\]
The integrand's primitive vanishes at both endpoints, so the expression is zero. This argument proves the differential equation directly for the function; checking a formal Taylor recurrence alone would not prove it, since the endpoint Taylor series diverges.
