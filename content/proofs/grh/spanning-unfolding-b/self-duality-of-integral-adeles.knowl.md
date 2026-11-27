+++
id = "proofs/grh/spanning-unfolding-b/self-duality-of-integral-adeles"
title = "Self-duality of the integral adeles for the self-dual character"
kind = "lemma"
summary = "The self-dual character of a filling datum is trivial on all integral multiples of a finite adele exactly when the adele is integral."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.forall_selfDualChar_mul_eq_one_iff", "New.Filling.selfDualChar_eq_one_of_mem"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\) and \(\psi_S(x)=\psi_f(-x/\varpi)\) its [[proofs/grh/spanning-unfolding-b/unipotent-character-agreement-stability|self-dual character]]. For a finite adele \(a\in\mathbb{A}_f\):
\[
\psi_S(ra)=1\ \text{for all }r\in\widehat{\mathcal{O}}\quad\Longleftrightarrow\quad a\in\widehat{\mathcal{O}} .
\]
In particular \(\psi_S\) is trivial on \(\widehat{\mathcal{O}}\).

## Proof

Put \(x=-a/\varpi\). Then \(\psi_S(ra)=\psi_f(rx)\). By the [[?lean:New.forall_ψf_mul_eq_one_iff|duality for \(\psi_f\)]], \(\psi_f(rx)=1\) for all \(r\in\widehat{\mathcal{O}}\) if and only if \(dx\in\widehat{\mathcal{O}}\) for every \(d\) in the [[?c:Different ideal|different]] \(\mathfrak{D}\) of \(E/\mathbb{Q}\). By hypothesis \(\mathfrak{D}=\varpi\mathcal{O}_E\), and for \(d=r\varpi\) with \(r\in\mathcal{O}_E\) one has \(dx=-ra\). So the condition is that \(ra\in\widehat{\mathcal{O}}\) for all \(r\in\mathcal{O}_E\), which is equivalent to \(a\in\widehat{\mathcal{O}}\) (take \(r=1\); conversely \(\mathcal{O}_E\subset\widehat{\mathcal{O}}\) and \(\widehat{\mathcal{O}}\) is a ring). The last assertion is the case \(r=1\).

## References

1. Lean: `New.Filling.forall_selfDualChar_mul_eq_one_iff`, `New.Filling.selfDualChar_eq_one_of_mem` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`.
