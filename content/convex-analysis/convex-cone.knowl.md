+++
id = "convex-analysis/convex-cone"
title = "Convex cone"
kind = "definition"
summary = "A nonempty set closed under nonnegative linear combinations of two of its elements."
aliases = []
domains = ["convex-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/vector-space", "convex-analysis/conical-combination", "convex-analysis/convex-set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **convex cone** in a real vector space is a nonempty set \(C\) such that
\[
x,y\in C,\quad a,b\ge0\quad\Longrightarrow\quad ax+by\in C.
\]
Equivalently, it is closed under all finite [[convex-analysis/conical-combination|conical combinations]]. This convention includes \(0\in C\), and it does not require \(C\) to be topologically closed.

## Examples and convention

The nonnegative coordinate orthant and the positive semidefinite matrices are convex cones. The strictly positive orthant is convex and invariant under positive scaling, but excludes zero. It is often called an open cone; adjoining zero makes it a convex cone in the convention above.

## References

- [Boyd and Vandenberghe, Convex Optimization, §2.1 (convex cones)](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf).
