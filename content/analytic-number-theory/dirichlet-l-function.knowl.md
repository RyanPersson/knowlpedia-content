+++
id = "analytic-number-theory/dirichlet-l-function"
title = "Dirichlet L-function"
kind = "definition"
summary = "The meromorphic continuation of a Dirichlet series weighted by a Dirichlet character."
aliases = ["Dirichlet L-series"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/dirichlet-character", "complex-analysis/analytic-continuation"]
+++

The **Dirichlet \(L\)-function** of a [[analytic-number-theory/dirichlet-character|Dirichlet character]] \(\chi\) is given for \(\operatorname{Re}s>1\) by
\[
L(s,\chi)=\sum_{n\ge1}\frac{\chi(n)}{n^s}
=\prod_p(1-\chi(p)p^{-s})^{-1}.
\]
It has an [[complex-analysis/analytic-continuation|analytic continuation]] to an entire function for a nonprincipal character. For a principal character it has a simple pole at \(1\).

## The first character

For the unique character of modulus \(1\), each coefficient is \(1\) and the function is the [[analytic-number-theory/riemann-zeta-function|Riemann zeta function]]. Changing the character changes the weights of individual primes in the product.

## References

- NIST Digital Library of Mathematical Functions, [§25.15(i), definition, Euler product and continuation](https://dlmf.nist.gov/25.15).
