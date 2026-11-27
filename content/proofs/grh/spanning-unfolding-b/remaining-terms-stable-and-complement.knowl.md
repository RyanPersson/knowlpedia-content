+++
id = "proofs/grh/spanning-unfolding-b/remaining-terms-stable-and-complement"
title = "The remaining terms are stable, and their complement among agreeing terms"
kind = "theorem"
summary = "The set of remaining terms is stable under the unipotent group; a term for which a norm-one pair occurs from index zero is not remaining, and an agreeing term that is not remaining has a norm-one pair from index zero."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.isStable_remainingTerms", "New.NormOnePairOccursFrom.notMem_remainingTerms", "New.Filling.CharsAgree.normOnePairOccursFrom_zero", "New.Filling.isotropicSpan_eq_iff_finrank"]
lean_files = ["src/New/Spanning/Unfolding/TermStructure.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\) with [[proofs/grh/spanning-unfolding-b/remaining-terms|remaining terms]] \(\Gamma^*\), and \(\gamma\in G(E)\).

1. \(A=\gamma A\) if and only if \(\dim(A\cap\gamma A)=\varrho\).
2. \(\Gamma^*\) is [[proofs/grh/spanning-unfolding-b/unipotent-character-agreement-stability|stable]]: for \(u,u'\in\mathsf{U}(E)\), \(u^{-1}\gamma u'\in\Gamma^*\iff\gamma\in\Gamma^*\).
3. If [[proofs/grh/spanning-unfolding-b/cell-rank-of-a-term|a norm-one pair occurs from \(0\)]] for \(\gamma\), then \(\gamma\notin\Gamma^*\).
4. If \(E\) contains a primitive \(5040\)-th root of unity, the characters agree at \(\gamma\) and \(\gamma\notin\Gamma^*\), then a norm-one pair occurs from \(0\) for \(\gamma\).

## Proof

(1) \(A\) and \(\gamma A\) both have dimension \(\varrho\) and contain \(A\cap\gamma A\).

(2) Under \(\gamma\mapsto u^{-1}\gamma u'\): the discriminant is unchanged ([[proofs/grh/spanning-unfolding-b/link-and-cells-are-invariant-under-the-unipotent-group|invariance of the discriminant]]); agreement of characters and \(\dim(A\cap\gamma A)\) are unchanged ([[proofs/grh/spanning-unfolding-b/unipotent-group-acts-on-the-structure-of-a-term|the unipotent group and the structure of a term]]); and by (1) the condition \(A\ne\gamma A\) depends only on this dimension.

(3) The pair at index \(0\) gives \(x,x'\) with \(f\cdot x=\gamma f\cdot x'\) and \(x'_0=1\), so \(x'\ne0\) and \(\operatorname{disc}(\gamma)=0\) by [[proofs/grh/spanning-unfolding-b/vanishing-of-the-term-discriminant|the vanishing criterion]]. By the sum decompositions for \(j=0\) (which use only that a norm-one pair occurs from \(0\le\varrho\); see [[proofs/grh/spanning-unfolding-b/flags-of-a-term-and-the-cell-rank|flags of a term]]), \(A=A_{\le0}+I_\gamma=I_\gamma\) and \(\gamma A=I_\gamma\). So \(A=\gamma A\), and neither alternative of the definition of \(\Gamma^*\) holds.

(4) Since \(\gamma\notin\Gamma^*\): \(\operatorname{disc}(\gamma)=0\), and, as the characters agree, \(A=\gamma A\), so \(0+\dim I_\gamma=\varrho\) by (1). By the converse part of the theorem on flags, \(\gamma\) has cell rank \(0\), whose first condition is the claim.

## References

1. Lean: `New.Filling.isStable_remainingTerms`, `New.NormOnePairOccursFrom.notMem_remainingTerms`, `New.Filling.CharsAgree.normOnePairOccursFrom_zero` in `src/New/Spanning/Unfolding/TermStructure.lean`.
