+++
id = "catalog/relationships/triality-magic-square-decomposition"
title = "Triality decomposition of the magic square"
kind = "theorem"
summary = "A symmetric vector-space presentation using two triality algebras and three tensor copies."
aliases = ["Triality decomposition of the magic square"]
domains = ["catalog", "lie-groups", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/relationships/vinberg-magic-square-construction", "catalog/relationships/triality-algebra", "lie-groups/lie-subalgebra"]
dependency_heuristic = "catalog-semantic-author-review-v1"
dependency_review_count = 1
+++

For real division composition algebras \(A,B\), the [[catalog/relationships/vinberg-magic-square-construction|magic-square Lie algebra]] admits the decomposition
\[
\mathfrak M(A,B)\cong\operatorname{tri}(A)\oplus
\operatorname{tri}(B)\oplus(A\otimes_{\mathbb R}B)^{\oplus3}
\]
as real vector spaces, with the two [[catalog/relationships/triality-algebra|triality algebras]] forming commuting [[lie-groups/lie-subalgebra|Lie subalgebras]]. Their three components act on the three tensor copies; the brackets among these copies couple the summands.

## Reading the dimensions

Writing \(t(A)=\dim\operatorname{tri}(A)\), this gives
\[
\dim\mathfrak M(A,B)=t(A)+t(B)+3\dim(A)\dim(B).
\]
The values \(t=0,2,9,28\) produce all sixteen dimensions of the compact square. In particular the octonion–octonion entry has dimension \(28+28+3\cdot64=248\).

## Lie sums versus vector sums

The tensor summands are not commuting Lie ideals. Replacing the construction bracket with a componentwise direct-sum bracket would destroy the exceptional algebras. Compare the genuine [[catalog/relationships/su3-direct-sum-su3|direct sum at the complex–complex entry]].

## References

1. C. H. Barton and A. Sudbery, “Magic squares and matrix models of Lie algebras,” §4.3, Theorem 4.4 and equations (4.22)–(4.26), pp. 21–22. [Paper](https://arxiv.org/pdf/math/0203010).
