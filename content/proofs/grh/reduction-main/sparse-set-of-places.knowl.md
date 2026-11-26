+++
id = "proofs/grh/reduction-main/sparse-set-of-places"
title = "Sparse set of infinite places"
kind = "definition"
summary = "A set of infinite places of E with no three members whose ratios are, up to sign, two distinct small powers of a small prime modulo the prime-to-l part of q1."
aliases = ["IsSparse", "sparse set"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.IsSparse"]
lean_files = ["src/New/Reduction/Data/AdmissibleData.lean"]
+++

Let \(P\) be [[proofs/grh/reduction-main/parameters|parameters]], \(s\ge0\), \(q_1=q_1(s)\), and \(\Phi\cong(\mathbb Z/q_1)^\times\) the [[proofs/grh/reduction-main/field-e-and-its-places|group of infinite places of \(E=E_s\)]]. Let \(L\) be a natural number. A finite set \(T\subseteq\Phi\) is **sparse for the primes up to \(L\)** if there do **not** exist

- a prime \(\ell\le L\),
- integers \(0<i<j<l_0(s)\),
- places \(\sigma,\tau,\rho\in T\) (not necessarily distinct), and signs \(\varepsilon,\varepsilon'\in\{\pm1\}\) (independent),

such that, with \(q_1'\) the largest divisor of \(q_1\) prime to \(\ell\),
\[
\tau/\sigma\equiv\varepsilon\,\ell^{\,i}\quad\text{and}\quad\rho/\sigma\equiv\varepsilon'\,\ell^{\,j}\pmod{q_1'} .
\]
Here \(\tau/\sigma\) is the quotient in the group \(\Phi\), read in \((\mathbb Z/q_1')^\times\) through the class map.

## Remarks

The condition is of Behrend type (no nontrivial solution of a system of linear relations among exponents); sparse sets of the size required by the [[proofs/grh/reduction-main/data|data]] are constructed in [[proofs/grh/reduction-main/sparse-places-exist|existence of a large sparse set]]. The Lean statement compares the residues with the integers \(\varepsilon\ell^i\), \(\varepsilon'\ell^j\) after casting to \(\mathbb Z/q_1'\).

## References

1. Lean: `New.Parameters.IsSparse` in `src/New/Reduction/Data/AdmissibleData.lean`.
