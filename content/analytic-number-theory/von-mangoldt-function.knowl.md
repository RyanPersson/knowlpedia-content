+++
id = "analytic-number-theory/von-mangoldt-function"
title = "Von Mangoldt function"
kind = "definition"
summary = "The weight Λ assigns log p to every positive power of p and zero to other integers."
aliases = ["Mangoldt weight", "von Mangoldt weight"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/prime-power", "real-analysis/natural-logarithm"]
+++

The **von Mangoldt function** \(\Lambda(n)\) is \(\log p\) when \(n=p^k\) is a [[analytic-number-theory/prime-power|prime power]], \(k\ge1\), and zero otherwise. Here \(\log\) is the [[real-analysis/natural-logarithm|natural logarithm]]. Thus \(\Lambda(9)=\log 3\), while \(\Lambda(1)=\Lambda(12)=0\).

## Why the exponent does not enter the weight

If \(p^e\) exactly divides \(n\), the divisors \(p,p^2,\dots,p^e\) contribute \(e\log p\). Summing over the primes that divide \(n\) gives \(\sum_{d\mid n}\Lambda(d)=\log n\). This turns the logarithm of a product into a sum over prime powers.

## References

- NIST Digital Library of Mathematical Functions, [§27.2, definition of the Mangoldt function](https://dlmf.nist.gov/27.2).
