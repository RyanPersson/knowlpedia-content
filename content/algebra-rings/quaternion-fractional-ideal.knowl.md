+++
id = "algebra-rings/quaternion-fractional-ideal"
title = "Fractional ideal of a quaternion order"
kind = "definition"
summary = "A full lattice stable under left or right multiplication by a specified quaternion order."
aliases = ["fractional quaternion ideal", "right fractional quaternion ideal", "left fractional quaternion ideal"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-order", "algebra-modules/full-lattice"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(B\) be a [[algebra-rings/quaternion-algebra|quaternion algebra]] over a number field \(K\), let \(R=\mathcal O_K\), and let \(\mathcal O\subseteq B\) be an \(R\)-[[algebra-rings/quaternion-order|order]]. A **right fractional \(\mathcal O\)-ideal** is a [[algebra-modules/full-lattice|full \(R\)-lattice]] \(I\subseteq B\) with \(I\mathcal O\subseteq I\). A **left fractional ideal** instead satisfies \(\mathcal OI\subseteq I\).

The side is part of the definition. An ideal need not be contained in \(\mathcal O\); one contained in \(\mathcal O\) is called integral relative to that order.

## Principal ideals

For \(a\in B^\times\), the lattice \(a\mathcal O\) is a principal right fractional ideal, and \(\mathcal Oa\) is a principal left fractional ideal. They need not be the same subset.

Every fractional ideal has a denominator: some nonzero \(d\in R\) satisfies \(dI\subseteq\mathcal O\). This follows by expressing finitely many lattice generators in a fraction-field basis of the order.

## The fullness condition

In a split matrix algebra, a nonzero one-sided ideal in the ring-theoretic sense need not span the full algebra. For example, \(E_{11}M_2(R)\) has only its first row possibly nonzero and is not a full fractional ideal of \(M_2(R)\).

For ideal-class arithmetic one uses [[algebra-rings/locally-principal-quaternion-ideal|locally principal fractional ideals]]. This is different from the commutative definition of a fractional ideal inside a field.

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), Definition 16.2.9 and Remark 16.2.10.
