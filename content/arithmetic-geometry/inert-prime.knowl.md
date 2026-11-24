+++
id = "arithmetic-geometry/inert-prime"
title = "Inert prime in a quadratic field"
kind = "definition"
summary = "A rational prime that remains prime in the quadratic ring of integers, giving residue degree two."
aliases = ["inert primes", "primes inert in a quadratic field"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/ring-of-integers", "algebra-fields-galois/finite-field"]
+++

A [[analytic-number-theory/prime-number|rational prime]] \(p\) is **inert** in a quadratic number field \(K\) when \(p\mathcal O_K\) is still a prime ideal in its [[algebra-fields-galois/ring-of-integers|ring of integers]]. There is one prime above \(p\), its ramification index is one and its [[algebra-commutative/residue-field|residue field]] is the [[algebra-fields-galois/finite-field|finite field]] with \(p^2\) elements.

## In the Gaussian integers

In \(\mathbb Z[i]\), reduction modulo \(3\) gives \(\mathbb F_3[T]/(T^2+1)\). The polynomial has no root in \(\mathbb F_3\), so this quotient is a field and \(3\) is inert. Modulo \(5\), the two roots \(2\) and \(-2\) give two primes above \(5\). The [[algebra-fields-galois/frobenius-unramified|Frobenius]] at an inert prime is the nonidentity automorphism of \(K/\mathbb Q\).

## References

- J. S. Milne, [Algebraic Number Theory, chapter 3, factorization of primes in extensions](https://www.jmilne.org/math/CourseNotes/ANTc.pdf).
