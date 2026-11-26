+++
id = "proofs/grh/derivatives-divisibility/change-of-directions"
title = "Change of directions"
kind = "theorem"
summary = "Integral matrices, one for each place and height, change given directions so that the pairings between new directions at a place and at its partner are divisible by pi, at a cost in determinants of at most the deduction."
aliases = ["changing the directions", "new directions"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_newDirection_dvd", "New.newDirection", "New.CongruenceChoice", "New.CongruenceChoice.cost", "New.CongruenceChoice.Covers", "New.exists_congruenceChoice_cost_eq_and_covers", "New.congruenceModulus", "New.norm_rpow_sum_cost_eq_prod_congruenceModulus", "New.dvd_sum_pow_mul_of_root_dvd", "New.PairingSide"]
lean_files = ["src/New/Derivatives/Divisibility/NullFrames.lean"]
proof_status = "full"
+++

**Theorem (change of directions).** Let \(p\) be a prime, \(\mathcal{O}\) the valuation ring of \(\mathbb{C}_p\), and \(\pi\in\mathcal{O}\) a divisor of \(p\). Let \(\Phi\) and \(n\) be finite sets, \(\operatorname{pr}\) a partner rule on \(\Phi\) (any map \(\mathbb{N}\times\Phi\to\Phi\)), \(S\) a finite set of exponents, \(N\ge 0\), \(\kappa\colon\Phi\times\mathbb{N}\to\mathbb{N}\), and \(\mathrm{ev}\subseteq\Phi\) a set of marked places. Let \(y_{\tau,a,k}\in\mathcal{O}\) be given for \(\tau\in\Phi\), \(a\in n\), \(k\ge 0\): the vector \(y_{\tau,\cdot,k}\in\mathcal{O}^n\) is the *direction* \(k\) at \(\tau\). Then there are matrices \(g_{\tau,h}\in M_h(\mathcal{O})\), for all \(\tau\in\Phi\) and \(h\ge0\), such that the **new directions**
\[
\beta_{\tau,h,k}=\sum_{k'<h}(g_{\tau,h})_{k,k'}\;y_{\tau,\cdot,k'}\in\mathcal{O}^n\qquad(k<h)
\]
have the following two properties.

1. For \(e\in S\), \(\tau\in\Phi\), heights \(h,h'\) and \(k<h\), \(k'<h'\): unless the pair \((h,h')\) is [[proofs/grh/derivatives-divisibility/deduction-term|exempt]] for \(\mathrm{ev}\) at \((\tau,\operatorname{pr}_e\tau)\),
\[
\pi\ \Bigm|\ \sum_{a\in n}\bigl(\beta_{\tau,h,k}\bigr)_a^{\,p^e}\,\bigl(\beta_{\operatorname{pr}_e\tau,h',k'}\bigr)_a .
\]
2. With the [[proofs/grh/derivatives-divisibility/deduction-term|deduction terms]] \(D_{\mathrm{ev}}\),
\[
\lvert\pi\rvert^{\;\sum_{e\in S}\sum_{\tau\in\Phi}D_{\mathrm{ev}}(\tau,\operatorname{pr}_e\tau,e)}\;\le\;\prod_{\tau\in\Phi}\ \prod_{h<N}\lvert\det g_{\tau,h}\rvert^{\kappa(\tau,h)} .
\]

## Proof

Since \(\mathbb{C}_p\) is algebraically closed and \(\mathcal{O}\) is integrally closed in it, every \(x\in\mathcal{O}\) has a \(p^e\)-th root in \(\mathcal{O}\); fix one, \(x^{1/p^e}\), for each \(x\) and \(e\) (with \(x^{1/p^0}=x\)).

**Step 1: four kinds of congruence.** Fix \(e\in S\) and \(\sigma\in\Phi\) with partner \(\sigma'=\operatorname{pr}_e\sigma\). For a row \(u\in\mathcal{O}^h\) write \(\beta(u)=\sum_{k<h}u_k\,y_{\sigma,\cdot,k}\), and similarly \(\beta'(u')\) at \(\sigma'\) for \(u'\in\mathcal O^{h'}\). Consider the congruences

* (SE) on a row \(u\) at \(\sigma\): all entries \(u_l\equiv0\pmod{\pi^{1/p^e}}\);
* (SP) on a row \(u\) at \(\sigma\): \(\sum_a (y_{\sigma',a,0})^{1/p^e}\,\beta(u)_a\equiv 0\pmod{\pi^{1/p^e}}\);
* (PE) on a row \(u'\) at \(\sigma'\): all entries \(u'_l\equiv0\pmod\pi\);
* (PP) on a row \(u'\) at \(\sigma'\): \(\sum_a y_{\sigma,a,0}^{\,p^e}\,\beta'(u')_a\equiv0\pmod\pi\).

We claim: \(\pi\) divides \(\sum_a\beta(u)_a^{p^e}\beta'(u')_a\) as soon as one of the following holds: (PE) for \(u'\); (SE) for \(u\); (PP) for \(u'\) and \(h=1\); (SP) for \(u\) and \(h'=1\).

Under (PE), \(\pi\) divides every coordinate of \(\beta'(u')\). Under (SE), \(\pi^{1/p^e}\) divides every coordinate of \(\beta(u)\), so \(\pi\) divides its \(p^e\)-th power. If \(h=1\), then \(\beta(u)=u_0\,y_{\sigma,\cdot,0}\) and the sum is \(u_0^{p^e}\sum_ay_{\sigma,a,0}^{p^e}\beta'(u')_a\), divisible by \(\pi\) under (PP). If \(h'=1\), then \(\beta'(u')=u'_0\,y_{\sigma',\cdot,0}\) and the sum is \(u'_0\sum_a\beta(u)_a^{p^e}y_{\sigma',a,0}\). Under (SP), \(\pi=(\pi^{1/p^e})^{p^e}\) divides \(\bigl(\sum_a (y_{\sigma',a,0})^{1/p^e}\beta(u)_a\bigr)^{p^e}\), and this power is congruent modulo \(\pi\) to \(\sum_a y_{\sigma',a,0}\,\beta(u)_a^{p^e}\), because \(p^e\)-th powers are [[?lean:New.dvd_sum_pow_sub_sum|additive modulo a divisor of \(p\)]].

**Step 2: a choice of congruences of cost \(D\).** For each height, decide which of the four kinds are imposed on the rows of that height. With \(t,r,B\) as in the [[proofs/grh/derivatives-divisibility/deduction-term|deduction term]], let \(\mathsf A_1\) be the statement \(t(\sigma)/p^e\le r(\sigma')+t(\sigma')\) and \(\mathsf A_2\) the statement \(B(\sigma)/p^e\le B(\sigma')\). Impose

* (SE) at height \(h\): if \(h=1\), when \(\sigma\notin\mathrm{ev}\) and \(\mathsf A_1\); if \(h\ne1\), when \(\mathsf A_2\);
* (SP) at every height \(h\neq1\);
* (PE) at height \(h'\ne1\) when \(\mathsf A_2\) fails;
* (PP) at height \(h'\) when \(\mathsf A_1\) fails and, if \(h'=1\), \(\sigma'\notin\mathrm{ev}\).

*Cost.* Count each congruence once for each column of that height below \(N\) (an entry congruence at height \(h\) counts \(h\) times), those at \(\sigma\) with the weight \(p^{-e}\). At \(\sigma\) the count is \([\mathsf A_1]\,t(\sigma)+r(\sigma)+[\mathsf A_2]\,B(\sigma)\); at \(\sigma'\) it is \([\neg\mathsf A_1]\,(r(\sigma')+t(\sigma'))+[\neg\mathsf A_2]\,B(\sigma')\). The weighted total is exactly \(D_{\mathrm{ev}}(\sigma,\sigma',e)\), each minimum being attained on the side chosen.

*Covering.* Let \((h,h')\) be not exempt. If \(h=1\): then \(\sigma\notin\mathrm{ev}\), and not both \(h'=1\) and \(\sigma'\in\mathrm{ev}\); so (SE) is imposed at height \(1\) if \(\mathsf A_1\), and (PP) at height \(h'\) otherwise. If \(h\ne1\) and \(h'=1\): (SP) is imposed at height \(h\). If \(h\neq 1\ne h'\): (SE) at height \(h\) if \(\mathsf A_2\), (PE) at height \(h'\) otherwise. In each case Step 1 applies to all rows satisfying the imposed congruences.

**Step 3: the matrices.** The linear forms in (SP), (PP) and the coordinate forms in (SE), (PE) depend only on \(y\), not on the matrices. For fixed \((\tau,h)\), collect all congruences imposed on rows of height \(h\) at \(\tau\): over all \(e\in S\) and \(\sigma\), those at the source if \(\sigma=\tau\) and those at the partner if \(\operatorname{pr}_e\sigma=\tau\). By [[proofs/grh/derivatives-divisibility/elimination-of-congruences|elimination]] there is \(g_{\tau,h}\in M_h(\mathcal{O})\) all of whose rows satisfy them, with \(\det g_{\tau,h}\) dividing the product \(M_{\tau,h}\) of the moduli. As \(\beta_{\tau,h,k}=\beta(u)\) for the row \(u\) number \(k\) of \(g_{\tau,h}\), Step 2 gives property 1.

For property 2, \(\lvert\pi^{1/p^e}\rvert=\lvert\pi\rvert^{1/p^e}\), so \(\lvert M_{\tau,h}\rvert=\lvert\pi\rvert^{E(\tau,h)}\), where \(E(\tau,h)\) is the number of congruences imposed at \((\tau,h)\), those at a source side for \(e\) weighted by \(p^{-e}\). Summing \(E(\tau,h)\kappa(\tau,h)\) over \(\tau\) and \(h<N\) and regrouping by \((e,\sigma)\) gives the sum of the costs, that is \(\sum_{e\in S}\sum_\sigma D_{\mathrm{ev}}(\sigma,\operatorname{pr}_e\sigma,e)\). Finally \(\det g_{\tau,h}\mid M_{\tau,h}\) means \(\lvert M_{\tau,h}\rvert\le\lvert\det g_{\tau,h}\rvert\). \(\blacksquare\)

## References

1. Lean: `New.exists_newDirection_dvd`, `New.newDirection`, `New.exists_congruenceChoice_cost_eq_and_covers`, `New.norm_rpow_sum_cost_eq_prod_congruenceModulus`, `New.dvd_sum_pow_mul_of_root_dvd` in `src/New/Derivatives/Divisibility/NullFrames.lean`.
