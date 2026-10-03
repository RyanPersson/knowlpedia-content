+++
id = "catalog/relationships/vinberg-magic-square-construction"
title = "Vinberg magic-square construction"
kind = "knowl"
summary = "A symmetric construction of a real Lie algebra from two real composition algebras."
aliases = ["Vinberg magic-square construction"]
domains = ["catalog", "lie-groups", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/composition-algebra", "linear-algebra/linear-map", "lie-groups/lie-algebra"]
dependency_heuristic = "catalog-semantic-author-review-v1"
dependency_review_count = 1
+++

The **Vinberg magic-square Lie algebra** of two real unital [[nonassociative-algebra/composition-algebra|composition algebras]] \(A,B\) is
\[
\mathfrak M(A,B)=\operatorname{Der}(A)\oplus\operatorname{Der}(B)
\oplus\mathfrak{sa}_3(A\otimes_{\mathbb R}B),
\]
as a real vector space. Here \(\operatorname{Der}(A)\) consists of [[linear-algebra/linear-map|linear maps]] satisfying \(D(xy)=D(x)y+xD(y)\), with commutator bracket, and \(\mathfrak{sa}_3\) consists of conjugate-skew matrices of trace zero. Tensor multiplication and conjugation act factorwise. The first two summands commute and act entrywise on the last; for matrices \(X,Y\), the remaining bracket is
\[
[X,Y]=(XY-YX)_0+\frac13\sum_{i,j}D_{X_{ij},Y_{ji}},
\qquad Z_0=Z-\frac{\operatorname{tr}Z}{3}I.
\]
For elements of either factor put
\[
D_{a,c}=[L_a,L_c]+[L_a,R_c]+[R_a,R_c],
\]
where \(L_a(x)=ax\), \(R_a(x)=xa\). Extend to tensor arguments bilinearly by
\[
D_{a\otimes b,c\otimes d}
=\langle b,d\rangle D_{a,c}+\langle a,c\rangle D_{b,d},
\qquad \langle x,y\rangle=\operatorname{Re}(x\bar y).
\]
These brackets satisfy the [[lie-groups/lie-algebra|Lie algebra]] axioms.

## Compact inputs

Taking each input from \(\mathbb R,\mathbb C,\mathbb H,\mathbb O\) gives the [[catalog/relationships/compact-freudenthal-magic-square|compact Freudenthal magic square]]. The derivation correction is essential: an uncorrected matrix commutator over octonionic tensor coefficients does not define this construction.

## References

1. C. H. Barton and A. Sudbery, “Magic squares and matrix models of Lie algebras,” §4.2, equations (4.19)–(4.21) and Theorem 4.3, pp. 19–21. [Paper](https://arxiv.org/pdf/math/0203010).
