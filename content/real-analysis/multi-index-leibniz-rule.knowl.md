+++
id = "real-analysis/multi-index-leibniz-rule"
title = "Multi-index Leibniz rule"
kind = "theorem"
summary = "The formula for all partial derivatives of a product, with multi-index binomial coefficients."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/product-rule", "real-analysis/multi-index-notation", "shared-foundations/binomial-coefficient", "real-analysis/class-ck-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For [[real-analysis/class-ck-map|smooth scalar functions]] \(f,g\) and a [[real-analysis/multi-index-notation|multi-index]] \(\alpha\), the **Leibniz rule** is
\[
\partial^\alpha(fg)=\sum_{\beta\le\alpha}
\binom{\alpha}{\beta}(\partial^\beta f)(\partial^{\alpha-\beta}g),
\qquad
\binom{\alpha}{\beta}=\prod_{i=1}^n\binom{\alpha_i}{\beta_i}.
\]
The inequality \(\beta\le\alpha\) is componentwise. It suffices to assume that the functions have continuous derivatives through order \(|\alpha|\).

## Derivation and estimates

Repeated application of the [[real-analysis/product-rule|first-derivative product rule]] gives the formula. At each step, the two possibilities for which factor is differentiated combine by Pascal's binomial identity. Taking absolute values yields a finite sum of derivative products, with constants depending only on the derivative order and dimension.

The same identity holds for a fixed bilinear product of finite-dimensional vector or matrix values, with the order of the two factors preserved.
