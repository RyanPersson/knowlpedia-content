+++
id = "convex-analysis/biconjugate"
title = "Biconjugate"
kind = "knowl"
summary = "The Fenchel conjugate of a function's conjugate, central to lower-semicontinuous convex relaxation."
aliases = ["biconjugate"]
domains = ["convex-analysis"]
prerequisites = ["shared-foundations/function", "convex-analysis/convex-conjugate-fenchel", "convex-analysis/closed-convex-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "convex-analysis/biconjugate.md"
+++

A **biconjugate** of an extended-real-valued [[shared-foundations/function|function]] \(f:\mathbb{R}^n\to(-\infty,+\infty]\) is the function
\[
f^{**}=(f^*)^*,
\]
where \(f^*\) is the [[convex-analysis/convex-conjugate-fenchel|Fenchel conjugate]] of \(f\).

If \(f\) is proper and has an affine minorant, then \(f^{**}\) is the greatest lower-semicontinuous convex function bounded above by \(f\). In particular, \(f^{**}\le f\) pointwise. The [[convex-analysis/fenchel-moreau-theorem|Fenchel–Moreau theorem]] states that a proper function satisfies \(f=f^{**}\) exactly when it is lower-semicontinuous and convex.

Here “lower-semicontinuous and convex” is also commonly called [[convex-analysis/closed-convex-function|closed convex]].

## Examples

- If \(f\) is proper, lower-semicontinuous, and convex—for instance, a norm—then \(f^{**}=f\).
- If \(C\subseteq\mathbb{R}^n\) is nonempty and \(\delta_C\) is its indicator function, then \(\delta_C^{**}=\delta_{\overline{\operatorname{conv}}(C)}\). For \(C=\{-1,1\}\subset\mathbb{R}\), this gives \(\delta_C^{**}=\delta_{[-1,1]}\).
