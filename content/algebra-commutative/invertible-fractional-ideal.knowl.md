+++
id = "algebra-commutative/invertible-fractional-ideal"
title = "Invertible fractional ideal"
kind = "definition"
summary = "A fractional ideal having a multiplicative inverse, which is necessarily its colon dual."
aliases = ["invertible fractional ideal", "invertible ideal"]
domains = ["algebra-commutative"]
section_mode = "progressive"
prerequisites = ["algebra-commutative/fractional-ideal", "algebra-commutative/product-fractional-ideals"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

A [[algebra-commutative/fractional-ideal|fractional ideal]] \(I\) of an integral domain \(R\) is **invertible** if another fractional ideal \(J\) satisfies \(IJ=R\), using [[algebra-commutative/product-fractional-ideals|fractional ideal multiplication]]. The inverse is unique and equals
\[
I^{-1}=(R:I)=\{x\in\operatorname{Frac}(R):xI\subseteq R\}.
\]

## Principal examples

Every nonzero [[algebra-commutative/principal-fractional-ideal|principal fractional ideal]] is invertible, but arbitrary fractional ideals need not be.

## Why the colon ideal is the inverse

If \(IJ=R\), then \(J\subseteq(R:I)\). Conversely write \(1=\sum a_jb_j\) with \(a_j\in I\) and \(b_j\in J\). For \(xI\subseteq R\), the equality \(x=\sum(xa_j)b_j\) puts \(x\) in \(J\).

The same finite expression proves that \(I\) is finitely generated: \(a=\sum a_j(b_ja)\) for every \(a\in I\). Invertible ideals are [[algebra-modules/invertible-module|invertible modules]], even when the domain is not Noetherian.

## A noninvertible ideal of a quadratic order

Let \(R=\mathbb Z[\sqrt{-3}]\) and \(I=(2,1+\sqrt{-3})\). Writing \(u=1+\sqrt{-3}\), one has \(u^2=2u-4\), so
\[
I^2=(4,2u,u^2)=(4,2u)=2I.
\]
If \(I\) were invertible, cancellation would give \(I=2R\); this is false because \(u\notin2R\). This example belongs to a nonmaximal [[algebra-rings/order-in-algebra|order]].

## Dedekind domains

Every fractional ideal of a [[algebra-commutative/dedekind-domain|Dedekind domain]] is invertible. Conversely, a domain that is not a field and whose every nonzero fractional ideal is invertible is Dedekind. The exclusion of fields matches the dimension-one convention used here.

## References

1. J. S. Milne, *Algebraic Number Theory*, [author's text](https://www.jmilne.org/math/CourseNotes/ANTc.pdf), §3, Theorem 3.20 and the following discussion of fractional-ideal inverses.
2. The displayed quadratic-order computation proves noninvertibility directly.
