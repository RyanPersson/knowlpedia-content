+++
id = "linear-algebra/matrix-exponential"
title = "Matrix exponential"
kind = "definition"
summary = "The absolutely convergent power series sum A^n/n! for a square real or complex matrix."
aliases = []
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/matrix", "linear-algebra/operator-norm", "functional-analysis/absolutely-convergent-banach-series", "shared-foundations/factorial", "real-analysis/exponential-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For a square [[linear-algebra/matrix|matrix]] \(A\), its **matrix exponential** is
\[
e^A=\sum_{n=0}^\infty\frac{A^n}{n!}.
\]
The operator norm bounds this series by \(e^{\|A\|}\), proving absolute convergence. The same definition works for a bounded operator on a Banach space.

## Constant-coefficient evolution

Termwise differentiation gives \(\frac{d}{dt}e^{tA}=Ae^{tA}=e^{tA}A\), so \(e^{(t-s)A}\) is the propagator of \(y'=Ay\). Also \(e^{tA}e^{sA}=e^{(t+s)A}\), hence \(e^{tA}\) is invertible. For distinct matrices, \(e^{A+B}=e^Ae^B\) is guaranteed when \(AB=BA\) and is false in general without a commutation hypothesis.
