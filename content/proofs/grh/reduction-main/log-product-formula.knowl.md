+++
id = "proofs/grh/reduction-main/log-product-formula"
title = "Product formula for the rational numbers, in logarithms"
kind = "lemma"
summary = "For a rational q, log|q| plus the sum of log|q|_p over the primes below a bound exceeding numerator and denominator is zero."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.log_product_formula"]
lean_files = ["src/New/Reduction/Lattices/Heights.lean"]
proof_status = "full"
+++

**Lemma.** Let \(q\in\mathbb Q\) be written in lowest terms as \(q=u/w\) with \(w\ge1\), and let \(M\) be a natural number with \(\lvert u\rvert<M\) and \(w<M\). Then
\[
\log\lvert q\rvert+\sum_{p<M,\ p\ \text{prime}}\log\lvert q\rvert_p=0 ,
\]
where \(\lvert\cdot\rvert_p\) is the [[?c:p-adic absolute value|\(p\)-adic absolute value]] with \(\lvert p\rvert_p=p^{-1}\), and where \(\log 0:=0\) (so the statement is \(0=0\) for \(q=0\)).

This is the [[?c:product formula for the rational numbers|product formula for \(\mathbb Q\)]] restricted to a finite set of primes containing all those dividing \(u\) or \(w\).

## Proof

For \(q=0\) all terms are \(0\) by the convention. Let \(q\ne0\). Every natural number \(n\) with \(0<n<M\) factors as \(n=\prod_{p<M}p^{v_p(n)}\) (all its prime divisors are below \(M\)), so \(\log n=\sum_{p<M}v_p(n)\log p\). Hence
\[
\log\lvert q\rvert=\log\lvert u\rvert-\log w=\sum_{p<M}\bigl(v_p(u)-v_p(w)\bigr)\log p .
\]
On the other hand \(\lvert q\rvert_p=p^{-(v_p(u)-v_p(w))}\), so \(\log\lvert q\rvert_p=\bigl(v_p(w)-v_p(u)\bigr)\log p\). The two sums cancel term by term.

## References

1. Lean: `New.log_product_formula` in `src/New/Reduction/Lattices/Heights.lean`.
