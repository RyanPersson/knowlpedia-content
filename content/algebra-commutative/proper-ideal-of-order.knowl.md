+++
id = "algebra-commutative/proper-ideal-of-order"
title = "Proper fractional ideal of an order"
kind = "definition"
summary = "A fractional ideal is proper for an order when that order is its entire multiplier ring."
aliases = ["proper fractional ideal", "proper ideal of an order"]
domains = ["algebra-commutative"]
section_mode = "progressive"
prerequisites = ["algebra-rings/order-in-algebra", "algebra-commutative/fractional-ideal", "algebra-commutative/multiplier-ring"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(\mathcal O\) be an [[algebra-rings/order-in-algebra|order]] in a [[algebra-fields-galois/number-field|number field]]. A [[algebra-commutative/fractional-ideal|fractional ideal]] \(I\) of \(\mathcal O\) is **proper for \(\mathcal O\)** if its [[algebra-commutative/multiplier-ring|multiplier ring]] satisfies
\[
(I:I)=\mathcal O.
\]

Here “proper” records the exact ring of scalars preserving \(I\). It does not mean \(I\subsetneq\mathcal O\); in particular \(\mathcal O\) itself is proper in this sense.

## Invertibility

Every [[algebra-commutative/invertible-fractional-ideal|invertible fractional ideal]] is proper, by multiplying \(xI\subseteq I\) by its inverse. For orders in quadratic number fields, the converse holds as well. This equivalence is special to the quadratic-order setting and should not be used for arbitrary higher-degree orders.

## Example

For \(\mathcal O=\mathbb Z[\sqrt{-3}]\), the ideal \(I=(2,1+\sqrt{-3})\) has multiplier ring \(\mathbb Z[(1+\sqrt{-3})/2]\), so it is not proper for \(\mathcal O\). As an ideal of the larger ring, it is principal and proper.

## References

1. Andrew Sutherland, [MIT 18.783 Lecture 18](https://math.mit.edu/classes/18.783/2019/LectureNotes18.pdf), §18.3 and Theorem 18.10, imaginary quadratic orders.
2. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), Exercise 16.16(b), properness and invertibility for quadratic orders.
