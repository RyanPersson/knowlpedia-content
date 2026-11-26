+++
id = "proofs/grh/reduction-main/prime-remainder-bound-from-data"
title = "The prime remainder at x bounded through the data"
kind = "lemma"
summary = "For all data: R_{q0}(x) <= phi(q0) (log b)^6 / m + |R_{q0}(x1)| + log b · |R_1(x1)|."
aliases = ["Data.primeRemainder_le"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.primeRemainder_le"]
lean_files = ["src/New/Reduction/OneSidedBound.lean"]
proof_status = "full"
+++

**Lemma.** Let \(D\) be [[proofs/grh/reduction-main/data|data]] for \(P=(q_0,d)\), and \(R_q\) the [[?lean:New.primeRemainder|prime remainder]]. Then
\[
R_{q_0}(x)\ \le\ \frac{\varphi(q_0)(\log b)^6}{m}+\lvert R_{q_0}(x_1)\rvert+\log b\cdot\lvert R_1(x_1)\rvert .
\]

## Proof

By the [[proofs/grh/reduction-main/total-remainder-formula|formula for the total remainder]], and since \(a>0\), \(\#\Phi_b>0\) (from (P2): \(0<\operatorname{towerDeg}(s)=\#\Phi_a\le\#\Phi_b\log b\)),
\[
R_{q_0}(x)=\frac{\mathrm{rem}}{a\,\#\Phi_b}+R_{q_0}(x_1)-\frac{\#\Phi_a}{\#\Phi_b}R_1(x_1).
\]
By the [[proofs/grh/reduction-main/star-inequality|main inequality]], \(\mathrm{rem}\le fa\log^5b/m\); with \(f=\varphi(q_0)\#\Phi_a\) the first term is at most \(\varphi(q_0)\frac{\#\Phi_a}{\#\Phi_b}\log^5b/m\). Finally \(\#\Phi_a/\#\Phi_b\le\log b\).

## References

1. Lean: `New.Data.primeRemainder_le` in `src/New/Reduction/OneSidedBound.lean`.
