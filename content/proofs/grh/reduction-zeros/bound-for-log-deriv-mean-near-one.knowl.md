+++
id = "proofs/grh/reduction-zeros/bound-for-log-deriv-mean-near-one"
title = "A bound for G_q(s)/s slightly to the left of the line Re s = 1"
kind = "lemma"
summary = "For all large l the function G_q(s)/s is holomorphic and at most l^26 on Re s >= 1 - l^(-26), |s| <= e^l."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.eventually_norm_logDerivMean_div_le", "New.norm_logDerivMean_le"]
lean_files = ["src/New/Reduction/Zeros/PrimeNumberTheorem.lean"]
proof_status = "full"
+++

**Lemma.** Let \(d\) be a prime, \(q\ge1\), and \(G_q\) the [[proofs/grh/reduction-zeros/log-deriv-mean|mean of logarithmic derivatives]]. There is \(l_0\) such that for all real \(l\ge l_0\) and all \(s\in\mathbb{C}\) with \(\operatorname{Re}s\ge1-l^{-26}\) and \(\lvert s\rvert\le e^{l}\): the function \(z\mapsto G_q(z)/z\) is holomorphic at \(s\) and \(\lvert G_q(s)/s\rvert\le l^{26}\).

## Proof

Let \(N=\varphi(q)\) be the number of characters modulo \(q\). By the [[proofs/grh/reduction-zeros/zero-free-region|zero-free region]], applied to each of the finitely many characters \(\psi\) and \(\psi\chi_K\), for all large \(l\) and all \(s\) with \(\operatorname{Re}s\ge1-l^{-25}\), \(\lvert s\rvert\le e^{l}\): none of the \(E_\psi\), \(E_{\psi\chi_K}\) vanishes at \(s\) and each logarithmic derivative is at most \(2l^{25}\) in absolute value. Take also \(l\ge8N+2\ge2\). The region of the lemma lies in this one, since \(l^{-26}\le l^{-25}\). There \(G_q\) is holomorphic, \(\operatorname{Re}s\ge1-l^{-25}\ge\tfrac12\), so \(s\ne0\) and \(\lvert s\rvert\ge\tfrac12\), and from the definition of \(G_q\) (dropping the factor \(1/\varphi(q)\le1\))
\[
\lvert G_q(s)\rvert\le N\cdot2\cdot2l^{25}+1,\qquad\Bigl\lvert\frac{G_q(s)}{s}\Bigr\rvert\le2(4Nl^{25}+1)\le(8N+2)\,l^{25}\le l^{26}.\ \blacksquare
\]

## References

1. Lean: `New.norm_logDerivMean_le`, `New.eventually_norm_logDerivMean_div_le` in `src/New/Reduction/Zeros/PrimeNumberTheorem.lean`.
