+++
id = "real-analysis/darboux-theorem"
title = "Darboux's theorem"
kind = "knowl"
summary = "Derivatives satisfy the intermediate value property even when they are not continuous."
aliases = ["darboux-theorem", "Darboux's theorem"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/interval", "real-analysis/intermediate-value-theorem", "topology/continuous-map", "real-analysis/discontinuity-point"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "real-analysis/darboux-theorem.md"
+++

**Darboux's theorem.** Let \(I\subseteq\mathbb R\) be an [[real-analysis/interval|interval]], and let \(f:I\to\mathbb R\) be differentiable. If \(a<b\) lie in the interior of \(I\) and \(y\) lies between \(f'(a)\) and \(f'(b)\), then there is \(c\in(a,b)\) such that
\[
f'(c)=y.
\]

Thus \(f'\) behaves like a function satisfying the [[real-analysis/intermediate-value-theorem|intermediate value theorem]], even though \(f'\) need not be a [[topology/continuous-map|continuous map]] and may have [[real-analysis/discontinuity-point|points of discontinuity]].
