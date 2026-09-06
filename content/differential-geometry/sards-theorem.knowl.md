+++
id = "differential-geometry/sards-theorem"
title = "Sard's theorem"
kind = "theorem"
summary = "Sard's theorem states that the critical values of a smooth map between finite-dimensional manifolds form a measure-zero set."
aliases = ["Morse-Sard theorem", "Sard theorem"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/smooth-map", "differential-geometry/critical-value-of-a-smooth-map", "measure-theory/lebesgue-measure", "fiber-bundles/regular-value"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) and \(N\) be finite-dimensional, second-countable
[[fiber-bundles/smooth-manifold|smooth manifolds]] without boundary, and let
\(f:M\to N\) be a
[[fiber-bundles/smooth-map|smooth map]]. **Sard's theorem** states that the set
of [[differential-geometry/critical-value-of-a-smooth-map|critical values]] of
\(f\) has measure zero in \(N\): in every smooth coordinate chart of \(N\),
its image has [[measure-theory/lebesgue-measure|Lebesgue measure]] zero.
Consequently, almost every \(y\in N\) is a
[[fiber-bundles/regular-value|regular value]] of \(f\). No measure or volume
form is part of the data; the
measure-zero conclusion is invariant under smooth coordinate changes.

## Differentiability threshold

The smooth hypothesis can be weakened. If \(\dim M=m\), \(\dim N=n\), and
\(f\) is \(C^k\), the Morse-Sard theorem holds when
\[
k>\max\{m-n,0\}.
\]
This threshold is essential in general; lower-regularity maps can have critical
value sets of positive measure.

## Consequences and examples

If the target is nonempty, regular values are dense because a measure-zero
subset cannot contain a coordinate-open set. Combined with the regular-level
set theorem, Sard's theorem produces [[differential-geometry/regular-level-set|regular fibers]] and is the measure-theoretic
engine behind generic transversality arguments.

For a constant map \(M\to N\) with \(\dim N>0\), its single image point is a
critical value and has measure zero. The theorem does not say that the set of
critical points in \(M\) is small.

## Conventions and scope

**Warning.** “Almost every” here is a chartwise null-set statement, not a
claim relative to a chosen [[probability/probability-measure|probability measure]]. Manifolds with boundary can
be treated by extension or by applying the theorem separately to boundary
strata, but the core states the boundaryless form. Infinite-dimensional
manifolds require different regular-value theorems and are not covered.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 6, Sard's theorem and regular values.
2. Victor Guillemin and Alan Pollack, *Differential Topology*, AMS Chelsea Publishing, 2010 reprint. [DOI record](https://doi.org/10.1090/chel/370). Relevant: Chapter 1, Sard's theorem and its applications.
