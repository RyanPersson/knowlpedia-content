+++
id = "proofs/grh/upper-elementary-divisors/large-defect-forces-divisibility"
title = "A large defect forces a divisible coefficient"
kind = "theorem"
summary = "If all SL_2 translates of a polynomial have order plus depth at least v0, then each term has order plus depth at least v0 plus a third of its defect."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.mem_gaussFiltration_sub_defect_div_three", "New.FrobeniusCycle.totalDegree_polyAction_le", "New.FrobeniusCycle.weight_sub_defectWeight_div_three"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/RootLemma.lean"]
proof_status = "full"
+++

**Theorem.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,R)\) with \(N\ge1\), \(a\ne a'\) indices below \(k\), \(i\) a letter, and \(\delta\) real weights of the variables with \(\delta(Y_s)-\delta(X_s)=1\) for every letter \(s\). Let \(v_0\in\mathbb{R}\) and \(f\in R[x_{b,s}]\) be such that \(g\cdot f\in\mathrm{G}_{v_0}(F^{w},\delta)\) for all \(g\in\mathrm{SL}_2^{a,a'}(W)\) ([[proofs/grh/upper-elementary-divisors/gauss-filtration|Gauss filtration]], [[proofs/grh/upper-elementary-divisors/root-data|root data]]). Then
\[
f\in\mathrm{G}_{v_0}\bigl(F^{w},\ \delta-\tfrac13\omega_{i,a,a'}\bigr),
\]
that is, the coefficient of each \(x^{\alpha}\) in \(f\) is divisible by \(w^{e}\) with \(e=\lceil v_0-\delta\cdot\alpha+\tfrac13\operatorname{def}_{i,a,a'}(\alpha)\rceil_+\).

## Proof

Let \(\omega'=\delta-\tfrac13\omega_{i,a,a'}\). By the [[proofs/grh/upper-elementary-divisors/defect-weight-bounds|bounds on defect weights]], \(\omega_{i,a,a'}(Y_s)-\omega_{i,a,a'}(X_s)\in[0,\tfrac32]\), so \(\omega'(Y_s)-\omega'(X_s)\in[\tfrac12,1]\).

Let \(\mathrm{Low}\) be the set of pairs \((\alpha,l)\), \(l\in\mathbb{N}\), with \(l+\omega'\cdot\alpha<v_0\) such that for some \(g\in\mathrm{SL}_2^{a,a'}(W)\), \(w^{l+1}\) does not divide the coefficient of \(x^{\alpha}\) in \(g\cdot f\). Observe: if \(t\le v_0\) and \(t\le l+\omega'\cdot\alpha\) for all \((\alpha,l)\in\mathrm{Low}\), then every translate lies in \(\mathrm{G}_t(F^{w},\omega')\). (If the coefficient at \(\alpha\) of \(g\cdot f\) is not divisible by \(w^{\lceil t-\omega'\cdot\alpha\rceil_+}\), write \(\lceil t-\omega'\cdot\alpha\rceil_+=l+1\); then \(l<t-\omega'\cdot\alpha\le v_0-\omega'\cdot\alpha\), so \((\alpha,l)\in\mathrm{Low}\) with \(l+\omega'\cdot\alpha<t\), a contradiction.) If \(\mathrm{Low}=\emptyset\), take \(t=v_0\), \(g=1\) to conclude.

Suppose \(\mathrm{Low}\neq\emptyset\). It is finite: the translates have total degree at most \(\deg f\) (the action is by linear substitutions), so only finitely many \(\alpha\) occur, and \(l<v_0-\omega'\cdot\alpha\). Choose \((\alpha,l)\in\mathrm{Low}\) minimising \(l+\omega'\cdot\alpha\), with witness \(g_0\). By the observation with \(t=l+\omega'\cdot\alpha\), all translates of \(f\), hence all translates \(g\cdot(g_0\cdot f)=(gg_0)\cdot f\), lie in \(\mathrm{G}_{l+\omega'\cdot\alpha}(F^{w},\omega')\), and \(w^{l+1}\) does not divide the coefficient of \(x^{\alpha}\) in \(g_0\cdot f\). The [[proofs/grh/upper-elementary-divisors/root-lemma|root lemma]] for \(g_0\cdot f\) and the weights \(\omega'\) gives \(\operatorname{def}_{i,a,a'}(\alpha)\le0\). Hence \(\delta\cdot\alpha=\omega'\cdot\alpha+\tfrac13\operatorname{def}(\alpha)\le\omega'\cdot\alpha\) and \(l<v_0-\delta\cdot\alpha\). But \(g_0\cdot f\in\mathrm{G}_{v_0}(F^{w},\delta)\) says \(w^{\lceil v_0-\delta\cdot\alpha\rceil_+}\), and so \(w^{l+1}\), divides that coefficient: a contradiction. \(\square\)

## References

1. Lean: `New.FrobeniusCycle.mem_gaussFiltration_sub_defect_div_three`, `New.FrobeniusCycle.totalDegree_polyAction_le`, `New.FrobeniusCycle.weight_sub_defectWeight_div_three` in `src/New/UpperBound/ElementaryDivisors/RootLemma.lean`.
