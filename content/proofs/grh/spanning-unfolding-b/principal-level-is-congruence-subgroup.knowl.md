+++
id = "proofs/grh/spanning-unfolding-b/principal-level-is-congruence-subgroup"
title = "The principal level is the congruence subgroup modulo M"
kind = "lemma"
summary = "An integral finite adelic isometry reduces to the identity at all chosen places if and only if it is congruent to one modulo M; so the principal level is the unitary congruence subgroup of level M."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.principalLevel_eq_unitaryLevel", "New.Filling.reduction_eq_one_iff", "New.Filling.inv_ideleM_smul_mem_iff", "New.Filling.intGL_map_reduceAboveM", "New.Filling.exists_map_eq_of_mem_latticeStabilizer", "New.Filling.invAdjoint", "New.Filling.idOrInvAdjoint", "New.Filling.reduceAboveM", "New.Filling.idOrInvAdjoint_false", "New.Filling.idOrInvAdjoint_true", "New.Filling.reduceAboveM_false", "New.Filling.reduceAboveM_true", "New.Filling.ideleM_val", "New.Filling.ideleM_mem"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] with level \(M\), [[proofs/grh/spanning-unfolding-b/filling-level-and-reduction|lattice stabiliser \(K\), reduction \(k\mapsto\bar k\) and principal level \(K(M)\)]]. For \(k\in K\),
\[
\bar k=1\quad\Longleftrightarrow\quad M^{-1}(k-1)\ \text{has entries in }\widehat{\mathcal{O}} .
\]
Consequently \(K(M)\) is the [[?lean:New.unitaryLevel|unitary congruence subgroup]] of level \(M\): the isometries \(k\) of the Gram matrix \(J^{\mathrm{lat}}\) over \(\mathbb{A}_f\) such that \(k,k^{-1}\) are integral and \(M^{-1}(k-1)\) is integral.

## Proof

*Step 1: divisibility by \(M\).* For \(r\in\widehat{\mathcal{O}}\), \(M^{-1}r\in\widehat{\mathcal{O}}\) if and only if \(M\mid r\) in \(\widehat{\mathcal{O}}\), and by condition 4 of a filling datum this holds if and only if \(r\) and \(\bar r\) reduce to \(0\) modulo every chosen place \(w\). Call \(r\mapsto r\bmod w\) and \(r\mapsto\bar r\bmod w\) the two *reductions above \(M\)* attached to \(w\); both are ring homomorphisms \(\widehat{\mathcal{O}}\to\mathbb{F}_w\).

*Step 2: reduction at the conjugate.* Let \(k\in K\) and \(w\) a chosen place. Applying \(r\mapsto r\bmod w\) entrywise to \(k\) gives the component \(\bar k_w\) of \(\bar k\). Applying \(r\mapsto\bar r\bmod w\) entrywise gives
\[
\overline{k}^{\,\mathrm{conj}}_w=J_w^{-1}\,(\bar k_w)^{-\mathsf T}\,J_w ,
\]
where \(J_w\) is the Gram matrix in the lattice basis over \(\mathbb{F}_w\). Indeed \(k\) is an isometry with entries in \(\widehat{\mathcal{O}}\) (an integral element of \(G_{\mathrm{fin}}\) is the image of an isometry over the ring \(\widehat{\mathcal{O}}\), since \(J^{\mathrm{lat}}\) is [[proofs/grh/spanning-unfolding-b/lattice-middle-form-is-unimodular|unimodular]]), so \(k^{*}J^{\mathrm{lat}}=J^{\mathrm{lat}}k^{-1}\). Transposing, using that \(J^{\mathrm{lat}}\) is symmetric, and reducing modulo \(w\) gives \(J_w\cdot(\bar k^{\mathsf T}\bmod w)=(k^{-\mathsf T}\bmod w)\cdot J_w\), where \(\bar k^{\mathsf T}\) is the entrywise conjugate of \(k\); this is the displayed identity. The map \(s\mapsto J_w^{-1}s^{-\mathsf T}J_w\) is an automorphism of \(\mathrm{GL}_r(\mathbb{F}_w)\), so it sends \(s\) to \(1\) only for \(s=1\).

*Step 3.* By Step 2, \(\bar k=1\) if and only if both reductions above \(M\) at every chosen place send \(k\) to the identity matrix, that is, send every entry of \(k-1\) to \(0\). By Step 1, applied to each entry, this holds if and only if \(M^{-1}(k-1)\) is integral.

*Conclusion.* \(K(M)\) is the set of \(k\in K\) with \(\bar k=1\), which by Step 3 is the set of integral isometries congruent to \(1\) modulo \(M\).

## References

1. Lean: `New.Filling.principalLevel_eq_unitaryLevel`, `New.Filling.reduction_eq_one_iff`, `New.Filling.inv_ideleM_smul_mem_iff`, `New.Filling.intGL_map_reduceAboveM` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`.
