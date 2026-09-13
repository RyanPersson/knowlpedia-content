+++
id = "real-analysis/gamma-average-profile"
title = "Gamma average of an algebraic factor"
kind = "definition"
summary = "A normalized Gamma integral averaging a negative power of one plus a nonnegative parameter."
aliases = ["normalized Gamma integral profile"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/gamma-function", "real-analysis/real-power", "measure-theory/lebesgue-integral", "real-analysis/exponential-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(a,b>0\), define the **Gamma average profile**
\[
F_{a,b}(z)=\frac1{\Gamma(a)}\int_0^\infty
e^{-v}v^{a-1}(1+zv)^{-b}\,dv,\qquad z\ge0.
\]
It is positive, at most one, and satisfies \(F_{a,b}(0)=1\). The normalization uses the [[real-analysis/gamma-function|Gamma integral]].

## Relation to Tricomi U

For \(z>0\), substituting \(t=zv\) gives
\[
F_{a,b}(z)=z^{-a}U(a,1+a-b,z^{-1}).
\]
The original integral, unlike this transformed expression, directly defines the endpoint value at zero. No values at negative \(z\) are supplied by the displayed real integral: the factor \(1+zv\) then reaches zero within the integration range.
