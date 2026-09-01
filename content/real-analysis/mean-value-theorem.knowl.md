+++
id = "real-analysis/mean-value-theorem"
title = "Mean value theorem"
kind = "knowl"
summary = "A differentiable function attains its average slope at some interior point."
aliases = ["mean-value-theorem", "Mean value theorem"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/differentiability-1d"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "real-analysis/mean-value-theorem.md"
+++

**Mean value theorem:** Let \(a<b\), and let \(f:[a,b]\to\mathbb{R}\) be continuous on \([a,b]\) and [[real-analysis/differentiability-1d|differentiable]] on \((a,b)\). Then there exists \(c\in(a,b)\) such that
\[
f'(c)=\frac{f(b)-f(a)}{b-a}.
\]

## Remarks

The theorem follows from [[real-analysis/rolles-theorem|Rolle's theorem]] by applying Rolle to a suitable affine adjustment of \(f\). It yields useful corollaries such as the [[real-analysis/mean-value-estimate-lemma|mean value estimate]] and monotonicity criteria from the sign of the [[real-analysis/derivative|derivative]].
