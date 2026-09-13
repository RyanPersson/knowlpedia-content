+++
id = "real-analysis/scaled-cutoff-estimate"
title = "Derivative estimates for scaled cutoffs"
kind = "theorem"
summary = "Rescaling a smooth cutoff by a length δ costs one factor δ⁻¹ for each derivative."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/cutoff-function", "real-analysis/multi-index-notation", "real-analysis/chain-rule-multivariable", "real-analysis/supremum-norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(\chi\in C_c^\infty(\mathbb R^n)\), \(a\in\mathbb R^n\), and \(\delta>0\). Set \(\chi_{a,\delta}(x)=\chi((x-a)/\delta)\). Then
\[
\partial^\alpha\chi_{a,\delta}(x)
=\delta^{-|\alpha|}(\partial^\alpha\chi)((x-a)/\delta),
\qquad
\|\partial^\alpha\chi_{a,\delta}\|_\infty
=\delta^{-|\alpha|}\|\partial^\alpha\chi\|_\infty.
\]
Thus the support shrinks with \(\delta\), while derivatives grow with inverse powers of \(\delta\). The identity follows by repeated use of the [[real-analysis/chain-rule-multivariable|chain rule]].

## Anisotropic scaling

For positive widths \(\delta_1,\ldots,\delta_n\), replacing the argument by \(((x_i-a_i)/\delta_i)_i\) gives the factor \(\prod_i\delta_i^{-\alpha_i}\). Different directions can therefore incur different derivative costs.

## Product errors

The [[real-analysis/multi-index-leibniz-rule|Leibniz formula]] records exactly which derivatives strike the cutoff when differentiating \(\chi_{a,\delta}f\). These terms are supported in its transition region when at least one derivative strikes a cutoff that is constant on its plateau and outside its support.
