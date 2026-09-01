+++
id = "algebra-commutative/integral-extension"
title = "Integral extension"
kind = "knowl"
summary = "A homomorphism of commutative rings A→B is integral when every element of B satisfies a monic polynomial over A."
aliases = ["integral-extension", "Integral extension"]
domains = ["algebra-commutative"]
prerequisites = ["algebra-rings/commutative-ring", "algebra-commutative/integral-element"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-commutative/integral-extension.md"
+++

Let \(A\to B\) be a homomorphism of [[algebra-rings/commutative-ring|commutative rings]]. The map (or extension) is **integral** if every \(b\in B\) is [[algebra-commutative/integral-element|integral over \(A\)]]: for each \(b\), some monic polynomial in \(A[T]\) has \(b\) as a root.

## Properties

If \(B\) is finitely generated as an \(A\)-module, then \(A\to B\) is integral. Localizing an integral extension at a multiplicative set preserves integrality (compare [[algebra-commutative/localization-ring|localization]]). Integral extensions also satisfy [[algebra-commutative/lying-over-theorem|lying over]] and [[algebra-commutative/going-up-theorem|going up]].

## Examples

1. **Adjoining a root of a monic polynomial.**
   For any commutative ring \(A\) and monic \(f(T)\in A[T]\), the quotient
   \[
   B := A[T]/(f)
   \]
   is integral over \(A\): the class of \(T\) in \(B\) satisfies \(f(T)=0\).

2. **Classical quadratic extensions.**
   The inclusion \(\mathbb{Z}\subseteq \mathbb{Z}[i]\) is integral because \(\mathbb{Z}[i]\) is generated as a \(\mathbb Z\)-module by \(1\) and \(i\).

3. **A cusp subring inside a polynomial ring.**
   Let \(k\) be a field and \(A=k[x^2,x^3]\subseteq B=k[x]\). Then \(B=A[x]\) is integral over \(A\) because \(x\) satisfies \(T^2-x^2=0\), whose constant coefficient \(x^2\) belongs to \(A\).

4. **Non-example: polynomial extensions are not integral.**
   If \(A\ne 0\), the inclusion \(A\subseteq A[x]\) is not integral: the indeterminate \(x\) satisfies no monic polynomial with coefficients in \(A\).
