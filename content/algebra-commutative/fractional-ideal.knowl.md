+++
id = "algebra-commutative/fractional-ideal"
title = "Fractional ideal"
kind = "definition"
summary = "A nonzero submodule of a fraction field whose denominators can be cleared."
aliases = ["fractional ideal"]
domains = ["algebra-commutative"]
section_mode = "progressive"
prerequisites = ["algebra-rings/integral-domain", "algebra-rings/fraction-field", "algebra-modules/submodule"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(R\) be an [[algebra-rings/integral-domain|integral domain]] with [[algebra-rings/fraction-field|fraction field]] \(K\). A **fractional ideal** of \(R\) is a nonzero \(R\)-[[algebra-modules/submodule|submodule]] \(I\subseteq K\) for which some \(0\ne c\in R\) satisfies \(cI\subseteq R\).

We use the convention excluding the zero module.

## Common denominators

Equivalently, \(I=c^{-1}J\) for a nonzero ordinary [[algebra-rings/ideal|ideal]] \(J\subseteq R\) and \(0\ne c\in R\): take \(J=cI\). An ordinary ideal is sometimes called an integral ideal to emphasize containment in \(R\).

If \(R\) is [[algebra-commutative/noetherian-ring|Noetherian]], fractional ideals are exactly the nonzero [[algebra-modules/finitely-generated-module|finitely generated]] \(R\)-submodules of \(K\). Finite generators have a common denominator; conversely, \(cI\) is a finitely generated ideal and multiplication by \(c\) identifies it with \(I\).

For example, \(\tfrac12\mathbb Z\) is fractional, while \(\mathbb Z[1/2]\subset\mathbb Q\) is not: no single nonzero integer clears the denominators \(2^m\) for every \(m\).

## Operations

The [[algebra-commutative/product-fractional-ideals|product]] \(IJ\) consists of finite sums of products \(xy\), with \(x\in I\), \(y\in J\). A [[algebra-commutative/principal-fractional-ideal|principal fractional ideal]] has the form \(aR\), \(a\in K^\times\). It need not lie inside \(R\); for example \(\tfrac12\mathbb Z\) is a fractional ideal of \(\mathbb Z\).

## Invertibility

A fractional ideal is [[algebra-commutative/invertible-fractional-ideal|invertible]] when it has a multiplicative inverse. Over a [[algebra-commutative/dedekind-domain|Dedekind domain]], each fractional ideal has inverse \(I^{-1}=\{x\in K:xI\subseteq R\}\), with \(II^{-1}=R\). This assertion is not valid for every integral domain; nonmaximal [[algebra-rings/order-in-algebra|orders]] supply examples.

The [[algebra-commutative/multiplier-ring|multiplier ring]] \((I:I)\) and [[algebra-commutative/fractional-ideal-quotient|colon quotient]] \((R:I)\) record two different scalar-preservation conditions.

## References

1. J. S. Milne, *Algebraic Number Theory*, v3.08. [Author’s text](https://www.jmilne.org/math/CourseNotes/ANTc.pdf), §3, “The ideal class group,” Theorem 3.20.
