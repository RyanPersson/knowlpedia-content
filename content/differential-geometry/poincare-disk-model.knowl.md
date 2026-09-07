+++
id = "differential-geometry/poincare-disk-model"
title = "Poincaré disk model"
kind = "definition"
summary = "The unit disk with its complete metric of constant curvature minus one, a model of the hyperbolic plane."
aliases = ["Poincaré disk", "Poincare disk model", "Poincaré metric on the disk"]
domains = ["differential-geometry", "hyperbolic-geometry", "mathematical-physics"]
section_mode = "progressive"
prerequisites = ["differential-geometry/riemannian-manifold"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 0
+++

The **Poincaré disk model** is the open unit disk
\(\mathbb D=\{z=x+iy\in\mathbb C:|z|<1\}\) equipped with the
[[differential-geometry/riemannian-manifold|Riemannian]]
metric
\[
ds^2=\frac{4(dx^2+dy^2)}{(1-|z|^2)^2}.
\]

## Properties

This metric has constant [[differential-geometry/gaussian-curvature|Gaussian curvature]] \(-1\), so \(\mathbb D\) is a
model of the hyperbolic plane.

## Geodesics and boundary

The hyperbolic [[differential-geometry/geodesic|geodesics]] are the Euclidean
circles and straight lines that meet the unit
[[complex-analysis/generalized-circle|generalized circle]] orthogonally. The ideal
[[topology/boundary|boundary]] is the unit circle \(S^1=\partial\mathbb D\).

## Relation to the half-plane model

A [[complex-analysis/mobius-transformation|Möbius transformation]] from the
upper half-plane to \(\mathbb D\) is an
isometry between the corresponding models of the hyperbolic plane.

## References

1. Benson Farb and Dan Margalit, *A Primer on Mapping Class Groups*,
   Princeton University Press, 2011, Chapter 1, §1.1.2, pp. 19–20.
   [Chapter excerpt](https://assets.press.princeton.edu/chapters/s9495.pdf).
