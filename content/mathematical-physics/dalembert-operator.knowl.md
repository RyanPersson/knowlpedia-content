+++
id = "mathematical-physics/dalembert-operator"
title = "d’Alembert operator"
kind = "definition"
summary = "The scalar normally hyperbolic operator obtained from a Lorentzian metric."
aliases = ["d'Alembertian", "wave operator", "box operator", "dalembert operator"]
domains = ["mathematical-physics", "partial-differential-equations", "differential-geometry"]
prerequisites = ["differential-geometry/lorentzian-manifold", "differential-geometry/laplace-beltrami-operator"]
dependency_review_count = 1
section_mode = "progressive"
+++

On a [[differential-geometry/lorentzian-manifold|Lorentzian manifold]] \((M,g)\) of signature \((1,n-1)\), the **d’Alembert operator** or **wave operator** is
\[
\Box_g f=-\operatorname{tr}_g(\nabla df)
=-\frac{1}{\sqrt{|\det g|}}\,
\partial_\mu\!\left(\sqrt{|\det g|}\,g^{\mu\nu}\partial_\nu f\right).
\]
It is the Lorentzian instance of the [[differential-geometry/laplace-beltrami-operator|Laplace–Beltrami operator]] in the sign convention adopted here.

## Minkowski form

On [[mathematical-physics/minkowski-spacetime|Minkowski spacetime]] with
\[
g=\operatorname{diag}(-1,1,\ldots,1),
\]
one has
\[
\Box_g=\partial_t^2-\sum_{j=1}^{n-1}\partial_{x_j}^2.
\]
Its [[differential-geometry/principal-symbol|principal symbol]] is
\[
\sigma_2(\Box_g)(x,\xi)=-g_x^{-1}(\xi,\xi),
\]
which vanishes exactly on null covectors. Thus \(\Box_g\) is hyperbolic rather than elliptic.

## Geometric role

The operator is [[mathematical-physics/normally-hyperbolic-operator|normally hyperbolic]]. A hypersurface is characteristic for \(\Box_g\) precisely where its conormal covector is null. This local symbol statement is distinct from the global [[mathematical-physics/cauchy-problem-for-normally-hyperbolic-operators|Cauchy theorem]] and the [[mathematical-physics/existence-of-advanced-and-retarded-green-operators|existence of advanced and retarded Green operators]], which require [[differential-geometry/globally-hyperbolic-spacetime|global hyperbolicity]].

## Sign convention

Many authors define \(\Box_g=\operatorname{tr}_g\nabla d\). With the same metric signature their operator is the negative of this one. The displayed Minkowski formula, not the symbol \(\Box\) by itself, fixes the convention.

## References

1. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: §§1.5 and 3.2.
2. Lars Hörmander, *The Analysis of Linear Partial Differential Operators III*, Springer, 1985. [Publisher record](https://doi.org/10.1007/978-3-540-49938-1). Relevant: Chapter XXIII.
