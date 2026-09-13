+++
id = "linear-algebra/unit-vector"
title = "Unit vector"
kind = "definition"
summary = "A vector of norm one and the normalization of a nonzero vector."
aliases = ["normalized vector", "unit vectors"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **unit vector** in a [[linear-algebra/normed-vector-space|normed vector space]] is a vector \(v\) satisfying \(\|v\|=1\). If \(w\ne0\), then
\[
\widehat w=\frac{w}{\|w\|}
\]
is a unit vector. Normalization is undefined at the zero vector.

## Euclidean interpretation

In a real inner-product space, the condition is \(v\cdot v=1\). Unit vectors identify directions; an [[linear-algebra/orthonormal-basis|orthonormal basis]] consists of unit vectors that are pairwise perpendicular. The set of all unit vectors is the [[linear-algebra/unit-sphere|unit sphere]].

## References

- [Sheldon Axler, Linear Algebra Done Right, 4th ed., Chapters 2–3, 6 and 9](https://linear.axler.net/LADR4e.pdf).
