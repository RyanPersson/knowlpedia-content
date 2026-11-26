+++
id = "proofs/grh/derivatives-vacuum/p-adic-size-of-period-factor"
title = "The p-adic size of the period factor"
kind = "lemma"
summary = "The period factor has the p-adic absolute value of the vacuum root, makes the linear forms of lattice vectors p-integral, and is a p-adic unit when p does not divide q1."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.norm_iota_periodFactor", "New.Parameters.norm_periodFactor_mul_conj_le_one", "New.Parameters.norm_iota_periodFactor_eq_one"]
lean_files = ["src/New/Derivatives/Vacuum/TightFrames.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/p-adic-size-of-vacuum-root|the \(p\)-adic size of the vacuum root]]; \(\varpi=s_0/u\) is the [[proofs/grh/derivatives-vacuum/jet-scale|period factor]].

**Lemma.** Let \(\iota_p\) be a \(p\)-adic place of \(\mathbb{C}\) and \(\tau\) an infinite place of \(E\).

1. \(\lvert\iota_p(\varpi)\rvert_p=\lvert\widehat\varphi_\tau(\alpha)\rvert_p^{-1}\).
2. If \(y\in\mathfrak{a}_0\) (that is, \(\alpha^{-1}y\in\widehat{\mathcal{O}}_E\)), then \(\lvert\iota_p(\varpi\,\overline{\Phi_\tau(y)})\rvert_p\le1\).
3. If \(p\nmid q_1\), then \(\lvert\iota_p(\varpi)\rvert_p=1\).

## Proof

1. The [[proofs/grh/derivatives-vacuum/chowla-selberg-unit|Chowla–Selberg unit]] satisfies \(\lvert\iota_p u\rvert_p=1\), so \(\lvert\iota_p\varpi\rvert_p=\lvert\iota_p s_0\rvert_p\), and part 1 of [[proofs/grh/derivatives-vacuum/p-adic-size-of-vacuum-root|the previous lemma]] applies.

2. By 1, \(\lvert\iota_p(\varpi\overline{\Phi_\tau(y)})\rvert_p=\lvert\widehat\varphi_\tau(\alpha)\rvert_p^{-1}\lvert\varphi_\tau(y)\rvert_p=\lvert\widehat\varphi_\tau(\alpha^{-1}y)\rvert_p\le1\), since \(\widehat\varphi_\tau\) maps integral adeles into the valuation ring of \(\mathbb{C}_p\).

3. Use part 2 of the previous lemma with \(\tau=1\): \(R s_0\) is spanned over \(R\) by the \(\overline{\Phi_1(y)}\) with \(\alpha y\) integral. Since \(\alpha^{-1}\) is an integral adele (\(\mathcal{O}_E\subseteq\mathfrak{a}_0\)), each such \(y=\alpha^{-1}(\alpha y)\) is integral, so \(\overline{\Phi_1(y)}\in R\); hence \(s_0\in R\), i.e. \(\lvert\iota_ps_0\rvert_p\le1\). Conversely \(q_1\alpha\) is an integral adele (\(q_1\mathfrak{a}_0\subseteq\mathcal{O}_E\), [[?lean:New.Parameters.q₁_mul_alpha_mem|\(q_1\alpha\in\widehat{\mathcal{O}}_E\)]]), so \(y=q_1\) is admissible and \(q_1=c\,s_0\) with \(c\in R\). As \(p\nmid q_1\), \(1=\lvert q_1\rvert_p=\lvert\iota_pc\rvert_p\lvert\iota_ps_0\rvert_p\le\lvert\iota_ps_0\rvert_p\). So \(\lvert\iota_p s_0\rvert_p=1\), and \(\lvert\iota_p\varpi\rvert_p=1\) as in 1.

## References

1. Lean: `New.Parameters.norm_iota_periodFactor`, `New.Parameters.norm_periodFactor_mul_conj_le_one`, `New.Parameters.norm_iota_periodFactor_eq_one` in `src/New/Derivatives/Vacuum/TightFrames.lean`.
