+++
id = "functional-analysis/analytic-coefficient-radial-estimates"
title = "Radial operator bounds in an analytic coefficient norm"
kind = "proposition"
summary = "Raising radial degree yields bounds for integration and for a parameter derivative followed by integration."
aliases = ["analytic integration compensates a derivative"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/two-index-analytic-coefficient-space", "differential-equations/radial-regular-inverse", "real-analysis/radial-averaging-operator", "linear-algebra/operator-norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(I_YF=\int_0^YF(s,\eta)\,ds\) in the [[functional-analysis/two-index-analytic-coefficient-space|two-index coefficient space]]. Its weights satisfy
\[
\frac{w_{\alpha\beta}}{w_{\alpha+1,\beta}}\le4R,
\qquad
\frac{w_{\alpha,\beta+1}}{(\alpha+1)w_{\alpha+1,\beta}}\le\frac{4R}{\rho}.
\]
These follow by canceling the factorials and binomial coefficients in the definition.

## Consequences

Multiplication by \(Y\) and \(I_Y\) each have norm at most \(4R\); the [[real-analysis/radial-averaging-operator|radial average]] has norm at most one; and \(\|\partial_\eta I_Y\|\le4R/\rho\). For \(\nu\ge1\), if \(F_\alpha=0\) for \(\alpha<b\), then
\[
\|J_\nu F\|_{R,\rho}
\le\frac{4R}{(b+1)(b+\nu)}\|F\|_{R,\rho}.
\]
This uses the coefficient divisor \((\alpha+1)(\alpha+\nu)\) of the [[differential-equations/radial-regular-inverse|regular radial inverse]]. A bare parameter derivative need not be bounded in the same norm; integration supplies the missing radial degree.
