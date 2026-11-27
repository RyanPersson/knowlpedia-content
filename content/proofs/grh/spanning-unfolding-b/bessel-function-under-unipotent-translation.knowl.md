+++
id = "proofs/grh/spanning-unfolding-b/bessel-function-under-unipotent-translation"
title = "Transformation of the Bessel function under rational unipotent elements"
kind = "lemma"
summary = "Left translation by the real image of a rational unipotent element multiplies the product Bessel function by the inverse of the finite unipotent character."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.besselFn_adelicToInf_mul_eq_prod_wave_smul", "New.Filling.besselFn_ratToInf_mul"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] and \(W\colon G_\infty\to\mathbb{C}^I\) the [[proofs/grh/spanning-unfolding-b/filling-amplitude|Bessel function]] of either side (full or cut).

1. If \(x\in G(\mathbb{A})\) lies in the Bessel unipotent group, then for all \(y\in G_\infty\)
\[
W(x_\infty y)=\Bigl(\prod_v\operatorname{wave}\bigl(\sigma((x_\infty)_v)\bigr)\Bigr)\,W(y).
\]
2. If \(\gamma\in G(E)\) lies in the Bessel unipotent group, then \(W(\gamma_\infty y)=\psi_{\mathsf U}(\gamma_{\mathrm{fin}})^{-1}\,W(y)\) for all \(y\).

## Proof

(1) Each component \((x_\infty)_v=D_v^{-1}x_vD_v\) lies in the Bessel unipotent group of \(G_1\): the entries of \(x_v\) on and below the block diagonal are those of the identity, and conjugation by a diagonal matrix preserves this. Each local function \(W_v\) of a Bessel system is a [[?lean:New.IsBesselFunction|Bessel function]], which includes the law \(W_v(ng)=\operatorname{wave}(\sigma(n))\,W_v(g)\) for \(n\) in the Bessel unipotent group of \(G_1\). Taking the product over \(v\) of the coordinates \(W_{v,i_v}\) gives the claim.

(2) Apply (1) to the adelic image of \(\gamma\) and use [[proofs/grh/spanning-unfolding-b/unipotent-character-at-infinity|the character at infinity]]: the product of waves is \(\overline{\psi_{\mathsf U}(\gamma_{\mathrm{fin}})}=\psi_{\mathsf U}(\gamma_{\mathrm{fin}})^{-1}\).

## References

1. Lean: `New.Filling.besselFn_adelicToInf_mul_eq_prod_wave_smul`, `New.Filling.besselFn_ratToInf_mul` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`.
