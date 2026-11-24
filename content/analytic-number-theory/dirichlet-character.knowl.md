+++
id = "analytic-number-theory/dirichlet-character"
title = "Dirichlet character"
kind = "definition"
summary = "A multiplicative character of the units modulo q, extended by zero on nonunits."
aliases = ["primitive Dirichlet character", "characters modulo q"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["algebra-groups/group-homomorphism", "algebra-rings/group-of-units"]
+++

A **Dirichlet character modulo \(q\)** is a [[algebra-groups/group-homomorphism|homomorphism]] \((\mathbb Z/q\mathbb Z)^\times\to\mathbb C^\times\), from the [[algebra-rings/group-of-units|group of units]] modulo \(q\). It extends to a periodic function on integers by giving value zero to each integer sharing a prime factor with \(q\). Its nonzero values are roots of unity. It is **primitive** if it does not come from a character of any proper divisor of \(q\).

## Example modulo four

The nonprincipal character modulo \(4\) takes the value \(1\) on integers congruent to \(1\), the value \(-1\) on integers congruent to \(3\), and zero on even integers. Its [[analytic-number-theory/weighted-prime-sum|weighted prime sum]] therefore subtracts contributions from one odd residue class from those in the other.

Squaring this character gives the principal character modulo \(4\), which equals \(1\) on odd integers and \(0\) on even integers. It is induced by the unique character of modulus \(1\).

## References

- NIST Digital Library of Mathematical Functions, [§27.8, Dirichlet characters](https://dlmf.nist.gov/27.8).
