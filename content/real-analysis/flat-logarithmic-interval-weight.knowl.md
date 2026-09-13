+++
id = "real-analysis/flat-logarithmic-interval-weight"
title = "Flat logarithmic interval weight"
kind = "definition"
summary = "A smooth weight on a positive interval that decays faster than every power of the logarithmic boundary margin."
aliases = ["flat radial-edge weight"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/flat-exponential", "real-analysis/natural-logarithm", "real-analysis/flat-factor-product", "real-analysis/smooth-zero-extension", "real-analysis/flat-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For \(0<a<b\) and \(c_a,c_b>0\), define the **flat logarithmic interval weight** by
\[
\zeta(X)=\exp\left(-\frac{c_a}{\log^2(X/a)}-\frac{c_b}{\log^2(b/X)}\right)
\quad(a<X<b),
\]
and set it to zero outside \((a,b)\). This function is smooth and [[real-analysis/flat-function|flat]] at both endpoints, and \(0<\zeta\le1\) in the interval.

## Boundary control

Put \(\delta(X)=\min\{1,\log(X/a),\log(b/X)\}\) on \((a,b)\). For every \(\theta>0\) and finite \(N\ge0\),
\[
\zeta(X)^\theta\delta(X)^{-N}\longrightarrow0
\quad\text{as }X\downarrow a\text{ or }X\uparrow b.
\]
Near each endpoint the corresponding logarithm is comparable to distance from that endpoint, and an [[real-analysis/flat-exponential|exponential of a negative reciprocal square]] absorbs every polynomial loss. Differentiating \(\zeta\) produces that same exponential times finite powers of reciprocal logarithms and smooth factors, proving smooth zero extension.

The minimum defining \(\delta\) is a pointwise weight and need not be differentiable where its branches meet. Derivative estimates involving \(\delta\) do not authorize differentiating it.
