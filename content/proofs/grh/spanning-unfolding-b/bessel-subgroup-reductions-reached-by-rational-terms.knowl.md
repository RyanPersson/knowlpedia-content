+++
id = "proofs/grh/spanning-unfolding-b/bessel-subgroup-reductions-reached-by-rational-terms"
title = "Reductions of the Bessel subgroup are reached by rational terms"
kind = "lemma"
summary = "For an admissible filling datum, each reduction of an integral element of the Bessel subgroup is, from each class, the reduction of a rational term in the Bessel subgroup ending at some class."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.exists_besselS_mem_termsOver"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]], \(c\) a class, and \(s\) an element of the [[proofs/grh/spanning-unfolding-b/filling-level-and-reduction|reduced image]] \(\bar{\mathsf S}=\bar R_0\) of the [[?lean:New.Shape.Form.besselS|Bessel subgroup]] \(\mathsf{S}\subset G_{\mathrm{fin}}\). Then there are a class \(d\) and a rational \(\gamma\in\mathsf{S}(E)\) that is a [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|term over]] \((c,s,d)\).

## Proof

Write \(s=\bar k\) with \(k\in K\cap\mathsf{S}\). Since \(h_c\in\mathsf{S}\) and \(\mathsf{S}=\mathsf{U}H\) ([[?lean:New.mem_besselS|decomposition of the Bessel subgroup]]), \(h_ck=u\,h\) with \(u\in\mathsf{U}\) and \(h\in H\); by [[proofs/grh/spanning-unfolding-b/bessel-groups-in-the-lattice-basis|the image of \(\iota_H\)]], \(h=\iota_H(g)\) with \(g\in U(X_0)(\mathbb{A}_f)\). By [[proofs/grh/spanning-unfolding-b/strong-approximation-for-bessel-unipotent-group|strong approximation]] there is \(x\in\mathsf{U}(E)\) with \(h^{-1}u^{-1}x_{\mathrm{fin}}h\in K(M)\). Since the \(g_d\) represent the double cosets, \(g=\eta\,g_d\,a\) with \(\eta\in U(X_0)(E)\), a class \(d\) and \(a\in L\) ([[?lean:New.exists_eq_map_mul_rep_mul|decomposition by representatives]]). Put \(\gamma=x\,\tilde\eta\in\mathsf{S}(E)\). Then, using \(k^{-1}h_c^{-1}=h^{-1}u^{-1}\) and \((\tilde\eta)_{\mathrm{fin}}h_d=\iota_H(\eta g_d)=h\,\iota_H(a)^{-1}\),
\[
k^{-1}h_c^{-1}\gamma_{\mathrm{fin}}h_d=\bigl(h^{-1}u^{-1}x_{\mathrm{fin}}h\bigr)\cdot\iota_H(a)^{-1}.
\]
The first factor lies in \(K(M)\), and \(\iota_H(a)\in K(M)\) because \(L=\iota_H^{-1}(K(M))\) by admissibility. So \(\gamma\) is a term over \((c,\bar k,d)\) by [[proofs/grh/spanning-unfolding-b/terms-compose-like-a-groupoid|the coset description of terms]].

## References

1. Lean: `New.Filling.exists_besselS_mem_termsOver` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`.
