+++
id = "catalog/algebras/split-quaternions"
title = "Split quaternions H_s"
kind = "definition"
summary = "Catalogue object: Split quaternions H_s; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["algebra-rings/matrix-ring"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **real split quaternion algebra** is \(\mathbb H_s=M_2(\mathbb R)\), with ordinary [[algebra-rings/matrix-ring|matrix multiplication]], conjugation \(\overline X=\operatorname{tr}(X)I_2-X\), and multiplicative [[linear-algebra/quadratic-form|quadratic form]] \(N(X)=\det X\). It is a four-dimensional real associative algebra.

## Quaternion basis

Take
\[
i=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
j=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad k=ij.
\]
Then \(i^2=-1\), \(j^2=k^2=1\), and \(ij=-ji\). In this basis, \(N(a+bi+cj+dk)=a^2+b^2-c^2-d^2\), of signature \((2,2)\).

## Distinction from Hamilton quaternions

The nonzero matrices \(\operatorname{diag}(1,0)\) and \(\operatorname{diag}(0,1)\) multiply to zero. Consequently this algebra is not the [[linear-algebra/quaternion-division-algebra|Hamilton division algebra]]. The split form and \(M_2(\mathbb R)\) have separate construction records joined by a specified isomorphism.

## References

1. [Alberto Elduque, Composition algebras](https://arxiv.org/html/1810.09979), Section 2.1, equation (7); Theorem 2.11 and Corollary 2.12.
