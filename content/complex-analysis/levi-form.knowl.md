+++
id = "complex-analysis/levi-form"
title = "Levi form of a function"
kind = "definition"
summary = "The Hermitian form defined by the mixed complex second derivatives of a twice differentiable real-valued function."
aliases = ["complex Hessian", "ddbar Hessian"]
domains = ["complex-analysis", "several-complex-variables", "differential-geometry"]
prerequisites = []
dependency_review_count = 1
section_mode = "progressive"
+++

For a real-valued \(C^2\) function \(u\) on an open subset of \(\mathbb C^d\),
the **Levi form** at \(z\) is the Hermitian form
\[
\mathcal L_u(z;v)=
\sum_{j,k=1}^d
\frac{\partial^2u}{\partial z_j\partial\bar z_k}(z)
v_j\overline{v_k},
\qquad v\in\mathbb C^d.
\]
Its matrix is \(\bigl(u_{z_j\bar z_k}\bigr)_{j,k}\).

## Real-coordinate formula

Using
\(\partial_{z_j}=\tfrac12(\partial_{x_j}-i\partial_{y_j})\) and
\(\partial_{\bar z_j}=\tfrac12(\partial_{x_j}+i\partial_{y_j})\), the Levi
matrix is a particular Hermitian combination of the blocks of the real
[[real-analysis/hessian-matrix|Hessian]].

## Positivity

A \(C^2\) function is
[[complex-analysis/plurisubharmonic-function|plurisubharmonic]] exactly when
its Levi form is represented by a
[[linear-algebra/positive-semidefinite-matrix|positive-semidefinite matrix]].
A uniform lower bound by a positive Hermitian form is
[[complex-analysis/strictly-plurisubharmonic-function|strict
plurisubharmonicity]].

## References

1. Steven G. Krantz, *Function Theory of Several Complex Variables*, 2nd ed., AMS Chelsea, 2001. [Publisher record](https://bookstore.ams.org/chel-340-h/).
