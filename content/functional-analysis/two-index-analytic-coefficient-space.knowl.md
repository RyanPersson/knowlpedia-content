+++
id = "functional-analysis/two-index-analytic-coefficient-space"
title = "Two-index analytic coefficient space"
kind = "definition"
summary = "A norm on radial coefficients and parameter derivatives coupling their orders through factorial and binomial weights."
aliases = ["factorially weighted analytic coefficients", "weighted analytic coefficient space"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/power-series", "real-analysis/class-ck-function", "shared-foundations/binomial-coefficient", "shared-foundations/factorial", "linear-algebra/norm", "real-analysis/uniform-convergence-differentiation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Fix \(R,\rho>0\) and a compact nondegenerate interval \(I\). For complex-valued coefficient functions \(F_\alpha(\eta)\), define
\[
w_{\alpha\beta}=
\frac{R^{-\alpha}\rho^{-\beta}\beta!\binom{\alpha+\beta}{\beta}}
{(\alpha+1)^2(\beta+1)^2},
\qquad
\|F\|_{R,\rho}=\sup_{\alpha,\beta\ge0}\sup_{\eta\in I}
\frac{|\partial_\eta^\beta F_\alpha(\eta)|}{w_{\alpha\beta}}.
\]
Here the [[shared-foundations/factorial|factorial]] and [[shared-foundations/binomial-coefficient|binomial coefficient]] are ordinary nonnegative-integer quantities.

The **two-index analytic coefficient space** consists of sequences with finite norm, whose coefficient derivatives are continuous on \(I\) at every order, with one-sided endpoint derivatives. The formal radial series is \(F(Y,\eta)=\sum_{\alpha\ge0}F_\alpha(\eta)Y^\alpha\).

## Completeness

A norm-Cauchy sequence converges uniformly at each coefficient and derivative order. The [[real-analysis/uniform-convergence-differentiation|uniform derivative-limit theorem]] identifies successive derivatives. Passing the uniform weighted Cauchy bound to the limit gives convergence in the original norm. Thus this is a Banach space.

## Meaning of the weights

The binomial factor allows higher parameter derivatives as radial degree increases. This coupling permits radial integration to compensate for a parameter derivative. The polynomial denominator in each index also makes coefficient convolution bounded; both assertions require the estimates in [[functional-analysis/analytic-coefficient-algebra|the algebra bound]] and [[functional-analysis/analytic-coefficient-radial-estimates|the radial operator bounds]].
