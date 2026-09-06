+++
id = "real-analysis/positive-derivative-implies-increasing"
title = "Positive derivative implies increasing"
kind = "knowl"
summary = "If a differentiable function has positive derivative everywhere on an interval, then it is strictly increasing."
aliases = ["positive-derivative-implies-increasing", "Positive derivative implies increasing"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/interval", "real-analysis/differentiability-1d", "real-analysis/mean-value-theorem"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "real-analysis/positive-derivative-implies-increasing.md"
+++

**Positive derivative implies increasing.** Let \(I\subseteq\mathbb R\) be an [[real-analysis/interval|interval]], and let \(f:I\to\mathbb R\) be continuous on \(I\) and [[real-analysis/differentiability-1d|differentiable]] at every interior point. If
\[
f'(x)>0
\]
for every interior point \(x\in I\), then \(f\) is strictly increasing on \(I\).

Indeed, the [[real-analysis/mean-value-theorem|mean value theorem]] applied to \(x<y\) gives \(f(y)-f(x)=f'(c)(y-x)>0\) for some \(c\in(x,y)\).
