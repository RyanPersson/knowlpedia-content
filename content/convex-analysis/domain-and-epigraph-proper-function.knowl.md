+++
id = "convex-analysis/domain-and-epigraph-proper-function"
title = "Domain, epigraph, and proper function"
kind = "knowl"
summary = "dom(f) is where f is finite; epi(f) is the set above the graph; proper means dom(f)≠∅"
aliases = ["domain-and-epigraph-proper-function", "Domain, epigraph, and proper function"]
domains = ["convex-analysis"]
prerequisites = ["convex-analysis/extended-real-number-system-and-conventions", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "convex-analysis/domain-and-epigraph-proper-function.md"
+++

Let \(X\) be a vector space and let \(f:X\to(-\infty,+\infty]\) be an [[convex-analysis/extended-real-number-system-and-conventions|extended-real-valued]] function.

- The **domain** of \(f\) is
\[
\mathrm{dom}(f):=\{x\in X: f(x)<\infty\}.
\]

- The **epigraph** of \(f\) is
\[
\mathrm{epi}(f):=\{(x,\alpha)\in X\times\mathbb{R}: f(x)\le \alpha\}.
\]

The function \(f\) is **proper** if \(\operatorname{dom}(f)\neq\varnothing\). With the stated codomain, this is equivalent to the usual requirement that \(f\) is never \(-\infty\) and is not identically \(+\infty\).

## Interpretation

The epigraph turns properties of \(f\) into geometric properties of sets; for example, \(f\) is [[convex-analysis/convex-function-via-epigraph|convex]] exactly when its epigraph is convex.
