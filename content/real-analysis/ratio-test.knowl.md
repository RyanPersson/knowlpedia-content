+++
id = "real-analysis/ratio-test"
title = "Ratio Test"
kind = "knowl"
summary = "A series converges absolutely if successive terms shrink by a uniform factor less than one."
aliases = ["ratio-test", "Ratio Test"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/series", "real-analysis/absolutely-convergent-series", "real-analysis/divergent-series"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "real-analysis/ratio-test.md"
+++

**Ratio test:** Let \(\sum_{n=1}^\infty a_n\) be a [[real-analysis/series|series]] with \(a_n\ne0\) for all sufficiently large \(n\), and define
\[
L^+=\limsup_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|,
\qquad
L^-=\liminf_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|.
\]
- If \(L^+<1\), then \(\sum a_n\) is [[real-analysis/absolutely-convergent-series|absolutely convergent]].
- If \(L^->1\), then \(a_n\not\to0\), so \(\sum a_n\) [[real-analysis/divergent-series|diverges]].
- In all other cases, these bounds alone are inconclusive.

In particular, if the ratio has a limit \(L\), the series converges absolutely for \(L<1\), diverges for \(L>1\), and the test is inconclusive for \(L=1\).

## Remarks

The ratio test is particularly effective for factorials, exponentials, and power-series-like terms, and it is closely related to the [[real-analysis/root-test|root test]] and the [[real-analysis/cauchy-hadamard-theorem|Cauchy–Hadamard theorem]] for [[real-analysis/power-series|power series]].
