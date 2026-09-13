+++
id = "measure-theory/averaged-second-moment-matrix"
title = "Averaged second-moment matrix"
kind = "definition"
summary = "The average of the outer product of a square-integrable vector with itself."
aliases = ["uncentered second-moment matrix", "averaged quadratic tensor"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/lp-space", "probability/probability-measure", "linear-algebra/outer-product", "linear-algebra/positive-semidefinite-matrix", "convex-analysis/holder-inequality-integrals"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

On a probability measure space, let \(w\in L^2(\mu;\mathbb R^d)\). Its **averaged second-moment matrix** is
\[
R(w)=\int w\otimes w\,d\mu,\qquad
R(w)_{ij}=\int w_iw_j\,d\mu.
\]
Each entry is integrable by Hölder's inequality. It is symmetric and [[linear-algebra/positive-semidefinite-matrix|positive semidefinite]], since \(\xi^TR(w)\xi=\int(\xi\cdot w)^2\,d\mu\ge0\).

## Centering and signs

This is an uncentered second moment. If \(\bar w=\int w\,d\mu\), its centered version is \(R(w)-\bar w\otimes\bar w\), the covariance matrix. Off-diagonal entries of either matrix can be negative even though the whole matrix is positive semidefinite. An average over a periodic variable is one example of a probability average; no physical randomness is required.
