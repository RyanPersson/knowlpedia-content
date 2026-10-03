+++
id = "algebra-rings/pure-quaternion"
title = "Pure quaternion"
kind = "definition"
summary = "An element of the trace-zero subspace of a quaternion algebra."
aliases = ["pure quaternion", "pure quaternions", "trace-zero quaternion"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-reduced-trace"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

A **pure quaternion** in a [[algebra-rings/quaternion-algebra|quaternion algebra]] \(B\) over a field \(F\) of characteristic different from two is an element with [[algebra-rings/quaternion-reduced-trace|reduced trace]] zero. Their space is
\[
B_0=\ker(\operatorname{trd}:B\to F)
=\{x\in B:\bar x=-x\}.
\]

It has dimension three. In \(B=(a,b)_F\), it is \(Fi\oplus Fj\oplus Fij\), and \(B=F1\oplus B_0\).

## Squares and the norm

For \(x\in B_0\), the reduced characteristic identity gives \(x^2=-\operatorname{nrd}(x)\). In the [[catalog/arithmetic/rational-hamilton-quaternions|rational Hamilton algebra]],
\[
(bi+cj+dk)^2=-(b^2+c^2+d^2).
\]
This is why quadratic-field embeddings there connect to sums of three squares.

## Linear space and Lie algebra

Pure quaternions are not generally closed under multiplication: \(i^2=a\) is scalar. They are closed under the commutator \([x,y]=xy-yx\), because reduced trace is cyclic. The multiplication and the commutator are different algebraic structures.

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), §§2.4 and 5.1, the trace-zero subspace.
2. The coordinate formulas and reduced characteristic identity directly verify the displayed properties.
