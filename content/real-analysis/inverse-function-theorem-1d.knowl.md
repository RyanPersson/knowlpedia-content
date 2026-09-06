+++
id = "real-analysis/inverse-function-theorem-1d"
title = "Inverse function theorem in one dimension"
kind = "knowl"
summary = "A differentiable function with nonzero derivative has a differentiable local inverse."
aliases = ["inverse-function-theorem-1d", "Inverse function theorem in one dimension"]
domains = ["real-analysis"]
prerequisites = ["shared-foundations/inverse-function", "real-analysis/differentiability-1d", "real-analysis/chain-rule"]
dependency_review_count = 1
legacy_source_path = "real-analysis/inverse-function-theorem-1d.md"
+++

**Inverse function theorem (one dimension).** Let \(I\subseteq\mathbb R\) be an open interval and let \(f:I\to\mathbb R\) be continuously differentiable. If \(x_0\in I\) and \(f'(x_0)\ne0\), then there are open intervals \(J\subseteq I\) and \(K\subseteq\mathbb R\), containing \(x_0\) and \(f(x_0)\), respectively, such that:

1. The restriction \(f|_J:J\to K\) is bijective.
2. Its [[shared-foundations/inverse-function|inverse]] \(g:K\to J\) is continuously differentiable and satisfies
   \[
   g'(y)=\frac{1}{f'(g(y))}.
   \]

## Remarks

In particular, \(g'(f(x_0))=1/f'(x_0)\). Continuity of \(f'\) makes \(f'\) have constant sign near \(x_0\); the derivative formula follows from the [[real-analysis/chain-rule|chain rule]] applied to \(f\circ g=\operatorname{id}\).
