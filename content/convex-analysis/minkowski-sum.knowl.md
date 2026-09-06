+++
id = "convex-analysis/minkowski-sum"
title = "Minkowski sum"
kind = "construction"
summary = "The set obtained by adding every point of one subset of a vector space to every point of another."
aliases = ["set addition", "Minkowski addition"]
domains = ["convex-analysis", "analysis"]
prerequisites = ["linear-algebra/vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For subsets \(A,B\) of a real or complex [[linear-algebra/vector-space|vector space]] \(V\), their
**Minkowski sum** is
\[
A+B=\{a+b:a\in A,\ b\in B\}.
\]
Scalar multiplication is defined similarly by
\(tA=\{ta:a\in A\}\).

## Algebraic properties

Set addition is associative and commutative, and
\(t(A+B)=tA+tB\). It is not a group operation on subsets: cancellation can
fail, and most sets have no additive inverse under Minkowski addition.

## Convexity and neighborhoods

If \(A\) and \(B\) are convex, then \(A+B\) is convex. In a normed vector
space, \(A+B_r\) is the
[[analysis/minkowski-thickening|Minkowski thickening]] of \(A\) by radius
\(r\).

## References

1. Rolf Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd ed., Cambridge University Press, 2014. [DOI record](https://doi.org/10.1017/CBO9781139003858).
