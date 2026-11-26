+++
id = "proofs/grh/reduction-main/total-remainder-formula"
title = "The total remainder in terms of the prime remainders"
kind = "theorem"
summary = "rem = a ( #Phi_b (R_{q0}(x) - R_{q0}(x1)) + #Phi_a R_1(x1) )."
aliases = ["totalRemainder_eq"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.totalRemainder_eq", "New.lambdaKResidueClass_eq_ite", "New.sum_lambdaKResidueClass_mul_posPart", "New.Data.card_aPlaces", "New.Data.f_eq_card_aPlaces_mul", "New.Data.mem_aPlaces_iff_of_mul_mem_bPlaces", "New.Data.card_filter_mem_bPlaces", "New.Data.sum_aPlaces_lambdaKResidueClass_mul_posPart", "New.Data.sum_aPlaces_primeSum", "New.Data.sum_log_weight", "New.Data.card_aPlaces_mul_mainPrimeSum"]
lean_files = ["src/New/Reduction/PrimeSums.lean"]
proof_status = "full"
+++

**Theorem.** Let \(D\) be [[proofs/grh/reduction-main/data|data]] for \(P=(q_0,d)\). For \(q\ge1\) let \(\lambda_q(n)=\Lambda_K(n)\) if \(n\equiv1\pmod q\) and \(0\) otherwise, and let
\[
R_q(z)=\sum_{n\le z}\lambda_q(n)\Bigl(\frac1n-\frac1z\Bigr)-\frac{\log z}{\varphi(q)}-c_q,\qquad c_q=\operatorname{Re}G_q(1),
\]
be the [[?lean:New.primeRemainder|prime remainder]]. Then, with the [[proofs/grh/reduction-main/main-amount-and-total-remainder|total remainder \(\mathrm{rem}\) and \(s_{\mathrm{main}}\)]],

1. \(\#\Phi_a=\operatorname{towerDeg}(s)\) and \(f=\#\Phi_a\cdot\varphi(q_0)\);
2. \(\displaystyle\sum_{\tau\in\Phi_a}s_{\mathrm{fin}}(a,\tau)=a\Bigl(\#\Phi_b\bigl(R_{q_0}(x)-R_{q_0}(x_1)\bigr)+\#\Phi_aR_1(x_1)\Bigr)+a\Bigl(\#\Phi_a(\log x_1+c_1)+\#\Phi_b\frac{\log x-\log x_1}{\varphi(q_0)}\Bigr)\);
3. \(\#\Phi_a\cdot s_{\mathrm{main}}\) equals the second bracket of (2) times \(a\);
4. \(\displaystyle\mathrm{rem}=a\Bigl(\#\Phi_b\bigl(R_{q_0}(x)-R_{q_0}(x_1)\bigr)+\#\Phi_a\,R_1(x_1)\Bigr).\)

## Proof

(1) is part (3) of [[proofs/grh/reduction-main/field-e-properties|properties of \(E\)]].

**A rescaled form of \(R_q\).** For an integer \(A\) and \(0<z\le A\),
\[
\sum_{n=1}^{A}\lambda_q(n)\Bigl(\frac An-\frac Az\Bigr)_+=A\Bigl(R_q(z)+\frac{\log z}{\varphi(q)}+c_q\Bigr), \tag{*}
\]
because \((A/n-A/z)_+=A(1/n-1/z)\) for \(n\le z\) and \(=0\) for \(n>z\) ([[?lean:New.primeRemainder_eq_sum|rescaled prime remainder]]).

**Counting.** Let \(n\ge1\). Suppose \(\tau\in\Phi\) with \(-n\tau=\operatorname{place}(-n)\tau\in\Phi_b\). By (P1) the class of \(-n\tau\) modulo \(q_0\) is \(-1\); hence \(\tau\equiv1\) iff \(\operatorname{place}(-n)\equiv-1\) modulo \(q_0\) iff \(-n\equiv-1\), i.e. \(n\equiv1\pmod{q_0}\) (part (5) of the properties of \(E\)). Consequently the number of \(\tau\in\Phi_a\) with \(-n\tau\in\Phi_b\) is \(\#\Phi_b\) if \(n\equiv1\pmod{q_0}\) (multiplication by \(\operatorname{place}(-n)\) is then a bijection from that set onto \(\Phi_b\)) and \(0\) otherwise.

**(2)** Since \(\kappa(\sigma)=a/x\) on \(\Phi_b\) and \(a/x_1\) elsewhere,
\[
\Bigl(\frac an-\kappa(\sigma)\Bigr)_+=\Bigl(\frac an-\frac a{x_1}\Bigr)_++\mathbf 1_{\sigma\in\Phi_b}\Bigl[\Bigl(\frac an-\frac ax\Bigr)_+-\Bigl(\frac an-\frac a{x_1}\Bigr)_+\Bigr].
\]
Summing over \(\tau\in\Phi_a\) with \(\sigma=-n\tau\), multiplying by \(\Lambda_K(n)\) and using the count,
\[
\sum_{\tau\in\Phi_a}\Lambda_K(n)\Bigl(\frac an-\kappa(-n\tau)\Bigr)_+=\#\Phi_a\,\lambda_1(n)\Bigl(\frac an-\frac a{x_1}\Bigr)_++\#\Phi_b\,\lambda_{q_0}(n)\Bigl[\Bigl(\frac an-\frac ax\Bigr)_+-\Bigl(\frac an-\frac a{x_1}\Bigr)_+\Bigr].
\]
Sum over \(1\le n\le a\) and apply \((*)\) three times with \(A=a\) (allowed since \(x\le x_1\le a\)): for \((q,z)=(1,x_1)\), \((q_0,x)\), \((q_0,x_1)\). The constants \(c_{q_0}\) cancel, \(\varphi(1)=1\), and (2) results.

**(3)** By (P4), \(\sum_{\tau\in\Phi}\log\kappa(\tau)=f(\log a-\log x_1)-\#\Phi_b(\log x-\log x_1)\). Insert this into the definition of \(s_{\mathrm{main}}\) and use \(f=\#\Phi_a\varphi(q_0)\):
\[
\#\Phi_a\,s_{\mathrm{main}}=a\Bigl(\#\Phi_a(\log x_1+c_1)+\#\Phi_b\frac{\log x-\log x_1}{\varphi(q_0)}\Bigr).
\]

**(4)** \(\mathrm{rem}=\sum_{\tau\in\Phi_a}s_{\mathrm{fin}}(a,\tau)-\#\Phi_a\,s_{\mathrm{main}}\); subtract (3) from (2).

## References

1. Lean: `New.Data.totalRemainder_eq` and the lemmas listed in the front matter, in `src/New/Reduction/PrimeSums.lean`.
