+++
id = "algebraic-geometry-foundations/algebraic-space"
title = "Algebraic space"
kind = "definition"
summary = "An étale sheaf admitting a representable diagonal and a surjective étale atlas by a scheme."
aliases = ["algebraic space"]
domains = ["algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/etale-morphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(S\) be a scheme. An **algebraic space** over \(S\) is a sheaf \(X\) on
the big étale site of \(S\) such that:

1. the diagonal \(X\to X\times_SX\) is representable by schemes; and
2. there is a scheme \(U\) and a representable, surjective
   [[algebraic-geometry-foundations/etale-morphism|étale morphism]]
   \(U\to X\).

The map \(U\to X\) is an **étale atlas**. Every scheme defines an algebraic
space by its functor of points, but an algebraic space need not be a scheme.

## Quotients

Algebraic spaces allow many étale equivalence relations to have geometric
quotients even when the quotient is not a scheme. They also provide the
representability class used for diagonals of
[[algebraic-geometry-foundations/algebraic-stack|algebraic stacks]].

## References

1. The Stacks Project Authors, “Algebraic Spaces,”
   [chapter](https://stacks.math.columbia.edu/book.pdf#spaces).
