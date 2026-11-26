+++
id = "proofs/grh/upper-elementary-divisors/signed-count-of-positive-steps"
title = "Signed count of permutations with positive steps"
kind = "lemma"
summary = "Summing the signs of products of permutations over the families for which all permuted steps are positive gives the indicator of the Pieri cone with positive steps, after sorting each block."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.sum_sign_indicator_pos_eq_indicator_pieriCone", "New.sum_indicator_positiveStepSet", "New.sum_comp_prod_ofFn"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/PieriCone.lean"]
proof_status = "full"
+++

**Lemma.** Let \(\mathcal{T}=\{0,\dots,m\}\) with addition modulo \(m+1\), signs \(v\), and \(P\ge0\); notation of the [[proofs/grh/upper-elementary-divisors/step-map-pieri-cone-slab|step map]].

1. Let \(\nu\) be a vector and \(\tau\) a family of permutations such that each block of \(\nu^{\tau}\) is weakly decreasing. Then
\[
\sum_{\sigma}\operatorname{sgn}(\sigma_0\cdots\sigma_m)\,\bigl[\mathrm{St}_\sigma\nu>0\text{ entrywise}\bigr]=\bigl[\mathrm{St}(\nu^{\tau})>0\text{ entrywise and }\nu^{\tau}\in\mathcal{C}_{v,P}\bigr].
\]
2. Let \(\Omega\) be a set with \(\mathrm{St}\,\nu\in\Omega\iff\nu\in\mathcal{C}_{v,P}\) for all \(\nu\). Then for every \(D\) and \(\nu\),
\[
\#\{\tau:\nu\in\mathrm{Pos}_D(1,\tau,\Omega)\}=\sum_{\sigma}\operatorname{sgn}(\sigma_0\cdots\sigma_m)\,\bigl[\nu\in\mathrm{Pos}_D(\sigma,1,\text{everything})\bigr].
\]
3. For a function \(f\) on permutations of \(\{0,\dots,k-1\}\): \(\sum_\sigma f(\sigma_0\cdots\sigma_m)=(k!)^{m}\sum_\pi f(\pi)\).

## Proof

(1) Let \(M_j\) be the \(k\times k\) matrix with \((M_j)_{b',b}=1\) if \(v_j\,(P\nu(b,j+1)-\nu(b',j))>0\), and \(0\) otherwise; so \((M_j)_{\sigma_j(b),b}\) indicates that the step of \(\mathrm{St}_\sigma\nu\) at \((b,j)\) is positive. Since \(\operatorname{sgn}(\sigma_0\cdots\sigma_m)=\prod_j\operatorname{sgn}\sigma_j\), the left side is \(\prod_j\sum_{\sigma_j}\operatorname{sgn}(\sigma_j)\prod_b(M_j)_{\sigma_j(b),b}=\prod_j\det M_j\) (Leibniz formula). Reindex the rows of \(M_j\) by \(\tau_j\) and the columns by \(\tau_{j+1}\): this multiplies \(\det M_j\) by \(\operatorname{sgn}\tau_j\operatorname{sgn}\tau_{j+1}\), and the product over the cycle of these signs is \(1\). With \(\nu'=\nu^{\tau}\), the reindexed matrix has entries \([v_j(P\nu'(b,j+1)-\nu'(b',j))>0]\). For \(v_j=+\) it is the transpose of the indicator matrix of the decreasing sequences \(x=P\nu'(\cdot,j+1)\) (decreasing because \(P\ge0\)), \(y=\nu'(\cdot,j)\); for \(v_j=-\) it is the indicator matrix of \(x=\nu'(\cdot,j)\), \(y=P\nu'(\cdot,j+1)\). By the [[proofs/grh/upper-elementary-divisors/interlacing-determinant|interlacing determinant]], its determinant is the indicator that \(y_b<x_b\) for all \(b\) (the steps of \(\mathrm{St}\,\nu'\) at letter \(j\) are positive) and \(x_{b+1}\le y_b\) (Pieri's inequality at letter \(j\)). Multiply over \(j\).

(2) If the degree condition fails for \(\nu\), both sides are \(0\). Otherwise, suppose \(\nu\in\mathrm{Pos}_D(1,\tau',\Omega)\): then \(\nu^{\tau'}\in\mathcal{C}_{v,P}\) with positive steps, and the cone inequality in the Lean form, \(0<\text{step}\le\nu^{\tau'}(b,j)-\nu^{\tau'}(b+1,j)\), shows that every block of \(\nu^{\tau'}\) is strictly decreasing. So \(\tau'\) is the unique family \(\tau\) sorting each block of \(\nu\) decreasingly (ties broken by index); the left side is therefore the indicator that \(\nu\in\mathrm{Pos}_D(1,\tau,\Omega)\) for this \(\tau\), i.e. the right side of (1), while the right side of (2) is the left side of (1).

(3) Choose \(\sigma_1,\dots,\sigma_m\) freely; \(\sigma_0\mapsto\sigma_0\sigma_1\cdots\sigma_m\) is then a bijection. \(\square\)

## References

1. Lean: `New.sum_sign_indicator_pos_eq_indicator_pieriCone`, `New.sum_indicator_positiveStepSet`, `New.sum_comp_prod_ofFn` in `src/New/UpperBound/ElementaryDivisors/PieriCone.lean`.
