+++
id = "algebra-fields-galois/integral-basis"
title = "Integral basis of a number field"
kind = "definition"
summary = "A basis of its ring of integers as a free abelian group."
aliases = []
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/ring-of-integers", "algebra-modules/free-module"]
+++

An **integral basis** of a degree-\(n\) number field \(K\) is a [[algebra-modules/free-module|basis over \(\mathbb Z\)]] of its [[algebra-fields-galois/ring-of-integers|ring of integers]]: elements \(\omega_1,\ldots,\omega_n\) such that each \(x\in\mathcal O_K\) has a unique expression
\[
x=m_1\omega_1+\cdots+m_n\omega_n,\qquad m_i\in\mathbb Z.
\]

## Existence and distinction

Every number field has an integral basis. Its elements are also a rational basis of \(K\), but the converse fails even for a rational basis made of algebraic integers.

For example, \((1,\sqrt{-3})\) is a rational basis of \(\mathbb Q(\sqrt{-3})\) but is not integral: it misses \((1+\sqrt{-3})/2\). The pair \((1,(1+\sqrt{-3})/2)\) is an integral basis.

## References

1. J. S. Milne, *Algebraic Number Theory*, v3.08. [Author’s text](https://www.jmilne.org/math/CourseNotes/ANTc.pdf), §2, Proposition 2.29 and Definition 2.32.
