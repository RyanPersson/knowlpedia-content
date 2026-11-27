+++
id = "proofs/grh/spanning-unfolding-b/bessel-groups-in-the-lattice-basis"
title = "Bessel groups under the change to the lattice basis"
kind = "lemma"
summary = "Membership in the Bessel unipotent group is the same in rational coordinates and in the lattice basis; the inclusion of U(X0) has image the group H, and class representatives lie in the Bessel subgroup."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.toLatticeBasis_mem_besselU", "New.Filling.ratToFin_mem_besselU_iff", "New.Filling.inclHFin_mem_besselH", "New.Filling.range_inclHFin", "New.Filling.ratToFin_toBesselH", "New.Filling.classRep_mem_besselS", "Membership.mem.translateByClassReps_mem_besselU", "New.Filling.map_splitGram_latticeMiddle", "Membership.mem.map_mem_agreeWithOneOn", "Membership.mem.ratToInf_mem_agreeWithOneOn", "New.Filling.isUnit_natCast_N"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] with [[proofs/grh/spanning-unfolding-b/filling-unitary-groups|groups and maps]] \(G(E)\), \(G(\mathbb{A}_f)\), \(G_{\mathrm{fin}}\), \(\iota_H\). In each of these groups let \(\mathsf{U}\) be the [[?lean:New.Shape.Form.besselU|Bessel unipotent group]], \(H\) the [[?lean:New.Shape.Form.besselH|group fixing all basis vectors outside \(X_0\)]] and \(\mathsf{S}\) the [[?lean:New.Shape.Form.besselS|Bessel subgroup]], which contains both.

1. For \(x\in G(\mathbb{A}_f)\): \(B^{-1}xB\in\mathsf{U}\) if and only if \(x\in\mathsf{U}\). For \(\gamma\in G(E)\): \(\gamma_{\mathrm{fin}}\in\mathsf{U}\) if and only if \(\gamma\in\mathsf{U}\).
2. The image of \(\iota_H\colon U(X_0)(\mathbb{A}_f)\to G_{\mathrm{fin}}\) is \(H\). For a rational \(\eta\in U(X_0)(E)\) with extension \(\tilde\eta\in G(E)\) by the identity, \((\tilde\eta)_{\mathrm{fin}}=\iota_H(\eta)\).
3. Every class representative \(h_c\) lies in \(H\subset\mathsf{S}\); and if \(\gamma\in\mathsf{U}(E)\), then \(h_c^{-1}\gamma_{\mathrm{fin}}h_c\in\mathsf{U}\).

## Proof

(1) The Bessel unipotent group consists of the isometries that are block upper unitriangular for the levels (\(a\) on \(e_a\), \(\varrho\) on the middle block, \(2\varrho-a\) on \(e_a^*\)). The lattice basis matrix \(B\) and its inverse are the identity outside the middle block, hence block triangular for these levels with invertible diagonal blocks; conjugation by such a matrix preserves block unitriangularity ([[?lean:New.conj_mem_unitriangular|conjugation of unitriangular matrices]]) in both directions. The second statement follows because \(\gamma_{\mathrm{fin}}=B^{-1}\gamma B\) and the conditions on the entries of \(\gamma\) are preserved and reflected by the injective map \(E\to\mathbb{A}_f\).

(2) The matrix \(B^{-1}\tilde gB\) fixes \(e_a\), \(e_a^*\) and \(z\) for every \(g\in U(X_0)(\mathbb{A}_f)\), by a direct block computation (the lattice basis only replaces \(x_{k_0}\) by \(x_{k_0}/\bar\pi+z/N\), and \(\tilde g\) fixes \(z\)); so the image lies in \(H\). Conversely, if \(x\in H\subset G_{\mathrm{fin}}\), then \(BxB^{-1}\) fixes the basis vectors outside \(\kappa\) in rational coordinates, and since \(N=\pi\bar\pi\) is a unit of \(\mathbb{A}_f\), every such isometry is the extension \(\tilde g\) of some \(g\in U(X_0)(\mathbb{A}_f)\) ([[?lean:New.exists_eq_toBesselH|elements of \(H\) come from \(U(X_0)\)]]). The formula for rational \(\eta\) is the definition of both sides.

(3) \(h_c=\iota_H(g_c)\in H\) by (2), and \(H\subset\mathsf{S}\). The Bessel subgroup normalises \(\mathsf{U}\) ([[?lean:New.besselS_le_normalizer_besselU|normaliser of the unipotent group]]), so \(h_c^{-1}\gamma_{\mathrm{fin}}h_c\in\mathsf{U}\) by (1).

## References

1. Lean: `New.Filling.toLatticeBasis_mem_besselU`, `New.Filling.ratToFin_mem_besselU_iff`, `New.Filling.range_inclHFin`, `New.Filling.ratToFin_toBesselH`, `New.Filling.classRep_mem_besselS` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`.
