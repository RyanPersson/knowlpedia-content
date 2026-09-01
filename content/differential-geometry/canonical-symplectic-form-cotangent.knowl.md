+++
id = "differential-geometry/canonical-symplectic-form-cotangent"
title = "Canonical symplectic form on a cotangent bundle"
kind = "definition"
summary = "The symplectic form obtained as minus the exterior derivative of the tautological one-form on a cotangent bundle."
aliases = ["cotangent symplectic form"]
domains = ["differential-geometry", "fiber-bundles"]
prerequisites = ["fiber-bundles/smooth-manifold", "differential-geometry/tautological-one-form-cotangent", "fiber-bundles/cotangent-bundle", "fiber-bundles/exterior-derivative", "differential-geometry/symplectic-manifold"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]] and \(\theta\) the [[differential-geometry/tautological-one-form-cotangent|tautological one-form]] on its [[fiber-bundles/cotangent-bundle|cotangent bundle]] \(T^*M\). The **canonical symplectic form** is
\[
\omega_{\mathrm{can}}=-d\theta,
\]
where \(d\) is the [[fiber-bundles/exterior-derivative|exterior derivative]]. It is closed because \(d^2=0\), and it is nondegenerate, so \((T^*M,\omega_{\mathrm{can}})\) is a [[differential-geometry/symplectic-manifold|symplectic manifold]]. This construction is intrinsic: it uses neither a metric nor a connection on \(M\). The displayed sign fixes the convention used throughout this knowl.

## Coordinate expression

For local coordinates \(q^1,\ldots,q^n\) on \(M\) and induced fiber coordinates \(p_1,\ldots,p_n\),
\[
\theta=\sum_i p_i\,dq^i,
\qquad
\omega_{\mathrm{can}}=\sum_i dq^i\wedge dp_i.
\]
This normal form directly shows nondegeneracy. It also explains why cotangent coordinates are the standard position-momentum coordinates of Hamiltonian mechanics.

## Naturality

The [[differential-geometry/cotangent-lift|cotangent lift]] of every [[fiber-bundles/diffeomorphism|diffeomorphism]] of base manifolds preserves \(\theta\), hence preserves \(\omega_{\mathrm{can}}\). In this sense the form is canonical not only because it requires no choices, but also because it is natural under changes of variables.

## Conventions and scope

**Warning.** Some authors take \(\omega_{\mathrm{can}}=d\theta\), or define the tautological form with the opposite sign. The resulting geometry is equivalent after a consistent sign change, but formulas for [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector fields]] and Poisson brackets must use one convention throughout.

## References

1. Ralph Abraham and Jerrold E. Marsden, *Foundations of Mechanics*, 2nd ed., Benjamin/Cummings, 1978. [CaltechAUTHORS record](https://authors.library.caltech.edu/records/3n0y2-7wa09). Relevant: §3.2, canonical forms on cotangent bundles.
2. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §1.2, tautological and canonical symplectic forms.
