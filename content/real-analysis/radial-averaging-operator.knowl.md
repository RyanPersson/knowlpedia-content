+++
id = "real-analysis/radial-averaging-operator"
title = "Radial averaging operator from the origin"
kind = "definition"
summary = "The regularized average Y inverse times the integral from zero to Y."
aliases = ["radial average", "averaging primitive"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/fundamental-theorem-of-calculus-i", "real-analysis/power-series"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For continuous \(F\) near zero, its **radial average** is
\[
(AF)(Y)=\int_0^1F(tY)\,dt.
\]
For \(Y\ne0\), this equals \(Y^{-1}\int_0^YF(s)\,ds\); the integral on the unit interval also defines \(AF(0)=F(0)\).

## Regularity and coefficients

If \(F\) is smooth, differentiation on the compact integration interval gives \((AF)^{(m)}(Y)=\int_0^1t^mF^{(m)}(tY)\,dt\), so the average is smooth through zero. If \(F=\sum F_\alpha Y^\alpha\) is analytic, then \((AF)_\alpha=F_\alpha/(\alpha+1)\). The apparent quotient singularity is removed by this integral representation.
