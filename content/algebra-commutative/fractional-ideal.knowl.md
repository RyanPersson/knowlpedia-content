+++
id = "algebra-commutative/fractional-ideal"
title = "Fractional ideal"
kind = "definition"
summary = "A nonzero submodule of a fraction field whose denominators can be cleared."
aliases = []
domains = ["algebra-commutative"]
section_mode = "progressive"
prerequisites = ["algebra-rings/integral-domain", "algebra-rings/fraction-field", "algebra-modules/module"]
+++

Let \(R\) be an [[algebra-rings/integral-domain|integral domain]] with [[algebra-rings/fraction-field|fraction field]] \(K\). A **fractional ideal** of \(R\) is a nonzero \(R\)-[[algebra-modules/module|submodule]] \(I\subseteq K\) for which some \(0\ne c\in R\) satisfies \(cI\subseteq R\).

We use the convention excluding the zero module. If \(R\) is Noetherian, these are exactly the nonzero finitely generated \(R\)-submodules of \(K\).

## Operations

The product \(IJ\) consists of finite sums of products \(xy\), with \(x\in I\), \(y\in J\). A principal fractional ideal has the form \(aR\), \(a\in K^\times\). It need not lie inside \(R\); for example \(\tfrac12\mathbb Z\) is a fractional ideal of \(\mathbb Z\).

## Invertibility

Over a [[algebra-commutative/dedekind-domain|Dedekind domain]], each fractional ideal has inverse \(I^{-1}=\{x\in K:xI\subseteq R\}\), with \(II^{-1}=R\). This assertion is not valid for every integral domain.

## References

1. J. S. Milne, *Algebraic Number Theory*, v3.08. [Author’s text](https://www.jmilne.org/math/CourseNotes/ANTc.pdf), §3, “The ideal class group,” Theorem 3.20.
