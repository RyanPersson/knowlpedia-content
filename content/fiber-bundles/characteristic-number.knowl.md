+++
id = "fiber-bundles/characteristic-number"
title = "Characteristic number"
kind = "definition"
summary = "A scalar obtained by evaluating a top-degree product of characteristic classes on a fundamental class."
aliases = ["characteristic class number", "characteristic number of a manifold"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
+++

Let \(M\) be a [[topology/closed-manifold|closed \(R\)-oriented \(n\)-manifold]], let \(E\to M\) be a [[fiber-bundles/vector-bundle|vector bundle]], and let \(P\) be a homogeneous polynomial of total cohomological degree \(n\) in [[fiber-bundles/characteristic-class|characteristic classes]] \(\alpha_i(E)\). The **characteristic number** determined by \(P\) is
\[
\bigl\langle P(\alpha_1(E),\alpha_2(E),\ldots),[M]\bigr\rangle\in R,
\]
where products are taken in the [[topology/cup-product-and-cohomology-ring|cohomology ring]] and \([M]\) is the [[topology/fundamental-class|fundamental class]]. A characteristic number of the manifold usually means one formed from characteristic classes of its [[fiber-bundles/tangent-bundle|tangent bundle \(TM\)]].

## Standard families

[[fiber-bundles/chern-number|Chern numbers]] evaluate degree-\(2n\) monomials in Chern classes on a closed almost-complex \(2n\)-manifold. [[fiber-bundles/pontryagin-number|Pontryagin numbers]] use degree-\(4k\) monomials on an oriented manifold, while Stiefel–Whitney numbers use mod-\(2\) classes and the mod-\(2\) [[topology/fundamental-class|fundamental class]]. The Euler number is
\[
\langle e(E),[M]\rangle
\]
when \(E\) is oriented of rank \(n\).

## Geometric significance

Characteristic numbers are unchanged by [[fiber-bundles/bundle-isomorphism|bundle isomorphisms]] over the identity. For tangent bundles they are invariants under orientation-preserving diffeomorphisms. Stiefel–Whitney numbers determine unoriented cobordism classes, while Pontryagin and Stiefel–Whitney numbers together determine [[differential-geometry/oriented-cobordism|oriented cobordism]] classes [Milnor–Stasheff, chapters 16–17].

## Conventions and scope

The coefficient ring, orientation, bundle, and polynomial are part of the data. Only the component of total degree \(n\) can pair with \([M]\). Mod-\(2\) numbers do not require an orientation, whereas integral Chern, Pontryagin, and Euler numbers use the appropriate integral orientation.

**Warning.** A characteristic class is a cohomology class; a characteristic number is the scalar produced only after a top-degree evaluation.

## References

1. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: chapters 16–17, characteristic numbers and cobordism.
2. Friedrich Hirzebruch, *Topological Methods in Algebraic Geometry*, 3rd ed., Springer, 1966. [DOI record](https://doi.org/10.1007/978-3-642-62018-8). Relevant: characteristic numbers and genera of manifolds.
