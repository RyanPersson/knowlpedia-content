+++
id = "fiber-bundles/line-bundle"
title = "Line bundle"
kind = "definition"
summary = "A real or complex vector bundle whose fibers have dimension one over the chosen scalar field."
aliases = ["real line bundle", "complex line bundle", "rank-one vector bundle"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/vector-bundle", "fiber-bundles/rank-of-a-vector-bundle", "fiber-bundles/local-trivialization", "linear-algebra/linear-map", "fiber-bundles/transition-function"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\mathbb F\) be \(\mathbb R\) or \(\mathbb C\). An \(\mathbb F\)-**line bundle** over a [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\) is a [[fiber-bundles/vector-bundle|vector bundle]] \(L\to M\) whose [[fiber-bundles/rank-of-a-vector-bundle|rank]] over \(\mathbb F\) is one. Thus every fiber \(L_x\) is a one-dimensional \(\mathbb F\)-vector space, and [[fiber-bundles/local-trivialization|local trivializations]] identify \(L|_U\) with \(U\times\mathbb F\) by fiberwise [[linear-algebra/linear-map|linear maps]]. Its [[fiber-bundles/transition-function|transition functions]] take values in \(\mathbb F^\times\). “Real” or “complex” must be specified because the scalar field changes both the structure group and the classification theory.

## Basic properties

A line bundle is trivial exactly when it admits a nowhere-vanishing [[fiber-bundles/section-of-a-fiber-bundle|global section]]: such a section is a basis in every fiber and hence a global frame.

The [[fiber-bundles/dual-vector-bundle|dual]] \(L^*\) and the [[fiber-bundles/tensor-product-vector-bundle|tensor product]] \(L\otimes K\) are again line bundles. The evaluation isomorphism \(L\otimes L^*\cong M\times\mathbb F\) makes dualization the inverse operation under tensor product. Isomorphism classes of line bundles therefore form an [[algebra-groups/abelian-group|abelian group]], often called a Picard group.

Over a paracompact space, complex line bundles are classified by their first Chern class in \(H^2(M;\mathbb Z)\). Real line bundles are classified by their first [[fiber-bundles/stiefel-whitney-class|Stiefel–Whitney class]] in \(H^1(M;\mathbb Z/2)\).

## Examples and non-examples

The product \(M\times\mathbb F\) is the trivial line bundle. The Möbius bundle over the circle is a nontrivial real line bundle. The tautological bundles over real and complex [[algebraic-geometry-foundations/projective-space|projective spaces]] are the canonical nontrivial examples in their respective categories.

A rank-two real vector bundle is not a real line bundle, even if it can be regarded fiberwise as a one-dimensional complex [[linear-algebra/vector-space|vector space]]: calling it a complex line bundle requires a smoothly varying complex structure and complex-linear transition functions.

The [[fiber-bundles/zero-section|zero section]] exists in every vector bundle but does not trivialize a line bundle, because it is nowhere nonzero.

## Conventions and scope

In algebraic geometry, “line bundle” usually means a locally free sheaf of rank one or its corresponding algebraic vector bundle. The present definition is smooth. Topological line bundles use continuous rather than smooth local trivializations.

## References

1. D. Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-4008-0). Relevant: chapters 1 and 3, vector bundles, line bundles, and classifying constructions.
2. J. W. Milnor and J. D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: chapter 1, real and complex vector bundles and their basic characteristic classes.
