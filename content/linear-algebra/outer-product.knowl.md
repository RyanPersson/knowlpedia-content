+++
id = "linear-algebra/outer-product"
title = "Outer product"
kind = "definition"
summary = "The rank-at-most-one matrix vw^T associated with two real vectors."
aliases = ["rank-one tensor", "dyadic product"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/matrix", "linear-algebra/inner-product", "linear-algebra/rank"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For real column vectors \(v\in\mathbb R^m\) and \(w\in\mathbb R^n\), their **outer product** is
\[
v\otimes w=vw^T,\qquad (v\otimes w)_{ij}=v_iw_j.
\]
It acts on a vector \(x\in\mathbb R^n\) by \((v\otimes w)x=v(w\cdot x)\). Its range is contained in the span of \(v\), and its [[linear-algebra/rank|rank]] is one when both vectors are nonzero.

## Quadratic tensors

The matrix \(v\otimes v\) is symmetric and positive semidefinite since
\(x^T(v\otimes v)x=(v\cdot x)^2\ge0\). For complex vectors, a Hermitian covariance uses \(vv^*\), with conjugation, whereas the bilinear tensor \(vv^T\) has a different meaning. State that convention explicitly.

## References

- [Sheldon Axler, Linear Algebra Done Right, 4th ed., Chapters 2–3, 6 and 9](https://linear.axler.net/LADR4e.pdf).
