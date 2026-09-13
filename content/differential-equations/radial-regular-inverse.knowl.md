+++
id = "differential-equations/radial-regular-inverse"
title = "Regular inverse of Y d2/dY2 plus nu d/dY"
kind = "construction"
summary = "The normalized solution of YG double prime plus nu G prime equals F, selected by regularity at zero."
aliases = ["normalized radial inverse", "radial inverse J nu"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/integrating-factor", "real-analysis/power-series", "real-analysis/fundamental-theorem-of-calculus-i"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(\nu>0\) and smooth \(F\) near \(Y=0\), the regular solution of
\[
YG''+\nu G'=F,\qquad G(0)=0
\]
is
\[
(J_\nu F)(Y)=\int_0^Y\int_0^1s^{\nu-1}F(st)\,ds\,dt.
\]
The integral is smooth through zero. For \(Y>0\), differentiating \(Y^\nu G'\) verifies the equation. The homogeneous derivative is a constant times \(Y^{-\nu}\), so \(C^1\) regularity and \(G(0)=0\) give uniqueness on the nonnegative side.

## Coefficients

For an analytic input \(F(Y)=\sum_{\alpha\ge0}F_\alpha Y^\alpha\), termwise integration gives
\[
(J_\nu F)_0=0,\qquad
(J_\nu F)_{\alpha+1}=\frac{F_\alpha}{(\alpha+1)(\alpha+\nu)}.
\]
The operator raises the smallest radial degree by one and divides by two degree factors. Its boundedness in any chosen coefficient norm must be checked against that norm's weights.
