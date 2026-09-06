+++
id = "convex-analysis/convex-function-via-epigraph"
title = "Convex function via epigraph"
kind = "knowl"
summary = "A function is convex if and only if its epigraph is a convex set"
aliases = ["convex-function-via-epigraph", "Convex function via epigraph"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convex-function-via-epigraph.md"
prerequisites = ["convex-analysis/extended-real-number-system-and-conventions", "convex-analysis/domain-and-epigraph-proper-function", "convex-analysis/convex-set"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a real vector space and let \(f:X\to \overline{\mathbb R}\) be an [[convex-analysis/extended-real-number-system-and-conventions|extended-real-valued function]].

The function \(f\) is **convex** if its [[convex-analysis/domain-and-epigraph-proper-function|epigraph]]
\[
\operatorname{epi}(f)=\{(x,r)\in X\times\mathbb R:f(x)\le r\}
\]
is a [[convex-analysis/convex-set|convex set]] in \(X\times\mathbb{R}\).

## Equivalent characterizations

**Context.** This geometric definition is equivalent to analytic inequalities such as Jensen's inequality; see [[convex-analysis/equivalent-characterizations-of-convex-functions|equivalent characterizations of convexity]].

## Examples

- On a normed space, \(x\mapsto \|x\|\) is convex (uses the triangle inequality; see [[convex-analysis/norm-normed-vector-space|norm]]).
- The [[convex-analysis/indicator-function-of-a-set|indicator function]] of a set \(\Omega\) is convex iff \(\Omega\) is convex.
- The [[convex-analysis/distance-function-to-a-set|distance function]] to a convex set is convex (in normed spaces).
