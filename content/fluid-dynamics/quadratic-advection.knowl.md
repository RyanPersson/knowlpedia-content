+++
id = "fluid-dynamics/quadratic-advection"
title = "Quadratic advection of a velocity field"
kind = "definition"
summary = "The nonlinear term (u·∇)u and its exact expansion around a background field."
aliases = ["quadratic fluid nonlinearity", "nonlinear advection"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/material-derivative", "linear-algebra/quadratic-map", "real-analysis/product-rule"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Using the [[fluid-dynamics/transport-operator|transport operator]], the **quadratic advection term** is
\[
\mathcal N(u)=(u\cdot\nabla)u,
\qquad
\mathcal N(u)_i=\sum_j u_j\partial_j u_i.
\]
On smooth velocity fields it is a quadratic map, built from the bilinear expression \(B(v,w)=(v\cdot\nabla)w\).

## Expansion about a background

For \(u=U+v\), bilinearity gives the exact identity
\[
\mathcal N(U+v)=\mathcal N(U)
+(U\cdot\nabla)v+(v\cdot\nabla)U+(v\cdot\nabla)v.
\]
The two middle terms are linear in the perturbation \(v\), and the last is quadratic. The bilinear expression is generally not symmetric: \((v\cdot\nabla)w\) need not equal \((w\cdot\nabla)v\).

This identity is the algebraic starting point for linearized fluid equations and estimates of their nonlinear residual.
