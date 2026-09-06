+++
id = "differential-geometry/connection-laplacian"
title = "Connection Laplacian"
kind = "definition"
summary = "The negative metric trace of the second covariant derivative on sections of a vector bundle."
aliases = ["rough Laplacian", "Bochner Laplacian"]
domains = ["differential-geometry", "partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/vector-bundle", "differential-geometry/pseudo-riemannian-manifold", "fiber-bundles/levicivita-connection-connection", "fiber-bundles/covariant-derivative-of-a-section"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\to M\) be a smooth [[fiber-bundles/vector-bundle|vector bundle]] with connection \(\nabla^E\), and let \(g\) be a [[differential-geometry/pseudo-riemannian-manifold|pseudo-Riemannian metric]] with [[fiber-bundles/levicivita-connection-connection|Levi–Civita connection]] \(\nabla^{\mathrm{LC}}\). The second [[fiber-bundles/covariant-derivative-of-a-section|covariant derivative of a section]] \(s\) is
\[
(\nabla^E)^2_{X,Y}s
=\nabla^E_X\nabla^E_Ys-\nabla^E_{\nabla^{\mathrm{LC}}_X Y}s.
\]
In the sign convention of this collection, the **connection Laplacian** is
\[
\Delta_{\nabla^E}s=-\operatorname{tr}_g\bigl((\nabla^E)^2s\bigr).
\]

For a Riemannian metric and a metric connection, this is also called the rough or Bochner Laplacian and has nonnegative leading sign. For a Lorentzian metric it is a connection wave operator and is [[mathematical-physics/normally-hyperbolic-operator|normally hyperbolic]]. On the trivial line bundle with its trivial connection, it reduces to the scalar [[differential-geometry/laplace-beltrami-operator|Laplace–Beltrami operator]].

## References

1. Peter Petersen, *Riemannian Geometry*, 3rd ed., Springer, 2016. [Publisher record](https://doi.org/10.1007/978-3-319-26654-1). Relevant: Chapter 4.
2. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: §1.5.
