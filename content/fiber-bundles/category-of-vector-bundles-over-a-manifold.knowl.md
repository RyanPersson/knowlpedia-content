+++
id = "fiber-bundles/category-of-vector-bundles-over-a-manifold"
title = "Category of vector bundles over a manifold"
kind = "definition"
summary = "The fixed-base category of finite-rank vector bundles whose morphisms cover the identity of the base."
aliases = ["Vect of M", "fixed-base vector-bundle category", "category of bundles over M"]
domains = ["fiber-bundles", "category-theory"]
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/vector-bundle-morphism", "topology/connected-component", "fiber-bundles/bundle-isomorphism"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Fix a finite-dimensional Hausdorff second-countable smooth manifold \(M\) and
\(\mathbb F\in\{\mathbb R,\mathbb C\}\). The **category of finite-rank
smooth \(\mathbb F\)-vector bundles over \(M\)**, denoted
\(\mathbf{Vect}_{\mathbb F}(M)\), has smooth finite-rank
[[fiber-bundles/vector-bundle|\(\mathbb F\)-vector bundles]]
\(E\to M\) as objects. A morphism \(E\to F\) is a smooth
[[fiber-bundles/vector-bundle-morphism|vector-bundle morphism]] whose base
map is exactly \(\operatorname{id}_M\).

The house convention is that \(M\) has no boundary. If \(M\) is disconnected,
the rank may be any finite locally constant function on \(M\); it need not be
bounded across all [[topology/connected-component|connected components]].

Composition is composition of total-space maps. Fiberwise addition and scalar
multiplication make each morphism set an \(\mathbb F\)-vector space, and
direct sum gives a biproduct. [[fiber-bundles/bundle-isomorphism|Bundle isomorphisms]] over \(M\) are precisely the
isomorphisms in this category.

## Why the base is fixed

A general vector-bundle morphism may cover a smooth map \(f:M\to N\). Such
morphisms belong to a larger varying-base category. They cannot all be
placed in \(\mathbf{Vect}_{\mathbb F}(M)\), because their source and target
have different bases.

The fixed-base convention is essential for the
[[fiber-bundles/serre-swan-theorem|Serre–Swan equivalence]]. A map
\(\Phi:E\to F\) over \(\operatorname{id}_M\) sends a section \(s\) to
\(\Phi\circ s\) and thereby gives a \(C^\infty(M,\mathbb F)\)-linear map.
If \(\Phi\) covers a nonidentity map, postcomposition does not have this
source and target and is not a homomorphism between [[fiber-bundles/module-of-smooth-sections|section modules]] over one
fixed ring.

## Sheaf formulation

Taking local sections defines a covariant functor from
\(\mathbf{Vect}_{\mathbb F}(M)\) to finite-rank locally free
\(C^\infty_M(\mathbb F)\)-module sheaves. This sheaf-level construction is
local and includes arbitrary finite locally constant rank on a disconnected
base.

The global-section Serre–Swan equivalence uses a smaller [[algebra-category-theory/full-subcategory|full subcategory]] when
\(M\) is disconnected. Write
\[
\mathbf{Vect}^{\mathrm{bd}}_{\mathbb F}(M)
\subseteq \mathbf{Vect}_{\mathbb F}(M)
\]
for bundles whose ranks are globally bounded across the connected
components. These, and only these, correspond to finitely generated
projective \(C^\infty(M,\mathbb F)\)-modules. For connected \(M\), the two
bundle categories agree.

## References

1. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: vector bundles, bundle maps, and direct sums.
2. Jet Nestruev, *Smooth Manifolds and Observables*, Springer, 2003. [DOI record](https://doi.org/10.1007/b98871). Relevant: Chapter 11, vector bundles and projective modules.
