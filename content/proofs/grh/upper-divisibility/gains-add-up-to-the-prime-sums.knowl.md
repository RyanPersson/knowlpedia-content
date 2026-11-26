+++
id = "proofs/grh/upper-divisibility/gains-add-up-to-the-prime-sums"
title = "The gains add up to the prime sums"
kind = "proposition"
summary = "Twice the sum of gain(p) log p over the small non-split primes equals m times the prime sums at the a-places plus m k times the prime sums at all places; hence the prime sums cancel in the exponent of the size bound."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.two_mul_sum_gain_mul_log", "New.Data.mainAmount_sub_add_two_mul_sum_gain"]
lean_files = ["src/New/UpperBound/Size/ArchimedeanSize.lean"]
proof_status = "full"
+++

Let \(D\) be [[?lean:New.Data|admissible data]]; \(S(y,\tau)\) is the [[?lean:New.Data.primeSum|prime sum]], \(s_\infty(l)=\log l!+l\log(M/\Omega)\) the [[?lean:New.Data.jetSize|jet size]], \(s_{\mathrm{main}}\) the [[?lean:New.Data.mainPrimeSum|main prime sum]], \(w\) the weight, and
\[
h_{\mathrm{main}}=mk\sum_{\tau\in\Phi}\bigl(s_\infty(w(\tau))-S(w(\tau),\tau)\bigr),\qquad\mathrm{rem}=\sum_{\tau\in\Phi_a}\bigl(S(a,\tau)-s_{\mathrm{main}}\bigr)
\]
the [[?lean:New.Data.mainAmount|main amount]] and the [[?lean:New.Data.totalRemainder|total remainder]]. Let \(\mathcal P\) be the set of primes \(p<x_1\) with \(\chi_K(p)\ne1\).

**Proposition.**
\[
2\sum_{p\in\mathcal P}\operatorname{gain}(p)\log p=m\sum_{\tau\in\Phi_a}S(a,\tau)+mk\sum_{\tau\in\Phi}S(w(\tau),\tau),
\]
\[
h_{\mathrm{main}}-m\,\mathrm{rem}+2\sum_{p\in\mathcal P}\operatorname{gain}(p)\log p=m\lvert\Phi_a\rvert s_{\mathrm{main}}+mk\sum_{\tau\in\Phi}s_\infty(w(\tau)).
\]

## Proof

The gain vanishes at split primes, so the sum may run over all primes below \(\lceil x_1\rceil\). By the [[proofs/grh/upper-divisibility/prime-sum-grouped-by-primes|grouping of the prime sum]] (with \(U=\lceil x_1\rceil\), and \(y=a\) or \(y=w(\tau)\le a\)), \(S(y,\tau)=\sum_{p<\lceil x_1\rceil}2s_p(y,\tau)\log p\). Insert this on the right, exchange the sums, and compare with the definition \(\operatorname{gain}(p)=m\bigl(\sum_{\tau\in\Phi_a}s_p(a,\tau)+k\sum_\tau s_p(w(\tau),\tau)\bigr)\). The second identity follows by substituting the first into the definitions of \(h_{\mathrm{main}}\) and \(\mathrm{rem}\): the terms \(mk\sum_\tau S(w(\tau),\tau)\) and \(m\sum_{\Phi_a}S(a,\tau)\) cancel. \(\blacksquare\)

## References

1. Lean: `New.Data.two_mul_sum_gain_mul_log`, `New.Data.mainAmount_sub_add_two_mul_sum_gain` in `src/New/UpperBound/Size/ArchimedeanSize.lean`. The formulas for the main amount and the total remainder are those stated in the comments of that file; their definitions are in `src/New/Reduction/PrimeSums.lean`.
