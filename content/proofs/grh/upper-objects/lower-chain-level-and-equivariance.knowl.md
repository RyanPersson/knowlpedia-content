+++
id = "proofs/grh/upper-objects/lower-chain-level-and-equivariance"
title = "Level, character and equivariance of the chain along the Y_j"
kind = "theorem"
summary = "Block upper triangular integral elements act on the image of the chain Y_0 to Y_m through an explicit product of tame characters and the action of the chosen group on Y_0; so the image has a known level and character, and the chain commutes with the chosen group."
aliases = ["last level", "last level character"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.algFormRep_lowerChain", "New.Data.formRep_liftY", "New.Data.formRep_lowerChainUpTo_eq_lowerChainUpTo_smul", "New.Data.lastResidueLevel", "New.Data.mem_lastResidueLevel", "New.Data.lastLevel", "New.Data.lastLevelChar", "New.Data.lowerChain_mem_levelSpace", "New.Data.lowerChainAtLevel", "New.Data.firstBlockLift", "New.Data.lowerChain_principalRep", "New.Data.det_eq_det_toBlocks₁₁_mul", "New.Data.det_toSquareBlock_toBlocks₁₁"]
lean_files = ["src/New/UpperBound/Objects/RowChain.lean"]
proof_status = "full"
+++

Let \(\Theta_\vartheta\) be the [[proofs/grh/upper-objects/lower-chain|chain along \(Y_0,\dots,Y_m\)]] for a tame character \(\vartheta\) with places \(Q\). The basis of \(Y_j\) is indexed by a block \(0\) of size \(r\) followed by blocks \(1,\dots,j\) of size \(t\). Let \(\psi_l\) be the tame part of the character \(\mu^0_{l+1}\vartheta^{l+1}\) of lift \(l+1\), and \(\bar G\) the [[proofs/grh/upper-objects/good-idempotent|group of the chosen places]] acting on forms of principal level on \(Y_0\).

**Theorem.**

1. *(Law of the chain.)* Let \(k\in K_0\) on \(Y_m\) have reductions \(g=(g_w)\) at the level places \(w\) (chosen places and \(Q\)) that are block upper triangular at every \(w\) and have block \(0\) equal to \(s_w\) at the chosen places, \(s\in\bar G\). Then for every form \(y\) of principal level on \(Y_0\)
\[
R(k)\,\Theta_\vartheta(y)=\Big(\prod_{w}\prod_{l<m}\psi_{l,w}\big(\det g_w^{(l+1)}\big)\Big)\cdot\Theta_\vartheta(s\cdot y),
\]
where \(g_w^{(l+1)}\) is the diagonal block \(l+1\) of \(g_w\).
2. *(Level and character.)* Let \(J_m\subseteq K_0\) be the group of elements that are \(1\) modulo the chosen places and block upper triangular modulo each place of \(Q\). Every \(k\in J_m\) multiplies \(\Theta_\vartheta(y)\) by \(\prod_w\prod_{l<m}\psi_{l,w}(\det\bar k_w^{(l+1)})\). So \(\Theta_\vartheta\) takes values in the algebraic forms on \(Y_m\) of level \(J_m\) with this character.
3. *(Equivariance.)* For \(s\in\bar G\), \(\Theta_\vartheta(s\cdot y)=R(\tilde s)\,\Theta_\vartheta(y)\), where \(\tilde s\in K_0\) on \(Y_m\) is a chosen element reducing to \(\operatorname{diag}(s,1)\) at the chosen places and to \(1\) at \(Q\).

## Proof

*One lift.* Let \(k\in K_0(Y_{j+1})\), \(k'\in K_0(Y_j)\) have reductions \(g,g'\) with \(g\iota=\iota g'\) at each level place. By the transformation law of the [[proofs/grh/upper-objects/point-datum-on-y|point datum]] and the equivariance of the theta lift, \(R(k)\operatorname{lift}_{j+1}(z)=\prod_w\frac{\psi_{j,w}(\det g_w)}{\psi_{j,w}(\det g'_w)}\cdot\operatorname{lift}_{j+1}(R(k')z)\) Here the equivariance of the lift of an arrow, \(R(k)\operatorname{Lift}(\phi)(z)=\operatorname{Lift}(\omega(k',k)\phi)(R(k')z)\), is the Lean statement `New.IsArrow.formRep_formLift` (cited), and the finite point acts on the datum only through its finite part.

*1.* Induction on \(j\le m\) for the composite of the first \(j\) lifts. A block upper triangular \(g\) on \(j+2\) blocks satisfies \(g\iota=\iota g_{11}\) with \(g_{11}\) its upper left corner on \(j+1\) blocks, which is again block upper triangular with the same first diagonal blocks, and \(\det g=\det g_{11}\cdot\det g^{(j+1)}\). Choose \(k'\in K_0(Y_j)\) whose reduction at every level place is the corner \(g_{11}\) of the reduction of \(k\) there: the level places are pairwise distinct and contain no conjugate pair, so the reduction of the integral unitary points onto the product of the groups \(\mathrm{GL}(\mathbb F_w)\) over these split places is surjective (Lean: `liftResidue`, `reduceFamily_liftResidue`, cited). Apply the one-lift law: the factor is \(\psi_{j,w}(\det g_w^{(j+1)})\). At \(j=0\): the forms of principal level are fixed by all integral points reducing to \(1\) at the chosen places, so any \(k\in K_0\) with reductions \(s\) at the chosen places acts as \(s\), whatever its reductions at \(Q\); and the scalar is an empty product. Translation commutes with the identification of forms on the definite space \(Y_m\) with algebraic forms (Lean: `toAlgForm_formRep`, cited).

*2.* Take \(s=1\) in 1.

*3.* Apply 1 to \(\tilde s\): its reductions are block diagonal with blocks \(l\ge1\) equal to \(1\), so the scalar is \(1\). \(\square\)

## References

1. Lean: `New.Data.algFormRep_lowerChain`, `New.Data.lowerChain_mem_levelSpace`, `New.Data.lowerChain_principalRep` in `src/New/UpperBound/Objects/RowChain.lean`.
