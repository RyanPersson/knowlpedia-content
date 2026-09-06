+++
id = "real-analysis/zero-derivative-constant-corollary"
title = "Zero derivative implies constant"
kind = "knowl"
summary = "If f' vanishes everywhere on an interval, the function is constant"
aliases = ["zero-derivative-constant-corollary", "Zero derivative implies constant"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/zero-derivative-constant-corollary.md"
prerequisites = ["real-analysis/continuity-on-a-set", "real-analysis/differentiability-one-variable", "real-analysis/mean-value-theorem"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(f:[a,b]\to\mathbb{R}\) be [[real-analysis/continuity-on-a-set|continuous]] on \([a,b]\) and [[real-analysis/differentiability-one-variable|differentiable]] on \((a,b)\).

**Corollary**: If \(f'(x)=0\) for all \(x\in(a,b)\), then \(f\) is constant on \([a,b]\).

**Connection to parent theorem**:
Apply the [[real-analysis/mean-value-theorem|mean value theorem]]: for any \(x<y\), there exists \(c\in(x,y)\) with \(f(y)-f(x)=f'(c)(y-x)=0\).
