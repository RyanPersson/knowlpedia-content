+++
id = "differential-geometry/thom-transversality-theorem"
title = "Thom transversality theorem"
kind = "theorem"
summary = "Smooth maps whose jet extensions are transverse to a fixed jet-space submanifold form a residual set."
aliases = ["jet transversality theorem", "Thom jet transversality"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-manifold", "differential-geometry/embedded-submanifold", "differential-geometry/whitney-c-infinity-topology", "differential-geometry/jet-of-a-smooth-map", "differential-geometry/map-transverse-to-a-submanifold"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M,N\) be [[fiber-bundles/smooth-manifold|smooth manifolds]], let \(r\geq0\), and let \(W\) be a [[differential-geometry/embedded-submanifold|smooth submanifold]] of the \(r\)-jet bundle \(J^r(M,N)\). The **Thom transversality theorem** states that
\[
\{f\in C^\infty(M,N):j^rf\pitchfork W\}
\]
is residual, hence dense, in the [[differential-geometry/whitney-c-infinity-topology|Whitney \(C^\infty\) topology]]. Here \(j^rf\) is the [[differential-geometry/jet-of-a-smooth-map|\(r\)-jet extension]] of \(f\), and transversality is understood as [[differential-geometry/map-transverse-to-a-submanifold|transversality of a map to a submanifold]]. If \(W\) is closed, this set is also open.

## Meaning of genericity

A [[topology/residual-set|residual set]] is a countable intersection of open [[topology/dense-set|dense sets]]. Since the Whitney mapping space is a [[topology/baire-space|Baire space]], residual conditions are dense, so every [[fiber-bundles/smooth-map|smooth map]] can be approximated by maps whose \(r\)-jets are transverse to \(W\). The theorem packages many general-position arguments into a single statement about jet extensions.

## Important special cases

For \(r=0\), the jet bundle is \(M\times N\), and choosing \(W=M\times Z\) recovers the ordinary transversality theorem for maps \(M\to N\) transverse to \(Z\subseteq N\). For \(r=1\), choosing rank-defect strata in the first-jet bundle makes the theorem a starting point for the study of generic singularities of smooth maps.

## Scope and cautions

The residual conclusion does not say that every transverse map lies in one prescribed finite-dimensional perturbation family. Parametric transversality supplies that separate statement under its own hypotheses. Openness also needs the stated closedness condition on \(W\); transversality to a nonclosed submanifold can be destroyed by behavior accumulating outside compact subsets.

## References

1. Morris W. Hirsch, *Differential Topology*, Springer, 1976. [Springer DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 2, §4, especially the Jet Transversality Theorem 2.8.
2. Martin Golubitsky and Victor Guillemin, *Stable Mappings and Their Singularities*, Springer, 1973. [Springer DOI record](https://doi.org/10.1007/978-1-4615-7904-5). Relevant: Chapter II, jet transversality and singularity strata.
