+++
id = "real-analysis/nonnegative-extended-series"
title = "Sum of nonnegative extended real terms"
kind = "definition"
summary = "The supremum of finite partial sums, with infinity allowed as a term or total."
aliases = ["nonnegative extended sum", "countable nonnegative sum"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["convex-analysis/extended-real-number-system-and-conventions", "shared-foundations/sequence", "shared-foundations/finite-sum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(a_j\in[0,\infty]\), define the **nonnegative extended sum** by
\[
\sum_{j=1}^\infty a_j=\sup_N\sum_{j=1}^N a_j\in[0,\infty].
\]
Addition uses \(a+\infty=\infty\) for \(a\ge0\). The sum is also the supremum over all finite subsums, so rearranging or regrouping its terms does not change the value.

## Infinite values

The value is infinite if any term is infinite or if the finite partial sums have no real upper bound. No cancellation of infinities is involved. This is the sum used in countable additivity of measures and in integrals of nonnegative functions. Signed series and differences of two infinite sums require different hypotheses.
