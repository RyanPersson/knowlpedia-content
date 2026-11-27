+++
id = "proofs/grh/spanning-unfolding-b/bessel-subgroup-terms-in-principal-level"
title = "Rational elements of the Bessel subgroup in the principal level are unipotent"
kind = "lemma"
summary = "For an admissible filling datum, a rational element of the Bessel subgroup that the representatives of two classes carry into the principal level joins a class to itself and lies in its unipotent group of level M."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.eq_and_mem_classUnipotent_of_besselS"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]], \(c,d\) [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|classes]] and \(\gamma\in G(E)\) a rational element of the [[?lean:New.Shape.Form.besselS|Bessel subgroup]] \(\mathsf{S}\). If \(h_c^{-1}\gamma_{\mathrm{fin}}h_d\in K(M)\), then \(c=d\) and \(\gamma\in\mathsf{U}_c(M)\).

## Proof

Since \(N\) is a unit of \(E\), every element of \(\mathsf{S}(E)\) is a product \(\gamma=u\,\tilde\eta\) with \(u\in\mathsf{U}(E)\) and \(\tilde\eta\) the extension by the identity of some \(\eta\in U(X_0)(E)\) ([[?lean:New.exists_besselU_mul_toBesselH|decomposition of the Bessel subgroup]]). Using \((\tilde\eta)_{\mathrm{fin}}=\iota_H(\eta)\) and \(h_c=\iota_H(g_c)\),
\[
h_c^{-1}\gamma_{\mathrm{fin}}h_d=\bigl(h_c^{-1}u_{\mathrm{fin}}h_c\bigr)\cdot\iota_H\bigl(g_c^{-1}\eta\,g_d\bigr),
\]
where the first factor lies in \(\mathsf{U}\) and the second in \(H\) ([[proofs/grh/spanning-unfolding-b/bessel-groups-in-the-lattice-basis|Bessel groups in the lattice basis]]). If a product \(u'h'\) with \(u'\in\mathsf{U}\), \(h'\in H\) is integral and congruent to \(1\) modulo \(M\), then so is \(h'\) ([[?lean:New.mem_unitaryLevel_of_besselU_mul|the \(H\)-part of a congruence element]]); with [[proofs/grh/spanning-unfolding-b/principal-level-is-congruence-subgroup|the description of \(K(M)\)]] this gives \(\iota_H(g_c^{-1}\eta g_d)\in K(M)\). By admissibility, \(L=\iota_H^{-1}(K(M))\), so \(g_c^{-1}\eta\,g_d\in L\).

The level \(L\) is free: if \(\delta\in U(X_0)(E)\) has \(g_d^{-1}\delta g_d\in L\), then \(\delta=1\). Since \(g_c,g_d\) are the representatives of the double cosets \(c,d\) and \(g_c^{-1}\eta g_d\in L\), the classes coincide and, by freeness, \(\eta=1\) ([[?lean:New.eq_and_eq_one_of_doubleCoset_rep|representatives of double cosets under a free action]]). Hence \(c=d\), \(\gamma=u\in\mathsf{U}(E)\), and \(h_c^{-1}\gamma_{\mathrm{fin}}h_c\in K(M)\), which is the definition of \(\gamma\in\mathsf{U}_c(M)\).

## References

1. Lean: `New.Filling.eq_and_mem_classUnipotent_of_besselS` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`.
