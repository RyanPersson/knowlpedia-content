+++
id = "complex-analysis/locally-uniform-limit-theorem"
title = "Locally uniform limit theorem for holomorphic functions"
kind = "theorem"
summary = "Uniform convergence on compact subsets preserves holomorphicity and all fixed-order derivatives."
aliases = ["Weierstrass convergence theorem for holomorphic functions"]
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["differential-geometry/holomorphic-map", "complex-analysis/cauchy-integral-formula", "real-analysis/uniform-convergence-on-compact-sets"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(f_n\) be holomorphic on a common open set \(\Omega\subseteq\mathbb C\). If \(f_n\to f\) [[real-analysis/uniform-convergence-on-compact-sets|uniformly on every compact subset]], then \(f\) is holomorphic, and every fixed derivative \(f_n^{(k)}\to f^{(k)}\) uniformly on compact subsets.

## Proof through a surrounding circle

Choose a closed disc inside \(\Omega\). Uniform convergence on its boundary passes the limit through the Cauchy integral formula. On a smaller disc the kernel and all its fixed-order derivatives are uniformly bounded, so the resulting integral is holomorphic and can be differentiated. A finite collection of smaller discs covers any given compact subset. A common domain and local uniform convergence are essential; pointwise convergence alone is insufficient.

## References

- [Dan Romik, Complex Analysis, §7](https://www.math.ucdavis.edu/~romik/data/uploads/teaching/math205a-2018/complex-analysis-2018.pdf).
