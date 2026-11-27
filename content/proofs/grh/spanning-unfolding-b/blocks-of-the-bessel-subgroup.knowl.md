+++
id = "proofs/grh/spanning-unfolding-b/blocks-of-the-bessel-subgroup"
title = "Blocks of the Bessel subgroup"
kind = "theorem"
summary = "A rational element of the Bessel subgroup acts on the Bessel function by a unitary matrix; the amplitude sums of the Bessel subgroup over a block are the unipotent covolume times this matrix, and translating a stable set by such an element multiplies its blocks by the adjoint matrix."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.amplitudeSum_besselS_apply", "New.Filling.amplitudeSum_besselS_inv", "New.Filling.amplitudeSum_mul_inv_apply", "New.Filling.exists_unitary_besselFn_mul", "New.Filling.besselFn_mul_of_eq_embedH", "New.Filling.amplitudeSum_besselS_eq_zero", "New.Filling.isStable_compl_besselS"]
lean_files = ["src/New/Spanning/Unfolding/SquareExpansion.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) contain a primitive \(5040\)-th root of unity and let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\). Let \(W\) be the full [[proofs/grh/spanning-unfolding-b/filling-amplitude|Bessel function]], \(A_T(c,s,c')\in\mathbb{C}^{I\times I}\) the amplitude sums for the full side, \(\nu=\operatorname{cov}_{\mathsf U}\) the [[proofs/grh/spanning-unfolding-b/filling-constants|unipotent covolume]] and \(\mathsf{S}=\mathsf{S}(E)\) the rational Bessel subgroup.

1. *(For either side.)* For every \(\gamma\in\mathsf{S}\) there is a unitary matrix \(M_\gamma\) on \(\mathbb{C}^I\) with \(W(\gamma_\infty y)=M_\gamma W(y)\) for all \(y\in G_\infty\). If \(\gamma=u\tilde\eta\) with \(u\in\mathsf{U}(E)\) and \((\tilde\eta_\infty)_v\) the image of \(k_v\in U(\kappa)\), then \(M_\gamma=\psi_{\mathsf U}(u_{\mathrm{fin}})^{-1}\bigotimes_v\operatorname{rep}_v(k_v)\), with \(\operatorname{rep}_v\) the representation of the Bessel system at \(v\).
2. If \(s\notin\bar R_0\), then \(A_{\mathsf{S}}(c,s,c')=0\) for all \(c,c'\) (either side).
3. If \(\gamma\in\mathsf{S}\) is a term over \((c,s,c')\) and \(W(\gamma_\infty y)=MW(y)\) for all \(y\), then for every class \(d\)
\[
A_{\mathsf{S}}(c,s,d)_{(i,j)}=\begin{cases}\nu\,M_{ij}&d=c',\\0&d\ne c'.\end{cases}
\]
4. \(A_{\mathsf{S}}(d,s^{-1},c)_{(j,i)}=\overline{A_{\mathsf{S}}(c,s,d)_{(i,j)}}\).
5. Let \(T\subset G(E)\) be stable with \(\gamma\in T\iff\gamma\delta^{-1}\in T\), where \(\delta\in\mathsf{S}\) is a term over \((d,t,d')\) with \(W(\delta_\infty y)=N\,W(y)\). Then
\[
A_T(c,st^{-1},d)_{(i,j)}=\sum_{k\in I}\overline{N_{jk}}\,A_T(c,s,d')_{(i,k)} .
\]
6. The complement of \(\mathsf{S}\) in \(G(E)\) is stable.

## Proof

(1) Write \(\gamma=u\tilde\eta\) ([[?lean:New.mem_besselS|decomposition of the Bessel subgroup]]). Each \((\tilde\eta_\infty)_v\) fixes the basis vectors outside \(X_0\), so it is the image of some \(k_v\in U(\kappa)\). By [[proofs/grh/spanning-unfolding-b/bessel-function-under-unipotent-translation|the unipotent transformation law]], \(W(u_\infty y')=\psi_{\mathsf U}(u_{\mathrm{fin}})^{-1}W(y')\); and each local function satisfies \(W_v(k_vg)=\operatorname{rep}_v(k_v)W_v(g)\) ([[?lean:New.IsBesselFunction|Bessel function]]), so the product function transforms by the Kronecker product. A scalar of modulus one times a Kronecker product of unitary matrices is unitary.

(2) If \(\gamma\in\mathsf{S}\) is a term over \((c,s,c')\), then \(h_c^{-1}\gamma_{\mathrm{fin}}h_{c'}\in K\cap\mathsf{S}\) ([[proofs/grh/spanning-unfolding-b/terms-of-cell-rank-zero-are-scalar-multiples-of-the-bessel-subgroup|part 4 of the theorem on scalar multiples]]) has reduction \(s\in\bar R_0\). So for \(s\notin\bar R_0\) the sum is empty.

(3) The Bessel kernel satisfies \(\mathcal{K}_{\gamma\delta}(\gamma_\infty y)_{(a,b)}=W_a(\gamma_\infty y)\overline{W_b(\delta_\infty^{-1}y)}=\sum_kM_{ak}\,\mathcal{K}_\delta(y)_{(k,b)}\), i.e. it is \(L=M\otimes1\) applied to \(\mathcal{K}_\delta(y)\). By the [[?lean:New.Filling.amplitudeSum_mul_mul_inv|block-moving lemma]] (for the stable set \(\mathsf{S}\), with \(\sigma=\gamma\) over \((c,s,c')\) and \(\sigma'=1\) over \((d,1,d)\); \(\mathsf{S}\) is [[?lean:New.Filling.isStable_besselS|stable]] and \(\gamma\delta\in\mathsf{S}\iff\delta\in\mathsf{S}\)), \(L\) takes the block over \((c',1,d)\) to the block over \((c,s,d)\). The block over \((c',1,d)\) is \(\nu\) times the identity matrix if \(c'=d\) and \(0\) otherwise ([[?lean:New.Filling.amplitudeSum_besselS_one_eq_ite|identity block of the Bessel subgroup]]). Applying \(L\) gives the formula.

(4) If no element of \(\mathsf{S}\) is a term over \((c,s,d)\), then none is a term over \((d,s^{-1},c)\) ([[proofs/grh/spanning-unfolding-b/terms-compose-like-a-groupoid|inverses of terms]]), and both sides are \(0\). Otherwise let \(\gamma\) be such a term, with unitary \(M\) from (1); then \(\gamma^{-1}\) is a term over \((d,s^{-1},c)\) acting by \(M^{-1}=M^*\), and by (3) both sides equal \(\nu\,\overline{M_{ij}}\).

(5) Here \(\mathcal{K}_{\gamma\delta^{-1}}(y)_{(a,b)}=W_a(y)\overline{W_b(\delta_\infty\gamma_\infty^{-1}y)}=\sum_k\overline{N_{bk}}\,\mathcal{K}_\gamma(y)_{(a,k)}\), i.e. \(L=1\otimes\bar N\). Apply the block-moving lemma with \(\sigma=1\) over \((c,1,c)\) and \(\sigma'=\delta\) over \((d,t,d')\): \(L\) takes the block over \((c,s,d')\) to that over \((c,st^{-1},d)\).

(6) Stability of \(\mathsf{S}\) means \(u^{-1}\gamma u'\in\mathsf{S}\iff\gamma\in\mathsf{S}\); negate both sides.

## References

1. Lean: `New.Filling.amplitudeSum_besselS_apply`, `New.Filling.amplitudeSum_besselS_inv`, `New.Filling.amplitudeSum_mul_inv_apply`, `New.Filling.exists_unitary_besselFn_mul`, `New.Filling.besselFn_mul_of_eq_embedH` in `src/New/Spanning/Unfolding/SquareExpansion.lean`.
