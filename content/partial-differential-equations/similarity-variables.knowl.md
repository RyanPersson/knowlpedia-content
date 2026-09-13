+++
id = "partial-differential-equations/similarity-variables"
title = "Similarity variables"
kind = "definition"
summary = "Rescaled space, time, and unknowns adapted to selected concentration exponents."
aliases = ["similarity coordinates"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["real-analysis/anisotropic-dilation", "real-analysis/chain-rule-multivariable", "real-analysis/partial-derivative", "real-analysis/natural-logarithm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Fix a time \(T\), put \(\tau=T-t>0\), and choose real exponents \(a,b_1,\ldots,b_d\). **Similarity variables** for a field \(u(t,x)\) are
\[
y_i=x_i\tau^{-b_i},\qquad s=-\log\tau,\qquad
U(s,y)=\tau^a u(T-\tau,D_\tau y),
\]
where \(D_\tau\) is the corresponding [[real-analysis/anisotropic-dilation|anisotropic dilation]]. The field need not be invariant under this change of variables.

## Derivative formulas

The [[real-analysis/chain-rule-multivariable|chain rule]] for \(u=\tau^{-a}U(s,y)\) gives
\[
\partial_tu=\tau^{-a-1}\left(aU+\partial_sU+\sum_i b_i y_i\partial_{y_i}U\right),
\qquad
\partial_{x_i}u=\tau^{-a-b_i}\partial_{y_i}U.
\]
These formulas describe the coordinate change for any exponents. Whether they make a particular PDE autonomous requires substituting into that equation.
