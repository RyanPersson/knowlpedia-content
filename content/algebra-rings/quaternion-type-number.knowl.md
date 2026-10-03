+++
id = "algebra-rings/quaternion-type-number"
title = "Type number of a quaternion algebra"
kind = "definition"
summary = "The number of conjugacy classes of maximal orders in a number-field quaternion algebra."
aliases = ["quaternion type number", "type number of a quaternion algebra"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/maximal-order", "algebra-rings/quaternion-algebra"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(B\) be a [[algebra-rings/quaternion-algebra|quaternion algebra]] over a [[algebra-fields-galois/number-field|number field]] \(K\), with \(R=\mathcal O_K\). Its **type number** is the number of conjugacy classes of [[algebra-rings/maximal-order|maximal \(R\)-orders]] in \(B\), where
\[
\mathcal O\sim\mathcal O'
\quad\Longleftrightarrow\quad
\mathcal O'=a\mathcal Oa^{-1}\text{ for some }a\in B^\times.
\]

This number is finite. In this setting, conjugacy is equivalent to isomorphism as \(R\)-algebras.

## Compared with class number

The [[algebra-rings/quaternion-ideal-class-set|class number]] of a fixed maximal order counts ideal classes. Type number counts maximal orders. Sending a right ideal class to the conjugacy class of its left order gives a surjection from the former set onto the latter; it need not be injective.

The [[catalog/arithmetic/rational-hamilton-quaternions|rational Hamilton algebra]] has type number one: every maximal order is conjugate to the [[catalog/arithmetic/hurwitz-order|Hurwitz order]]. This does not say that all maximal orders are literally the same subset of the algebra.

## Convention

One can also count types within the genus of a nonmaximal order. This knowl uses the maximal-order type number of the ambient algebra.

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), §17.4, especially Lemma 17.4.13, and Main Theorem 17.7.1.
