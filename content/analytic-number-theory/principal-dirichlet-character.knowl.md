+++
id = "analytic-number-theory/principal-dirichlet-character"
title = "Principal Dirichlet character"
kind = "definition"
summary = "The character taking value one on each invertible residue class."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/dirichlet-character"]
+++

For \(q\ge1\), the **principal [[analytic-number-theory/dirichlet-character|Dirichlet character]]** modulo \(q\) is \(\chi_0(n)=1\) if \(\gcd(n,q)=1\) and \(\chi_0(n)=0\) otherwise.

## Its L-function

Removing the primes dividing \(q\) from the Euler product gives \(L(s,\chi_0)=\zeta(s)\prod_{p\mid q}(1-p^{-s})\) for \(\Re s>1\). The [[analytic-number-theory/riemann-zeta-function|zeta function]] gives it a simple pole at \(1\).

## References

- [NIST DLMF, §27.8, Dirichlet characters](https://dlmf.nist.gov/27.8)
