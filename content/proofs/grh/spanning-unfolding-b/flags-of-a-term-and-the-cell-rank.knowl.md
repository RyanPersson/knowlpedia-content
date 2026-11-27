+++
id = "proofs/grh/spanning-unfolding-b/flags-of-a-term-and-the-cell-rank"
title = "Flags of a term and the cell rank"
kind = "theorem"
summary = "For a term of discriminant zero at which the characters agree, the isotropic span and its image split as the first j flag vectors plus the common isotropic space, and the cell rank is the rank of the frame minus one minus the rank of the common isotropic space."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.CharsAgree.add_finrank_commonIsotropic_eq", "New.Filling.CharsAgree.hasCellRank_of_add_finrank_eq", "New.Filling.HasCellRank.flagSpan_one_sup_commonIsotropic", "New.Filling.HasCellRank.flagSpan_coe_sup_commonIsotropic", "New.Filling.CharsAgree.disjoint_flagSpan_one_commonIsotropic", "New.Filling.CharsAgree.disjoint_flagSpan_coe_commonIsotropic", "New.Filling.CharsAgree.disjoint_flagSpan_one", "New.Filling.CharsAgree.disjoint_flagSpan_coe", "New.Filling.HasCellRank.isLeast_normOnePairOccursFrom", "New.NormOnePairOccursFrom.flagSpan_coe_sup_commonIsotropic", "New.NormOnePairOccursFrom.flagSpan_one_sup_commonIsotropic", "New.Filling.flagSpan_sup_eq_isotropicSpan", "New.Filling.frameImage_mulVec_mem_commonIsotropic", "New.Filling.leadingMinor_eq_zero_of_mulVec_eq_zero"]
lean_files = ["src/New/Spanning/Unfolding/TermStructure.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\), \(\gamma\in G(E)\) with \(\operatorname{disc}(\gamma)=0\), \(A=\langle e_0,\dots,e_{\varrho-1}\rangle\), \(I_\gamma=A\cap\gamma A\), and \(A_{\le j}\), \(\gamma A_{\le j}\) the [[proofs/grh/spanning-unfolding-b/spaces-of-the-two-frames|flags]].

1. If \(\gamma\) has [[proofs/grh/spanning-unfolding-b/cell-rank-of-a-term|cell rank]] \(j\), then \(j\le\varrho\),
\[
A=A_{\le j}+I_\gamma,\qquad\gamma A=\gamma A_{\le j}+I_\gamma ,
\]
and \(j\) is the least index from which a norm-one pair occurs for \(\gamma\).
2. Suppose in addition that \(E\) contains a primitive \(5040\)-th root of unity and that the [[proofs/grh/spanning-unfolding-b/characters-agree|characters agree]] at \(\gamma\). If \(\gamma\) has cell rank \(j\), then \(A_{\le j}\cap I_\gamma=0\), \(\gamma A_{\le j}\cap I_\gamma=0\), and
\[
j+\dim I_\gamma=\varrho .
\]
Conversely, if \(0\le j\le\varrho+1\) satisfies \(j+\dim I_\gamma=\varrho\), then \(\gamma\) has cell rank \(j\).

## Proof

(1) \(j\le\varrho\) by the third condition of the cell rank. *Sums.* Let \(x\in E^{\varrho+1}\) with \(x_\varrho=0\), so \(\gamma f\cdot x\in\gamma A\). By [[proofs/grh/spanning-unfolding-b/norm-one-pairs-under-inversion-and-unipotent-multiplication|the lemma on norm-one pairs]] there are \(w,x'\) with \(f\cdot w=\gamma f\cdot x'\) and \(x'_a=x_a\) for \(a\ge j\); in particular \(x'_\varrho=0\). By [[proofs/grh/spanning-unfolding-b/norm-identity-for-combinations-of-the-moved-frame|the norm identity lemma]], \(\bar w_\varrho w_\varrho=\bar x'_\varrho x'_\varrho=0\), so \(w_\varrho=0\) and the shared vector lies in \(A\cap\gamma A=I_\gamma\). Then \(\gamma f\cdot x=\gamma f\cdot(x-x')+\gamma f\cdot x'\) with \(x-x'\) supported on indices \(<j\). This gives \(\gamma A\subset\gamma A_{\le j}+I_\gamma\); the other inclusion is clear as \(j\le\varrho\). For \(A\), apply the same argument to \(\gamma^{-1}\), for which a norm-one pair also occurs from \(j\), and move the shared vector by \(\gamma\).

*Minimality.* Suppose a norm-one pair occurs from some \(i<j\). The shared vector at the index \(i\) gives \(x,x'\) with \(f\cdot x=\gamma f\cdot x'\), \(x'_i=1\), and \(x_b=x'_b=0\) for \(b>i\). Since \(i<j\le\varrho\), \(x_\varrho=0\), so \(Z(\gamma)x'=(0,\dots,0,-Nx_\varrho)=0\). The nonzero vector \(x'\) is supported on indices \(<j\), so its truncation is a nonzero vector killed by the leading \(j\times j\) block of \(Z(\gamma)\), and \(D_j=0\), contradicting the second condition of the cell rank.

(2) By (1), \(j\) is the least index from which a norm-one pair occurs. For such \(j\), when the characters agree, every nonzero common vector \(f\cdot x=\gamma f\cdot x'\) has an index \(l\ge j\) with \(x_l\ne0\) and \(x'_l\ne0\) ([[?lean:New.Filling.CharsAgree.exists_coords_ne_zero_of_common_vector|coordinates of a common vector]]). Hence \(A_{\le j}\cap\gamma A^+=0\) and \(\gamma A_{\le j}\cap A^+=0\); since \(I_\gamma\subset A^+\cap\gamma A^+\), both flags meet \(I_\gamma\) trivially. So \(\gamma A=\gamma A_{\le j}\oplus I_\gamma\), and comparing dimensions (\(\dim\gamma A=\varrho\), \(\dim\gamma A_{\le j}=j\)) gives \(j+\dim I_\gamma=\varrho\).

For the converse, \(\gamma\) has some cell rank \(i\) ([[?lean:New.Filling.CharsAgree.exists_hasCellRank|existence of the cell rank]]), and \(i+\dim I_\gamma=\varrho\) by what was just proved; so \(i=j\).

## References

1. Lean: `New.Filling.CharsAgree.add_finrank_commonIsotropic_eq`, `New.Filling.CharsAgree.hasCellRank_of_add_finrank_eq`, `New.Filling.HasCellRank.flagSpan_one_sup_commonIsotropic`, `New.Filling.HasCellRank.flagSpan_coe_sup_commonIsotropic`, `New.Filling.HasCellRank.isLeast_normOnePairOccursFrom` in `src/New/Spanning/Unfolding/TermStructure.lean`.
