+++
id = "analytic-number-theory/prime-number-theorem-progressions"
title = "Prime number theorem in arithmetic progressions"
kind = "theorem"
summary = "For a fixed modulus, prime powers in reduced residue classes have equal leading von Mangoldt weight."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/von-mangoldt-function", "analytic-number-theory/euler-totient"]
+++

For a fixed positive integer \(q\) and \(a\) relatively prime to \(q\), the **prime number theorem in arithmetic progressions** states that
\[
\sum_{\substack{n\le x\\ n\equiv a\pmod q}}\Lambda(n)
   \sim \frac{x}{\varphi(q)}\quad (x\to\infty).
\]
Here \(\Lambda\) is the [[analytic-number-theory/von-mangoldt-function|von Mangoldt function]] and \(\varphi\) is [[analytic-number-theory/euler-totient|Euler’s totient]].

## Logarithmic savings

For fixed \(q\) the error is \(O_{q,B}(x/(\log x)^B)\) for each fixed \(B>0\). [[analytic-number-theory/partial-summation|Partial summation]] transfers this estimate to a prime sum with a smooth decreasing weight.

## References

- [Lib/Analytic/PrimeNumberTheorem/ZeroFreeRegion.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/ZeroFreeRegion.lean)
- [New/Reduction/Zeros/PrimeNumberTheorem.lean, eventually_abs_primeRemainder_le](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeNumberTheorem.lean#L217)
