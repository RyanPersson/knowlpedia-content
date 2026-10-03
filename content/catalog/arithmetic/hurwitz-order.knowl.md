+++
id = "catalog/arithmetic/hurwitz-order"
title = "Hurwitz quaternion order"
kind = "definition"
summary = "Hurwitz quaternion order with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-rings"]
section_mode = "progressive"
prerequisites = ["catalog/arithmetic/rational-hamilton-quaternions", "algebra-rings/order-in-algebra"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

The **Hurwitz quaternion order** is the subring
\[
\mathcal O_{\mathrm{Hur}}=\mathbb Z\,1+\mathbb Z i+\mathbb Z j+\mathbb Z\frac{1+i+j+k}{2}
\]
of the [[catalog/arithmetic/rational-hamilton-quaternions|rational Hamilton quaternion algebra]]. Equivalently, its four coordinates in \(1,i,j,k\) are either all integers or all half-integers in \(\mathbb Z+1/2\). It is an [[algebra-rings/order-in-algebra|integer order]], with inherited quaternion multiplication.

## Relationship to Lipschitz quaternions

The [[catalog/arithmetic/lipschitz-order|Lipschitz order]] has index two in this lattice. The Hurwitz order is [[algebra-rings/maximal-order|maximal]] in its rational quaternion algebra. Replacing the displayed last basis vector by \((-1+i+j+k)/2\) gives the same lattice, since the two differ by \(1\).

## Units and scalar caution

Its unit group consists of \(\pm1,\pm i,\pm j,\pm k\) and the sixteen elements \((\pm1\pm i\pm j\pm k)/2\), with independent signs. There are 24 units. The order itself is an infinite ring of additive rank four, not this finite group and not a rational vector space.

## References

1. [John Voight, Quaternion Algebras, Chapter 11: The Hurwitz order](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_11), §11.1, equation (11.1.1), Lemma 11.1.2 and equation (11.1.3); §11.2.
