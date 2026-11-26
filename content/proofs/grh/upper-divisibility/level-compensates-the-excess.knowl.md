+++
id = "proofs/grh/upper-divisibility/level-compensates-the-excess"
title = "The level compensates the archimedean excess"
kind = "lemma"
summary = "The excess m(s_inf(a) - s_main) of the m lifts over the main prime sum is at most a log N + 32 a log b, because log N lies in its prescribed window."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.mul_jetSize_sub_mainPrimeSum_sub_le", "New.Data.jetSize_sub_mainPrimeSum_le", "New.Data.card_aPlaces_mul_excess_le", "New.Data.chainSize_sub_le", "New.Data.chainSize"]
lean_files = ["src/New/UpperBound/Size/ArchimedeanSize.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]]; \(\log\bar\kappa=f^{-1}\sum_{\tau}\log w(\tau)\), \(\mathrm{rd}_E\) the root discriminant of \(E\), \(G=\log\bigl(M\,\mathrm{rd}_E/2\pi\bigr)\), \(s_\infty\) the jet size, and \(s_{\mathrm{main}}=a\bigl(\log(a/\bar\kappa)+c_1\bigr)\) the [[?lean:New.Data.mainPrimeSum|main prime sum]], with \(c_1\) the real part of the [[?lean:New.logDerivMean|mean logarithmic derivative]] at \(q=1\). The **chain size** is \(\operatorname{cs}=m\bigl(\lvert\Phi_a\rvert s_\infty(a)+k\sum_\tau s_\infty(w(\tau))\bigr)\).

**Lemma.**

1. \(s_\infty(a)-s_{\mathrm{main}}\le a(\log\bar\kappa+G)+1+\tfrac12\log a\).
2. \(m\bigl(s_\infty(a)-s_{\mathrm{main}}\bigr)-a\log N\le32\,a\log b\).
3. \(\lvert\Phi_a\rvert\bigl(m(s_\infty(a)-s_{\mathrm{main}})-a\log N\bigr)\le32\,fa\log b\).
4. \(\operatorname{cs}-\lvert\Phi_a\rvert a\log N\le h_{\mathrm{main}}-m\,\mathrm{rem}+2\sum_{p<x_1,\ \chi_K(p)\ne1}\operatorname{gain}(p)\log p+32fa\log b\).

## Proof

(1) By [[?c:Stirling's formula|Stirling's bound]] \(\log a!\le a\log a-a+1+\tfrac12\log a\) (the Stirling sequence is decreasing). By the definition of the period, \(\log\Omega=-1-c_1+\log(2\pi/\mathrm{rd}_E)\), so \(\log(M/\Omega)=1+c_1+G\). Hence \(s_\infty(a)\le a\log a+a(c_1+G)+1+\tfrac12\log a\), and subtracting \(s_{\mathrm{main}}=a\log a-a\log\bar\kappa+ac_1\) the constant \(c_1\) cancels.

(2) The level satisfies \(\log N\ge\log N_-=m(\log\bar\kappa+G)-(G+\tfrac{15}2\log b)\) ([[?lean:New.Data.log_N_mem_Icc_logLevelTarget|window for \(\log N\)]]; recall \(N_-=\bar\kappa^{m}(M\mathrm{rd}_E/2\pi)^{m-1}b^{-15/2}\)). By (1),
\[
m(s_\infty(a)-s_{\mathrm{main}})-a\log N\le m\bigl(1+\tfrac12\log a\bigr)+a\bigl(G+\tfrac{15}2\log b\bigr),
\]
the terms \(ma(\log\bar\kappa+G)\) cancelling. With \(m(1+\tfrac12\log a)\le a\log b\) and \(\lvert G\rvert\le23\log b\) (size comparisons of the data, quoted) the right side is at most \(a\log b+a(23+8)\log b\).

(3) Multiply (2) by \(\lvert\Phi_a\rvert\le f\); if the left factor is negative the bound is trivial since the right side is nonnegative.

(4) By the [[proofs/grh/upper-divisibility/gains-add-up-to-the-prime-sums|identity for the gains]], the right side without the last term equals \(m\lvert\Phi_a\rvert s_{\mathrm{main}}+mk\sum_\tau s_\infty(w(\tau))\); subtract and apply (3). \(\blacksquare\)

*Status.* The window for \(\log N\), the bound \(\lvert G\rvert\le23\log b\) and the comparison \(m(1+\tfrac12\log a)\le a\log b\) are quoted from the data.

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Size/ArchimedeanSize.lean`.
