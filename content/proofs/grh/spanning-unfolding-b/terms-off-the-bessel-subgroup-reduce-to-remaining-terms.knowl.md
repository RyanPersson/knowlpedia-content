+++
id = "proofs/grh/spanning-unfolding-b/terms-off-the-bessel-subgroup-reduce-to-remaining-terms"
title = "Terms off the Bessel subgroup reduce to the remaining terms"
kind = "lemma"
summary = "Over a block whose residue lies in a set avoiding the scalar cosets, the terms outside the Bessel subgroup have the same amplitude sum as the remaining terms."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.AvoidsScalarCosets.amplitudeSum_compl_besselS_eq"]
lean_files = ["src/New/Spanning/Unfolding/SquareExpansion.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\) contain a primitive \(5040\)-th root of unity and let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\). Let \(\Omega\subset\bar G\) [[proofs/grh/spanning-unfolding-b/avoiding-scalar-cosets|avoid the scalar cosets]], \(s\in\Omega\), and \(c,c'\) classes. Then, for either side, the [[proofs/grh/spanning-unfolding-b/filling-amplitude|amplitude sums]] satisfy
\[
A_{G(E)\setminus\mathsf{S}}(c,s,c')=A_{\Gamma^*}(c,s,c'),
\]
where \(\mathsf{S}\) is the rational Bessel subgroup and \(\Gamma^*\) the set of [[proofs/grh/spanning-unfolding-b/remaining-terms|remaining terms]].

## Proof

Put \(O=G(E)\setminus\mathsf{S}\). First, \(\Gamma^*\subset O\): an element of \(\mathsf{S}\) has a norm-one pair from index \(0\) ([[proofs/grh/spanning-unfolding-b/terms-of-cell-rank-zero-are-scalar-multiples-of-the-bessel-subgroup|norm-one pairs and the Bessel subgroup]]), hence is not remaining ([[proofs/grh/spanning-unfolding-b/remaining-terms-stable-and-complement|complement of the remaining terms]]). Amplitude sums are additive over a decomposition of the set of terms into a part and its complement ([[?lean:New.Filling.amplitudeSum_eq_inter_compl_add_inter|additivity of amplitude sums]]), so
\[
A_O=A_{\Gamma^*}+A_{O\setminus\Gamma^*,\ \text{not agreeing}}+A_{O\setminus\Gamma^*,\ \text{agreeing}},
\]
where "agreeing" refers to [[proofs/grh/spanning-unfolding-b/characters-agree|agreement of characters]].

*The disagreeing part.* The set of \(\gamma\in O\setminus\Gamma^*\) at which the characters do not agree is stable: \(O\) is stable ([[proofs/grh/spanning-unfolding-b/blocks-of-the-bessel-subgroup|blocks of the Bessel subgroup]]), \(\Gamma^*\) is stable, and agreement is invariant under \(\gamma\mapsto u^{-1}\gamma u'\) ([[proofs/grh/spanning-unfolding-b/unipotent-group-acts-on-the-structure-of-a-term|the unipotent group and the structure of a term]]). A stable set none of whose elements agrees has amplitude sum \(0\) over every block ([[?lean:New.Filling.amplitudeSum_eq_zero_of_not_charsAgree|vanishing of disagreeing terms]]).

*The agreeing part.* If \(\gamma\in O\setminus\Gamma^*\) agrees, then a norm-one pair occurs from \(0\) for \(\gamma\) (part 4 of the theorem on remaining terms). By [[proofs/grh/spanning-unfolding-b/residues-near-the-reduced-bessel-group|part 5 of the lemma on residues]], such a \(\gamma\notin\mathsf{S}\) is not a term over \((c,s,c')\) with \(s\in\Omega\). So this part of the sum over the block \((c,s,c')\) is empty.

## References

1. Lean: `New.Filling.AvoidsScalarCosets.amplitudeSum_compl_besselS_eq` in `src/New/Spanning/Unfolding/SquareExpansion.lean`.
