+++
id = "proofs/grh/spanning-unfolding-b/second-moments-of-the-poincare-operators"
title = "Second moments of the operators P* s P"
kind = "theorem"
summary = "For a map P with amplitude blocks: the operators P_s are close to the twisted translations near the reduced Bessel group, P is nearly an isometry, and the sum of the squared norms of all P_s is at most (1 + 9 b^(-4)) times the main second moment."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.HasAmplitudeBlocks.sum_hilbertSchmidtNorm_sub_besselTranslate_sq_le", "New.Filling.HasAmplitudeBlocks.hilbertSchmidtNorm_sub_one_sq_le", "New.Filling.HasAmplitudeBlocks.hilbertSchmidtNorm_adjoint_comp_sq_le", "New.Filling.HasAmplitudeBlocks.sum_hilbertSchmidtNorm_sq_le", "New.Filling.le_sourceDim_div_of_card_nsmul_le"]
lean_files = ["src/New/Spanning/Unfolding/Moments.lean"]
proof_status = "full"
+++

**Theorem (the two moment bounds).** Let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over a CM field \(E\) containing a primitive \(5040\)-th root of unity, and let \((\rho,P)\) [[proofs/grh/spanning-unfolding-b/amplitude-blocks|have amplitude blocks]], with \(V\) finite-dimensional, \(P_s=P^*\rho(s)P\), and Hilbert–Schmidt norms.

1. *(Near the Bessel subgroup.)* For \(i\in\{0,1\}\), with \(\Omega_i\) the set of \(s\in\bar G\) that agree with an element of \(\bar R_0\) at the chosen places above \(p_i\),
\[
\sum_{s\in\Omega_i}\lVert P_s-r_\psi(s)\rVert^2\le b^{-12}\,\mathcal{M}_{\mathrm{id}} .
\]
2. *(Near isometry.)* \(\lVert P^*P-1\rVert^2\le b^{-12}\dim_S\), and \(\lVert P^*P\rVert^2\le2\dim_S\).
3. *(Second moment.)* If moreover \(E\) carries [[?lean:New.WeilData|Weil data]] and \(\rho\) is unitary, then
\[
\sum_{s\in\bar G}\lVert P_s\rVert^2\le\bigl(1+9b^{-4}\bigr)\,\mathcal{M}_{\mathrm{main}} .
\]

## Proof

(1) By [[proofs/grh/spanning-unfolding-b/hilbert-schmidt-norms-of-the-blocks|the norms of the blocks]], the left side is \(\mathsf{E}(A_{G(E)\setminus\mathsf{S}},\Omega_i)\), which is bounded by [[proofs/grh/spanning-unfolding-b/second-moment-near-the-bessel-subgroup|the second moment near the Bessel subgroup]].

(2) Put \(D=P^*P-1\). For \(s\in\bar R_0\), [[proofs/grh/spanning-unfolding-b/equivariance-of-maps-with-amplitude-blocks|right equivariance]] gives \(P_s=P_1r_\psi(s)\), so \(P_s-r_\psi(s)=D\,r_\psi(s)\). Its norm is that of its adjoint \(r_\psi(s^{-1})D^*\), which equals \(\lVert D^*\rVert=\lVert D\rVert\) because \(r_\psi(s^{-1})\) is unitary ([[proofs/grh/spanning-unfolding-b/bessel-translate-is-a-unitary-representation|unitarity of \(r_\psi\)]]). As \(\bar R_0\subset\Omega_1\), part (1) gives \(\lvert\bar R_0\rvert\,\lVert D\rVert^2\le b^{-12}\mathcal{M}_{\mathrm{id}}=b^{-12}\lvert\bar R_0\rvert\dim_S\). For the second bound, \(\lVert D\rVert\le b^{-6}\sqrt{\dim_S}\le\tfrac13\lVert1\rVert\), so \(\lVert P^*P\rVert\le\tfrac43\lVert1\rVert\) and \(\lVert P^*P\rVert^2\le\tfrac{16}9\dim_S\).

(3) Let \(\beta(s)=\lVert P_s\rVert^2=\mathsf{E}(A_{G(E)},\{s\})\). It is of positive type: for the operators \(T_a=(\rho(a)P)(\rho(a)P)^*\) on \(V\), the Hilbert–Schmidt inner product is \(\langle T_a,T_b\rangle=\lVert P^*\rho(a^{-1}b)P\rVert^2=\beta(a^{-1}b)\) when \(\rho\) is unitary ([[?lean:New.inner_hilbertSchmidtVector_translate|inner products of translates]]). And \(\beta(1)=\lVert P^*P\rVert^2\le2\dim_S\) by (2). Now apply [[proofs/grh/spanning-unfolding-b/second-moment-over-the-whole-group|the second moment over the whole group]].

## References

1. Lean: `New.Filling.HasAmplitudeBlocks.sum_hilbertSchmidtNorm_sub_besselTranslate_sq_le`, `New.Filling.HasAmplitudeBlocks.hilbertSchmidtNorm_sub_one_sq_le`, `New.Filling.HasAmplitudeBlocks.sum_hilbertSchmidtNorm_sq_le` in `src/New/Spanning/Unfolding/Moments.lean`.
