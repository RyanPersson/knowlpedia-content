+++
id = "differential-geometry/normal-bundle"
title = "Normal bundle"
kind = "definition"
summary = "The quotient of the ambient tangent bundle along an embedded submanifold by its tangent bundle."
aliases = ["normal vector bundle", "normal bundle of an embedding"]
domains = ["differential-geometry", "fiber-bundles"]
section_mode = "progressive"
prerequisites = ["differential-geometry/embedded-submanifold", "fiber-bundles/vector-subbundle", "fiber-bundles/tangent-bundle", "fiber-bundles/quotient-vector-bundle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(i:S\hookrightarrow M\) be an [[differential-geometry/embedded-submanifold|embedded submanifold]]. The differential of \(i\) identifies \(TS\) with a [[fiber-bundles/vector-subbundle|vector subbundle]] of the restricted [[fiber-bundles/tangent-bundle|tangent bundle]] \(i^*TM=TM|_S\). The **normal bundle** of the embedding is the [[fiber-bundles/quotient-vector-bundle|quotient vector bundle]]
\[
\nu(S\subset M)=TM|_S/TS\longrightarrow S.
\]
Its fiber at \(p\in S\) is \(T_pM/T_pS\), and its rank is the codimension of \(S\) in \(M\). The quotient is intrinsic to the embedding: no metric or choice of complementary subspaces is part of the definition.

## Metric realization

If \(M\) carries a Riemannian metric, the [[linear-algebra/orthogonal-complement|orthogonal complement]]
\[
(TS)^\perp=\{v\in TM|_S:\langle v,w\rangle=0\text{ for all }w\in TS\}
\]
maps isomorphically onto \(\nu(S\subset M)\). This realizes normal classes by normal vectors, but the realization depends on the metric; the quotient bundle does not.

## Tubular neighborhoods

For an embedded submanifold satisfying the usual closedness hypotheses, a neighborhood of the [[fiber-bundles/zero-section|zero section]] in the normal bundle is diffeomorphic to a neighborhood of \(S\) in \(M\). This tubular-neighborhood theorem turns linear normal data into ambient local geometry.

## Examples and non-examples

The normal bundle of the standard sphere \(S^n\subset\mathbb R^{n+1}\) is a trivial [[fiber-bundles/line-bundle|line bundle]], generated after choosing the Euclidean metric by the outward unit normal. An arbitrary complement of \(TS\) in \(TM|_S\) is a model for the normal bundle only when it varies smoothly; a pointwise choice need not form a vector subbundle.

## References

1. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [Springer DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 10, normal bundles and tubular neighborhoods.
2. M. W. Hirsch, *Differential Topology*, Springer, 1976. [Springer DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 4, tubular neighborhoods.
