+++
id = "proofs/grh/reduction-zeros/prime-remainder-as-integral"
title = "The remainder as an integral of the counting error"
kind = "lemma"
summary = "R_q(y) is the integral of the counting error over t^2 from 1 to y, less c_q; the counting error is at most 13t."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.countError", "New.abs_countError_le", "New.sum_Icc_vonMangoldt_le_six_mul", "New.intervalIntegrable_countError_div_sq", "New.primeRemainder_eq_integral_countError_sub"]
lean_files = ["src/New/Reduction/Zeros/PrimeNumberTheorem.lean"]
proof_status = "full"
+++

**Lemma.** Let \(d\) be a prime, \(q\ge1\), \(\lambda\) the [[proofs/grh/reduction-zeros/weight-lambda-k|weight]] and \(R_q\), \(c_q\) as in the [[proofs/grh/reduction-zeros/prime-remainder|remainder]]. Define the **counting error**
\[
\mathcal{E}_q(t)=\sum_{n\le t}\lambda(n)-\frac{t}{\varphi(q)}\qquad(t\ge0).
\]

1. \(\lvert\mathcal{E}_q(t)\rvert\le13\,t\) for \(t\ge0\).
2. For \(y\ge1\): \(\displaystyle R_q(y)=\int_1^{y}\frac{\mathcal{E}_q(t)}{t^{2}}\,dt-c_q\).

## Proof

1. By the [[?c:Chebyshev bound for the psi function|Chebyshev bound]] \(\sum_{n\le t}\Lambda(n)\le(\log4+4)t\le6t\) and \(\lambda\le2\Lambda\), we get \(0\le\sum_{n\le t}\lambda(n)\le12t\); also \(0\le t/\varphi(q)\le t\).

2. Let \(A(t)=\sum_{n\le t}\lambda(n)\). The [[?c:Abel summation formula|Abel summation formula]] with the function \(1/t\) gives
\[
\sum_{n\le y}\frac{\lambda(n)}{n}=\frac{A(y)}{y}+\int_1^{y}\frac{A(t)}{t^{2}}\,dt .
\]
Since \(\sum_{n\le y}\lambda(n)(1/n-1/y)=\sum_{n\le y}\lambda(n)/n-A(y)/y\) and \(\int_1^{y}\frac{t/\varphi(q)}{t^2}dt=\frac{\log y}{\varphi(q)}\), the claim follows from the definition of \(R_q\). \(\blacksquare\)

## References

1. Lean: `New.countError`, `New.abs_countError_le`, `New.primeRemainder_eq_integral_countError_sub` in `src/New/Reduction/Zeros/PrimeNumberTheorem.lean`.
