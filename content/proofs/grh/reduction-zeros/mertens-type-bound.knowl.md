+++
id = "proofs/grh/reduction-zeros/mertens-type-bound"
title = "A bound of Mertens type"
kind = "lemma"
summary = "The sum of Lambda(n)/n over n up to N is at most 2 log N."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.sum_vonMangoldt_div_le"]
lean_files = ["src/New/Reduction/Zeros/PrimeError.lean"]
proof_status = "full"
+++

**Lemma.** For every integer \(N\ge0\), with \(\Lambda\) the [[?c:von Mangoldt function|von Mangoldt function]],
\[
\sum_{1\le n\le N}\frac{\Lambda(n)}{n}\le2\log N .
\]
(For \(N=0\) both sides are \(0\) with the convention \(\log0=0\).)

## Proof

Let \(N\ge1\). For \(1\le n\le N\) we have \(\lfloor N/n\rfloor\ge1\) and \(N/n<\lfloor N/n\rfloor+1\le2\lfloor N/n\rfloor\). Hence
\[
N\sum_{n\le N}\frac{\Lambda(n)}{n}\le2\sum_{n\le N}\Lambda(n)\Bigl\lfloor\frac Nn\Bigr\rfloor=2\sum_{m\le N}\sum_{n\mid m}\Lambda(n)=2\sum_{m\le N}\log m\le2N\log N,
\]
using \(\sum_{n\mid m}\Lambda(n)=\log m\). Divide by \(N\). \(\blacksquare\)

## References

1. Lean: `New.sum_vonMangoldt_div_le` in `src/New/Reduction/Zeros/PrimeError.lean`.
