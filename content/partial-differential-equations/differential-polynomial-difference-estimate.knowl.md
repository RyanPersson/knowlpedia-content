+++
id = "partial-differential-equations/differential-polynomial-difference-estimate"
title = "Difference estimate for a differential polynomial"
kind = "theorem"
summary = "Subtracting products one factor at a time bounds the nonlinear change by the difference jet times a polynomial in the input jets."
aliases = []
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/differential-polynomial", "real-analysis/cartesian-jet", "real-analysis/multi-index-leibniz-rule", "shared-foundations/finite-product", "real-analysis/real-power"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(F\) be a fixed [[partial-differential-equations/differential-polynomial|differential polynomial]] of order at most \(s\) and degree at most \(d\ge1\). If its coefficient derivatives through order \(m\) are bounded by \(C_m q^{-H_m}\), then pointwise
\[
|F(v+e)-F(v)|_m
\le C'_m q^{-H_m}|e|_{m+s}
\bigl(1+|v|_{m+s}+|e|_{m+s}\bigr)^{d-1}.
\]
The jet size \(|\cdot|_k\) includes derivatives through order \(k\). Constants depend on the fixed polynomial and the stated coefficient bounds, not on \(v,e\).

## Product telescoping

For a product of \(r\) factors, the difference between its values at \(v+e\) and \(v\) is a sum of \(r\) products, each with one difference factor and all other factors chosen from the two inputs. After up to \(m\) derivatives, Leibniz gives finitely many products of jets through order \(m+s\). Each contains at least one derivative of \(e\), yielding the estimate. Degree-zero terms cancel exactly.

Coefficient bounds are needed only on common regions containing the supports of the corresponding field factors, provided those regions work for both inputs and all comparisons. They cannot depend on the truncation index. A fixed finite list of coefficient logarithms may be absorbed into a fixed extra negative power of \(q\).
