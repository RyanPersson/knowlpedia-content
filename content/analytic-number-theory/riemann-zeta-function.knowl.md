+++
id = "analytic-number-theory/riemann-zeta-function"
title = "Riemann zeta function"
kind = "definition"
summary = "The meromorphic continuation of the sum of n to the power −s over positive integers."
aliases = ["Riemann zeta", "zeta function"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["complex-analysis/analytic-continuation", "langlands/euler-product-and-local-factor"]
+++

For a complex variable \(s\) with \(\operatorname{Re}s>1\), the **Riemann zeta function** is
\[
\zeta(s)=\sum_{n=1}^{\infty}n^{-s}=\prod_{p\ {\rm prime}}(1-p^{-s})^{-1}.
\]
The [[langlands/euler-product-and-local-factor|Euler product]] follows by expanding each factor and using unique prime factorization. The function extends by [[complex-analysis/analytic-continuation|analytic continuation]] to the complex plane with a single simple pole at \(1\).

## Where the hypothesis enters

The zeros at negative even integers are called trivial zeros. The [[analytic-number-theory/riemann-hypothesis|Riemann hypothesis]] concerns the zeros in the strip \(0<\operatorname{Re}s<1\).

## References

- NIST Digital Library of Mathematical Functions, [§25.2, definition and analytic properties](https://dlmf.nist.gov/25.2) and [§25.10, zeros](https://dlmf.nist.gov/25.10).
