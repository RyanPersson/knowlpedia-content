+++
id = "proofs/grh/spanning-unfolding-b/second-moment-off-the-reduced-bessel-group"
title = "Second moments over residues outside the reduced Bessel group"
kind = "lemma"
summary = "The second moment over a set is the sum of the second moments at its elements, and over residues outside the reduced Bessel group all terms and the terms off the Bessel subgroup have the same second moment."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.secondMoment_univ_eq_secondMoment_compl_besselS", "New.Filling.secondMoment_singleton", "New.Filling.secondMoment_eq_sum_secondMoment_singleton"]
lean_files = ["src/New/Spanning/Unfolding/MomentBounds.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] and \(\mathsf{E}(A,\Omega)=\nu^{-2}\sum_{c,c'}\sum_{s\in\Omega}\lVert A(c,s,c')\rVert^2\) the [[?lean:New.Filling.secondMoment|second moment]] of a family of blocks.

1. \(\mathsf{E}(A,\Omega)=\sum_{s\in\Omega}\mathsf{E}(A,\{s\})\).
2. Let \(E\) contain a primitive \(5040\)-th root of unity and \(S\) be [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]]. If \(\Omega\cap\bar R_0=\varnothing\), then for the amplitude sums \(A\) of the full side
\[
\mathsf{E}\bigl(A_{G(E)},\Omega\bigr)=\mathsf{E}\bigl(A_{G(E)\setminus\mathsf{S}},\Omega\bigr).
\]

## Proof

(1) is an exchange of finite sums. (2) By [[?lean:New.Filling.amplitudeSum_eq_inter_compl_add_inter|additivity of amplitude sums]], \(A_{G(E)}=A_{G(E)\setminus\mathsf{S}}+A_{\mathsf{S}}\), and \(A_{\mathsf{S}}(c,s,c')=0\) for \(s\notin\bar R_0\) ([[proofs/grh/spanning-unfolding-b/blocks-of-the-bessel-subgroup|blocks of the Bessel subgroup]]).

## References

1. Lean: `New.Filling.secondMoment_univ_eq_secondMoment_compl_besselS`, `New.Filling.secondMoment_eq_sum_secondMoment_singleton` in `src/New/Spanning/Unfolding/MomentBounds.lean`.
