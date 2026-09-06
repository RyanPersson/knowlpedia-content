+++
id = "real-analysis/change-of-variables-formula"
title = "Change of variables formula"
kind = "knowl"
summary = "A multivariable substitution rule involving the Jacobian determinant."
aliases = ["change-of-variables-formula", "Change of variables formula"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/change-of-variables-formula.md"
prerequisites = ["topology/open-set", "fiber-bundles/diffeomorphism", "real-analysis/jacobian-determinant"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(U,V\subseteq\mathbb R^n\) be [[topology/open-set|open sets]], let \(\Phi:U\to V\) be a \(C^1\) [[fiber-bundles/diffeomorphism|diffeomorphism]], and let \(f:V\to\mathbb R\) be continuous with compact support. The **change of variables formula** is
\[
\int_V f(x)\,dx = \int_U f(\Phi(u))\,\bigl|\det D\Phi(u)\bigr|\,du,
\]

where \(\det D\Phi(u)\) is the [[real-analysis/jacobian-determinant|Jacobian determinant]] of \(\Phi\) at \(u\).

## Remarks

This is the multivariable generalization of the one-dimensional [[real-analysis/substitution-rule|substitution rule]], and it is fundamental for computing [[real-analysis/multiple-riemann-integral|multiple Riemann integrals]] under smooth coordinate changes.
