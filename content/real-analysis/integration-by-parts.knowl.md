+++
id = "real-analysis/integration-by-parts"
title = "Integration by parts"
kind = "knowl"
summary = "An identity relating the integral of a product to boundary terms and another integral."
aliases = ["integration-by-parts", "Integration by parts"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/riemann-integrable-function"]
dependency_review_count = 1
legacy_source_path = "real-analysis/integration-by-parts.md"
+++

Let \(a<b\). Suppose \(u,v:[a,b]\to\mathbb R\) are continuous on \([a,b]\), differentiable on \((a,b)\), and their derivatives extend to [[real-analysis/riemann-integrable-function|Riemann-integrable]] functions on \([a,b]\). Then
\[
\int_a^b u(x)\,v'(x)\,dx = u(b)v(b)-u(a)v(a) - \int_a^b u'(x)\,v(x)\,dx.
\]

## Remarks

This is the integral form of the product rule: apply the [[real-analysis/fundamental-theorem-of-calculus-ii|fundamental theorem of calculus]] to \((uv)'=u'v+uv'\).
