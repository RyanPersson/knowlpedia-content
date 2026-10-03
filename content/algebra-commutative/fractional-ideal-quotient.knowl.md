+++
id = "algebra-commutative/fractional-ideal-quotient"
title = "Quotient of fractional ideals"
kind = "definition"
summary = "The colon fractional ideal (I:J) consists of scalars carrying J into I."
aliases = ["fractional ideal quotient", "colon fractional ideal", "colon ideal in a fraction field"]
domains = ["algebra-commutative"]
section_mode = "progressive"
prerequisites = ["algebra-commutative/fractional-ideal"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

For nonzero [[algebra-commutative/fractional-ideal|fractional ideals]] \(I,J\) of an integral domain \(R\) with [[algebra-rings/fraction-field|fraction field]] \(K\), their **fractional ideal quotient** is
\[
(I:J)=\{x\in K:xJ\subseteq I\}.
\]

This is a nonzero fractional ideal. The ambient field matters: restricting \(x\) to \(R\) would give the ring-theoretic colon ideal \((I:J)\cap R\).

## Why it is fractional

Choose \(0\ne a\in I\) and \(0\ne d\in R\) with \(dJ\subseteq R\). Then \(ad\in(I:J)\), so it is nonzero. Choose \(0\ne b\in J\); since \(b(I:J)\subseteq I\), a denominator for \(I\), together with a denominator for \(b\), yields a common denominator for \((I:J)\).

## Inverses and multipliers

The candidate inverse of \(I\) is \((R:I)\). It is an actual multiplicative inverse exactly when \(I\) is [[algebra-commutative/invertible-fractional-ideal|invertible]]. One must not cancel a noninvertible fractional ideal in a product equation.

The quotient \((I:I)\) is the [[algebra-commutative/multiplier-ring|multiplier ring]] of \(I\), which may be larger than \(R\).

## References

1. The displayed containment and denominator argument verify the definition over arbitrary integral domains; no Noetherian hypothesis is used.
