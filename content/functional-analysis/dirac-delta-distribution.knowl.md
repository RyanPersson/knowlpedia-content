+++
id = "functional-analysis/dirac-delta-distribution"
title = "Dirac delta distribution"
kind = "definition"
summary = "The distribution that evaluates a test function at one specified point."
aliases = ["Dirac delta", "delta distribution", "point source"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/distribution", "functional-analysis/test-function-space", "functional-analysis/tempered-distribution"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(a\in\mathbb R^n\), the **Dirac delta distribution at \(a\)** is
\[
\langle\delta_a,\varphi\rangle=\varphi(a)
\]
for every [[functional-analysis/test-function-space|test function]] \(\varphi\). Evaluation is linear and continuous in the test-function topology, so this defines a distribution.

## Point mass and derivatives

It is also the distribution associated with the unit point-mass measure and extends continuously to Schwartz functions, hence is tempered. Its derivative is defined by \(\langle\partial_j\delta_a,\varphi\rangle=-\partial_j\varphi(a)\). The delta is not represented by a locally integrable function. With the Fourier convention \(e^{-2\pi ix\cdot\xi}\), \(\widehat{\delta_0}=1\) as tempered distributions.
