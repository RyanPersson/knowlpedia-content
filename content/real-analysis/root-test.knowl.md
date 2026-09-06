+++
id = "real-analysis/root-test"
title = "Root test"
kind = "knowl"
summary = "A convergence test using the limsup of the nth roots of the term magnitudes."
aliases = ["root-test", "Root test"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/root-test.md"
prerequisites = ["real-analysis/series", "real-analysis/absolutely-convergent-series", "real-analysis/divergent-series"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Root test.** For a [[real-analysis/series|series]] \(\sum_{n=1}^\infty a_n\), define
\[
L=\limsup_{n\to\infty}\sqrt[n]{|a_n|},
\]
where the limit superior is allowed to take the value \(+\infty\).

- If \(L<1\), the series is [[real-analysis/absolutely-convergent-series|absolutely convergent]].
- If \(L>1\), including \(L=+\infty\), the series [[real-analysis/divergent-series|diverges]].
- If \(L=1\), the test is inconclusive.

## Remarks

The root test is especially natural for [[real-analysis/power-series|power series]] and is closely related to the [[real-analysis/cauchy-hadamard-theorem|Cauchy–Hadamard theorem]]; compare also the [[real-analysis/ratio-test|ratio test]].
