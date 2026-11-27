+++
id = "proofs/grh/spanning-unfolding-a/petersson-products-of-poincare-series"
title = "Petersson products of translated Poincaré series are amplitude sums"
kind = "theorem"
summary = "For a = (c, i), a' = (c', i') and an integral k with reduction s, the Petersson product of k P_a' with P_a is vol(J_M) times the (i, i') entry of the full amplitude sum over all terms of the block (c, s, c')."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.petersson_poincare", "New.Filling.Fits.mem_principalLevel_iff_mem_termsOver", "New.Filling.Fits.amplitudeSum_apply_eq_integral_tsum", "New.Filling.Fits.hasLevel_mul_right"]
lean_files = ["src/New/Spanning/Unfolding/PoincareSeries.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], and \(V\) a space [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fitting]] \(S\). For a pair \(a\) let \(\mathcal P_a=\mathcal P(\mathbf e_a)\) be the image of the basis vector under the [[proofs/grh/spanning-unfolding-a/poincare-series-are-forms|Poincaré map]]. Let \(a=(c,i)\), \(a'=(c',i')\), and let \(k\in G_f\) be integral (in the [[?lean:New.stdLevel|standard level]] \(K_0\)) with reductions \(s=(s_w)\) at the chosen places. Then, for the [[?lean:New.Space.petersson|Petersson product]] \(\langle F,F'\rangle=\int_{\Gamma\backslash G}\overline FF'\) and the right translation action of \(G_f\) on forms,
\[
\bigl\langle k\cdot\mathcal P_{a'},\ \mathcal P_a\bigr\rangle=\operatorname{vol}(J_M)\cdot A^{\mathrm{full}}_{\mathrm{all}}(c,s,c')_{(i,i')},
\]
where \(A^{\mathrm{full}}_{\mathrm{all}}(c,s,c')=\sum_{\gamma\in\mathcal T(c,s,c')}\int\beta_c(y)\beta_{c'}(\gamma^{-1}y)\,W(y)\otimes W(\gamma^{-1}y)^{*}\,dy\) is the [[?lean:New.Filling.amplitudeSum|block sum]] of the set of all rational [[?c:Isometry of a hermitian space|isometries]], for the full Bessel function.

## Proof

Let \(z=k\cdot\mathcal P_{a'}\), \(z(g)=\mathcal P_{a'}(g\,(1,k))\).

*Level.* \(J_M\) is normal in \(K_0\) (it is the kernel of the reductions), so \(z\), and its complex conjugate, are right \(J_M\)-invariant: \(g(1,u)(1,k)=g(1,k)(1,k^{-1}uk)\).

*Value on the class points.* For \(x\in G_\infty\), with \(y=\theta(x)\),
\[
z(x,x_c)=\sum_{\gamma\in\mathcal T(c,s,c')}\beta_{c'}(\gamma^{-1}y)\,W_{i'}(\gamma^{-1}y).\tag{1}
\]
Indeed \(z(x,x_c)=\sum_\gamma B_{a'}(\gamma^{-1}(x,x_ck))\), the sum over all rational \(\gamma\). By property 1 of the [[proofs/grh/spanning-unfolding-a/poincare-series-of-bessel-functions|cut-off Bessel function]], the term of \(\gamma^{-1}\) is \(\beta_{c'}(\gamma^{-1}y)W_{i'}(\gamma^{-1}y)\) if \(h_{c'}^{-1}\gamma_f^{-1}\iota(\eta)\psi(x_ck)\in K(M)\) and \(0\) otherwise. Now \(\iota(\eta)\psi(x_c)=h_c\) and \(\psi(k)\in K\) has reduction \(s\). For \(m\in K\) of reduction \(s\): \(h_{c'}^{-1}\gamma_f^{-1}h_c\,m=(h_c^{-1}\gamma_fh_{c'})^{-1}m\) lies in \(K(M)\) if and only if \(h_c^{-1}\gamma_fh_{c'}\in K\) with reduction \(s\), i.e. \(\gamma\in\mathcal T(c,s,c')\) (\(K(M)\) is the kernel of the reduction on \(K\)).

*Folding.* The conjugate \(\bar z\) is a form (a bounded automorphic function) of level \(J_M\). By the theorem on [[proofs/grh/spanning-unfolding-a/folding-of-poincare-series|folding]] with \(\varphi=\mathbf e_a\),
\[
\langle z,\mathcal P_a\rangle=\int_{\Gamma\backslash G}\bar z\,\mathcal P_{\mathbf e_a}=\operatorname{vol}(J_M)\int_{G_\infty}\beta_c(\theta(x))\,W_i(\theta(x))\,\overline{z(x,x_c)}\,dx .
\]
Since \(\theta\) preserves [[harmonic-analysis/haar-measure|Haar measure]], by (1) this is \(\operatorname{vol}(J_M)\int\sum_\gamma\beta_c(y)\beta_{c'}(\gamma^{-1}y)W_i(y)\overline{W_{i'}(\gamma^{-1}y)}\,dy\).

*Exchange.* The sum over \(\gamma\) of the integrals of the norms of the integrands is finite by the theorem on [[proofs/grh/spanning-unfolding-a/convergence-of-block-sums|convergence of block sums]], so the \((i,i')\) entry of the block sum, a sum of integrals, equals the integral of the sum ([[?c:Dominated convergence theorem|dominated convergence]] for series). This gives the claim.

## References

1. Lean: `New.Filling.Fits.petersson_poincare` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
2. Lean: `New.Filling.Fits.mem_principalLevel_iff_mem_termsOver` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
3. Lean: `New.Filling.Fits.amplitudeSum_apply_eq_integral_tsum` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
4. Lean: `New.Filling.Fits.hasLevel_mul_right` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
