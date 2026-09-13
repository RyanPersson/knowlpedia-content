+++
id = "fluid-dynamics/transport-operator"
title = "Transport operator along a vector field"
kind = "definition"
summary = "The first-order spatial differential operator b·∇."
aliases = ["advection operator"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["real-analysis/euclidean-vector-field", "real-analysis/directional-derivative", "real-analysis/partial-derivative"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a vector field \(b(t,x)\), the **transport operator** along \(b\) is
\[
T_b=b\cdot\nabla=\sum_{j=1}^d b_j(t,x)\partial_{x_j}.
\]
For a differentiable scalar \(q\), \(T_bq\) is its spatial directional derivative along the vector \(b\) at that point. For fixed \(b\), it is linear in \(q\).

## Time dependence

The [[fluid-dynamics/material-derivative|material derivative]] adds the explicit time derivative: \(D_t=\partial_t+T_b\). Even if \(b\) depends on time, the operator \(T_b\) differentiates only the spatial argument of the field on which it acts.

For Cartesian vector components it acts componentwise. Position-dependent bases must also be differentiated when transporting a vector.
