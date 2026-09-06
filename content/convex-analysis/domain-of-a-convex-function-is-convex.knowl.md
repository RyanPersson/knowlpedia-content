+++
id = "convex-analysis/domain-of-a-convex-function-is-convex"
title = "Domain of a convex function is convex"
kind = "knowl"
summary = "The effective domain of an extended-real-valued convex function is a convex set."
aliases = ["domain-of-a-convex-function-is-convex", "Domain of a convex function is convex"]
domains = ["convex-analysis"]
prerequisites = ["convex-analysis/convex-function-via-epigraph", "convex-analysis/domain-and-epigraph-proper-function", "convex-analysis/convex-set"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "convex-analysis/domain-of-a-convex-function-is-convex.md"
+++

Let \(X\) be a real vector space and let \(f:X\to(-\infty,+\infty]\) be a [[convex-analysis/convex-function-via-epigraph|convex function]]. Then its effective [[convex-analysis/domain-and-epigraph-proper-function|domain]]
\[
\operatorname{dom}(f)=\{x\in X:f(x)<+\infty\}
\]
is a [[convex-analysis/convex-set|convex set]].

## Proof

If \(x,y\in\operatorname{dom}(f)\) and \(0\le \lambda\le 1\), convexity gives
\[
f(\lambda x+(1-\lambda)y)
\le \lambda f(x)+(1-\lambda)f(y)<+\infty.
\]
Thus \(\lambda x+(1-\lambda)y\in\operatorname{dom}(f)\).
