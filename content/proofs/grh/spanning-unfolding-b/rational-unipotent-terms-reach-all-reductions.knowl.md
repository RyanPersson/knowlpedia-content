+++
id = "proofs/grh/spanning-unfolding-b/rational-unipotent-terms-reach-all-reductions"
title = "Rational unipotent terms reach every reduction of the unipotent group"
kind = "theorem"
summary = "For an admissible filling datum and each class, the reductions of the integral rational unipotent terms are exactly the reduced image of the finite adelic unipotent group, and the approximation keeps the unipotent character."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.mem_reducedImage_besselU_iff_exists_termsOver", "New.Filling.exists_rat_approx_unipotentChar_eq"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] and \(c\) a [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|class]].

1. For every \(u\in\mathsf{U}\subset G_{\mathrm{fin}}\) there is \(u_0\in\mathsf{U}(E)\) with \(u^{-1}h_c^{-1}(u_0)_{\mathrm{fin}}h_c\in K(M)\) and \(\psi_{\mathsf U}((u_0)_{\mathrm{fin}})=\psi_{\mathsf U}(u)\).
2. For \(s\in\bar G\): \(s\) lies in the [[proofs/grh/spanning-unfolding-b/filling-level-and-reduction|reduced image]] \(\bar{\mathsf U}\) of \(\mathsf{U}\) if and only if there is \(\gamma\in\mathsf{U}(E)\) that is a term over \((c,s,c)\).

## Proof

(1) The element \(h_cuh_c^{-1}\) lies in \(\mathsf{U}\), because \(h_c\in\mathsf{S}\) normalises \(\mathsf{U}\) ([[proofs/grh/spanning-unfolding-b/bessel-groups-in-the-lattice-basis|Bessel groups in the lattice basis]]). By [[proofs/grh/spanning-unfolding-b/strong-approximation-for-bessel-unipotent-group|strong approximation]] with \(x=h_cuh_c^{-1}\) and \(y=h_c\) there is \(u_0\in\mathsf{U}(E)\) with \(h_c^{-1}(h_cu^{-1}h_c^{-1})(u_0)_{\mathrm{fin}}h_c=u^{-1}h_c^{-1}(u_0)_{\mathrm{fin}}h_c\in K(M)\). The equality of characters is [[proofs/grh/spanning-unfolding-b/unipotent-character-on-level-cosets|the constancy of the unipotent character]] applied to \(u\), \(v=(u_0)_{\mathrm{fin}}\) and \(g=g_c\).

(2) If \(s=\bar k\) with \(k\in K\cap\mathsf{U}\), take \(\gamma=u_0\) from (1) for \(u=k\); then \(k^{-1}h_c^{-1}\gamma_{\mathrm{fin}}h_c\in K(M)\), so \(\gamma\) is a term over \((c,\bar k,c)\) by [[proofs/grh/spanning-unfolding-b/terms-compose-like-a-groupoid|the coset description of terms]]. Conversely, if \(\gamma\in\mathsf{U}(E)\) is a term over \((c,s,c)\), then \(k=h_c^{-1}\gamma_{\mathrm{fin}}h_c\) lies in \(K\), has reduction \(s\), and lies in \(\mathsf{U}\); so \(s\in\bar{\mathsf U}\).

## References

1. Lean: `New.Filling.mem_reducedImage_besselU_iff_exists_termsOver`, `New.Filling.exists_rat_approx_unipotentChar_eq` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`.
