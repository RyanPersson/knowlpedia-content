+++
id = "real-analysis/divergence-of-tensor"
title = "Row divergence of a matrix field"
kind = "definition"
summary = "The vector obtained by differentiating a matrix field in its second index."
aliases = ["tensor divergence", "matrix divergence"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/tensor-field", "real-analysis/partial-derivative", "shared-foundations/finite-sum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a differentiable [[real-analysis/tensor-field|matrix field]] \(T\), its **row divergence** is the vector
\[
(\operatorname{div}T)_i=\sum_j\partial_{x_j}T_{ij}.
\]
Thus each row is treated as a vector field. Some conventions differentiate the first index; the two agree for symmetric tensors but must be distinguished otherwise.

## Outer-product calculation

With \((v\otimes w)_{ij}=v_iw_j\), the product rule gives
\[
\operatorname{div}(v\otimes w)=(w\cdot\nabla)v+v\operatorname{div}w,
\qquad ((w\cdot\nabla)v)_i=\sum_jw_j\partial_jv_i.
\]
In particular, a divergence-free velocity satisfies
\(\operatorname{div}(u\otimes u)=(u\cdot\nabla)u\).
For \(T=pI\), row divergence is \(\nabla p\).
