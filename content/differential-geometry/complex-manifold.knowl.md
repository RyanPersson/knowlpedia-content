+++
id = "differential-geometry/complex-manifold"
title = "Complex manifold"
kind = "definition"
summary = "A space locally modeled on complex Euclidean space with holomorphic transition maps."
aliases = ["holomorphic manifold", "complex-manifold structure", "complex structure on a manifold"]
domains = ["differential-geometry", "topology"]
prerequisites = []
dependency_review_count = 1
section_mode = "progressive"
+++

A **complex manifold of complex dimension \(n\)** is a Hausdorff, second-countable space covered by coordinate charts \(\varphi_i:U_i\to V_i\subseteq\mathbb C^n\) such that each transition map \(\varphi_j\circ\varphi_i^{-1}\) is [[differential-geometry/holomorphic-map|holomorphic]] wherever it is defined.

“Holomorphic manifold” is a synonym, not a separate kind of object. The adjective “complex” describes the coordinate structure; it does not mean merely that the underlying topological space or tangent spaces have been complexified.

## Underlying smooth and almost-complex structures

Holomorphic transition maps are smooth as maps of real variables. Forgetting the complex coordinates therefore gives an underlying [[fiber-bundles/smooth-manifold|smooth manifold]] of real dimension \(2n\). The charts also determine an [[differential-geometry/almost-complex-structure|almost-complex structure]] \(J\) on its tangent bundle.

Conversely, an almost-complex structure comes from complex charts exactly when it is [[differential-geometry/integrable-almost-complex-structure|integrable]]. Thus one may equivalently describe a complex manifold as a smooth even-dimensional manifold equipped with an integrable almost-complex structure. The equivalence is supplied by the Newlander–Nirenberg theorem in the smooth category.

## Morphisms

The natural morphisms between complex manifolds are [[differential-geometry/holomorphic-map|holomorphic maps]]. In terms of the underlying almost-complex structures, a smooth map \(f:X\to Y\) is holomorphic exactly when
\[
df\circ J_X=J_Y\circ df.
\]
Complex manifolds and holomorphic maps form the [[differential-geometry/category-of-complex-manifolds|category of complex manifolds]]. Its isomorphisms are [[differential-geometry/biholomorphism|biholomorphisms]], and the automorphisms of one object form its [[differential-geometry/biholomorphism-group|biholomorphism group]].

## Examples and distinctions

Open subsets of \(\mathbb C^n\), complex projective space, complex tori, and the [[complex-analysis/riemann-sphere|Riemann sphere]] are complex manifolds. A real smooth manifold may support several inequivalent complex structures or none at all. A [[differential-geometry/hermitian-manifold|Hermitian manifold]] adds a compatible Riemannian metric, while a [[differential-geometry/kahler-manifold|Kähler manifold]] imposes an additional closedness condition on the associated two-form.

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: Chapters 1–2, complex manifolds, almost-complex structures, and holomorphic maps.
2. August Newlander and Louis Nirenberg, “Complex Analytic Coordinates in Almost Complex Manifolds,” *Annals of Mathematics* 65 (1957), 391–404. [DOI record](https://doi.org/10.2307/1970051).
