+++
id = "real-analysis/mollifier"
title = "Mollifier"
kind = "definition"
summary = "A smooth nonnegative unit-mass kernel rescaled to approximate the identity."
aliases = ["mollification", "smoothing kernel"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/test-function-space", "measure-theory/lebesgue-integral", "harmonic-analysis/convolution-on-locally-compact-group", "differential-geometry/bump-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **mollifier** on \(\mathbb R^n\) is a nonnegative [[functional-analysis/test-function-space|test function]] \(\rho\), supported in the unit ball, with \(\int\rho=1\). Its rescalings are
\[
\rho_\varepsilon(x)=\varepsilon^{-n}\rho(x/\varepsilon),\qquad \varepsilon>0.
\]
The mollification of a locally integrable function is \(u_\varepsilon=\rho_\varepsilon*u\), wherever this convolution uses values in the domain of \(u\).

## Approximation and differentiation

The convolution is smooth on points at distance greater than \(\varepsilon\) from the boundary. Distributional derivatives commute with mollification. For \(u\in L^p(\mathbb R^n)\), \(1\le p<\infty\), translation continuity and unit mass give \(u_\varepsilon\to u\) in \(L^p\). An \(L^\infty\) function need not converge in the essential-supremum norm. A nonnegative bump, divided by its positive integral, supplies such a kernel.
