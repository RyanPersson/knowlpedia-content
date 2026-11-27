+++
id = "proofs/grh/spanning-unfolding-a/poincare-series-are-forms"
title = "The Poincaré series are forms of the discrete series type and principal level"
kind = "theorem"
summary = "For admissible data the series sum_gamma cutBessel_a(gamma g) is a form of type e_l and level J_M; this defines the linear Poincaré map phi -> P_phi."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.exists_levelSpace_tsum_cutBessel_eq", "New.Filling.Fits.poincareMap", "New.Filling.Fits.coe_poincareMap", "New.Filling.Fits.integral_typeKernel_mul_besselFn", "New.Filling.Fits.realConv_tsum_cutBessel_classUnipotent"]
lean_files = ["src/New/Spanning/Unfolding/PoincareSeries.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], and \(V\) a space [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fitting]] \(S\) with parameters \(l\). For every \(a=(c,i)\) the series \(g\mapsto\sum_{\gamma\in\Gamma}B_a(\gamma g)\) of the [[proofs/grh/spanning-unfolding-a/poincare-series-of-bessel-functions|cut-off Bessel function]] is a [[?lean:New.Space.IsForm|form]] on \(V\) of type \(e_l\) ([[?lean:New.typeKernel|type kernel]]: continuous, left \(\Gamma\)-invariant, bounded, right invariant under an open subgroup, and fixed by right convolution with \(e_l\) over \(G_\infty\)), and it is right invariant under the principal level \(J_M\).

Consequently there is a linear map, the **Poincaré map**,
\[
\mathcal P:\mathbb C^{\{a\}}\longrightarrow\{\text{forms of type }e_l\text{ on }V\}^{J_M},\qquad\mathcal P(\varphi)=\mathcal P_\varphi\ \text{ as functions on }G .
\]

## Proof

*The kernel fixes the Bessel function.* For \(x\in G_\infty\) and a coordinate \(i\),
\[
\int_{G_\infty}e_l(z)\,W_i(\theta(xz))\,dz=W_i(\theta(x)).\tag{1}
\]
Indeed \(\theta(xz)_v=\theta(x)_v\cdot(pz_vp^{-1})\), both \(e_l\) and \(W_i\) are products over the places, and at each place the [[?c:Discrete series representation|discrete series]] kernel fixes the local Bessel function under right convolution, which is part of the hypothesis that the Bessel system has type \((l_v,kw_v)\) ([[?lean:New.Filling.IsDiscreteSeriesBessel.integral_dsKernel_mul|the kernel fixes the Bessel function]]).

*Grouping by cosets.* Write \(\Gamma\cong G_S(E)\) as the disjoint union of cosets \(q\,\mathsf U_c(M)\) and put \(F_q(g)=\sum_{u\in\mathsf U_c(M)}B_a(\tilde q\,u\,g)\) for a representative \(\tilde q\). By property 3 of \(B_a\) (applied to \(\delta g\), \(\delta\) a rational element), each such partial sum is \(W_i(\theta((\delta g)_\infty))\) times the indicator of a condition on the finite part of \(\delta g\); by (1) it is fixed by right convolution with \(e_l\) over \(G_\infty\) (which does not change finite parts). By the proposition on [[proofs/grh/spanning-unfolding-a/convergence-of-poincare-series|convergence]], \(\sum_q\lvert F_q(g)\rvert\le\sum_\gamma\lvert B_a(\gamma g)\rvert\le C\) and \(\sum_\gamma B_a(\gamma g)=\sum_qF_q(g)\).

*Conclusion.* \(B_a\) is measurable and right \(J_M\)-invariant, and \(e_l\) is an [[?c:Idempotent element|idempotent]] kernel (part of the fitting hypothesis). The general theorem on Poincaré series ([[?lean:New.Space.exists_form_eq_tsum|forms from Poincaré series]]: if \(\sum_\gamma c(\gamma g)=\sum_iW_i(g)\) with \(c\) right \(K\)-invariant and \(\sum_i\lvert W_i\rvert\) bounded, then \(\sum_i(W_i*e)\) is a form of type \(e\) fixed by \(K\)) shows that \(\sum_q(F_q*e_l)=\sum_qF_q=\sum_\gamma B_a(\gamma\,\cdot)\) is a form of type \(e_l\) and level \(J_M\).

The Poincaré map is defined on the standard basis by these forms and extended linearly; evaluating at \(g\) is linear, so \(\mathcal P(\varphi)(g)=\sum_a\varphi_a\sum_\gamma B_a(\gamma g)=\mathcal P_\varphi(g)\).

## References

1. Lean: `New.Filling.Fits.exists_levelSpace_tsum_cutBessel_eq` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
2. Lean: `New.Filling.Fits.poincareMap` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
3. Lean: `New.Filling.Fits.coe_poincareMap` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
4. Lean: `New.Filling.Fits.integral_typeKernel_mul_besselFn` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
5. Lean: `New.Filling.Fits.realConv_tsum_cutBessel_classUnipotent` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
