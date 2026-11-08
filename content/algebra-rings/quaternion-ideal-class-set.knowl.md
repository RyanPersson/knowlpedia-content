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

## Ideal classes versus invertible bimodules

An invertible \((\mathcal O,\mathcal O)\)-[[algebra-modules/bimodule|bimodule]] \(M\) has another such bimodule \(N\) with
\[
M\otimes_{\mathcal O}N\cong\mathcal O,
\qquad N\otimes_{\mathcal O}M\cong\mathcal O
\]
as bimodules. Their bimodule-isomorphism classes form a group under tensor product. For an order over a commutative base \(R\), one may require the two \(R\)-actions to coincide and use \(R\)-central bimodules throughout. This is a different equivalence relation and a different collection of objects from right ideal classes.

In particular, a full right ideal may be invertible between its left order \(\mathcal O_L(I)\) and its right order \(\mathcal O\), without being an invertible \((\mathcal O,\mathcal O)\)-bimodule. The [[algebra-rings/quaternion-fractional-ideal|example \(J=hM_2(\mathbb Z)\)]] has \([J]=[\mathcal O]\) as a right ideal class, but \(\mathcal OJ\ne J\). That failure concerns equality of ideals; by itself it is not a proof of failure of a law on equivalence classes. The underlying issue for a proposed tensor law is that right-module isomorphism classes do not specify compatible left actions.

For two-sided invertible fractional ideals with both orders fixed, [[algebra-rings/ideal-tensor-multiplication-isomorphism|multiplication agrees with tensor product]]. For compatible ideals between varying orders, composition likewise works, with inverses returning to the appropriate order. Neither construction generally supplies an ordinary multiplication law on all of \(\operatorname{Cls}_R(\mathcal O)\). A class set with one element, such as that of the Hurwitz order, of course admits the trivial group structure; this does not make its one-sided ideal arithmetic commutative.

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), Definitions 17.3.1 and 17.3.4, Remarks 17.3.5–17.3.6, Main Theorem 17.7.1, and §11.3 for the Hurwitz order.
