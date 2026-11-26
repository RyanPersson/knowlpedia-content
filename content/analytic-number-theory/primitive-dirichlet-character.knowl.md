+++
id = "analytic-number-theory/primitive-dirichlet-character"
title = "Primitive Dirichlet character"
kind = "definition"
summary = "A character which cannot be induced from a smaller divisor of its modulus."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/dirichlet-character"]
+++

A [[analytic-number-theory/dirichlet-character|Dirichlet character]] \(\chi\) modulo \(q\) is **primitive** if no proper positive divisor \(f\mid q\) admits a character \(\psi\bmod f\) with \(\chi(n)=\psi(n)\) for every \(n\) coprime to \(q\).

## Example

The character modulo \(4\) that takes values \(1,-1\) on \(1,3\bmod4\) is primitive. Both odd classes reduce to the same class modulo \(2\), so no character modulo \(2\) or \(1\) induces it.

## References

- [NIST DLMF, §27.8, Dirichlet characters](https://dlmf.nist.gov/27.8)
