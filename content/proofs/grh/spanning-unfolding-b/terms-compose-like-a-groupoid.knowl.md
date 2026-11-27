+++
id = "proofs/grh/spanning-unfolding-b/terms-compose-like-a-groupoid"
title = "Terms over blocks compose like a groupoid"
kind = "lemma"
summary = "Products and inverses of terms over blocks are terms over the composed and inverse blocks, and a term has the reduction of an integral element exactly when it lies in its coset of the principal level."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.termsOver.mul", "New.Filling.termsOver.inv", "New.Filling.mem_termsOver_reduction_iff"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] with [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|terms over blocks]] \(\mathcal{T}(c,s,c')\), where \(c,c'\) are classes and \(s\in\bar G\).

1. If \(\gamma\in\mathcal{T}(c,s,c')\) and \(\delta\in\mathcal{T}(c',t,c'')\), then \(\gamma\delta\in\mathcal{T}(c,st,c'')\).
2. If \(\gamma\in\mathcal{T}(c,s,c')\), then \(\gamma^{-1}\in\mathcal{T}(c',s^{-1},c)\).
3. For \(k\) in the [[proofs/grh/spanning-unfolding-b/filling-level-and-reduction|lattice stabiliser \(K\)]] and \(\gamma\in G(E)\): \(\gamma\in\mathcal{T}(c,\bar k,d)\) if and only if \(k^{-1}h_c^{-1}\gamma_{\mathrm{fin}}h_d\in K(M)\).

## Proof

Write \(\tau_{c,c'}(\gamma)=h_c^{-1}\gamma_{\mathrm{fin}}h_{c'}\). Since \(\gamma\mapsto\gamma_{\mathrm{fin}}\) is a homomorphism, \(\tau_{c,c'}(\gamma)\,\tau_{c',c''}(\delta)=\tau_{c,c''}(\gamma\delta)\) and \(\tau_{c,c'}(\gamma)^{-1}=\tau_{c',c}(\gamma^{-1})\). (1) and (2) follow because \(K\) is a group and the reduction \(K\to\bar G\) is a homomorphism.

(3) If \(\tau_{c,d}(\gamma)=k'\in K\) with \(\bar k'=\bar k\), then \(k^{-1}k'\in K\) reduces to \(1\), so it lies in \(K(M)\). Conversely, if \(k^{-1}\tau_{c,d}(\gamma)=k'\in K(M)\), then \(\tau_{c,d}(\gamma)=kk'\in K\) has reduction \(\bar k\cdot1\).

## References

1. Lean: `New.Filling.termsOver.mul`, `New.Filling.termsOver.inv`, `New.Filling.mem_termsOver_reduction_iff` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`.
