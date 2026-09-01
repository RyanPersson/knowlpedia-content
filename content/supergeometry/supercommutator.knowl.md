+++
id = "supergeometry/supercommutator"
title = "Supercommutator"
kind = "construction"
summary = "The graded commutator ab - (-1)^(|a||b|)ba in an associative superalgebra."
aliases = ["graded commutator", "super bracket of an associative superalgebra"]
domains = ["supergeometry", "algebra-rings"]
prerequisites = ["supergeometry/superalgebra", "supergeometry/lie-superalgebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\) be an associative [[supergeometry/superalgebra|superalgebra]]. For
homogeneous \(a,b\in A\), their **supercommutator** is
\[
[a,b]_{\mathrm s}
=ab-(-1)^{|a||b|}ba.
\]
It extends bilinearly to all of \(A\). This bracket is graded-skew and
satisfies the super Jacobi identity, so it turns \(A\) into a
[[supergeometry/lie-superalgebra|Lie superalgebra]].

If either element is even, this is the usual commutator. If both are odd, then
\[
[a,b]_{\mathrm s}=ab+ba,
\]
so their supercommutator is their ordinary anticommutator.

## References

1. M. Scheunert, *The Theory of Lie Superalgebras*, Lecture Notes in
   Mathematics 716, Springer, 1979. [Publisher
   record](https://doi.org/10.1007/BFb0073442). Relevant: Chapter 1.
2. I. M. Musson, *Lie Superalgebras and Enveloping Algebras*, American
   Mathematical Society, 2012. [Publisher
   record](https://doi.org/10.1090/gsm/131). Relevant: Chapter 1.
