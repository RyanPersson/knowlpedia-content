+++
id = "complex-analysis/complex-monge-ampere-operator"
title = "Complex Monge–Ampère operator"
kind = "definition"
summary = "The determinant of the Levi matrix, extended as a measure for suitable plurisubharmonic functions."
aliases = ["complex Monge-Ampere operator", "complex Monge–Ampère measure"]
domains = ["complex-analysis", "several-complex-variables", "partial-differential-equations"]
section_mode = "progressive"
+++

For a real-valued \(C^2\) function \(u\) on \(U\subseteq\mathbb C^d\), the
**complex Monge–Ampère operator** is the determinant of its
[[complex-analysis/levi-form|Levi matrix]]:
\[
\operatorname{MA}_{\mathbb C}(u)
=\det\!\left(\frac{\partial^2u}
{\partial z_j\partial\bar z_k}\right).
\]
If \(u\) is [[complex-analysis/plurisubharmonic-function|plurisubharmonic]],
this determinant is nonnegative. Equivalently one packages it, up to the
chosen normalization of \(d^c\), as the top-degree measure \((dd^cu)^d\).

## Nonsmooth extension

Bedford–Taylor theory defines \((dd^cu)^d\) for locally bounded
plurisubharmonic functions by iterated products of positive currents. The
result agrees with the smooth determinant measure and is continuous under
appropriate monotone limits. For arbitrary unbounded PSH functions the
operator is not automatically defined; an energy class or another domain of
definition must be specified.

## Real and quaternionic analogues

The real Monge–Ampère operator takes the determinant of the real
[[real-analysis/hessian-matrix|Hessian]]. Replacing the complex Hessian by the
[[complex-analysis/quaternionic-hessian|quaternionic Hessian]] and the ordinary
determinant by the [[linear-algebra/moore-determinant|Moore determinant]] gives
the [[complex-analysis/quaternionic-monge-ampere-measure|quaternionic
Monge–Ampère measure]].

## References

1. Eric Bedford and B. A. Taylor, “A new capacity for plurisubharmonic functions,” *Acta Mathematica* 149 (1982), 1–40. [DOI record](https://doi.org/10.1007/BF02392348).
2. Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*, 2012. [Author-hosted text](https://www-fourier.ujf-grenoble.fr/~demailly/manuscripts/agbook.pdf). Relevant: Chapter III.
