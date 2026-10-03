+++
id = "algebra-rings/quaternion-ideal-class-set"
title = "Ideal class set of a quaternion order"
kind = "definition"
summary = "Locally principal right fractional ideals modulo left multiplication by an invertible quaternion."
aliases = ["quaternion ideal class set", "quaternion class number", "right ideal class set"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-order", "algebra-rings/locally-principal-quaternion-ideal"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(\mathcal O\) be an [[algebra-rings/quaternion-order|order in a quaternion algebra]] \(B\) over a number field. Write \(\mathcal I_R(\mathcal O)\) for its locally principal right fractional ideals. Its **right ideal class set** is
\[
\operatorname{Cls}_R(\mathcal O)=\mathcal I_R(\mathcal O)/\!\sim,
\qquad I\sim J\iff J=aI\text{ for some }a\in B^\times.
\]

The ideals are [[algebra-rings/locally-principal-quaternion-ideal|locally principal]] relative to the specified right order. The cardinality \(h(\mathcal O)=\#\operatorname{Cls}_R(\mathcal O)\) is its **right class number**; it is finite in this number-field setting.

## Why the scalar acts on the left

Left multiplication by \(a\) gives an isomorphism of right \(\mathcal O\)-modules \(I\to aI\). Conversely such a module isomorphism extends over the fraction field to an isomorphism of right \(B\)-modules, which must be left multiplication by an element of \(B^\times\).

## A pointed set, not generally a group

The class of \(\mathcal O\) is distinguished, but ordinary ideal multiplication does not generally define a group law on these classes. Noncommutative left and right orders must be compatible before multiplying ideal classes. This differs from the commutative [[algebra-commutative/picard-group|Picard group]].

The [[catalog/arithmetic/hurwitz-order|Hurwitz order]] has class number one. Its [[algebra-rings/quaternion-type-number|type number]] also equals one, but type number counts orders rather than ideals.

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), Definitions 17.3.1 and 17.3.4, Remarks 17.3.5–17.3.6, Main Theorem 17.7.1, and §11.3 for the Hurwitz order.
