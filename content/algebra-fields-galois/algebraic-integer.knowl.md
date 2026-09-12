+++
id = "algebra-fields-galois/algebraic-integer"
title = "Algebraic integer"
kind = "definition"
summary = "An algebraic number satisfying a monic polynomial with integer coefficients."
aliases = []
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-commutative/integral-element", "algebra-fields-galois/algebraic-element"]
+++

An [[algebra-fields-galois/algebraic-element|algebraic number]] \(\alpha\in\overline{\mathbb Q}\) is an **algebraic integer** if it is [[algebra-commutative/integral-element|integral]] over \(\mathbb Z\): there are \(n\ge1\) and \(a_0,\ldots,a_{n-1}\in\mathbb Z\) with
\[
\alpha^n+a_{n-1}\alpha^{n-1}+\cdots+a_0=0.
\]
The leading coefficient must be one.

## Examples

Both \(i\) and \(\sqrt2\) are algebraic integers, using \(T^2+1\) and \(T^2-2\). The rational number \(1/2\) is algebraic but not integral: clearing a monic equation of degree \(n\) would make an odd integer equal to an even integer.

## Rational special case

More generally, if \(a/b\) is in lowest terms with \(b>0\), a monic integral equation forces \(b\mid a^n\), hence \(b=1\). Thus the rational algebraic integers are exactly \(\mathbb Z\).

## References

1. J. S. Milne, *Algebraic Number Theory*, v3.08. [Author’s text](https://www.jmilne.org/math/CourseNotes/ANTc.pdf), §2, “Integral elements,” especially Proposition 2.11.
