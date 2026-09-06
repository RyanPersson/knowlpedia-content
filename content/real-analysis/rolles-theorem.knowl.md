+++
id = "real-analysis/rolles-theorem"
title = "Rolle's theorem"
kind = "knowl"
summary = "A differentiable function equal at two endpoints has a critical point in between."
aliases = ["rolles-theorem", "Rolle's theorem"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/differentiability-1d", "real-analysis/local-extremum", "real-analysis/mean-value-theorem"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "real-analysis/rolles-theorem.md"
+++

**Rolle's theorem:** Let \(f:[a,b]\to\mathbb{R}\) be continuous on \([a,b]\) and [[real-analysis/differentiability-1d|differentiable]] on \((a,b)\). If \(f(a)=f(b)\), then there exists \(c\in(a,b)\) such that
\[
f'(c)=0.
\]

This is a foundational consequence of the existence of a [[real-analysis/local-extremum|local extremum]] for continuous functions on compact intervals, and it is the key ingredient in the [[real-analysis/mean-value-theorem|mean value theorem]].
