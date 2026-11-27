+++
id = "proofs/grh/spanning-unfolding-b/hilbert-schmidt-norms-of-the-blocks"
title = "Hilbert–Schmidt norms of the translated Gram operators"
kind = "lemma"
summary = "For a map with amplitude blocks, the squared Hilbert–Schmidt norms of P* s P and of its difference with the twisted translation are the second moments at s of all terms and of the terms off the Bessel subgroup."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.HasAmplitudeBlocks.hilbertSchmidtNorm_sq_eq_secondMoment", "New.Filling.HasAmplitudeBlocks.hilbertSchmidtNorm_sub_besselTranslate_sq", "New.Filling.hasAmplitudeBlocks_smul_of_inner_eq", "New.Filling.hilbertSchmidtNorm_one_sq_eq_sourceDim", "New.Filling.finrank_source_eq_sourceDim"]
lean_files = ["src/New/Spanning/Unfolding/Moments.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]], \(\rho\) a representation of \(\bar G\) on a finite-dimensional inner product space \(V\), \(P\colon\mathcal{X}\to V\) linear, \(P_s=P^*\rho(s)P\), and \(\lVert\cdot\rVert\) the [[?lean:New.hilbertSchmidtNorm|Hilbert–Schmidt norm]].

1. If \(\langle\rho(s)Pe_y,Pe_x\rangle=c\,A(c_x,s,c_y)_{(i_x,i_y)}\) for a real \(c>0\) and all \(s,x,y\), then \((c\nu)^{-1/2}P\) [[proofs/grh/spanning-unfolding-b/amplitude-blocks|has amplitude blocks]].
2. If \((\rho,P)\) has amplitude blocks, then \(\lVert P_s\rVert^2=\mathsf{E}(A_{G(E)},\{s\})\), the [[?lean:New.Filling.secondMoment|second moment]] at \(s\) of all terms.
3. If moreover \(E\) contains a primitive \(5040\)-th root of unity and \(S\) is admissible, then \(\lVert P_s-r_\psi(s)\rVert^2=\mathsf{E}(A_{G(E)\setminus\mathsf{S}},\{s\})\), with the [[proofs/grh/spanning-unfolding-b/bessel-translate|twisted translation]] \(r_\psi(s)\).
4. \(\lVert1_{\mathcal{X}}\rVert^2=\dim\mathcal{X}=\dim_S\).

## Proof

(1) Scaling \(P\) by the real number \(\lambda=(c\nu)^{-1/2}\) multiplies the inner products by \(\lambda^2=1/(c\nu)\). (2) The squared Hilbert–Schmidt norm is the sum of the squared absolute values of the matrix entries in orthonormal bases; the entries of \(P_s\) are \(\langle P_se_y,e_x\rangle=\langle\rho(s)Pe_y,Pe_x\rangle=A(c,s,c')_{(i,j)}/\nu\), and \(\sum_{i,j}\lvert A(c,s,c')_{(i,j)}\rvert^2=\lVert A(c,s,c')\rVert^2\). (3) By [[?lean:New.Filling.amplitudeSum_eq_inter_compl_add_inter|additivity of amplitude sums]], \(A_{G(E)}=A_{G(E)\setminus\mathsf{S}}+A_{\mathsf{S}}\), and the entries of \(r_\psi(s)\) are \(\langle r_\psi(s)e_y,e_x\rangle=A_{\mathsf{S}}(c,s,c')_{(i,j)}/\nu\); subtract and argue as in (2). (4) is the count of basis vectors.

## References

1. Lean: `New.Filling.HasAmplitudeBlocks.hilbertSchmidtNorm_sq_eq_secondMoment`, `New.Filling.HasAmplitudeBlocks.hilbertSchmidtNorm_sub_besselTranslate_sq`, `New.Filling.hasAmplitudeBlocks_smul_of_inner_eq` in `src/New/Spanning/Unfolding/Moments.lean`.
