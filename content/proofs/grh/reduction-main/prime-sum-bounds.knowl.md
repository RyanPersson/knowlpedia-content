+++
id = "proofs/grh/reduction-main/prime-sum-bounds"
title = "Bounds for the prime sums, the jet sizes and the main amount"
kind = "lemma"
summary = "0 <= s_fin(y, tau) <= y log b; 20 y log b <= s_inf(y) <= 25 y log b; b #Phi_a <= h_dir <= 25 f b log b; and x^4 f a <= h_main."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.lambdaKResidueClass_mul_posPart_le_ite", "New.Data.primeSum_le", "New.Data.primeSum_mem_Icc", "New.Data.jetSize_mem_Icc", "New.Data.jetSize_sub_primeSum_mem_Icc", "New.Data.directionAmount_mem_Icc", "New.Data.le_mainAmount", "New.Data.mainAmount_nonneg"]
lean_files = ["src/New/Reduction/PrimeSums.lean"]
proof_status = "full"
+++

**Lemma.** Let \(D\) be [[proofs/grh/reduction-main/data|data]], with [[proofs/grh/reduction-main/prime-sum|\(s_{\mathrm{fin}}\), \(s_\infty\), \(h_{\mathrm{dir}}\)]] and [[proofs/grh/reduction-main/main-amount-and-total-remainder|\(h_{\mathrm{main}}\)]].

1. For real \(0\le y\le a\) and \(\tau\in\Phi\): \(0\le s_{\mathrm{fin}}(y,\tau)\le4y\log x_1\le y\log b\).
2. For an integer \(0\le y\le a\): \(20\,y\log b\le s_\infty(y)\le25\,y\log b\).
3. For \(\tau\in\Phi\) and \(y=\kappa(\tau)\): \(y\log b\le s_\infty(y)-s_{\mathrm{fin}}(y,\tau)\le25\,y\log b\).
4. \(b\cdot\#\Phi_a\le h_{\mathrm{dir}}\le25\,f\,b\log b\).
5. \(x^4fa\le h_{\mathrm{main}}\); in particular \(h_{\mathrm{main}}\ge0\).

## Proof

(1) Each term \(\Lambda_K(n)(y/n-\kappa(\sigma))_+\) is \(\ge0\). If \(n>x_1\), then \(y/n\le a/x_1\le\kappa(\sigma)\) and the term vanishes. If \(n\le x_1\), it is at most \(2\Lambda(n)\cdot y/n\). Hence \(s_{\mathrm{fin}}(y,\tau)\le2y\sum_{n\le x_1}\Lambda(n)/n\le2y\cdot2\log x_1\), by the elementary bound \(\sum_{n\le X}\Lambda(n)/n\le2\log X\) ([[?c:Mertens' first theorem|Mertens-type bound]]; `sum_vonMangoldt_div_le` in the source). Finally \(4\log x_1\le\log b\) by (S4).

(2) \(y!\le y^y\le a^y\le(b^2)^y\) since \(a=xb\le b^2\); so \(0\le\log y!\le2y\log b\). By [[proofs/grh/reduction-main/data-sizes|sizes of the data]], \(20\log b\le\log(M/\Omega)\le23\log b\). Add.

(3) \(\kappa(\tau)\le a\); combine (1) and (2): lower bound \(20y\log b-y\log b\ge y\log b\), upper bound \(25y\log b-0\).

(4) Lower bound: by (3), \(h_{\mathrm{dir}}\ge\sum_{\tau\in\Phi}\kappa(\tau)\log b\ge\sum_{\tau\in\Phi_b}b\log b=b\,\#\Phi_b\log b\ge b\operatorname{towerDeg}(s)=b\,\#\Phi_a\), using (P2) and [[proofs/grh/reduction-main/total-remainder-formula|\(\#\Phi_a=\operatorname{towerDeg}(s)\)]]. Upper bound: by (3) and \(\kappa\le b\).

(5) By (4), \(h_{\mathrm{main}}=mk\,h_{\mathrm{dir}}\ge mk\,b\operatorname{towerDeg}(s)\). Since \(f=\operatorname{towerDeg}(s)\varphi(q_0)\) and \(a=xb\), it remains to see \(x^5\varphi(q_0)\le mk\); indeed \(mk\ge\sqrt x\cdot r/2\ge x^{5.5}/2\) and \(2\varphi(q_0)\le2c_P\le\sqrt x\). (The Lean proof obtains this comparison from the [[proofs/grh/reduction-main/log-bound-calculus|calculus of logarithmic bounds]].)

## References

1. Lean: `New.Data.primeSum_le`, `primeSum_mem_Icc`, `jetSize_mem_Icc`, `jetSize_sub_primeSum_mem_Icc`, `directionAmount_mem_Icc`, `le_mainAmount`, `mainAmount_nonneg` in `src/New/Reduction/PrimeSums.lean`.
