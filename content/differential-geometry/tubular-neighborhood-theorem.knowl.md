+++
id = "differential-geometry/tubular-neighborhood-theorem"
title = "Tubular neighborhood theorem"
kind = "theorem"
summary = "Every embedded submanifold has a neighborhood modeled on a neighborhood of the zero section in its normal bundle."
aliases = ["tubular neighborhood existence theorem"]
domains = ["differential-geometry", "fiber-bundles"]
prerequisites = ["differential-geometry/embedded-submanifold", "fiber-bundles/smooth-manifold", "differential-geometry/tubular-neighborhood", "fiber-bundles/zero-section", "differential-geometry/normal-bundle", "fiber-bundles/diffeomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(S\subseteq M\) be an [[differential-geometry/embedded-submanifold|embedded submanifold]] of a [[fiber-bundles/smooth-manifold|smooth manifold]]. The **tubular neighborhood theorem** states that \(S\) admits a [[differential-geometry/tubular-neighborhood|tubular neighborhood]]: some open neighborhood of the [[fiber-bundles/zero-section|zero section]] in the [[differential-geometry/normal-bundle|normal bundle]] \(\nu(S\subset M)\) is [[fiber-bundles/diffeomorphism|diffeomorphic]] to an open neighborhood of \(S\) in \(M\), and the diffeomorphism restricts to the inclusion on the zero section. No compactness hypothesis on \(S\) is needed; for noncompact \(S\), the allowable radius in the normal directions may vary from point to point.

## Construction idea

Choose a Riemannian metric on \(M\), identify the normal bundle with the [[linear-algebra/orthogonal-complement|orthogonal complement]] of \(TS\) in \(TM|_S\), and apply the [[fiber-bundles/exponential-map|exponential map]] to normal vectors. The [[shared-foundations/inverse-function|inverse function]] theorem gives the required model near each zero vector. A locally finite shrinking argument produces a single open neighborhood on which this map is injective.

## Consequences

After choosing a fiberwise star-shaped domain, the tubular model deformation retracts onto \(S\). It therefore gives a controlled neighborhood with the homotopy type of the submanifold. The theorem is also the starting point for the [[fiber-bundles/thom-isomorphism-theorem|Thom isomorphism]], collar-like constructions away from boundaries, and isotopy extension arguments.

## Scope and refinements

The theorem guarantees existence but not a canonical neighborhood: different metrics and shrinkings give different embeddings. Relative and equivariant versions require compatibility with extra subsets or [[algebra-groups/group-action|group actions]]. For manifolds with boundary, neatness or other boundary conditions are normally imposed so that the tubular model respects the boundary.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 10, tubular neighborhood theorem.
2. Morris W. Hirsch, *Differential Topology*, Springer, 1976. [DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 4, tubular neighborhoods.
