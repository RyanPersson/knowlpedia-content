+++
id = "real-analysis/integration-by-parts-riemann-stieltjes"
title = "Integration by parts for Riemann–Stieltjes integrals"
kind = "knowl"
summary = "A boundary-term identity relating two Riemann–Stieltjes integrals."
aliases = ["integration-by-parts-riemann-stieltjes", "Integration by parts for Riemann–Stieltjes integrals"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/integration-by-parts-riemann-stieltjes.md"
prerequisites = ["real-analysis/bounded-variation-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(a<b\). If \(f,g:[a,b]\to\mathbb R\) are [[real-analysis/bounded-variation-function|of bounded variation]] and at least one is continuous, then both Riemann–Stieltjes integrals exist and
\[
\int_a^b f\,dg \;+\; \int_a^b g\,df \;=\; f(b)g(b)-f(a)g(a).
\]

## Remarks

When \(f\) and \(g\) are continuously differentiable, substituting \(df=f'(x)\,dx\) and \(dg=g'(x)\,dx\) gives the usual [[real-analysis/integration-by-parts|integration-by-parts formula]]. The stated existence follows from the more general criterion that two bounded-variation functions with no common discontinuity are integrable with respect to one another.
