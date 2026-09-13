+++
id = "harmonic-analysis/diophantine-direction"
title = "Diophantine direction"
kind = "definition"
summary = "A direction whose nonzero integer dot products have a specified reciprocal polynomial lower bound."
aliases = ["directional Diophantine inequality"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/inner-product", "discrete-structures/lattice-zd", "linear-algebra/euclidean-norm", "real-analysis/real-power"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A vector \(v\in\mathbb R^n\) is a **Diophantine direction** with constants \(c>0\) and \(\tau\ge0\) if
\[
|v\cdot m|\ge c(1+|m|)^{-\tau}
\qquad(m\in\mathbb Z^n\setminus\{0\}).
\]
The [[linear-algebra/inner-product|dot product]] and norm are Euclidean. This convention is a lower bound on distance to zero, not on distance to the nearest integer; the latter appears in a different Diophantine condition for rotations.

## Example and dependence

For a quadratic irrational \(\alpha\), the vector \((1,\alpha)\) satisfies the condition with \(\tau=1\) by the [[real-analysis/quadratic-irrational-lower-bound|quadratic lower bound]]. Multiplying a direction by a nonzero scalar rescales \(c\). Estimates based on the condition must track their dependence on \(c\) and \(\tau\); the bound excludes every nonzero resonant Fourier mode.
