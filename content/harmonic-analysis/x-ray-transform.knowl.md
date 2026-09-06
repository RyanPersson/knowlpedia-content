+++
id = "harmonic-analysis/x-ray-transform"
title = "X-ray transform"
kind = "definition"
summary = "The integral of a function over affine lines, parameterized by a base point and a direction."
aliases = ["line transform", "Euclidean X-ray transform"]
domains = ["harmonic-analysis", "integral-geometry"]
section_mode = "progressive"
prerequisites = ["measure-theory/lebesgue-integrable-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For an integrable function \(f:\mathbb R^d\to\mathbb C\), its **X-ray
transform** is
\[
Xf(x,\theta)=\int_{\mathbb R}f(x+t\theta)\,dt,
\qquad \theta\in S^{d-1}.
\]
It depends only on the oriented affine line represented by \((x,\theta)\):
\(Xf(x+a\theta,\theta)=Xf(x,\theta)\).

## Redundant parameterization

One often restricts \(x\in\theta^\perp\) to choose a unique base point. Replacing
\(\theta\) by \(-\theta\) leaves the unoriented line integral unchanged.

## Relation to the Radon transform

The X-ray transform integrates over one-dimensional affine subspaces. The
classical Radon transform in \(\mathbb R^d\) integrates over
[[convex-analysis/hyperplane|hyperplanes]]; they
coincide only in dimension two after identifying lines with hyperplanes.

## Role in plurisubharmonic extension

For the linewise extension used in higher-dimensional Beurling–Malliavin
theory, transverse components of the Levi form are X-ray transforms of the
real Hessian of the boundary weight.

## References

1. Sigurdur Helgason, *The Radon Transform*, 2nd ed., Birkhäuser, 1999. [DOI record](https://doi.org/10.1007/978-1-4757-1463-0).
