+++
id = "real-analysis/local-diffeomorphism-corollary"
title = "Local diffeomorphism corollary"
kind = "knowl"
summary = "Nonvanishing Jacobian determinant implies a map is a diffeomorphism in a neighborhood of each point."
aliases = ["local-diffeomorphism-corollary", "Local diffeomorphism corollary"]
domains = ["real-analysis"]
prerequisites = ["topology/open-set", "real-analysis/jacobian-determinant", "real-analysis/inverse-function-theorem-rk", "fiber-bundles/diffeomorphism"]
dependency_review_count = 1
legacy_source_path = "real-analysis/local-diffeomorphism-corollary.md"
+++

Let \(U\subseteq\mathbb R^k\) be an [[topology/open-set|open set]], and let \(f:U\to\mathbb R^k\) be continuously differentiable. If
\[
\det Df(x)\neq 0\qquad\text{for every }x\in U,
\]
then for each \(x_0\in U\) there are neighborhoods \(A\) of \(x_0\) and \(B\) of \(f(x_0)\) such that \(f|_A:A\to B\) is a [[fiber-bundles/diffeomorphism|diffeomorphism]].

## Remarks

This is the [[real-analysis/inverse-function-theorem-rk|inverse function theorem]] applied at each point. In this situation, \(f\) is called a local diffeomorphism.
