+++
id = "real-analysis/mean-value-inequality"
title = "Mean value inequality"
kind = "knowl"
summary = "A bound on the change of a differentiable map using a bound on its derivative."
aliases = ["mean-value-inequality", "Mean value inequality"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/mean-value-inequality.md"
prerequisites = ["linear-algebra/operator-norm"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Mean value inequality.** Let \(U\subseteq\mathbb R^k\) be open, let \(f:U\to\mathbb R^m\) be continuously differentiable, and suppose the line segment \([x,y]\) lies in \(U\). If \(M\ge0\) satisfies
\[
\|Df(z)\|\le M \quad \text{for all } z \text{ on the segment from } x \text{ to } y,
\]
where \(\lVert Df(z)\rVert\) is the [[linear-algebra/operator-norm|operator norm]], then
\[
\|f(y)-f(x)\|\le M\|y-x\|.
\]

## Remarks

For \(k=m=1\), this gives \(|f(y)-f(x)|\le M|y-x|\).
