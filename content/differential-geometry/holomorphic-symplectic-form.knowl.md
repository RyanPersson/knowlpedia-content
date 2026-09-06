+++
id = "differential-geometry/holomorphic-symplectic-form"
title = "Holomorphic symplectic form"
kind = "definition"
summary = "A closed holomorphic two-form that is nondegenerate at every point of a complex manifold."
aliases = ["complex symplectic form", "nondegenerate closed holomorphic 2-form"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/complex-manifold", "differential-geometry/holomorphic-section", "differential-geometry/holomorphic-cotangent-bundle", "fiber-bundles/bundle-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a [[differential-geometry/complex-manifold|complex manifold]]. A **holomorphic symplectic form** on \(X\) is a [[differential-geometry/holomorphic-section|holomorphic section]]
\[
\sigma\in H^0\left(X,\bigwedge\nolimits^2T^{*1,0}X\right)
\]
of the second exterior power of the [[differential-geometry/holomorphic-cotangent-bundle|holomorphic cotangent bundle]] such that \(d\sigma=0\) and \(\sigma\) is pointwise nondegenerate. Nondegeneracy means that the [[fiber-bundles/bundle-map|bundle map]] \(T^{1,0}X\to T^{*1,0}X\), \(v\mapsto\sigma(v,\mathord{-})\), is an isomorphism. Thus closedness is a differential condition and nondegeneracy is a fiberwise linear-algebra condition; both are part of the definition adopted here.

## Immediate consequences

The complex dimension of \(X\) must be even, say \(2m\), and
\[
\sigma^m=\underbrace{\sigma\wedge\cdots\wedge\sigma}_{m\ \mathrm{factors}}
\]
is a nowhere-vanishing holomorphic section of the canonical bundle. Hence a holomorphic symplectic form canonically trivializes that bundle. The inverse bivector \(\sigma^{-1}\) is holomorphic, and the equation \(d\sigma=0\) is equivalent to its Poisson bracket satisfying the Jacobi identity.

Writing \(\sigma=\alpha+i\beta\) as real forms on the underlying [[fiber-bundles/smooth-manifold|smooth manifold]] produces two closed, nondegenerate real \(2\)-forms. Therefore both \(\alpha\) and \(\beta\) are symplectic forms, although neither alone records the full holomorphic structure.

## Canonical example

If \(Y\) is a complex manifold, the total space of its holomorphic cotangent bundle has a tautological holomorphic \(1\)-form \(\theta\). In local coordinates \((z^i,\xi_i)\),
\[
\theta=\sum_i\xi_i\,dz^i,
\qquad
\sigma=d\theta=\sum_i d\xi_i\wedge dz^i.
\]
This \(\sigma\) is closed and nondegenerate, so it is a holomorphic symplectic form.

## A decisive near-miss

On \(\mathbb C^4\), the holomorphic form
\[
\tau=dz^1\wedge dz^2+e^{z^1}dz^3\wedge dz^4
\]
is nondegenerate everywhere, but
\[
d\tau=e^{z^1}dz^1\wedge dz^3\wedge dz^4\neq0.
\]
It is therefore a nondegenerate holomorphic \(2\)-form but not a holomorphic symplectic form under the closedness convention.

## References

1. Daniel Huybrechts, “Compact Hyperkähler Manifolds: Basic Results,” *Inventiones Mathematicae* 135 (1999), 63–113. [DOI record](https://doi.org/10.1007/s002220050280). Relevant: §1, holomorphic symplectic forms and irreducible symplectic manifolds.
2. Arnaud Beauville, “Holomorphic Symplectic Geometry: A Problem List,” in *Complex and Differential Geometry*, Springer Proceedings in Mathematics 8, 2011. [Author-hosted paper](https://math.univ-cotedazur.fr/~beauvill/pubs/Pbsymp.pdf). Relevant: §1.1, basic definitions and canonical forms.
