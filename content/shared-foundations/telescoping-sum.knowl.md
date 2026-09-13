+++
id = "shared-foundations/telescoping-sum"
title = "Telescoping sum"
kind = "identity"
summary = "Cancellation of successive differences in a finite sum and the additional limit needed for an infinite sum."
aliases = ["telescoping", "telescoping series"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/finite-sum", "shared-foundations/sequence", "algebra-groups/abelian-group"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(b_0,\ldots,b_n\) in an additive [[algebra-groups/abelian-group|abelian group]], the **telescoping identity** is
\[
\sum_{j=1}^{n}(b_j-b_{j-1})=b_n-b_0.
\]
To prove it, expand the finite sum: every intermediate \(b_j\) appears once with each sign and cancels.

## Infinite limits

If the \(b_j\) lie in a normed vector space and converge to \(b\), the identity for partial sums gives
\[
\sum_{j=1}^{\infty}(b_j-b_{j-1})=b-b_0.
\]
This establishes convergence in that norm. It need not establish absolute convergence of the series of norms. Without convergence of \(b_n\), the finite cancellation identity alone gives no infinite sum.
