+++
id = "differential-geometry/whitney-embedding-theorem"
title = "Whitney embedding theorem"
kind = "theorem"
summary = "Every positive-dimensional smooth manifold embeds smoothly in Euclidean space of twice its dimension."
aliases = ["smooth Whitney embedding theorem"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/smooth-embedding", "differential-geometry/embedded-submanifold", "linear-algebra/euclidean-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a Hausdorff, second-countable [[fiber-bundles/smooth-manifold|smooth manifold]] without boundary and of positive dimension \(n\). The **Whitney embedding theorem** states that there exists a [[fiber-bundles/smooth-embedding|smooth embedding]]
\[
M\hookrightarrow\mathbb R^{2n}.
\]
Consequently every abstract smooth manifold can be realized as an [[differential-geometry/embedded-submanifold|embedded submanifold]] of a finite-dimensional [[linear-algebra/euclidean-space|Euclidean space]], with its original topology and smooth structure. The dimension bound depends only on \(n\), not on compactness or on auxiliary geometric choices. Separate versions handle zero-dimensional manifolds and manifolds with boundary.

## Significance

The theorem permits intrinsic manifold questions to be studied using ambient Euclidean constructions without making Euclidean realization part of the definition of a manifold. Once embedded, \(M\) acquires a [[differential-geometry/normal-bundle|normal bundle]] and admits a [[differential-geometry/tubular-neighborhood|tubular neighborhood]], tools used in transversality, cobordism, and characteristic-class arguments.

## Proof architecture

A weak form first constructs an embedding into a sufficiently large Euclidean space using coordinate charts and a [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]]. Generic linear projections then lower the ambient dimension while avoiding both tangent-direction collapses and coincidences of distinct points. The final \(2n\) bound requires controlling these two bad loci simultaneously.

## Dimension and variants

The bound \(2n\) is a universal [[shared-foundations/upper-bound|upper bound]], not the least embedding dimension of each manifold. Many manifolds embed in smaller spaces, while topology obstructs such embeddings for others. A related Whitney immersion theorem gives an immersion into \(\mathbb R^{2n-1}\) for \(n>1\); an immersion does not by itself identify \(M\) homeomorphically with its image.

## References

1. Morris W. Hirsch, *Differential Topology*, Springer, 1976. [DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 2, Whitney immersion and embedding theorems.
2. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 6, Whitney embedding theorem.
