+++
id = "analysis/bounded-overlap-sum-estimate"
title = "Lp estimate for sums with bounded overlap"
kind = "theorem"
summary = "A multiplicity bound controls the Lp norm of a countable sum in terms of the individual Lp norms."
aliases = []
domains = ["analysis"]
section_mode = "progressive"
prerequisites = ["analysis/finitely-overlapping-family", "measure-theory/lp-norm", "convex-analysis/holder-inequality-finite-sums", "measure-theory/tonellis-theorem"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \((f_j)\) be a countable family of measurable scalar or finite-dimensional vector-valued functions. Suppose that at almost every point at most \(N\ge1\) terms are nonzero. For \(1\le p<\infty\),
\[
\left\|\sum_jf_j\right\|_p^p
\le N^{p-1}\sum_j\|f_j\|_p^p.
\]
For \(p=\infty\), the corresponding estimate is
\[
\left\|\sum_jf_j\right\|_\infty\le N\sup_j\|f_j\|_\infty.
\]
The sum is pointwise finite almost everywhere; it can be assigned any value on the exceptional null set.

## Proof

At each ordinary point, the triangle inequality and finite-sum [[convex-analysis/holder-inequality-finite-sums|Hölder inequality]] give \(|\sum_j f_j|^p\le N^{p-1}\sum_j|f_j|^p\). Integrate and use [[measure-theory/tonellis-theorem|Tonelli's theorem]]. The supremum estimate follows directly from the triangle inequality.

This estimate does not assert differentiability of the sum. That requires [[analysis/locally-finite-smooth-sum|local finiteness]] or appropriate derivative convergence.
