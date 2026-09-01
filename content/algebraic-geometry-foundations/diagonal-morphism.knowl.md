+++
id = "algebraic-geometry-foundations/diagonal-morphism"
title = "Diagonal morphism"
kind = "knowl"
summary = "The canonical map from a scheme to its fiber square over the target."
aliases = ["diagonal-morphism", "Diagonal morphism", "diagonal of a morphism"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/morphism-of-schemes", "algebraic-geometry-foundations/fiber-product-of-schemes"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
+++

Let \(f:Y\to X\) be a [[algebraic-geometry-foundations/morphism-of-schemes|morphism of schemes]]. The two identity maps from \(Y\) to itself have the same composite \(f\) to \(X\). The universal property of the [[algebraic-geometry-foundations/fiber-product-of-schemes|fiber product]] therefore gives a unique morphism
\[
\Delta_f:Y\longrightarrow Y\times_XY
\]
whose composites with both projections \(Y\times_XY\to Y\) are the identity. This is the **diagonal morphism** of \(f\).

The notation is the scheme-theoretic analogue of the point-set diagonal \(y\mapsto(y,y)\). Its scheme structure also records infinitesimal information about the fibers of \(f\), which is why properties of the diagonal characterize separation and ramification conditions.
