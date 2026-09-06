+++
id = "differential-geometry/complex-atlas"
title = "Complex atlas"
kind = "definition"
summary = "A covering family of complex coordinate charts whose transition maps are holomorphic."
aliases = ["holomorphic atlas", "complex analytic atlas"]
domains = ["differential-geometry"]
prerequisites = ["topology/topological-manifold", "differential-geometry/complex-coordinate-chart", "shared-foundations/equivalence-class", "differential-geometry/holomorphic-map"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
section_mode = "progressive"
+++

Let \(M\) be a Hausdorff, second-countable [[topology/topological-manifold|topological manifold]] of real dimension \(2n\). A **complex atlas of complex dimension \(n\)** on \(M\) is a family of [[differential-geometry/complex-coordinate-chart|complex coordinate charts]] \(\{(U_\alpha,\varphi_\alpha)\}\) whose domains cover \(M\) and such that, whenever \(U_\alpha\cap U_\beta\neq\varnothing\), the transition map
\[
\varphi_\beta\circ\varphi_\alpha^{-1}
\]
is [[differential-geometry/holomorphic-map|holomorphic]] on \(\varphi_\alpha(U_\alpha\cap U_\beta)\). Two complex atlases are equivalent when their union is again a complex atlas. A complex-manifold structure is equivalently an [[shared-foundations/equivalence-class|equivalence class]] of complex atlases, or the unique maximal atlas containing any representative.

## Maximal atlases and equivalence

Every complex atlas is contained in a unique maximal one: add every complex coordinate chart compatible with all charts already present. Two atlases generate the same maximal atlas exactly when their union is compatible. Thus changing to a smaller covering atlas does not change the resulting [[differential-geometry/complex-manifold|complex manifold]].

## Examples and non-examples

The single identity chart on an open subset of \(\mathbb C^n\) is a complex atlas. The standard affine charts on complex [[algebraic-geometry-foundations/projective-space|projective space]] form another. By contrast, a covering by complex coordinate charts is not a complex atlas if even one overlap map is merely smooth but not holomorphic.

## Conventions and scope

Some authors use “complex atlas” only for a maximal atlas; others, as here, allow any compatible covering family and say “maximal complex atlas” when maximality matters. The equivalence-class formulation removes this terminological difference.

## References

1. D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Springer DOI record](https://doi.org/10.1007/b137952). Relevant: §2.1, complex manifolds and holomorphic atlases.
2. O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981. [Springer DOI record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: §1, complex charts and atlases.
