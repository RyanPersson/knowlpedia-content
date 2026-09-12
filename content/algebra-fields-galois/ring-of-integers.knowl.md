+++
id = "algebra-fields-galois/ring-of-integers"
title = "Ring of integers of a number field"
kind = "definition"
summary = "The subring consisting of all algebraic integers in a number field."
aliases = ["ring of integers", "number ring"]
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/number-field", "algebra-fields-galois/algebraic-integer", "algebra-commutative/integral-closure"]
+++

The **ring of integers** of a [[algebra-fields-galois/number-field|number field]] \(K\) is
\[
\mathcal O_K=\{\alpha\in K:\alpha\text{ is an algebraic integer}\}.
\]
Equivalently, it is the [[algebra-commutative/integral-closure|integral closure]] of \(\mathbb Z\) in \(K\). Addition and multiplication preserve [[algebra-fields-galois/algebraic-integer|integrality]], so this subset is a subring with identity.

## Size and coordinates

As an additive group it is free of rank \([K:\mathbb Q]\). A choice of its integer coordinates is an [[algebra-fields-galois/integral-basis|integral basis]]. This does not assert that it has a basis of powers of one element.

## Examples

One has \(\mathcal O_{\mathbb Q}=\mathbb Z\) and \(\mathcal O_{\mathbb Q(i)}=\mathbb Z[i]\). For \(\mathbb Q(\sqrt{-3})\), the element \((1+\sqrt{-3})/2\) is also integral, so merely adjoining the square root misses part of the ring.

## References

1. J. S. Milne, *Algebraic Number Theory*, v3.08. [Author’s text](https://www.jmilne.org/math/CourseNotes/ANTc.pdf), §2, Proposition 2.29 and Corollary 2.30.
