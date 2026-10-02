+++
id = "algebra-rings/quaternion-order-discriminant"
title = "Reduced discriminant of a quaternion Z-order"
kind = "definition"
summary = "The positive square root of the absolute determinant of the reduced-trace pairing on an integral basis."
aliases = ["reduced discriminant of a quaternion order", "quaternion order discriminant"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-order", "algebra-rings/quaternion-reduced-trace"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(\mathcal O\) be a \(\mathbb Z\)-[[algebra-rings/quaternion-order|order]] in a quaternion algebra \(B/\mathbb Q\), and let \(e_1,\ldots,e_4\) be a \(\mathbb Z\)-basis. Its **reduced discriminant** is the positive integer
\[
\operatorname{discrd}(\mathcal O)=
\sqrt{\left|\det\bigl(\operatorname{trd}(e_i e_j)\bigr)_{i,j=1}^4\right|},
\]
where \(\operatorname{trd}\) is [[algebra-rings/quaternion-reduced-trace|reduced trace]]. For a quaternion order the determinant has square absolute value, and the result is independent of the integral basis.

## Basis changes and larger orders

A unimodular basis change multiplies the determinant by the square of \(\pm1\), hence leaves it unchanged. If \(\mathcal O\subseteq\mathcal O'\), then
\[
\operatorname{discrd}(\mathcal O)
=[\mathcal O':\mathcal O]\operatorname{discrd}(\mathcal O').
\]
The positive integer is therefore distinct from the determinant itself, whose absolute value is its square.

## Lipschitz and Hurwitz orders

For the [[catalog/arithmetic/lipschitz-order|Lipschitz order]], the basis \(1,i,j,k\) has trace-pairing matrix \(\operatorname{diag}(2,-2,-2,-2)\), so the reduced discriminant is \(4\).

The [[catalog/arithmetic/hurwitz-order|Hurwitz order]] contains it with index two, so its reduced discriminant is \(2\). This equals the [[algebra-rings/quaternion-discriminant|discriminant of the rational Hamilton algebra]]. In general, equality with the algebra discriminant characterizes maximal quaternion \(\mathbb Z\)-orders.

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), §15.1, Definition 15.4.4, Lemma 15.4.7, and Theorem 15.5.5.
