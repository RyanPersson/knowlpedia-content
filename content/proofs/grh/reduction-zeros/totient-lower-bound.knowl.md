+++
id = "proofs/grh/reduction-zeros/totient-lower-bound"
title = "A lower bound for Euler's totient"
kind = "lemma"
summary = "Every positive integer n satisfies n <= phi(n)(2 log n + 1)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.le_totient_mul_log", "New.div_add_card_le_prod_one_sub_inv"]
lean_files = ["src/Lib/Analytic/Primes.lean"]
proof_status = "full"
+++

**Lemma.** For every integer \(n\ge1\), with \(\varphi\) the [[?c:Euler totient function|Euler totient function]],
\[
n\le\varphi(n)\,(2\log n+1).
\]

## Proof

*A product bound.* If \(S\) is a finite set of integers all greater than \(a\ge0\), then \(\prod_{p\in S}(1-1/p)\ge a/(a+\#S)\). Induction on \(\#S\): remove the least element \(b\ge a+1\); by induction applied with \(b\) in place of \(a\) the remaining product is \(\ge b/(b+\#S-1)\), and \((1-1/b)\,b/(b+\#S-1)=(b-1)/(b+\#S-1)\ge a/(a+\#S)\).

*The bound.* Let \(j\) be the number of distinct primes dividing \(n\). They are all \(>1\), so \(\varphi(n)/n=\prod_{p\mid n}(1-1/p)\ge1/(1+j)\). Also \(2^{j}\le n\), so \(j\le\log n/\log2\le2\log n\). Hence \(n\le\varphi(n)(1+j)\le\varphi(n)(1+2\log n)\). \(\blacksquare\)

## References

1. Lean: `New.div_add_card_le_prod_one_sub_inv`, `New.le_totient_mul_log` in `src/Lib/Analytic/Primes.lean`.
