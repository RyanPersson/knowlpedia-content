+++
id = "proofs/grh/derivatives-divisibility/predicted-divisibility"
title = "Predicted divisibility of a family of diagrams"
kind = "definition"
summary = "The real number, computed from the column counts and the partner rule, by which the jets along products of minors are predicted to be divisible at a prime p; it equals gamma_p times the number of boxes minus the total deduction."
aliases = ["predicted divisibility", "deduction"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.predictedDivisibility", "New.heightOneColumns", "New.lowColumnCount", "New.lowBoxCount", "New.eraseHeightOne", "New.deductionAt", "New.mul_tsum_deductionAt", "New.mul_sum_deductionTerm_le", "New.summable_deductionAt", "New.deductionTerm_empty", "New.deductionTerm_eraseHeightOne", "New.boxes_eq_sum"]
lean_files = ["src/New/Derivatives/Divisibility/Count.lean"]
proof_status = "full"
+++

**Definition (predicted divisibility).** Let \(d\) and \(p\) be primes, with \(v(\pi_p)\), \(\gamma_p\), \(I_p^\circ\), \(I_p\) as in the [[proofs/grh/derivatives-divisibility/p-adic-setting|\(p\)-adic setting]]. Let \(\Phi\) be a finite set with a partner rule \(\operatorname{pr}\), \(\kappa\colon\Phi\times\mathbb{N}\to\mathbb{N}\) column counts and \(N\ge0\). For \(\tau\in\Phi\) let
\[
a_\tau=\begin{cases}\kappa(\tau,1)&1<N\\0&\text{else}\end{cases},\qquad a'_\tau=\sum_{h<N,\ h\ne1}\kappa(\tau,h),\qquad l_\tau=\sum_{h<N,\ h\neq 1}h\,\kappa(\tau,h)
\]
be the number of columns of height one, the number of *low* columns (the others), and the number of boxes in the low columns. With \(u_+=\max(u,0)\), the **predicted divisibility** is
\[
\operatorname{pd}(\kappa)=v(\pi_p)\sum_{e\in I_p}\ \sum_{\tau\in\Phi}\Bigl[\Bigl(\frac{a_\tau}{p^e}-a_{\tau_e}-a'_{\tau_e}\Bigr)_{\!+}+\Bigl(\frac{l_\tau}{p^e}-l_{\tau_e}\Bigr)_{\!+}-\frac{a'_\tau}{p^e}\Bigr]\;-\;\epsilon,\qquad\tau_e=\operatorname{pr}_e\tau,
\]
where \(\epsilon=0\) if \(p\ne d\) and \(\epsilon=\tfrac12\sum_\tau\bigl(\min(a_\tau,a_{\tau_0}+a'_{\tau_0})+a'_\tau+\min(l_\tau,l_{\tau_0})\bigr)\) if \(p=d\). For a finite set \(\mathrm{ev}\subseteq\Phi\) of marked places, \(\kappa^\circ\) denotes \(\kappa\) with the columns of height one at the marked places removed: \(\kappa^\circ(\tau,1)=0\) for \(\tau\in\mathrm{ev}\), and \(\kappa^\circ=\kappa\) elsewhere.

**Lemma (deduction and prediction).** Let \(B(\kappa)=\sum_\tau\sum_{h<N}h\kappa(\tau,h)\) and let \(D_{\mathrm{ev}}\) be the [[proofs/grh/derivatives-divisibility/deduction-term|deduction term]] (for \(\kappa\), \(N\)).

1. \(\displaystyle v(\pi_p)\sum_{e\in I_p^\circ}\sum_{\tau}D_{\emptyset}(\tau,\operatorname{pr}_e\tau,e)=\gamma_p\,B(\kappa)-\operatorname{pd}(\kappa)\), and the series converges.
2. For every marked set \(\mathrm{ev}\) and every \(e_0\ge 0\),
\[
v(\pi_p)\sum_{\substack{e\in I_p^\circ\\ e\le e_0}}\ \sum_\tau D_{\mathrm{ev}}(\tau,\operatorname{pr}_e\tau,e)\ \le\ \gamma_p\,B(\kappa^\circ)-\operatorname{pd}(\kappa^\circ).
\]

## Proof

1. Without marked places \(t=a\), \(r=a'\), \(B(\sigma)=l_\sigma\) in the deduction term, so \(0\le D_\emptyset(\tau,\tau_e,e)\le(a_\tau+a'_\tau+l_\tau)/p^e\), and the series is dominated by a [[real-analysis/geometric-series|geometric series]]. Using \((u-u')_+=u-\min(u,u')\), for \(e\ge1\) the bracket in the definition equals \((a_\tau+l_\tau)/p^e-D_\emptyset(\tau,\tau_e,e)\). Now \(\sum_\tau(a_\tau+l_\tau)=B(\kappa)\) and \(\sum_{e\in I_p}p^{-e}=\gamma_p/v(\pi_p)\) (a geometric series: \(\sum_{e\ \mathrm{odd}}p^{-e}=p/(p^2-1)\) for inert \(p\), and \(\sum_{e\ge1}p^{-e}=1/(p-1)\) for \(p=d\), where \(v(\pi_p)=\tfrac12\); both sides vanish if \(p\) splits). Hence \(\operatorname{pd}(\kappa)+\epsilon=\gamma_pB(\kappa)-v(\pi_p)\sum_{e\in I_p}\sum_\tau D_\emptyset\). The exponent \(e=0\) lies in \(I_p^\circ\) only for \(p=d\), and then \(v(\pi_p)\sum_\tau D_\emptyset(\tau,\tau_0,0)=\epsilon\).

2. Marking has the same effect on deduction terms as removing the columns of height one at the marked places: \(D_{\mathrm{ev}}\) for \(\kappa\) equals \(D_\emptyset\) for \(\kappa^\circ\), since only \(t\) involves height one. Apply 1 to \(\kappa^\circ\) and drop the nonnegative terms with \(e>e_0\). \(\blacksquare\)

## References

1. Lean: `New.predictedDivisibility`, `New.eraseHeightOne`, `New.mul_tsum_deductionAt`, `New.mul_sum_deductionTerm_le` in `src/New/Derivatives/Divisibility/Count.lean`; `New.hasSum_div_pow_positivePartnerExponents` in `src/Lib/CM/FormalGroup/PrimeNotation.lean`.
