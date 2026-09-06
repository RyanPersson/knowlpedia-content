+++
id = "complex-analysis/octonionic-radon-transform"
title = "Octonionic Radon transform"
kind = "definition"
summary = "The injective transform integrating a function on the octonionic plane over affine octonionic lines."
aliases = ["Radon transform on O^2", "octonionic line transform"]
domains = ["complex-analysis", "octonionic-analysis", "integral-geometry"]
prerequisites = ["functional-analysis/test-function-space", "complex-analysis/octonionic-affine-line", "complex-analysis/octonionic-hessian"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For a [[functional-analysis/test-function-space|compactly supported smooth
function]] \(f\) on \(\mathbb O^2\), its
**octonionic Radon transform** is the function on affine octonionic lines
defined by
\[
(Rf)(E)=\int_E f(q)\,dq,
\qquad E\in\mathcal A\mathbb OP^1,
\]
where \(dq\) is the eight-dimensional Euclidean measure induced on the
[[complex-analysis/octonionic-affine-line|affine octonionic line]] \(E\).

## Injectivity

The transform \(R\) is injective. An inversion operator averages a fourth
power of the transverse eight-dimensional Laplacian over the family of
octonionic lines through a point and satisfies
\[
D(Rf)=c f
\]
for a nonzero constant \(c\).

## Role in octonionic pluripotential theory

Injectivity implies that linear combinations of distributions supported on
affine octonionic lines are weakly dense among distributions on
\(\mathbb O^2\). This linewise control is used to pass from restrictions of a
function to positivity statements about its
[[complex-analysis/octonionic-hessian|octonionic Hessian]].

## Symmetry

Both the transform and its inversion commute with translations and the
[[lie-groups/spin9-spin-representation|\(\operatorname{Spin}(9)\) action]] on
the octonionic plane.

## References

1. Semyon Alesker, “Plurisubharmonic functions on the octonionic plane and \(\operatorname{Spin}(9)\)-invariant valuations on convex sets,” *Journal of Geometric Analysis* 18 (2008), 651–686. [arXiv record](https://arxiv.org/abs/0707.4385). Relevant: §2.
