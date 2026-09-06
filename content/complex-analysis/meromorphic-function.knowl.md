+++
id = "complex-analysis/meromorphic-function"
title = "Meromorphic function"
kind = "definition"
summary = "A function holomorphic away from isolated poles, equivalently locally a quotient of holomorphic functions."
aliases = ["meromorphic map to the Riemann sphere"]
domains = ["complex-analysis", "differential-geometry"]
prerequisites = ["complex-analysis/complex-domain"]
dependency_review_count = 1
section_mode = "progressive"
+++

A **meromorphic function** on a [[complex-analysis/complex-domain|domain]] \(D\) is a function holomorphic away from a discrete subset \(P\subset D\) such that every point of \(P\) is a pole. Equivalently, it is locally a quotient \(g/h\) of holomorphic functions with \(h\) not identically zero.

## Riemann-sphere viewpoint

After assigning the value \(\infty\) at each pole, a meromorphic function is the same as a [[differential-geometry/holomorphic-map|holomorphic map]] not identically equal to \(\infty\),
\[
D\longrightarrow\widehat{\mathbb C},
\]
where \(\widehat{\mathbb C}\) is the [[complex-analysis/riemann-sphere|Riemann sphere]]. This formulation extends unchanged to meromorphic functions on Riemann surfaces.

## Algebraic structure

Meromorphic functions on a connected Riemann surface form a field. Zeros and poles carry integer [[complex-analysis/order-of-zero-or-pole|orders]], and the reciprocal of a nonzero meromorphic function exchanges them.

## Warning

A function with an essential singularity is not meromorphic across that point. In several complex variables and algebraic geometry, “meromorphic” has sheaf-theoretic refinements; this knowl records the one-variable notion.

## References

1. Otto Forster, *Lectures on Riemann Surfaces*, Springer, 1981. [Publisher record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: Chapter 1, §§8–10.
