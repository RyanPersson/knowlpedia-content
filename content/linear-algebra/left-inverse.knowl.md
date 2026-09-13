+++
id = "linear-algebra/left-inverse"
title = "Left inverse of a linear map"
kind = "definition"
summary = "A linear map L with LT equal to the identity on the domain of T."
aliases = ["left-inverse"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/linear-map", "shared-foundations/composition", "shared-foundations/injective-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **left inverse** of a [[linear-algebra/linear-map|linear map]] \(T:V\to W\) is a linear map \(L:W\to V\) satisfying \(LT=I_V\). Therefore \(T\) is injective: \(Tv=0\) implies \(v=LTv=0\).

## Rectangular matrices

If a real matrix \(B\) has linearly independent columns, then its Gram matrix \(B^TB\) is invertible and
\[
L=(B^TB)^{-1}B^T
\]
is a left inverse. For complex matrices, use conjugate transpose instead of transpose. The product \(BL\) is the orthogonal projection onto the column space; it is not generally the identity on the larger ambient space.

## Example

The inclusion \(T(x,y)=(x,y,0)\) has left inverse \(L(x,y,z)=(x,y)\). This lets a vector in a two-dimensional moving plane be described by two coordinates even when the ambient space has dimension three.

## References

- [Sheldon Axler, Linear Algebra Done Right, 4th ed., Chapters 2–3, 6 and 9](https://linear.axler.net/LADR4e.pdf).
