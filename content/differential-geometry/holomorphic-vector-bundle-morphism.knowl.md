+++
id = "differential-geometry/holomorphic-vector-bundle-morphism"
title = "Holomorphic vector-bundle morphism"
kind = "definition"
summary = "A holomorphic map of vector-bundle total spaces that is linear on fibers and covers a holomorphic base map."
aliases = ["holomorphic bundle map", "analytic vector-bundle morphism"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/holomorphic-vector-bundle", "differential-geometry/holomorphic-map", "fiber-bundles/vector-bundle-morphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\to X\) and \(F\to Y\) be [[differential-geometry/holomorphic-vector-bundle|holomorphic vector bundles]]. A **holomorphic vector-bundle morphism** from \(E\) to \(F\) is a pair \((\Phi,f)\) in which \(f:X\to Y\) and \(\Phi:E\to F\) are [[differential-geometry/holomorphic-map|holomorphic maps]], the projections satisfy \(\pi_F\circ\Phi=f\circ\pi_E\), and each restriction \(\Phi_x:E_x\to F_{f(x)}\) is complex-linear. Thus it is a [[fiber-bundles/vector-bundle-morphism|vector-bundle morphism]] in the smooth category with the additional requirement of holomorphicity. A morphism over \(X\) means \(X=Y\) and \(f=\operatorname{id}_X\).

## Local characterization

In holomorphic trivializations, \(\Phi\) has the form
\[
(x,v)\longmapsto\bigl(f(x),A(x)v\bigr),
\]
where \(A(x)\) is a matrix of holomorphic functions. Conversely, compatible matrices of holomorphic functions define such a morphism. The morphism is an isomorphism exactly when \(f\) is a [[differential-geometry/biholomorphism|biholomorphism]] and every \(A(x)\) is invertible.

## Composition and induced maps

Holomorphic vector bundles and their morphisms form a category under composition. A morphism \(E\to F\) over \(X\) sends local [[differential-geometry/holomorphic-section|holomorphic sections]] of \(E\) to local holomorphic sections of \(F\). Duals, tensor products, direct sums, and exterior powers produce new holomorphic morphisms in the expected covariant or contravariant direction.

## Rank and subbundles

If a morphism over \(X\) has locally constant rank, its kernel and image are holomorphic [[fiber-bundles/vector-subbundle|vector subbundles]], and its cokernel is a holomorphic vector bundle. Without constant rank, these objects generally belong to the category of coherent analytic sheaves rather than locally free bundles; fiberwise kernels alone do not guarantee local triviality.

## References

1. D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: §2.2, morphisms and exact sequences of holomorphic vector bundles.
