+++
id = "algebra-rings/quaternion-discriminant"
title = "Discriminant of a quaternion algebra"
kind = "definition"
summary = "The product of the finite prime ideals at which a number-field quaternion algebra ramifies."
aliases = ["quaternion algebra discriminant", "discriminant of a quaternion algebra"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-ramification", "algebra-fields-galois/ring-of-integers", "algebra-rings/product-of-ideals"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(B\) be a [[algebra-rings/quaternion-algebra|quaternion algebra]] over a number field \(K\), and let \(\mathcal O_K\) be its [[algebra-fields-galois/ring-of-integers|ring of integers]]. The **discriminant of \(B\)** is the squarefree ideal
\[
\operatorname{disc}(B)=
\prod_{\substack{\mathfrak p\subset\mathcal O_K\\B\text{ ramified at }\mathfrak p}}
\mathfrak p,
\]
where the product runs over finite [[algebra-rings/quaternion-ramification|ramified places]]. The empty product is \(\mathcal O_K\).

## Over the rational numbers

For \(K=\mathbb Q\), one usually writes the positive [[shared-foundations/square-free-integer|squarefree integer]] \(D_B\) generating this ideal. The rational Hamilton algebra has \(D_B=2\), since its ramification set is \(\{2,\infty\}\). The split matrix algebra has \(D_B=1\).

## What it records

The discriminant records finite ramification. It omits real places; the full ramification set is needed to classify quaternion algebras over general number fields.

This invariant belongs to the algebra. The [[algebra-rings/quaternion-order-discriminant|reduced discriminant of an order]] depends on the chosen order, and agrees with the algebra discriminant for [[algebra-rings/maximal-order|maximal orders]].

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), Definition 14.5.4, Remark 14.5.5, and §15.5.
