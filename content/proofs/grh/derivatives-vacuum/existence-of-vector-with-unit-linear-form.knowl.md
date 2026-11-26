+++
id = "proofs/grh/derivatives-vacuum/existence-of-vector-with-unit-linear-form"
title = "One of two explicit vectors has a unit linear form at each prime"
kind = "lemma"
summary = "At every p-adic place either 1 or zeta times the last dual vector has a unit linear form."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.exists_hasUnitLinearForm", "New.Parameters.norm_map_zeta_mul_dualVector"]
lean_files = ["src/New/Derivatives/Vacuum/ShortVectors.lean"]
proof_status = "full"
+++

**Lemma.** For every prime \(p\) and \(p\)-adic place \(\iota_p\) of \(\mathbb{C}\), one of the vectors \(y=1\), \(y=\zeta\,e_{\varphi(q_1)-1}\) (with \(e_i\) the [[proofs/grh/derivatives-vacuum/dual-vectors|dual vectors]]) [[proofs/grh/derivatives-vacuum/unit-linear-form|has a unit linear form]] at \(\iota_p\).

## Proof

Let \(\varphi_\tau(y)=\iota_p(\overline{\Phi_\tau(y)})\) be the weight embeddings. The prime of \(E\) induced by \(\varphi_\tau\) contains \(\beta\) iff \(\lvert\iota_p(\bar\beta)\rvert_p<1\) (here \(\bar\beta=(1-i\sqrt d)/2\in\mathbb{C}\)); this does not depend on \(\tau\). By [[proofs/grh/derivatives-vacuum/p-adic-size-of-period-factor|the size of the period factor]] and the formula for \(\widehat\varphi_\tau(\alpha)\) in [[proofs/grh/derivatives-vacuum/p-adic-size-of-vacuum-root|the size of the vacuum root]],
\[ \lvert\iota_p\varpi\rvert_p=\begin{cases}1&\lvert\iota_p\bar\beta\rvert_p\ge1,\\ \lvert\varphi_\tau(g)\rvert_p&\lvert\iota_p\bar\beta\rvert_p<1.\end{cases} \]
In the first case \(y=1\) works. In the second case, \(Q\) being monic of degree \(\varphi(q_1)-1\), \(y=\zeta e_{\varphi(q_1)-1}=\zeta\bar\beta^{\,j}/g\). At the prime of \(\varphi_\tau\), which contains \(\beta\), the element \(\bar\beta=1-\beta\) is a unit, and \(\zeta\) is a root of unity; so \(\lvert\varphi_\tau(y)\rvert_p=\lvert\varphi_\tau(g)\rvert_p^{-1}\) and \(\lvert\iota_p(\varpi\overline{\Phi_\tau(y)})\rvert_p=1\).

## References

1. Lean: `New.Parameters.exists_hasUnitLinearForm`, `New.Parameters.norm_map_zeta_mul_dualVector` in `src/New/Derivatives/Vacuum/ShortVectors.lean`.
