+++
id = "differential-geometry/laplace-beltrami-operator"
title = "Laplace–Beltrami operator"
kind = "definition"
summary = "The negative metric trace of the covariant Hessian, with a sign chosen to be nonnegative in Riemannian signature."
aliases = ["metric Laplacian", "scalar Laplacian", "Laplace-Beltrami operator"]
domains = ["differential-geometry", "partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-geometry/pseudo-riemannian-manifold", "fiber-bundles/levicivita-connection-connection", "differential-geometry/principal-symbol"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((M,g)\) be a [[differential-geometry/pseudo-riemannian-manifold|pseudo-Riemannian manifold]] with [[fiber-bundles/levicivita-connection-connection|Levi–Civita connection]] \(\nabla\). In the convention used here, the **Laplace–Beltrami operator** on a smooth function \(f\) is
\[
\Delta_g f=-\operatorname{tr}_g(\nabla df)
=-\frac{1}{\sqrt{|\det g|}}\,
\partial_i\!\left(\sqrt{|\det g|}\,g^{ij}\partial_j f\right).
\]
Its [[differential-geometry/principal-symbol|principal symbol]], with no factors of \(i\), is
\[
\sigma_2(\Delta_g)(x,\xi)=-g_x^{-1}(\xi,\xi).
\]

## Riemannian signature

If \(g\) is positive definite, \(\Delta_g\) is [[differential-geometry/elliptic-differential-operator|elliptic]]. On compactly supported functions it satisfies
\[
\int_M \overline f\,\Delta_g f\,d\mu_g
=\int_M |df|_g^2\,d\mu_g,
\]
so the convention adopted here gives a nonnegative operator. On Euclidean space it is \(-\sum_i\partial_i^2\). Authors who define \(\Delta=\operatorname{div}\operatorname{grad}\) use the negative of this operator.

## Indefinite signature

For an indefinite metric, the same coordinate expression is still defined but is not elliptic because its symbol vanishes on nonzero null covectors. In Lorentzian signature it is the normally hyperbolic [[mathematical-physics/dalembert-operator|d’Alembert operator]] \(\Box_g\). The name “Laplace–Beltrami operator” is most often reserved for the Riemannian case, while “wave operator” or “d’Alembertian” emphasizes the Lorentzian case.

## Related operators

This scalar operator should not be confused with the [[differential-geometry/hodge-laplacian|Hodge Laplacian]] on differential forms or with a [[differential-geometry/connection-laplacian|connection Laplacian]] on sections of a vector bundle. They agree on functions when their sign conventions are aligned, but their domains and lower-order geometry differ.

## References

1. Peter Petersen, *Riemannian Geometry*, 3rd ed., Springer, 2016. [Publisher record](https://doi.org/10.1007/978-3-319-26654-1). Relevant: Chapters 2 and 4.
2. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: §1.5 and Chapter 3.
