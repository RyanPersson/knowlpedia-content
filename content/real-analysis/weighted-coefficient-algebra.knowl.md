+++
id = "real-analysis/weighted-coefficient-algebra"
title = "Product bounds for weighted coefficients and amplitudes"
kind = "lemma"
summary = "Leibniz estimates that add parameter orders and combine spatial envelope factors."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/weighted-coefficient-class", "real-analysis/envelope-controlled-amplitude", "real-analysis/multi-index-leibniz-rule"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For the classes \(\mathcal C^\alpha(w)\) and \(\mathcal A^\alpha(w,P)\) with the same domain, weights, and uniformity convention,
\[
\mathcal C^\alpha\mathcal C^\beta\subset\mathcal C^{\alpha+\beta},\qquad
\mathcal C^\alpha\mathcal A^\beta\subset\mathcal A^{\alpha+\beta},\qquad
\mathcal A^\alpha\mathcal A^\beta\subset\mathcal C^{\alpha+\beta}\cap\mathcal A^{\alpha+\beta}.
\]
Finite sums preserve each class, and any fixed coordinate derivative preserves the order \(\alpha\).

## Proof

Apply the [[real-analysis/multi-index-leibniz-rule|Leibniz rule]]. Each derivative of a product is a finite sum of factors with orders adding to \(\alpha+\beta\), and logarithmic and margin exponents adding to finite exponents. Since \(w,P\le1\),
\[
w^2\le w,\qquad w^{3/2}P\le\sqrt w P,\qquad
wP^2\le w,\quad wP^2\le\sqrt w P.
\]
Reindexing the derivative bounds proves the last assertion.

## Limits of the conclusion

The estimates do not provide Fourier frequency bookkeeping, support compatibility, or convergence of infinite sums. They apply to products of coefficients with jointly uniform bounds. Derivatives that contain parameter-dependent large prefactors must track those prefactors separately.
