+++
id = "algebra-commutative/multiplier-ring"
title = "Multiplier ring of a fractional ideal"
kind = "definition"
summary = "The overring of fraction-field scalars that preserve a fractional ideal."
aliases = ["multiplier ring", "multiplicator ring", "endomorphism ring of a fractional ideal"]
domains = ["algebra-commutative"]
section_mode = "progressive"
prerequisites = ["algebra-commutative/fractional-ideal"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(I\) be a nonzero [[algebra-commutative/fractional-ideal|fractional ideal]] of a domain \(R\), with [[algebra-rings/fraction-field|fraction field]] \(K\). Its **multiplier ring** is
\[
(I:I)=\{x\in K:xI\subseteq I\}.
\]

It is a subring of \(K\) containing \(R\). Multiplication identifies it with \(\operatorname{End}_R(I)\): an \(R\)-linear endomorphism extends to the one-dimensional \(K\)-vector space \(K\otimes_R I\cong K\), and hence is scalar multiplication.

## Orders

If \(R=\mathcal O\) is an [[algebra-rings/order-in-algebra|order]] in a number field \(K\), then \((I:I)\) is another order containing \(\mathcal O\). To see finiteness, choose \(0\ne a\in I\); then \((I:I)\subseteq a^{-1}I\), a finite integer lattice. It spans \(K\) because it contains \(\mathcal O\).

If \(I\) is [[algebra-commutative/invertible-fractional-ideal|invertible]], multiplying \(xI\subseteq I\) by \(I^{-1}\) gives \(x\mathcal O\subseteq\mathcal O\), so \((I:I)=\mathcal O\).

## A larger multiplier ring

Put \(s=\sqrt{-3}\), \(\omega=(1+s)/2\), \(R=\mathbb Z[s]\), and \(I=(2,1+s)=2\mathbb Z[\omega]\). Then
\[
(I:I)=\mathbb Z[\omega]\supsetneq R.
\]
The identity follows by cancelling the nonzero scalar \(2\): a scalar preserves \(\mathbb Z[\omega]\) precisely when it belongs to that ring.

## References

1. Andrew Sutherland, [MIT 18.783 Lecture 18](https://math.mit.edu/classes/18.783/2019/LectureNotes18.pdf), §18.3, the multiplier order of a fractional ideal.
2. The localization and lattice arguments above verify the endomorphism and order claims directly.
