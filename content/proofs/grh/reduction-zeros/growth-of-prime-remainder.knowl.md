+++
id = "proofs/grh/reduction-zeros/growth-of-prime-remainder"
title = "Exponential growth of the partial sums and of the remainder"
kind = "lemma"
summary = "The sums S_r(e^v) are at most 2e^v and the remainder R_q(e^v) is at most (|c_q| + 5)e^v in absolute value."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.abs_lambdaKSum_exp_le", "New.abs_primeRemainder_exp_le"]
lean_files = ["src/New/Reduction/Zeros/PrimeError.lean"]
proof_status = "full"
+++

**Lemma.** Let \(d\) be a prime and \(q\ge1\), with the notation \(S_r\), \(R_q\), \(c_q\) of the [[proofs/grh/reduction-zeros/prime-remainder|remainder]].

1. For every integer \(r\ge0\) and real \(v\): \(\lvert S_r(e^{v})\rvert\le2e^{v}\).
2. For \(v\ge0\): \(\lvert R_q(e^{v})\rvert\le(\lvert c_q\rvert+5)\,e^{v}\).

## Proof

1. The sum defining \(S_r(e^v)\) has at most \(e^{v}\) terms. For \(1\le n\le e^{v}\), \(0\le\lambda(n)/n\le2\) by the [[proofs/grh/reduction-zeros/weight-lambda-k|bound \(\lambda(n)\le2n\)]], and \(n^{r}\le e^{rv}\). So the sum is at most \(e^{v}\cdot2e^{rv}\), and dividing by \(e^{rv}\) gives the claim.

2. \(R_q(e^{v})=S_0(e^v)-S_1(e^v)-v/\varphi(q)-c_q\). By 1 the first two terms are at most \(2e^v\) each; \(0\le v/\varphi(q)\le v\le e^{v}\); and \(\lvert c_q\rvert\le\lvert c_q\rvert e^{v}\). \(\blacksquare\)

## References

1. Lean: `New.abs_lambdaKSum_exp_le`, `New.abs_primeRemainder_exp_le` in `src/New/Reduction/Zeros/PrimeError.lean`.
