+++
id = "arithmetic-geometry/inert-prime-divisibility"
title = "Logarithmic divisibility from prescribed valuations"
kind = "construction"
summary = "Guaranteed prime powers dividing an integer give a lower bound on its logarithmic size."
aliases = ["forced divisibility", "total forced divisibility"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["shared-foundations/p-adic-valuation", "shared-foundations/divisibility"]
+++

Let \(A\) be a nonzero integer. If its [[shared-foundations/p-adic-valuation|\(p\)-adic valuations]] satisfy \(v_p(A)\ge e_p\) for primes in a finite set \(S\), with \(e_p\) nonnegative integers, then \(\prod_{p\in S}p^{e_p}\) [[shared-foundations/divisibility|divides]] \(|A|\). The **forced logarithmic divisibility** contributed by these primes is therefore bounded by
\[
\sum_{p\in S} e_p\log p\ \le\ \log |A|.
\]
For a nonzero algebraic integer, the corresponding sum uses prime ideals and the logarithms of their norms.

## Counting powers of inert primes in a factorial

Take \(A=n!\) and restrict to primes [[arithmetic-geometry/inert-prime|inert]] in a fixed quadratic field. Each multiple of \(p^j\) in the factorial supplies one unit to the count for that [[analytic-number-theory/prime-power|prime power]], so
\[
\sum_{\substack{p\ {\rm inert}\\p\le n}}v_p(n!)\log p
=\sum_{\substack{p\ {\rm inert}\\p^j\le n,\ j\ge1}}\left\lfloor\frac{n}{p^j}\right\rfloor\log p.
\]
For \(n=10\) and the field \(\mathbb Q(i)\), the inert primes up to \(10\) are \(3\) and \(7\). Their combined contribution is \(4\log3+\log7\), since \(3,6,9\) supply three factors of \(3\) and \(9\) supplies a fourth.
