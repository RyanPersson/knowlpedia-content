+++
id = "arithmetic-geometry/inert-prime-divisibility"
title = "Divisibility contributed by inert primes"
kind = "construction"
summary = "A lower bound on logarithmic divisibility obtained by adding guaranteed local valuations at inert primes."
aliases = ["forced divisibility", "total forced divisibility"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/inert-prime", "shared-foundations/p-adic-valuation", "analytic-number-theory/prime-power"]
+++

Suppose a nonzero integer \(A\) is known to be divisible by \(p^{e_p}\) for each prime in a finite set \(S\), with \(e_p\ge0\). Its **forced logarithmic divisibility** from \(S\) is \(\sum_{p\in S}e_p\log p\). This is at most \(\log |A|\). For a number field the corresponding finite-place contributions use prime-ideal norms.

## Why a sum over prime powers appears

For a model, take \(A=n!\) and retain only the primes [[arithmetic-geometry/inert-prime|inert]] in a fixed quadratic field. Counting multiples of \(p,p^2,\ldots\) gives
\[
\sum_{\substack{p\ {\rm inert}\\ p\le n}}v_p(n!)\log p
=\sum_{\substack{p\ {\rm inert}\\p^j\le n,\ j\ge1}}\left\lfloor\frac{n}{p^j}\right\rfloor\log p.
\]
Thus many local divisibilities become one truncated [[analytic-number-theory/weighted-prime-sum|prime-power sum]]. For CM evaluations the exponents come from the specific integral construction. Alpöge’s one-curve example involves odd powers of inert primes.

## References

- Levent Alpöge, [announcement, p. 3, item 2](https://alpo.ge/remark.pdf).
