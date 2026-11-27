+++
id = "proofs/grh/spanning-unfolding-b/second-moment-over-open-elements-of-a-fixer"
title = "The second moment over the open elements of a fixer"
kind = "lemma"
summary = "The open residues that fix given frame vectors at a set of a places above the first level prime carry at most (1 + 4 b^(-4)) b^(-6ka) times the main second moment."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.secondMoment_fixer_isOpenElement_le"]
lean_files = ["src/New/Spanning/Unfolding/MomentBounds.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\) be a CM field with [[?lean:New.WeilData|Weil data]] (which include a primitive \(5040\)-th root of unity) and \(S\) an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]]. Let \(Q\subset C_0\), frame vectors \(d_w\) and \(\operatorname{Fix}(Q,d)\) be as in [[proofs/grh/spanning-unfolding-b/second-moment-over-a-full-fixer|the lemma on a full fixer]], and let \(\Omega\) be the set of [[?lean:New.Filling.IsOpenElement|open]] elements of \(\operatorname{Fix}(Q,d)\). Then for the amplitude sums of all terms (full side)
\[
\mathsf{E}(A_{G(E)},\Omega)\le\bigl(1+4b^{-4}\bigr)\,b^{-6k\lvert Q\rvert}\,\mathcal{M}_{\mathrm{main}} .
\]

## Proof

Put \(T=b^{-6k\lvert Q\rvert}\mathcal{M}_{\mathrm{main}}\) and \(x=b^{-4}\). By the last assertion of the lemma on a full fixer, \(\mathcal{M}_{\mathrm{id}}\le b^{5kf}\mathcal{M}_{\mathrm{id}}\le T\). No open element lies in a scalar coset ([[proofs/grh/spanning-unfolding-b/residues-near-the-reduced-bessel-group|residues near the reduced Bessel group]]), so \(\Omega\) avoids the scalar cosets and is disjoint from \(\bar R_0\); hence \(\mathsf{E}(A_{G(E)},\Omega)=\mathsf{E}(A_{G(E)\setminus\mathsf{S}},\Omega)\) ([[proofs/grh/spanning-unfolding-b/second-moment-off-the-reduced-bessel-group|residues outside \(\bar R_0\)]]). The main term estimate ([[?lean:New.Filling.linkSecondMoment_isOpenElement_le|link second moment over open elements]]) gives \(\mathsf{E}_{\mathrm{link}}(\{\operatorname{disc}\ne0\},\Omega)\le(1+x)T\nu^2\). By [[proofs/grh/spanning-unfolding-b/expansion-of-the-squares|the expansion of the squares]],
\[
\sqrt{\mathsf{E}(A_{G(E)\setminus\mathsf{S}},\Omega)}\le\sqrt{(1+x)T}+b^{-15}\sqrt{\mathcal{M}_{\mathrm{id}}}\le\Bigl(1+\frac x2\Bigr)\sqrt T+\frac x2\sqrt T=(1+x)\sqrt T,
\]
using \(\sqrt{1+x}\le1+x/2\), \(b^{-15}\le b^{-4}/2\) and \(\mathcal{M}_{\mathrm{id}}\le T\). Squaring, \(\mathsf{E}\le(1+x)^2T\le(1+4x)T\) since \(x\le1\).

## References

1. Lean: `New.Filling.secondMoment_fixer_isOpenElement_le` in `src/New/Spanning/Unfolding/MomentBounds.lean`.
