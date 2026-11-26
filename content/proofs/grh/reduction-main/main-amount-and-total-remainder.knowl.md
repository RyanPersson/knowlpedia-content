+++
id = "proofs/grh/reduction-main/main-amount-and-total-remainder"
title = "Main amount, expected prime sum and total remainder"
kind = "definition"
summary = "The main amount m k h_dir, the expected value s_main of the prime sums at the a-places, and the total remainder rem, the sum over the a-places of s_fin(a, tau) - s_main."
aliases = ["mainAmount", "mainPrimeSum", "totalRemainder", "main amount", "total remainder"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.mainAmount", "New.Data.mainPrimeSum", "New.Data.totalRemainder"]
lean_files = ["src/New/Reduction/PrimeSums.lean"]
+++

Let \(D\) be [[proofs/grh/reduction-main/data|data]] for \(P=(q_0,d)\), with [[proofs/grh/reduction-main/data-derived-quantities|derived quantities]] \(m,k,a,f,\Phi_a\), weight \(\kappa\), [[proofs/grh/reduction-main/prime-sum|prime sum \(s_{\mathrm{fin}}\) and direction amount \(h_{\mathrm{dir}}\)]]. Let \(c_1:=\operatorname{Re}G_1(1)\) be the constant of the [[?lean:New.primeRemainder|prime remainder \(R_1\)]] (\(G_q\) is [[?lean:New.logDerivMean|the mean logarithmic derivative]]).

- The **main amount** is \(h_{\mathrm{main}}:=m\,k\,h_{\mathrm{dir}}=m\,k\sum_{\tau\in\Phi}\bigl(s_\infty(\kappa(\tau))-s_{\mathrm{fin}}(\kappa(\tau),\tau)\bigr)\).
- The **expected prime sum** is
\[
s_{\mathrm{main}}:=a\Bigl(\log a-\frac1f\sum_{\tau\in\Phi}\log\kappa(\tau)+c_1\Bigr)=a\bigl(\log(a/\bar\kappa)+c_1\bigr),
\]
\(\bar\kappa\) being the geometric mean of the weights.
- The **total remainder** is \(\mathrm{rem}:=\sum_{\tau\in\Phi_a}\bigl(s_{\mathrm{fin}}(a,\tau)-s_{\mathrm{main}}\bigr)\).

The total remainder is expressed through the prime remainders \(R_q\) in [[proofs/grh/reduction-main/total-remainder-formula|the formula for the total remainder]]; sizes are in [[proofs/grh/reduction-main/prime-sum-bounds|bounds for the prime sums]].

## References

1. Lean: `New.Data.mainAmount`, `New.Data.mainPrimeSum`, `New.Data.totalRemainder` in `src/New/Reduction/PrimeSums.lean`.
