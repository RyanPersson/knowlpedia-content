+++
id = "langlands/tame-ramification"
title = "Tame ramification"
kind = "definition"
summary = "Ramification of an etale local system for which wild inertia acts trivially."
aliases = ["tamely ramified local system"]
domains = ["langlands", "algebraic-geometry-foundations"]
prerequisites = ["algebra-fields-galois/valuation-on-a-field", "fiber-bundles/local-system", "langlands/regular-singular-connection"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(K\) be a discretely [[algebra-fields-galois/valuation-on-a-field|valued field]] with inertia subgroup \(I_K\) and wild
inertia subgroup \(P_K\). An étale representation, or the corresponding
étale [[fiber-bundles/local-system|local system]], is **tamely ramified** if
\[
P_K
\]
acts trivially. It may still have nontrivial action of the tame quotient
\(I_K/P_K\).

This étale definition should not be identified with [[langlands/regular-singular-connection|regular singularity]] of a
complex connection without invoking a comparison theorem.

## References

1. Jean-Pierre Serre, *Local Fields*, Graduate Texts in Mathematics 67,
   Springer, 1979, Chapter IV.
