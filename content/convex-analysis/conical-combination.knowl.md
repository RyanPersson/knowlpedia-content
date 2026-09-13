+++
id = "convex-analysis/conical-combination"
title = "Conical combination"
kind = "definition"
summary = "A finite linear combination with nonnegative coefficients, without a normalization on their sum."
aliases = ["nonnegative linear combination"]
domains = ["convex-analysis"]
section_mode = "progressive"
prerequisites = ["convex-analysis/linear-combination", "shared-foundations/real-numbers", "shared-foundations/finite-sum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **conical combination** of vectors \(v_1,\ldots,v_m\) in a real vector space is a [[convex-analysis/linear-combination|linear combination]]
\[
\sum_{j=1}^m a_jv_j,\qquad a_j\ge0.
\]
The coefficients need not sum to one. The empty combination is zero.

## Comparison with convex combinations

If \(s=\sum_j a_j>0\), the combination is \(s\) times the convex combination \(\sum_j(a_j/s)v_j\). Nonnegative coefficients may include zeros; strictly positive coefficients specify a smaller set of representations when generators are fixed.

## References

- [Boyd and Vandenberghe, Convex Optimization, §2.1 (convex cones)](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf).
