+++
id = "algebra-rings/maximal-order"
title = "Maximal order"
kind = "definition"
summary = "An order contained in no strictly larger order over the same base in the same algebra."
aliases = ["maximal order", "maximal R-order", "maximal Z-order"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/order-in-algebra"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

An \(R\)-[[algebra-rings/order-in-algebra|order]] \(\mathcal O\) in an algebra \(A\) is **maximal** if every \(R\)-order \(\mathcal O'\) with \(\mathcal O\subseteq\mathcal O'\subseteq A\) equals \(\mathcal O\).

The base ring and ambient algebra are fixed. Maximality is with respect to inclusion among orders, not among all subrings of \(A\).

## Number fields

For a number field \(K\), its [[algebra-fields-galois/ring-of-integers|ring of integers]] \(\mathcal O_K\) is the unique maximal \(\mathbb Z\)-order: every order consists of [[algebra-fields-galois/algebraic-integer|algebraic integers]], and \(\mathcal O_K\) is itself a [[algebra-modules/full-lattice|full lattice]].

An order in \(K\) is a [[algebra-commutative/dedekind-domain|Dedekind domain]] exactly when it equals \(\mathcal O_K\). Every such order is Noetherian of dimension one; the missing condition for a nonmaximal order is integral closedness.

## Noncommutative algebras

Maximal orders need not be unique as embedded subrings. For example, \(M_2(\mathbb Z)\) and \(gM_2(\mathbb Z)g^{-1}\), with \(g=\operatorname{diag}(2,1)\), are distinct maximal orders in \(M_2(\mathbb Q)\).

To see maximality of \(M_2(\mathbb Z)\), an overorder containing a matrix \(x\) also contains \(E_{ai}xE_{ja}=x_{ij}E_{aa}\). Each rational coefficient \(x_{ij}\) must be integral over \(\mathbb Z\), hence an integer. Conjugation preserves maximality.

The number of conjugacy classes of maximal orders is a [[algebra-rings/quaternion-type-number|type number]] in the quaternion setting.

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), Definition 10.4.1 and §10.5.
