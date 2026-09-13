+++
id = "functional-analysis/mixed-derivative-radial-estimate"
title = "A mixed-derivative estimate after radial inversion"
kind = "proposition"
summary = "A radial inverse controls a product containing one parameter derivative and one dilation derivative."
aliases = ["mixed analytic radial estimate"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/analytic-coefficient-algebra", "functional-analysis/analytic-coefficient-radial-estimates", "real-analysis/logarithmic-radial-derivative"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

In the [[functional-analysis/two-index-analytic-coefficient-space|two-index norm]], let \(D=Y\partial_Y\) and \(\nu\ge1\). Then
\[
\|J_\nu[(\partial_\eta F)(DG)]\|_{R,\rho}
\le\frac{1024R}{\rho}\|F\|_{R,\rho}\|G\|_{R,\rho}.
\]

## Allocation of the new degree

For output degree \(N=\alpha+1\), assign the degree created by \(J_\nu\) to the factor carrying \(\partial_\eta\). The weight ratio converts its degree \(i\), derivative order \(k+1\), to degree \(i+1\), order \(k\), at cost at most \((4R/\rho)(i+1)\). The factor \(DG\) contributes \(\alpha-i\). Their product divided by \(N(\alpha+\nu)\) is at most one. The two convolution sums cost at most \(16^2\), proving the bound. At \(\alpha=0\), the differentiated radial factor is zero.

## Additional factors

The same reasoning without one derivative gives the corresponding simpler estimate. Undifferentiated factors can then be included using the algebra bound. This is an estimate for the composed expression, not a claim that both derivatives separately act boundedly on the space.
