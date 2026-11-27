+++
id = "proofs/grh/spanning-unfolding-a/identity-block-of-the-bessel-subgroup"
title = "The identity block of the Bessel subgroup"
kind = "theorem"
summary = "For the full Bessel function, the block of the Bessel subgroup at s = 1 is the unipotent covolume times the identity if c = c', and 0 otherwise."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.amplitudeSum_besselS_one_eq_ite"]
lean_files = ["src/New/Spanning/Unfolding/AmplitudeSums.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity and \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]]. Let \(T_{\mathsf S}\) be the set of rational points of the [[?lean:New.Shape.Form.besselS|Bessel subgroup]]. For classes \(c,c'\) and tuples \(i,j\) of [[?lean:New.Filling.BesselCoord|Bessel coordinates]], the \((i,j)\) entry of the [[?lean:New.Filling.amplitudeSum|block sum]] for the full Bessel function at \(s=1\) is
\[
A^{\mathrm{full}}_{T_{\mathsf S}}(c,1,c')_{(i,j)}=\begin{cases}\operatorname{cov}_{\mathsf U}&\text{if }c=c'\text{ and }i=j,\\0&\text{otherwise,}\end{cases}
\]
with \(\operatorname{cov}_{\mathsf U}\) the [[?lean:New.Filling.unipotentCovolume|unipotent covolume]].

## Proof

A rational \(\gamma\) of the Bessel subgroup with \(h_c^{-1}\gamma h_{c'}\in K(M)\) (a term over \((c,1,c')\)) exists only if \(c=c'\), and then \(\gamma\in\mathsf U_c(M)\) ([[?lean:New.Filling.eq_and_mem_classUnipotent_of_besselS|terms of the Bessel subgroup at the identity]]). So for \(c\ne c'\) the sum is empty. Let \(c=c'\); the index set is \(X=\mathsf U_c(M)\).

*One term.* Let \(\varphi(\gamma,y)=\beta_c(y)\) if \(\gamma=1\) and \(0\) otherwise. For \(\gamma\in X\), in the orbit sum \(\sum_{(u,u')}\varphi(u\gamma u'^{-1},uy)\) only the pairs with \(u'=u\gamma\) contribute, giving \(\sum_u\beta_c(uy)=1\). \(T_{\mathsf S}\) is stable. By the theorem on [[proofs/grh/spanning-unfolding-a/change-of-weight-in-block-sums|change of weight]], the block sum is the single integral
\[
\int_{G_\infty}\beta_c(y)\,\mathcal K^{\mathrm{full}}_1(y)\,dy,\qquad\mathcal K_1^{\mathrm{full}}(y)_{(i,j)}=\prod_vF_v(y_v),\quad F_v(x)=W_{v,i_v}(x)\overline{W_{v,j_v}(x)},
\]
and the integrand is integrable.

*Unfolding.* \(F_v\) is left invariant under \(\mathsf U\): the Bessel function transforms by a character of modulus \(1\), which cancels against its conjugate. Unfolding over \(\mathsf U_\infty\) as in the lemma on [[proofs/grh/spanning-unfolding-a/unfolding-class-cutoff-against-invariant-weights|unfolding a class cutoff]] (complex-valued version, using integrability) and the integral \(\int_{\mathsf U_\infty}\beta_c(ux)\,du=\operatorname{cov}_{\mathsf U}\) gives
\[
\operatorname{cov}_{\mathsf U}\prod_v\int_{\mathsf U\backslash G_1}W_{v,i_v}\overline{W_{v,j_v}}\,d\dot x .
\]
*Orthonormality.* The coordinates of the full Bessel function are orthonormal in \(L^2(\mathsf U\backslash G_1)\): each local integral is \(1\) if \(i_v=j_v\) and \(0\) otherwise ([[?lean:New.BesselSystem.orthonormal|orthonormality of the Bessel coordinates]]). The product over \(v\) is \(1\) exactly when \(i=j\).

## References

1. Lean: `New.Filling.amplitudeSum_besselS_one_eq_ite` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
