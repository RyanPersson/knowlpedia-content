+++
id = "complex-analysis/hormander-l2-dbar-theorem"
title = "Hörmander L2 theorem for the d-bar equation"
kind = "theorem"
summary = "A strictly plurisubharmonic weight gives a weighted L2 solution of the d-bar equation for closed (0,1)-forms."
aliases = ["Hörmander d-bar estimate", "Hörmander L2 existence theorem"]
domains = ["complex-analysis", "several-complex-variables", "partial-differential-equations"]
prerequisites = []
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\phi:\mathbb C^d\to\mathbb R\) be plurisubharmonic with Levi form bounded
below in the distributional sense by \(\kappa(z)I\), where \(\kappa>0\). If a
((0,1))-form \(\eta\) satisfies \(\bar\partial\eta=0\) and
\[
\int_{\mathbb C^d}|\eta|^2\frac{e^{-\phi}}{\kappa}<\infty,
\]
then there is a distributional solution \(g\) of
\(\bar\partial g=\eta\) such that
\[
\int_{\mathbb C^d}|g|^2e^{-\phi}
\le
\int_{\mathbb C^d}|\eta|^2\frac{e^{-\phi}}{\kappa}.
\]

## Geometric input

The operator \(\bar\partial\) is the Dolbeault operator from
[[differential-geometry/dolbeault-operators|Dolbeault theory]]. Positivity of
the [[complex-analysis/levi-form|Levi form]] is the curvature term that makes
the weighted estimate coercive.

## Holomorphic correction

If \(h\) is a smooth cutoff and \(g\) solves
\(\bar\partial g=\bar\partial h\), then \(f=h-g\) is entire. Choosing a weight
with a strong singular or convex term near a point can make \(g\) small there,
ensuring \(f\) is nonzero.

## References

1. Lars Hörmander, “\(L^2\) estimates and existence theorems for the \(\bar\partial\) operator,” *Acta Mathematica* 113 (1965), 89–152. [DOI record](https://doi.org/10.1007/BF02391775).
2. Lars Hörmander, *An Introduction to Complex Analysis in Several Variables*, 3rd ed., North-Holland, 1990.
