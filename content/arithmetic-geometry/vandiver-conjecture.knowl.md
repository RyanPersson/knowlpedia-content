+++
id = "arithmetic-geometry/vandiver-conjecture"
title = "Vandiver’s conjecture"
kind = "statement"
summary = "An odd prime does not divide the class number of the maximal real subfield of its cyclotomic field of prime conductor."
aliases = ["Kummer–Vandiver conjecture", "Vandiver conjecture"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/cyclotomic-extension", "algebra-fields-galois/ideal-class-group"]
+++

For an odd prime \(\ell\), let \(\zeta_\ell\) be a primitive \(\ell\)th root of unity. The maximal real subfield of the [[algebra-fields-galois/cyclotomic-extension|cyclotomic field]] \(\mathbb Q(\zeta_\ell)\) is \(K^+=\mathbb Q(\zeta_\ell+\zeta_\ell^{-1})\). **Vandiver’s conjecture** asserts that \(\ell\) does not divide the order of the [[algebra-fields-galois/ideal-class-group|ideal class group]] of \(K^+\). Equivalently, the only ideal class of \(\ell\)-power order in \(K^+\) is the identity.

## The case of conductor three

For \(\ell=3\), the relation \(1+\zeta_3+\zeta_3^2=0\) gives \(\zeta_3+\zeta_3^{-1}=-1\), so \(K^+=\mathbb Q\). Every nonzero ideal of \(\mathbb Z\) is a [[algebra-rings/principal-ideal|principal ideal]]. The class number is \(1\), which verifies the assertion for this prime.

## References

- J. P. Buhler and D. Harvey, [Irregular primes to 163 million, §1, the Kummer–Vandiver conjecture](https://arxiv.org/pdf/0912.2121).
