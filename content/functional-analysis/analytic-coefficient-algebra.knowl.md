+++
id = "functional-analysis/analytic-coefficient-algebra"
title = "Product estimate in a two-index analytic coefficient space"
kind = "proposition"
summary = "Coefficient convolution and the Leibniz rule are bounded by the factorial-binomial weights."
aliases = ["analytic coefficient product bound"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/two-index-analytic-coefficient-space", "real-analysis/product-rule", "real-analysis/cauchy-product", "functional-analysis/bounded-bilinear-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For the [[functional-analysis/two-index-analytic-coefficient-space|two-index coefficient norm]], coefficient multiplication
\((FG)_\alpha=\sum_{i=0}^\alpha F_iG_{\alpha-i}\) obeys
\[
\|FG\|_{R,\rho}\le256\|F\|_{R,\rho}\|G\|_{R,\rho}.
\]
The constant is uniform in \(R,\rho\); no optimality is claimed.

## Convolution estimate

For every \(N\ge0\), splitting the sum at \(N/2\) gives
\[
\sum_{i=0}^N\frac{(N+1)^2}{(i+1)^2(N-i+1)^2}
\le8\sum_{j=1}^\infty j^{-2}\le16.
\]
In the Leibniz formula for \(\partial_\eta^\beta(F_iG_{\alpha-i})\), the derivative binomial cancels the derivative factorials. The remaining binomial ratio is at most one because
\[
\binom{i+k}{k}\binom{\alpha-i+\beta-k}{\beta-k}
\le\binom{\alpha+\beta}{\beta}.
\]
The left side counts a restricted collection of subsets counted on the right. Applying the convolution estimate to both indices gives \(16^2\). Rescaling the norm by 256 makes multiplication submultiplicative, producing a Banach-algebra norm.
