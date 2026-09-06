+++
id = "differential-geometry/immersed-submanifold"
title = "Immersed submanifold"
kind = "definition"
summary = "An immersed submanifold is a manifold equipped with an injective immersion into an ambient smooth manifold."
aliases = ["injectively immersed submanifold"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/smooth-immersion"]
dependency_heuristic = "semantic-curriculum-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]]. An **immersed submanifold** of \(M\) is a smooth manifold \(S\) together with an injective [[fiber-bundles/smooth-immersion|smooth immersion]] \(\iota:S\to M\). Thus each differential \(d\iota_s:T_sS\to T_{\iota(s)}M\) is injective, but the topology and smooth structure on \(S\) are part of the data and need not be induced from \(M\). When \(\iota\) is understood, one often identifies \(S\) set-theoretically with \(\iota(S)\), while retaining its given manifold topology. Its codimension is \(\dim M-\dim S\).

## Local form

The constant-rank theorem implies that near each \(s\in S\), there are coordinates on \(S\) and \(M\) in which
\[
\iota(x^1,\ldots,x^k)=(x^1,\ldots,x^k,0,\ldots,0).
\]
Consequently every immersion is locally an embedding near each source point. This statement is source-local: distinct pieces of the source may accumulate in or pass through the same ambient region.

## Comparison with embedded submanifolds

An injective immersion is an embedding exactly when it is a homeomorphism onto its image with the [[topology/subspace-topology|subspace topology]]. Hence every [[differential-geometry/embedded-submanifold|embedded submanifold]] is immersed, but not conversely. Proper injective immersions are embeddings.

## Examples and conventions

For irrational \(\alpha\), the map
\[
t\longmapsto (e^{it},e^{i\alpha t})
\]
injectively immerses \(\mathbb{R}\) as a dense subset of the two-torus. It is not an embedding because its source topology is not the subspace topology of the dense image.

**Warning.** Some authors allow a noninjective immersion and call its image an immersed submanifold. Under the convention here, a figure-eight immersion is an immersed image but not an immersed submanifold.

## References

1. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2013. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapters 4–5.
2. M. W. Hirsch, *Differential Topology*, Springer, 1976. [DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 1.
