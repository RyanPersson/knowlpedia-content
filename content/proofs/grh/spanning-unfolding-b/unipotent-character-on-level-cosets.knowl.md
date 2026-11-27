+++
id = "proofs/grh/spanning-unfolding-b/unipotent-character-on-level-cosets"
title = "The unipotent character is constant on cosets of the principal level"
kind = "lemma"
summary = "Two finite adelic unipotent elements that differ by conjugation with an element of H and an element of the principal level have the same unipotent character; hence the character at infinity of an integral rational unipotent term is the conjugate of the finite character of any integral unipotent element with the same reduction."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.unipotentChar_eq_of_mem_principalLevel", "New.Filling.unipotentChar_one", "New.Filling.prod_wave_eq_star_unipotentChar"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]], \(\psi_{\mathsf U}\) its [[proofs/grh/spanning-unfolding-b/unipotent-character-agreement-stability|unipotent character]], and \(\mathsf{U}\subset G_{\mathrm{fin}}\) the Bessel unipotent group.

1. Let \(u,v\in\mathsf{U}\), let \(g\in U(X_0)(\mathbb{A}_f)\) and \(h=\iota_H(g)\). If \(u^{-1}h^{-1}vh\in K(M)\), then \(\psi_{\mathsf U}(v)=\psi_{\mathsf U}(u)\). Also \(\psi_{\mathsf U}(1)=1\).
2. Let \(c\) be a class, \(\gamma\in\mathsf{U}(E)\), and \(k\in K\cap\mathsf{U}\) such that \(\gamma\) is a [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|term over]] \((c,\bar k,c)\). Then
\[
\prod_v\operatorname{wave}\bigl(\sigma((\gamma_\infty)_v)\bigr)=\overline{\psi_{\mathsf U}(k)} .
\]

## Proof

(1) Put \(k=u^{-1}h^{-1}vh\), so \(vh=h\,u\,k\). The elements \(u,v\) lie in the Bessel subgroup \(\mathsf{S}\supset\mathsf{U}\), and so does \(h\in H\) ([[proofs/grh/spanning-unfolding-b/bessel-groups-in-the-lattice-basis|image of \(\iota_H\)]]); hence \(k\in\mathsf{S}\). The simple root sum \(\sigma\) is [[?lean:New.simpleRootSum_mul|additive on \(\mathsf{S}\)]], so \(\sigma(v)+\sigma(h)=\sigma(h)+\sigma(u)+\sigma(k)\), that is \(\sigma(v)=\sigma(u)+\sigma(k)\). Since \(k\) is integral and congruent to \(1\) modulo \(M\) ([[proofs/grh/spanning-unfolding-b/principal-level-is-congruence-subgroup|the principal level as a congruence subgroup]]), each entry of \(k\) off the diagonal is divisible by \(M\), so \(M^{-1}\sigma(k)\in\widehat{\mathcal{O}}\) ([[?lean:New.inv_mul_simpleRootSum_mem|divisibility of the simple root sum]]). The [[proofs/grh/spanning-unfolding-b/self-duality-of-integral-adeles|self-dual character is trivial on \(\widehat{\mathcal{O}}\)]], so
\[
\psi_{\mathsf U}(v)=\psi_S\bigl(\sigma(u)/M\bigr)\,\psi_S\bigl(\sigma(k)/M\bigr)=\psi_{\mathsf U}(u).
\]
For the identity, \(\sigma(1)=0\).

(2) By [[proofs/grh/spanning-unfolding-b/unipotent-character-at-infinity|the character at infinity]] the product equals \(\overline{\psi_{\mathsf U}(\gamma_{\mathrm{fin}})}\). By [[proofs/grh/spanning-unfolding-b/terms-compose-like-a-groupoid|the coset description of terms]], \(k^{-1}h_c^{-1}\gamma_{\mathrm{fin}}h_c\in K(M)\), and \(\gamma_{\mathrm{fin}}\in\mathsf{U}\). Now (1) with \(u=k\), \(v=\gamma_{\mathrm{fin}}\), \(g=g_c\) gives \(\psi_{\mathsf U}(\gamma_{\mathrm{fin}})=\psi_{\mathsf U}(k)\).

## References

1. Lean: `New.Filling.unipotentChar_eq_of_mem_principalLevel`, `New.Filling.prod_wave_eq_star_unipotentChar` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`.
