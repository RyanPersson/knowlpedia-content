+++
id = "catalog/arithmetic/rational-hamilton-quaternions"
title = "Rational Hamilton quaternion algebra"
kind = "definition"
summary = "Rational Hamilton quaternion algebra with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-algebra"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

The **rational Hamilton quaternion algebra** is the associative unital [[algebra-rings/quaternion-algebra|quaternion algebra]]
\[
B=(-1,-1)_{\mathbb Q}=\mathbb Q\oplus\mathbb Q i\oplus\mathbb Q j\oplus\mathbb Q k,\qquad i^2=j^2=-1,\quad k=ij=-ji.
\]
Its scalars and four coordinates are rational; multiplication is extended bilinearly from these relations.

## Division and scalar extension

Conjugation negates the \(i,j,k\) coordinates. For \(x=a+bi+cj+dk\), the reduced norm is \(x\bar x=a^2+b^2+c^2+d^2\). It is positive for every nonzero rational coordinate vector, so \(x^{-1}=\bar x/(x\bar x)\); thus this is a division algebra. Extending scalars to \(\mathbb R\) gives Hamilton’s [[linear-algebra/quaternion-division-algebra|real quaternions]].

## Integral structures

The [[catalog/arithmetic/lipschitz-order|Lipschitz order]] and [[catalog/arithmetic/hurwitz-order|Hurwitz order]] are distinct integral subrings whose rational spans equal \(B\). They are not alternative names for this rational algebra.

## References

1. [John Voight, Quaternion Algebras, Chapter 11: The Hurwitz order](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_11), §11.1, equation (11.1.1), Lemma 11.1.2 and equation (11.1.3); §11.2.
