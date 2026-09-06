+++
id = "real-analysis/differentiability-implies-continuity"
title = "Differentiability implies continuity"
kind = "knowl"
summary = "If a function is differentiable at a point, then it is continuous at that point."
aliases = ["differentiability-implies-continuity", "Differentiability implies continuity"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/differentiability-implies-continuity.md"
prerequisites = ["shared-foundations/function", "real-analysis/interval", "real-analysis/differentiability-1d", "real-analysis/differentiable-map", "real-analysis/frechet-derivative", "topology/continuous-map", "real-analysis/derivative", "real-analysis/limit-at-a-point"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Differentiability implies continuity:** Let \(f:I\to\mathbb{R}\) be a [[shared-foundations/function|function]] on an [[real-analysis/interval|interval]] \(I\), and let \(a\in I\) be an interior point. If \(f\) is [[real-analysis/differentiability-1d|differentiable]] at \(a\), then
\[
\lim_{x\to a} f(x) \;=\; f(a),
\]

so \(f\) is continuous at \(a\).

More generally, if \(f:U\to\mathbb{R}^m\) is [[real-analysis/differentiable-map|differentiable]] at \(a\in U\) in the sense of the [[real-analysis/frechet-derivative|Fréchet derivative]], then \(f\) is continuous at \(a\) (i.e. a [[topology/continuous-map|continuous map]] at that point). This connects [[real-analysis/derivative|derivatives]] to [[real-analysis/limit-at-a-point|limits at a point]].
