+++
id = "convex-analysis/strictly-convex-function"
title = "Strictly convex function"
kind = "knowl"
summary = "A convex function with strict inequality for distinct points"
aliases = ["strictly-convex-function", "Strictly convex function"]
domains = ["convex-analysis"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "convex-analysis/strictly-convex-function.md"
+++

Let \(X\) be a real vector space and let \(f:X\to(-\infty,+\infty]\) have a convex effective domain
\[
\operatorname{dom}(f)=\{x\in X:f(x)<+\infty\}.
\]
The function \(f\) is **strictly convex** if, for all distinct \(x,y\in\operatorname{dom}(f)\) and all \(\lambda\in(0,1)\),
\[
f(\lambda x+(1-\lambda)y)<\lambda f(x)+(1-\lambda)f(y).
\]

## Examples

- On \(\mathbb R\), \(f(x)=x^2\) is strictly convex.
- On a real Hilbert space, \(f(x)=\lVert x\rVert^2\) is strictly convex.
- The function \(f(x)=|x|\) on \(\mathbb R\) is convex but not strictly convex: equality holds between distinct points on the same ray.

## Remarks

Strict convexity strengthens [[convex-analysis/convex-function-via-epigraph|convexity]]. If a strictly convex function attains a minimum on a convex set, that minimizer is unique.
