+++
id = "differential-geometry/parametric-transversality-theorem"
title = "Parametric transversality theorem"
kind = "theorem"
summary = "A smooth family transverse to a submanifold has transverse members for almost every parameter."
aliases = ["transversality theorem with parameters", "parametric Sard theorem"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-manifold", "differential-geometry/embedded-submanifold", "fiber-bundles/smooth-map", "differential-geometry/map-transverse-to-a-submanifold"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M,P,N\) be finite-dimensional, second-countable
[[fiber-bundles/smooth-manifold|smooth manifolds]] without boundary, let
\(S\subseteq N\) be an
[[differential-geometry/embedded-submanifold|embedded submanifold]], and let
\(F:M\times P\to N\) be a [[fiber-bundles/smooth-map|smooth map]]. Write
\(F_p(x)=F(x,p)\). The
**parametric transversality theorem** states that if \(F\) is
[[differential-geometry/map-transverse-to-a-submanifold|transverse to \(S\)]], then \(F_p\) is transverse to \(S\) for almost every \(p\in P\).
Equivalently, the exceptional parameters form a measure-zero subset in every
coordinate chart of \(P\). In particular, every nonempty open subset of \(P\)
contains a parameter whose slice is transverse.

## Reduction to Sard's theorem

Transversality makes \(Z=F^{-1}(S)\) an embedded submanifold of the
[[differential-geometry/product-manifold|product manifold]] \(M\times P\).
For the restricted projection \(\pi:Z\to P\), a parameter \(p\) is a regular
value exactly when \(F_p\pitchfork S\). The conclusion therefore follows by
applying [[differential-geometry/sards-theorem|Sard's theorem]] to \(\pi\).

## Consequences and examples

If \(S=\{y\}\), the theorem says that almost every member of a family is
transverse to the point \(y\), hence has \(y\) as a
[[fiber-bundles/regular-value|regular value]]. Translation
families in [[linear-algebra/euclidean-space|Euclidean space]] give a standard application: once the total
evaluation map is a submersion, almost every translate meets a fixed
submanifold transversely.

The theorem is a principal device for turning an adjustable finite-dimensional
parameter into a generic geometric position.

## Conventions and scope

**Warning.** The hypothesis concerns the total map \(F\), not each slice.
The theorem guarantees an almost-everywhere, hence dense, set of good
parameters; openness of that set needs additional compactness and closedness
hypotheses. Versions for manifolds with boundary or corners require
transversality on the relevant strata. Infinite-dimensional parameter spaces
belong to a different transversality theory.

## References

1. Victor Guillemin and Alan Pollack, *Differential Topology*, AMS Chelsea Publishing, 2010 reprint. [DOI record](https://doi.org/10.1090/chel/370). Relevant: Chapter 2, the transversality theorem with parameters.
2. Morris W. Hirsch, *Differential Topology*, Graduate Texts in Mathematics 33, Springer, 1976. [DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 3, parametric transversality and Sard's theorem.
