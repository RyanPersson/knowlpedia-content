+++
id = "proofs/grh/spanning-unfolding-b/second-moment-over-the-scalar-cosets"
title = "The scalar cosets carry a small part of the second moment"
kind = "lemma"
summary = "There are at most M^f times the order of the reduced Bessel group residues in scalar cosets, so if each second moment is at most twice the source dimension their total is at most 2 M^f times the identity second moment."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.card_inScalarCoset_le", "New.Filling.sum_secondMoment_inScalarCoset_le"]
lean_files = ["src/New/Spanning/Unfolding/MomentBounds.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\) with \(f\) infinite places.

1. The number of \(s\in\bar G\) that lie in a [[proofs/grh/spanning-unfolding-b/avoiding-scalar-cosets|scalar coset]] \(\zeta\bar R_0\) for some integral finite adele \(\zeta\) is at most \(M^f\lvert\bar R_0\rvert\).
2. Let \(E\) contain a primitive \(5040\)-th root of unity and \(S\) be admissible, and let \(\beta(s)=\mathsf{E}(A_{G(E)},\{s\})\) for the full side. If \(\beta(s)\le2\dim_S\) for all \(s\), then
\[
\sum_{s\in\bigcup_\zeta\zeta\bar R_0}\beta(s)\le2M^f\,\mathcal{M}_{\mathrm{id}} .
\]

## Proof

(1) An element \(s\) with \(s_w=(\zeta\bmod w)t_w\) is determined by \(t\in\bar R_0\) and the residues \((\zeta\bmod w)_w\in\prod_{i}\prod_{w\in C_i}\mathbb{F}_w\). This product has \(p_0^fp_1^f=M^f\) elements, since \(\lvert C_i\rvert=f\) and \(\lvert\mathbb{F}_w\rvert=p_i\). (2) The sum has at most \(M^f\lvert\bar R_0\rvert\) terms, each at most \(2\dim_S\), and \(\mathcal{M}_{\mathrm{id}}=\lvert\bar R_0\rvert\dim_S\).

## References

1. Lean: `New.Filling.card_inScalarCoset_le`, `New.Filling.sum_secondMoment_inScalarCoset_le` in `src/New/Spanning/Unfolding/MomentBounds.lean`.
