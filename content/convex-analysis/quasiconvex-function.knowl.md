+++
id = "convex-analysis/quasiconvex-function"
title = "Quasiconvex function"
kind = "knowl"
summary = "A function whose value on a line segment never exceeds the larger endpoint value."
aliases = ["quasiconvex-function", "Quasiconvex function"]
domains = ["convex-analysis"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "convex-analysis/quasiconvex-function.md"
+++

Let \(X\) be a real vector space and let \(f:X\to(-\infty,\infty]\) be an extended-real-valued function. The function \(f\) is **quasiconvex** if, for all \(x,y\in X\) and \(\lambda\in[0,1]\),
\[
f(\lambda x+(1-\lambda)y)\le \max\{f(x),f(y)\}.
\]

Equivalently, every sublevel set \(\{x\in X:f(x)\le \alpha\}\) is convex.

## Examples

- Any [[convex-analysis/convex-function-via-epigraph|convex function]] is quasiconvex.
- The function \(f(x)=\sqrt{|x|}\) on \(\mathbb R\) is quasiconvex but not convex.
- Any constant function is quasiconvex.

## Remarks

Quasiconvexity is weaker than convexity: it controls sublevel sets but does not require the graph to lie below its chords.
