+++
id = "differential-geometry/tautological-one-form-cotangent"
title = "Tautological one-form on a cotangent bundle"
kind = "definition"
summary = "The canonical one-form that evaluates a cotangent vector on the projection of a tangent vector to the base."
aliases = ["canonical one-form", "Liouville one-form", "Poincaré one-form"]
domains = ["differential-geometry", "fiber-bundles"]
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/cotangent-bundle", "fiber-bundles/differential-k-form"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]] and \(\pi:T^*M\to M\) its [[fiber-bundles/cotangent-bundle|cotangent bundle]]. The **tautological one-form** \(\theta\) is the [[fiber-bundles/differential-k-form|differential one-form]] on \(T^*M\) defined at a covector \(\alpha_x\in T_x^*M\) by
\[
\theta_{\alpha_x}(v)=\alpha_x\!\left(d\pi_{\alpha_x}(v)\right),
\qquad v\in T_{\alpha_x}(T^*M).
\]
Thus \(\theta\) evaluates the covector represented by the base point of \(T^*M\) on the component of \(v\) projected to \(M\). The construction uses only the cotangent projection and therefore requires no coordinates, metric, or connection.

## Coordinate expression

For local coordinates \(q^1,\ldots,q^n\) on \(M\) and induced fiber coordinates \(p_1,\ldots,p_n\) on \(T^*M\),
\[
\theta=\sum_{i=1}^n p_i\,dq^i.
\]
Although this formula is coordinate-dependent in appearance, the defining evaluation formula proves that the one-form is intrinsic.

## Canonical symplectic form

With the convention used here, the canonical symplectic form on \(T^*M\) is
\[
\omega_{\mathrm{can}}=-d\theta=\sum_{i=1}^n dq^i\wedge dp_i.
\]
It is closed because \(d^2=0\), and the coordinate expression shows that it is nondegenerate. Hence every cotangent bundle carries canonical symplectic geometry without any auxiliary choice.

## Conventions and scope

**Warning.** Some authors define the tautological form with the opposite sign or set \(\omega_{\mathrm{can}}=d\theta\). Either choice is consistent when used throughout. Here \(\theta_{\alpha_x}(v)=\alpha_x(d\pi(v))\) and \(\omega_{\mathrm{can}}=-d\theta\); these two formulas fix both signs. “Liouville form” may also denote related primitives on other [[differential-geometry/exact-symplectic-manifold|exact symplectic manifolds]].

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §1.2, the tautological form and canonical symplectic form on a cotangent bundle.
2. Ralph Abraham and Jerrold E. Marsden, *Foundations of Mechanics*, 2nd ed., Benjamin/Cummings, 1978. [CaltechAUTHORS record](https://authors.library.caltech.edu/records/3n0y2-7wa09). Relevant: cotangent bundles and canonical forms.
