+++
id = "proofs/grh/spanning-unfolding-b/unipotent-group-acts-on-the-structure-of-a-term"
title = "The unipotent group and the structure of a term"
kind = "theorem"
summary = "Multiplying a term on both sides by Bessel unipotent elements moves the common isotropic space by the left factor, and does not change whether the characters agree; the finite unipotent character is multiplicative and conjugation invariant on rational unipotent elements."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.commonIsotropic_besselU_mul", "New.Filling.finrank_commonIsotropic_besselU_mul", "New.Filling.charsAgree_mul_mul_iff_of_mem_besselU", "New.Filling.unipotentChar_ratToFin_mul", "New.Filling.unipotentChar_ratToFin_conj", "New.Filling.mulVec_mem_isotropicSpan_one", "New.Filling.mulVec_mem_isotropicSpan_one_iff"]
lean_files = ["src/New/Spanning/Unfolding/TermStructure.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\), \(\gamma\in G(E)\), and \(u,u'\in\mathsf{U}(E)\) elements of the rational Bessel unipotent group. Let \(I_\gamma=A\cap\gamma A\) and \(\chi(u)=\psi_{\mathsf U}(u_{\mathrm{fin}})\) with the [[proofs/grh/spanning-unfolding-b/unipotent-character-agreement-stability|unipotent character]].

1. \(I_{u\gamma u'}=u\,I_\gamma\); in particular \(\dim I_{u\gamma u'}=\dim I_\gamma\).
2. \(\chi(uu')=\chi(u)\chi(u')\) and \(\chi(u^{-1}u'u)=\chi(u')\).
3. The [[proofs/grh/spanning-unfolding-b/characters-agree|characters agree]] at \(u\gamma u'\) if and only if they agree at \(\gamma\).

## Proof

(1) An element of \(\mathsf{U}\) is block upper unitriangular, so it maps \(A\) (the vectors with vanishing middle and \(e^*\) blocks) into itself; applying this to the inverse, \(uy\in A\iff y\in A\). Now \(y\in I_{u\gamma u'}\) means \(y\in A\) and \(u'^{-1}\gamma^{-1}u^{-1}y\in A\), which is equivalent to \(u^{-1}y\in A\) and \(\gamma^{-1}(u^{-1}y)\in A\), that is \(u^{-1}y\in I_\gamma\). As \(u\) is invertible, the dimensions agree.

(2) The simple root sum \(\sigma\) is [[?lean:New.simpleRootSum_mul|additive on the Bessel subgroup]], which contains \(u_{\mathrm{fin}},u'_{\mathrm{fin}}\) ([[proofs/grh/spanning-unfolding-b/bessel-groups-in-the-lattice-basis|Bessel groups in the lattice basis]]); so \(\sigma((uu')_{\mathrm{fin}})=\sigma(u_{\mathrm{fin}})+\sigma(u'_{\mathrm{fin}})\), and \(\psi_{\mathsf U}=\psi_S(\sigma/M)\) with \(\psi_S\) an additive character. For the second identity, \(\chi(u)\chi(u^{-1}u'u)=\chi(u'u)=\chi(u')\chi(u)\), and \(\chi(u)\ne0\).

(3) It suffices to show: if the characters agree at \(\delta\) and \(a,a'\in\mathsf{U}(E)\), then they agree at \(a\delta a'^{-1}\) (apply this to \((u^{-1},u')\) and \(u\gamma u'\), and to \((u,u'^{-1})\) and \(\gamma\)). Let \(w,w'\in\mathsf{U}(E)\) with \(w\,(a\delta a'^{-1})=(a\delta a'^{-1})\,w'\). Then \((a^{-1}wa)\,\delta=\delta\,(a'^{-1}w'a')\), so agreement at \(\delta\) gives \(\chi(a^{-1}wa)=\chi(a'^{-1}w'a')\), and by (2) these are \(\chi(w)\) and \(\chi(w')\).

## References

1. Lean: `New.Filling.commonIsotropic_besselU_mul`, `New.Filling.finrank_commonIsotropic_besselU_mul`, `New.Filling.charsAgree_mul_mul_iff_of_mem_besselU`, `New.Filling.unipotentChar_ratToFin_mul`, `New.Filling.unipotentChar_ratToFin_conj` in `src/New/Spanning/Unfolding/TermStructure.lean`.
