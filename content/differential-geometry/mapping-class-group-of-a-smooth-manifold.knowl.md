+++
id = "differential-geometry/mapping-class-group-of-a-smooth-manifold"
title = "Mapping class group of a smooth manifold"
kind = "definition"
summary = "The group of smooth self-diffeomorphisms of a manifold modulo smooth isotopy."
aliases = ["smooth mapping class group", "diffeomorphisms modulo isotopy"]
domains = ["differential-geometry", "topology"]
prerequisites = ["fiber-bundles/smooth-manifold", "differential-geometry/diffeomorphism-group", "differential-geometry/smooth-isotopy", "algebra-groups/normal-subgroup"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]]. Its **smooth mapping class group** is
\[
\operatorname{Mod}^{\mathrm{sm}}(M)
=\operatorname{Diff}(M)/\operatorname{Diff}_0(M),
\]
where \(\operatorname{Diff}(M)\) is the [[differential-geometry/diffeomorphism-group|diffeomorphism group]] and \(\operatorname{Diff}_0(M)\) consists of diffeomorphisms smoothly isotopic to the identity. Equivalently, its elements are smooth self-diffeomorphisms modulo the relation \(f_0\sim f_1\) when they are joined by a [[differential-geometry/smooth-isotopy|smooth isotopy]] through diffeomorphisms. Composition descends to the quotient because the identity isotopy class is a [[algebra-groups/normal-subgroup|normal subgroup]]. Notation and the class of permitted diffeomorphisms must be specified when orientation, boundary, marked points, or support conditions are present.

## Variants

For an oriented manifold, one often replaces \(\operatorname{Diff}(M)\) by the orientation-preserving subgroup. If \(M\) has boundary, \(\operatorname{Diff}(M\mathbin{\mathrm{rel}}\partial M)\) denotes diffeomorphisms fixing the boundary pointwise, while setwise boundary preservation gives a different group. Marked submanifolds may likewise be fixed pointwise or only preserved as sets. These variants are not automatically isomorphic.

## Relation to the topology of the diffeomorphism group

With the standard \(C^\infty\) topology in the compact-manifold setting, the quotient is commonly written \(\pi_0\operatorname{Diff}(M)\): it records the path components and discards higher homotopy information. The full diffeomorphism group retains continuous families inside each component, whereas the mapping class group remembers only which diffeomorphisms cannot be connected by isotopy.

## Examples and scope

For a closed oriented surface \(S_g\), the usual mapping class group is the group of orientation-preserving diffeomorphisms modulo isotopy. In higher dimensions, “mapping class group” may instead be defined using homeomorphisms, [[topology/homotopy-equivalence|homotopy equivalences]], or boundary-relative diffeomorphisms. The category must therefore be read from context.

## References

1. Benson Farb and Dan Margalit, *A Primer on Mapping Class Groups*, Princeton Mathematical Series 49, Princeton University Press, 2012. [DOI record](https://doi.org/10.1515/9781400839049). Relevant: §1.1, mapping classes and surface conventions.
2. Allen Hatcher and Nathalie Wahl, “Stabilization for mapping class groups of 3-manifolds,” *Duke Mathematical Journal* 155 (2010), 205–269. [DOI record](https://doi.org/10.1215/00127094-2010-055). Relevant: §1, mapping class groups as components of boundary-relative diffeomorphism groups.
