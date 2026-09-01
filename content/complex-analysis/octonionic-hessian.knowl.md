+++
id = "complex-analysis/octonionic-hessian"
title = "Octonionic Hessian"
kind = "definition"
summary = "The octonionic Hermitian matrix of mixed Dirac derivatives of a real-valued function on the octonionic plane."
aliases = ["octonionic Hessian matrix", "Hessian over the octonions"]
domains = ["complex-analysis", "octonionic-analysis", "partial-differential-equations"]
prerequisites = ["nonassociative-algebra/octonionic-spin-factor"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Write an octonion as \(q=\sum_{r=0}^7x_re_r\), with \(e_0=1\). For an
octonion-valued function \(F\), set
\[
\frac{\partial F}{\partial\bar q}
=\sum_{r=0}^7e_r\frac{\partial F}{\partial x_r},
\qquad
\frac{\partial F}{\partial q}
=\sum_{r=0}^7\frac{\partial F}{\partial x_r}\bar e_r.
\]
For a real-valued \(C^2\) function \(u\) on \(\mathbb O^2\), its
**octonionic Hessian** is
\[
\operatorname{Hess}_{\mathbb O}u
=\left(\frac{\partial^2u}
{\partial\bar q_i\,\partial q_j}\right)_{i,j=1}^2.
\]
It is an
[[nonassociative-algebra/octonionic-spin-factor|octonionic Hermitian
\(2\times2\) matrix]].

## Positivity criterion

A \(C^2\) function is
[[complex-analysis/octonionic-plurisubharmonic-function|octonionic
plurisubharmonic]] exactly when this Hessian is positive semidefinite at every
point.

## Dimension restriction

Mixed octonionic derivatives can be written for more coordinates, but the
determinant and covariance used in this theory are specific to the
\(2\times2\) Hermitian Hessian. The established octonionic pluripotential
theory here is therefore a theory on \(\mathbb O^2\), not a formal replacement
of \(\mathbb H^n\) by arbitrary \(\mathbb O^n\).

## Convention warning

Left and right placement of octonionic units matters even more than in the
quaternionic case because multiplication is nonassociative. The displayed
operators and derivative order are part of the definition.

## References

1. Semyon Alesker, “Plurisubharmonic functions on the octonionic plane and \(\operatorname{Spin}(9)\)-invariant valuations on convex sets,” *Journal of Geometric Analysis* 18 (2008), 651–686. [arXiv record](https://arxiv.org/abs/0707.4385). Relevant: §§0.1, 1.2, and 3.1.
