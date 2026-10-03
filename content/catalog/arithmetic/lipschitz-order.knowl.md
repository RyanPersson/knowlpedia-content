+++
id = "catalog/arithmetic/lipschitz-order"
title = "Lipschitz quaternion order"
kind = "definition"
summary = "Lipschitz quaternion order with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/order-in-algebra", "catalog/arithmetic/rational-hamilton-quaternions"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

The **Lipschitz quaternion order** is the [[algebra-rings/order-in-algebra|integer order]]
\[
L=\mathbb Z\oplus\mathbb Z i\oplus\mathbb Z j\oplus\mathbb Z k
\]
in the [[catalog/arithmetic/rational-hamilton-quaternions|rational Hamilton quaternion algebra]], where \(i^2=j^2=k^2=-1\) and \(ij=k=-ji\). Its multiplication is the inherited quaternion multiplication.

## Integral rather than rational

The additive group is free of rank four and its rational span is the ambient algebra. It is not a rational vector space: for example \(1/2\notin L\). The multiplication table has integral structure constants, so the lattice is closed under products.

## Units and enlargement

The norm-one elements are exactly \(\{\pm1,\pm i,\pm j,\pm k\}\); these form its eight-element unit group. The [[catalog/arithmetic/hurwitz-order|Hurwitz order]] contains \(L\) with index two, so \(L\) is not maximal.

## References

1. [John Voight, Quaternion Algebras, Chapter 11: The Hurwitz order](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_11), §11.1, equation (11.1.1), Lemma 11.1.2 and equation (11.1.3); §11.2.
