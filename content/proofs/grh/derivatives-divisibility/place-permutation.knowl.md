+++
id = "proofs/grh/derivatives-divisibility/place-permutation"
title = "Automorphisms of C over K permute the embeddings of the CM type"
kind = "lemma"
summary = "An automorphism sigma of C over K carries the embedding of E chosen at the place v to the one chosen at the place obtained by multiplying v with the place of sigma composed with the base embedding."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.placePerm", "New.Parameters.apply_Phi_eq_Phi_placePerm"]
lean_files = ["src/New/Derivatives/Field/PrimeDecomposition.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E=K(\zeta)\) with the embeddings \(\Phi_v\) (see the [[proofs/grh/reduction-main/field-e-and-its-places|field \(E\)]]) and let \(\sigma\) be a field automorphism of \(\mathbb{C}\) fixing \(K\). Let \(v_0\in\Phi\) be the place induced by \(\sigma\circ\Phi_1\), and \(\operatorname{perm}_\sigma\colon\Phi\to\Phi\), \(v\mapsto v_0v\). Then
\[
\sigma\bigl(\Phi_v(x)\bigr)=\Phi_{\operatorname{perm}_\sigma(v)}(x)\qquad(v\in\Phi,\ x\in E).
\]

## Proof

\(\sigma\circ\Phi_1\) is an embedding of \(E\) over \(K\). Two embeddings over \(K\) inducing the same place are equal (they could only differ by complex conjugation, which is not the identity on \(K\)); hence \(\sigma\circ\Phi_1=\Phi_{v_0}\). Then \(\sigma\circ\Phi_v=\sigma\circ\Phi_1\circ\sigma_v=\Phi_{v_0}\circ\sigma_v=\Phi_{v_0v}\). \(\blacksquare\)

## References

1. Lean: `New.Parameters.placePerm`, `New.Parameters.apply_Phi_eq_Phi_placePerm` in `src/New/Derivatives/Field/PrimeDecomposition.lean`.
