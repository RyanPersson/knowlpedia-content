+++
id = "proofs/grh/spanning-unfolding-b/second-moment-over-a-full-fixer"
title = "The second moment over residues fixing a vector at every place above the first level prime"
kind = "lemma"
summary = "If each second moment is at most twice the source dimension, the residues that fix a nonzero frame vector at each of the f chosen places above the first level prime carry at most b^(-6kf) times the main second moment."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.secondMoment_fixer_univ_le", "New.Filling.pow_mul_identitySecondMoment_le_mul_mainSecondMoment", "New.Filling.eight_mul_M_pow_mul_identitySecondMoment_le", "New.Filling.div_levelPrime_pow_mul_mainSecondMoment_le", "New.Filling.levelPrime_pow_le_meetNorm_of_mem_fixer"]
lean_files = ["src/New/Spanning/Unfolding/MomentBounds.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\) contain a primitive \(5040\)-th root of unity and let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]]. For each chosen place \(w\in C_0\) let \(d_w\) be a [[?lean:New.Filling.FrameVector|frame vector]]: a nonzero vector of the span of the frame modulo \(w\), or modulo the conjugate of \(w\). For a set \(Q\subset C_0\) let \(\operatorname{Fix}(Q,d)\subset\bar G\) be the [[?lean:New.Filling.fixer|subgroup]] of the \(s\) whose action modulo that place fixes \(d_w\), for every \(w\in Q\). Put \(\beta(s)=\mathsf{E}(A_{G(E)},\{s\})\) (full side) and suppose \(\beta(s)\le2\dim_S\) for all \(s\). Then
\[
\sum_{s\in\operatorname{Fix}(C_0,d)}\beta(s)\le b^{-6kf}\,\mathcal{M}_{\mathrm{main}} .
\]
Moreover, for every \(Q\subset C_0\): \(b^{5kf}\mathcal{M}_{\mathrm{id}}\le b^{-6k\lvert Q\rvert}\mathcal{M}_{\mathrm{main}}\).

## Proof

Put \(T=b^{-6kf}\mathcal{M}_{\mathrm{main}}\). *Numerical facts.* (a) Since \(\lvert Q\rvert\le f\) and \(b^{11kf}\mathcal{M}_{\mathrm{id}}\le\mathcal{M}_{\mathrm{main}}\), \(b^{6k\lvert Q\rvert}b^{5kf}\mathcal{M}_{\mathrm{id}}\le\mathcal{M}_{\mathrm{main}}\); this is the last assertion. (b) \(8M^f\le b\cdot b^{23f}\le b^{5kf}\) because \(23f+1\le5kf\); with (a), \(8M^f\mathcal{M}_{\mathrm{id}}\le T\). (c) With \(b^{10}\le p_0\): \(L:=(b^{2f}/p_0^f)^k\mathcal{M}_{\mathrm{main}}\le b^{-8kf}\mathcal{M}_{\mathrm{main}}=b^{-2kf}T\le T/8\), as \(b^{2kf}\ge2^{80}\ge8\).

*Scalar cosets.* By [[proofs/grh/spanning-unfolding-b/second-moment-over-the-scalar-cosets|the bound for scalar cosets]] and (b), the \(s\) in scalar cosets contribute at most \(2M^f\mathcal{M}_{\mathrm{id}}\le T/2\).

*The rest.* Let \(\Omega\) be the set of \(s\in\operatorname{Fix}(C_0,d)\) in no scalar coset. It avoids the scalar cosets and is disjoint from \(\bar R_0\) (the coset of \(\zeta=1\)). Each \(s\in\Omega\) meets at the \(f\) places \((w,\epsilon_w)\) ([[?lean:New.Filling.meetsAt_of_mem_vectorFixer|a fixed vector is a common vector]]), so its meet norm is at least \(p_0^f\). By [[proofs/grh/spanning-unfolding-b/second-moment-off-the-reduced-bessel-group|the lemma on residues outside \(\bar R_0\)]], the [[?lean:New.Filling.linkSecondMoment_le_of_le_meetNorm|bound for one link at a time]] with \(z=p_0^f\), and [[proofs/grh/spanning-unfolding-b/expansion-of-the-squares|the expansion of the squares]] with \(C=L\),
\[
\sum_{s\in\Omega}\beta(s)=\mathsf{E}(A_{G(E)\setminus\mathsf{S}},\Omega)\le\bigl(\sqrt L+b^{-15}\sqrt{\mathcal{M}_{\mathrm{id}}}\bigr)^2\le2\bigl(L+b^{-30}\mathcal{M}_{\mathrm{id}}\bigr)\le2\Bigl(\frac T8+\frac T8\Bigr)=\frac T2,
\]
using (c) and \(b^{-30}\mathcal{M}_{\mathrm{id}}\le\mathcal{M}_{\mathrm{id}}\le T/8\) from (b). Adding the two parts (\(\beta\ge0\)) gives the claim.

## References

1. Lean: `New.Filling.secondMoment_fixer_univ_le`, `New.Filling.pow_mul_identitySecondMoment_le_mul_mainSecondMoment` in `src/New/Spanning/Unfolding/MomentBounds.lean`.
