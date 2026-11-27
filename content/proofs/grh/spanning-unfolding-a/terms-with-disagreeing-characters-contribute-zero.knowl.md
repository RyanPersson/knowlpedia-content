+++
id = "proofs/grh/spanning-unfolding-a/terms-with-disagreeing-characters-contribute-zero"
title = "A stable set of terms whose characters do not agree contributes zero"
kind = "theorem"
summary = "If no element of a stable set T has agreeing unipotent characters, every block sum of T vanishes."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.amplitudeSum_eq_zero_of_not_charsAgree", "New.Filling.integral_besselKernel_eq_zero_of_not_charsAgree", "New.Filling.tsum_indicator_smul_eq_tsum_stabilizer"]
lean_files = ["src/New/Spanning/Unfolding/Climbing.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity and \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]]. Say that the characters of a rational [[?c:Isometry of a hermitian space|isometry]] \(\gamma\) **agree** ([[?lean:New.Filling.CharsAgree|agreeing characters]]) if \(\psi(u)=\psi(u')\) for all rational \(u,u'\in\mathsf U\) with \(u\gamma=\gamma u'\), where \(\psi\) is the [[?lean:New.Filling.unipotentChar|unipotent character]] evaluated at the finite adelic images. Let \(T\) be a [[?lean:New.Filling.IsStable|stable]] set of rational isometries such that the characters of no \(\gamma\in T\) agree. Then for every side \(\tau\), all classes \(c,c'\) and every \(s\) in the residue group, the [[?lean:New.Filling.amplitudeSum|block sum]] vanishes:
\[
A^{\tau}_T(c,s,c')=0 .
\]

## Proof

Write \(\Delta_c=\mathsf U_c(M)\), \(\Delta_{c'}=\mathsf U_{c'}(M)\). For a coset \(x=\gamma\Delta_{c'}\) let \(\operatorname{Stab}(x)=\{k\in\Delta_c:\gamma^{-1}k\gamma\in\Delta_{c'}\}\) be its stabiliser under left multiplication by \(\Delta_c\), and \(\Gamma_x\subseteq G_\infty\) its image at the [[?c:Infinite place of a number field|infinite places]].

**Step 1 (one term).** Let \(\gamma\) be rational with non-agreeing characters, \(x=\gamma\Delta_{c'}\). The group \(\Gamma_x\) is discrete, and there is a measurable \(\varphi_x\ge0\) with \(\sum_{k\in\operatorname{Stab}(x)}\varphi_x(ky)=1\) for all \(y\) ([[?lean:New.Filling.exists_cutoff_classUnipotent|cutoffs for subgroups of the unipotent congruence subgroup]]). For any such weight,
\[
\int_{G_\infty}\varphi_x(y)\,\mathcal K^{\tau}_\gamma(y)\,dy=0 .
\]
Indeed \(y\mapsto\mathcal K^{\tau}_\gamma(y)=W(y)\otimes W(\gamma^{-1}y)^{*}\) is continuous and \(\Gamma_x\)-invariant: for \(k\in\operatorname{Stab}(x)\), \(W(ky)=W(y)\) and \(W(\gamma^{-1}ky)=W((\gamma^{-1}k\gamma)\gamma^{-1}y)=W(\gamma^{-1}y)\), by the invariance of \(W\) under the unipotent congruence subgroups (proved with [[proofs/grh/spanning-unfolding-a/block-sums-under-unipotent-reductions|blocks under unipotent reductions]]). So the integral is the integral of \(\mathcal K^{\tau}_\gamma\) over \(\Gamma_x\backslash G_\infty\) ([[?lean:New.IsCutoff.integral_orbitMeasure|integral over the quotient through a cutoff]]). By hypothesis there are rational \(u,u'\in\mathsf U\) with \(u\gamma=\gamma u'\) and \(\psi(u)\ne\psi(u')\); since \(\gamma=u\gamma u'^{-1}\), the transformation rule of the kernel gives \(\mathcal K^{\tau}_\gamma(uy)=\chi\,\mathcal K^{\tau}_\gamma(y)\) with \(\chi=\psi(u)^{-1}\psi(u')\), \(\lvert\chi\rvert=1\), \(\chi\ne1\). A continuous \(\Gamma\)-invariant function that left translation by some element multiplies by such a constant has integral \(0\) over the quotient ([[?lean:New.integral_quotMeasure_eq_zero_of_twist|vanishing of twisted integrals over a quotient]]).

**Step 2 (a weight adapted to the stabilisers).** In each \(\Delta_c\)-orbit of cosets choose a representative, and for each coset \(x\) an element \(a_x\in\Delta_c\) with \(a_xx\) the representative of its orbit. For rational \(\gamma\) with coset \(x\) and \(y\in G_\infty\) define
\[
\operatorname{wt}(\gamma,y)=\beta_{c'}(\gamma^{-1})\cdot\mathbf 1[x\text{ is a chosen representative}]\cdot\varphi_x(y),
\]
where \(\beta_{c'}(\gamma^{-1})\) is the [[?lean:New.Filling.classCutoff|class cutoff]] at the point \(\gamma^{-1}\in G_\infty\) (the image of \(\gamma^{-1}\)); for fixed \(\gamma\) this is a constant multiple of \(\varphi_x\). Its sum over the orbit \((u\gamma u'^{-1},uy)\), \((u,u')\in\Delta_c\times\Delta_{c'}\), is \(1\): the coset of \(u\gamma u'^{-1}\) is \(ux\), independent of \(u'\), and \(\sum_{u'}\beta_{c'}(u'\gamma^{-1}u^{-1})=1\) by the proposition on [[proofs/grh/spanning-unfolding-a/class-cutoff-translates-sum-to-one|class cutoffs]] at the point \(\gamma^{-1}u^{-1}\). In the remaining sum \(\sum_u\mathbf 1[ux\text{ is a representative}]\,\varphi_{ux}(uy)\) only the \(u\in\operatorname{Stab}(a_xx)\,a_x\) contribute, and \(\sum_{v\in\operatorname{Stab}(a_xx)}\varphi_{a_xx}(v\,a_xy)=1\).

**Step 3.** By the theorem on [[proofs/grh/spanning-unfolding-a/change-of-weight-in-block-sums|change of weight]], \(A^{\tau}_T(c,s,c')=\sum_{\gamma\in T\cap\mathcal T(c,s,c')}\int\operatorname{wt}(\gamma,y)\,\mathcal K^{\tau}_\gamma(y)\,dy\). Each term is a constant times the integral of Step 1, hence \(0\).

## References

1. Lean: `New.Filling.amplitudeSum_eq_zero_of_not_charsAgree` in `src/New/Spanning/Unfolding/Climbing.lean`.
2. Lean: `New.Filling.integral_besselKernel_eq_zero_of_not_charsAgree` in `src/New/Spanning/Unfolding/Climbing.lean`.
3. Lean: `New.Filling.tsum_indicator_smul_eq_tsum_stabilizer` in `src/New/Spanning/Unfolding/Climbing.lean`.
