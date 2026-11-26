+++
id = "proofs/grh/upper-objects/block-datum-laws"
title = "Laws of the block datum"
kind = "lemma"
summary = "The block datum is a sum of translates of the identity block datum over the product of GL_r of the residue fields at Q, and it is an eigenvector of the level under the Weil representation."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.residueBlockDatum_eq_sum", "New.DescentPair.blockDatum_eq_sum_modDatum", "New.DescentPair.residueBlockDatum_inv_mul_mul", "New.DescentPair.omega_blockDatum_eq_smul", "New.DescentPair.charV_detFin_eq_prod"]
lean_files = ["src/New/UpperBound/Objects/AuxiliaryPair.lean"]
proof_status = "outline"
+++

Let \(O\) be a [[proofs/grh/upper-objects/descent-pair|descent pair]], \(\Psi_{\mathrm{bl}}\) its [[proofs/grh/upper-objects/block-datum|block datum]], \(\Psi^1\) the identity block indicator, and \(\omega\) the Weil representation of the theta kernel of \((W,V)\) with the characters \(\nu_W,\nu_V\). Write \(K_0(W)\), \(K_0(V)\) for the standard maximal compact subgroups of the finite adelic points.

**Lemma.**

1. *(Residues.)* \(\Psi_{\mathrm{bl}}(X)=\sum_{A}\mathbf 1\big[X_w=\iota_u\ (w\in M),\ (X_w)_u=A_w\ (w\in Q)\big]\prod_{w\in Q}\psi_w(\det A_w)\), the sum over \(A\in\prod_{w\in Q}\mathrm{GL}_r(k_w)\).
2. *(Sum of translates.)* \(\Psi_{\mathrm{bl}}\otimes\mathrm{vac}=\sum_{A}\omega\big(\tilde A,1\big)\big(\Psi^1\otimes\mathrm{vac}\big)\), where \(\tilde A\in K_0(W)\) is a chosen element reducing to \(A_w^{-1}\) at the places of \(Q\) and to \(1\) at those of \(M\).
3. *(Residues, equivariance.)* Let \(k,k'\) be families of invertible residue matrices of sizes \(r,n\) and \(j\in\bar K_O\) with \(k'_w=\operatorname{diag}(k_w,1)\,j_w\) at \(M\) and \(k'_w=j_w\) at \(Q\). Then
\[
\Psi_{\mathrm{bl}}\big((k'^{-1}_wX_wk_w)_w\big)=\chi_O(j)\prod_{w\in Q}\psi_w(\det k_w)\cdot\Psi_{\mathrm{bl}}(X),
\]
with \(\chi_O\) the residue level character.
4. *(Level.)* If \(k\in K_0(W)\), \(k'\in K_0(V)\) and \(j\in\bar K_O\) satisfy \(\bar k'=\operatorname{diag}(\bar k,1)_M\cdot j\) (reductions at \(M\sqcup Q\), the first factor being \(1\) at \(Q\)), then
\[
\omega(k,k')\big(\Psi_{\mathrm{bl}}\otimes\mathrm{vac}\big)=\Big(\prod_{w\in M}\psi_w(\det\bar k_w)\Big)^{-1}\chi_O(j)\cdot\Psi_{\mathrm{bl}}\otimes\mathrm{vac}.
\]

## Proof

*1.* If all blocks \((X_w)_u\), \(w\in Q\), are invertible, exactly one \(A\) matches and its term is the value of \(\Psi_{\mathrm{bl}}\). If some block is singular, no \(A\) matches and \(\psi_w\) of its determinant is \(0\).

*3.* Supports: at \(w\in M\), \(j_w\iota_u=\iota_u\) and \(\operatorname{diag}(k_w,1)\iota_u=\iota_uk_w\), so \(k'^{-1}_wX_wk_w=\iota_u\) iff \(X_w=\iota_u\). Values: at \(w\in Q\), since \(j_w^{-1}\) is block triangular, the rows \(u\) of \(j_w^{-1}X_wk_w\) are \((j_w^{-1})_{00}\,(X_w)_u\,k_w\); take determinants and note \(\chi_O(j)=\prod_{w\in Q}\psi_w(\det (j_w^{-1})_{00})\).

*2 and 4* are obtained from 1 and 3 by the formula for the action of \(K_0(W)\times K_0(V)\) on a datum that is a function of residues modulo a modulus tensored with the vacuum: \(\omega(k,k')\) replaces the function \(x\mapsto f(x)\) by \(x\mapsto\nu_W(\det k')\,\nu_V(\det k)^{-1}f(\bar k'^{-1}x\bar k)\). This formula is the Lean lemma `New.pairWeil_modDatum_stdLevel` of another area and is only cited here. One also uses that \(\nu_W\circ\det\) is trivial on integral points and that \(\nu_V(\det k)=\prod_{w\in M\sqcup Q}\psi_w(\det\bar k_w)\) for \(k\in K_0(W)\) (from the weight and tame part of \(\mu\), with \(\psi_w=1\) off \(M\sqcup Q\); Lean: `New.DescentPair.charV_detFin_eq_prod`, resting on `New.AutChar.HasWeight.apply_det_eq_prod`). In 2 the scalar \(\nu_V(\det\tilde A)^{-1}=\prod_{w\in Q}\psi_w(\det A_w)\) appears; in 4 the factors at \(Q\) of \(\nu_V(\det k)^{-1}\) cancel against \(\prod_{w\in Q}\psi_w(\det\bar k_w)\) from 3. \(\square\)

## References

1. Lean: `New.DescentPair.blockDatum_eq_sum_modDatum`, `New.DescentPair.omega_blockDatum_eq_smul` in `src/New/UpperBound/Objects/AuxiliaryPair.lean`.
