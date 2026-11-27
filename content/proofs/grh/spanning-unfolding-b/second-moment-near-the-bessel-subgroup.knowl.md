+++
id = "proofs/grh/spanning-unfolding-b/second-moment-near-the-bessel-subgroup"
title = "The second moment near the Bessel subgroup"
kind = "theorem"
summary = "Over the residues that agree with the reduced Bessel group above one level prime, the second moment of the terms off the Bessel subgroup is at most b^(-12) times the identity second moment."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.secondMoment_compl_besselS_le", "New.Filling.M_div_b_le_levelPrime_sq"]
lean_files = ["src/New/Spanning/Unfolding/SquareExpansion.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) contain a primitive \(5040\)-th root of unity and let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\). For \(i\in\{0,1\}\) let
\[
\Omega_i=\{s\in\bar G:\ \exists\,t\in\bar R_0,\ s_w=t_w\ \text{for all chosen places }w\text{ above }p_i\}.
\]
Then, with the second moment \(\mathsf{E}\) and the amplitude sums \(A\) of the full side as in [[proofs/grh/spanning-unfolding-b/expansion-of-the-squares|the expansion of the squares]],
\[
\mathsf{E}\bigl(A_{G(E)\setminus\mathsf{S}},\Omega_i\bigr)\le b^{-12}\,\mathcal{M}_{\mathrm{id}} .
\]

## Proof

By [[proofs/grh/spanning-unfolding-b/residues-near-the-reduced-bessel-group|the lemma on residues near the reduced Bessel group]], \(\Omega_i\) avoids the scalar cosets, and every \(s\in\Omega_i\) has meet norm at least \(z=p_i^{2f}\ne0\). By the [[?lean:New.Filling.linkSecondMoment_le_of_le_meetNorm|bound for one link at a time]],
\[
\mathsf{E}_{\mathrm{link}}\bigl(\{\operatorname{disc}\ne0\},\Omega_i\bigr)\le C\nu^2,\qquad C=\Bigl(\frac{b^{2f}}{z}\Bigr)^{k}\mathcal{M}_{\mathrm{main}} .
\]
*Bound for \(C\).* Each level prime is at most \(b\) times the other (\(p_j\le b^{11}\le p_ib\)), so \(M=p_0p_1\le p_i^2b\), i.e. \(M/b\le p_i^2\) and \(z\ge(M/b)^f\). With condition 6 of admissibility, \(\mathcal{M}_{\mathrm{main}}\le(M/b^6)^{kf}\mathcal{M}_{\mathrm{id}}\):
\[
C\le\Bigl(\frac{b^{3f}}{M^f}\Bigr)^{k}\Bigl(\frac{M}{b^6}\Bigr)^{kf}\mathcal{M}_{\mathrm{id}}=b^{-3kf}\mathcal{M}_{\mathrm{id}}\le b^{-30}\mathcal{M}_{\mathrm{id}},
\]
as \(kf\ge40\). By the expansion of the squares,
\[
\sqrt{\mathsf{E}(A_{G(E)\setminus\mathsf{S}},\Omega_i)}\le\sqrt{b^{-30}\mathcal{M}_{\mathrm{id}}}+b^{-15}\sqrt{\mathcal{M}_{\mathrm{id}}}=2b^{-15}\sqrt{\mathcal{M}_{\mathrm{id}}} .
\]
Squaring, \(\mathsf{E}\le4b^{-30}\mathcal{M}_{\mathrm{id}}\le b^{-12}\mathcal{M}_{\mathrm{id}}\), since \(4\le b^{18}\).

## Remarks

In terms of the operators of [[proofs/grh/spanning-unfolding-b/second-moments-of-the-poincare-operators|the second moment theorem]], the left side is \(\sum_{s\in\Omega_i}\lVert P_s-r_\psi(s)\rVert^2\) in the Hilbert–Schmidt norm: the blocks of \(P_s\) are the conjugates of the amplitude sums of all terms, and those of \(r_\psi(s)\) come from the Bessel subgroup.

## References

1. Lean: `New.Filling.secondMoment_compl_besselS_le` in `src/New/Spanning/Unfolding/SquareExpansion.lean`.
