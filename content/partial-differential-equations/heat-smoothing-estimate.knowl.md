+++
id = "partial-differential-equations/heat-smoothing-estimate"
title = "Heat smoothing estimate"
kind = "theorem"
summary = "Gaussian convolution gains spatial derivatives and improves integrability with explicit powers of time."
aliases = ["heat kernel derivative estimate"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/heat-semigroup", "harmonic-analysis/young-convolution-inequality", "real-analysis/multi-index-notation", "measure-theory/lp-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(1\le p\le q\le\infty\), a spatial multi-index \(\alpha\), and \(t>0\), the [[partial-differential-equations/heat-semigroup|heat semigroup]] satisfies
\[
\|\partial_x^\alpha T_tf\|_q
\le C(\nu t)^{-|\alpha|/2-\frac n2(1/p-1/q)}\|f\|_p.
\]
The constant depends on \(n,p,q,\alpha\), and is independent of \(\nu,t,f\).

## Kernel estimate

Every Gaussian derivative is a polynomial times a Gaussian. Scaling gives
\[
\|\partial^\alpha G_\nu(t)\|_r
=C_{\alpha,n,r}(\nu t)^{-|\alpha|/2-\frac n2(1-1/r)}.
\]
Choose \(r\) with \(1+1/q=1/p+1/r\) and apply Young's convolution inequality. The negative powers as \(t\downarrow0\) express the cost of recovering derivatives from rough initial data.
