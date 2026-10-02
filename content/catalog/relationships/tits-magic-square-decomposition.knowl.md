+++
id = "catalog/relationships/tits-magic-square-decomposition"
title = "Tits decomposition of the magic square"
kind = "theorem"
summary = "The Jordan-algebra decomposition of a compact magic-square Lie algebra."
aliases = ["Tits decomposition of the magic square"]
domains = ["catalog", "lie-groups", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/relationships/vinberg-magic-square-construction", "nonassociative-algebra/derivation-of-a-jordan-algebra", "lie-groups/lie-subalgebra"]
dependency_heuristic = "catalog-semantic-author-review-v1"
dependency_review_count = 1
+++

For \(A,B\in\{\mathbb R,\mathbb C,\mathbb H,\mathbb O\}\), the [[catalog/relationships/vinberg-magic-square-construction|magic-square Lie algebra]] has a real-vector-space decomposition
\[
\mathfrak M(A,B)\cong\operatorname{Der}(A)\oplus
\operatorname{Der}(H_3(B))\oplus
\bigl(\operatorname{Im}A\otimes_{\mathbb R}H_3(B)_0\bigr).
\]
Here \(H_3(B)\) has Jordan product \(X\circ Y=(XY+YX)/2\), and the subscript \(0\) means trace zero. The first two summands form a commuting [[lie-groups/lie-subalgebra|Lie subalgebra]] and act on the tensor summand by their natural actions. The whole display is a vector-space decomposition; brackets between tensor elements also have components in the derivation summands.

## The real row

Since \(\operatorname{Der}(\mathbb R)=0=\operatorname{Im}\mathbb R\),
\[
\mathfrak M(\mathbb R,B)\cong\operatorname{Der}(H_3(B))
\]
as Lie algebras. Thus the first row records [[catalog/relationships/hermitian-cubic-derivation-algebras|derivations of cubic Hermitian Jordan algebras]].

## Dimension check

If \(a=\dim_{\mathbb R}A\), \(b=\dim_{\mathbb R}B\), then
\[
\dim\mathfrak M(A,B)=\dim\operatorname{Der}(A)
+\dim\operatorname{Der}(H_3(B))+(a-1)(2+3b).
\]
This checks dimensions but does not determine the Lie bracket or its real form.

## References

1. John C. Baez, “The Octonions,” §4.3, the Tits decomposition following Table 5. [Checked section](https://math.ucr.edu/home/baez/octonions/node16.html).
