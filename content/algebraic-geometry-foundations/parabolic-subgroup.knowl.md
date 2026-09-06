+++
id = "algebraic-geometry-foundations/parabolic-subgroup"
title = "Parabolic subgroup"
kind = "definition"
summary = "A subgroup of a reductive algebraic group whose homogeneous quotient is proper."
aliases = ["parabolic algebraic subgroup", "parabolic subgroup"]
domains = ["algebraic-geometry-foundations", "langlands"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebraic-geometry-foundations/algebraically-closed-field", "algebraic-geometry-foundations/borel-subgroup"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
algebraic group]] over a field \(k\). A smooth closed subgroup \(P\subseteq G\)
is **parabolic** if the quotient \(G/P\) is proper over \(k\).

Over an [[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed field]], this is equivalent to requiring \(P\) to
contain a [[algebraic-geometry-foundations/borel-subgroup|Borel subgroup]].
Every Borel subgroup is therefore parabolic.

## Flag variety

The quotient \(G/P\) is a
[[algebraic-geometry-foundations/flag-variety|flag variety]]. For
\(G=GL_n\), parabolic subgroups are stabilizers of flags of prescribed
dimensions.

## References

1. T. A. Springer, *Linear Algebraic Groups*, 2nd ed., Birkhäuser, 1998,
   Chapter 6. [DOI](https://doi.org/10.1007/978-0-8176-4840-4).
