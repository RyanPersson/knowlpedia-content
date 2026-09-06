+++
id = "real-analysis/m-test-corollary"
title = "Corollary of the M-test"
kind = "knowl"
summary = "If the sum of supremum norms is finite, then the corresponding series of functions converges uniformly."
aliases = ["m-test-corollary", "Corollary of the M-test"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/uniform-convergence"]
dependency_review_count = 1
legacy_source_path = "real-analysis/m-test-corollary.md"
+++

**Corollary of the M-test.** Let \(E\) be a set and let \(f_n:E\to\mathbb R\) or \(f_n:E\to\mathbb C\) be bounded functions. If
\[
\sum_{n=1}^\infty \|f_n\|_\infty
\]
converges, where \(\|f_n\|_\infty=\sup_{x\in E}|f_n(x)|\), then \(\sum_{n=1}^\infty f_n\) converges [[real-analysis/uniform-convergence|uniformly]] on \(E\) and absolutely at each point.

## Remarks

This is the [[real-analysis/weierstrass-m-test|Weierstrass M-test]] with \(M_n=\|f_n\|_\infty\).
