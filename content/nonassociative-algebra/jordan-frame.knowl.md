+++
id = "nonassociative-algebra/jordan-frame"
title = "Jordan frame"
kind = "definition"
summary = "A decomposition of the unit of a Euclidean Jordan algebra into pairwise orthogonal primitive idempotents."
aliases = ["complete system of primitive orthogonal idempotents", "Jordan algebra frame"]
domains = ["nonassociative-algebra"]
prerequisites = ["nonassociative-algebra/euclidean-jordan-algebra", "nonassociative-algebra/primitive-jordan-idempotent"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(J\) be a finite-dimensional unital
[[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan algebra]].
A **Jordan frame** is a tuple \((e_1,\ldots,e_r)\) of
[[nonassociative-algebra/primitive-jordan-idempotent|primitive idempotents]]
such that
\[
e_i\circ e_j=0\quad(i\ne j),
\qquad
e_1+\cdots+e_r=1_J.
\]
If the order is irrelevant, the same data may be regarded as the set
\(\{e_1,\ldots,e_r\}\). The number \(r\) is the rank of \(J\).

## Matrix example

In the [[nonassociative-algebra/hermitian-matrix-jordan-algebra|Hermitian
Jordan algebra]] \(H_n(\mathbb K)\), the diagonal matrix units
\[
E_{11},E_{22},\ldots,E_{nn}
\]
form the standard Jordan frame. A frame is the Jordan-algebraic analogue of
an [[linear-algebra/orthonormal-basis|orthonormal basis]] of rank-one projections.

## Why labels matter

An automorphism can fix every \(e_i\), or merely preserve the frame as an
unordered set while permuting its members. These are different stabilizer
conventions. For the [[nonassociative-algebra/exceptional-jordan-algebra|Albert algebra]], the pointwise stabilizer of a labelled
frame is \(\mathrm{Spin}(8)\), whereas the setwise stabilizer can additionally
permute the three idempotents; see
[[nonassociative-algebra/spin8-stabilizer-of-an-albert-algebra-frame|the
frame-stabilizer theorem]].

## References

1. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994, Chapter IV, §2. [Publisher record](https://doi.org/10.1093/oso/9780198534778.001.0001).
2. Kevin McCrimmon, *A Taste of Jordan Algebras*, Springer, 2004, §13.1. [Publisher record](https://doi.org/10.1007/b97489).
