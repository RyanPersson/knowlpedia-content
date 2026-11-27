+++
id = "proofs/grh/spanning-unfolding-b/trace-of-the-twisted-translations"
title = "Trace of the twisted translations"
kind = "lemma"
summary = "For a residue that is trivial above one level prime, the trace of the twisted translation is the source dimension times the reduced unipotent character."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.trace_besselTranslate_eq_mul_reducedChar", "New.Filling.mem_besselU_of_reduction_eq_one"]
lean_files = ["src/New/Spanning/Unfolding/Moments.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over a CM field \(E\) with [[?lean:New.WeilData|Weil data]] (in particular a primitive \(5040\)-th root of unity), and \(j\in\{0,1\}\).

1. Let \(\gamma\in\mathsf{S}(E)\), \(c\) a class and \(k=h_c^{-1}\gamma_{\mathrm{fin}}h_c\). If \(k\in K\) and \(\bar k\) is trivial at all chosen places above \(p_j\), then \(k\in\mathsf{U}\).
2. If \(s\in\bar G\) is trivial at all chosen places above \(p_j\), then \(\operatorname{tr}r_\psi(s)=\dim_S\cdot\bar\psi_{\mathsf U}(s)\), with the [[proofs/grh/spanning-unfolding-b/reduced-unipotent-character|reduced character]].

## Proof

(1) Write \(\gamma=u\tilde\delta\) with \(u\in\mathsf{U}(E)\), \(\delta\in U(X_0)(E)\). Then \(k=u'\,\iota_H(y)\) with \(u'=h_c^{-1}u_{\mathrm{fin}}h_c\in\mathsf{U}\) and \(y=g_c^{-1}\delta g_c\). The \(H\)-part of an integral element of \(\mathsf{U}H\) is integral ([[?lean:New.mem_unitaryLevel_of_besselU_mul|the \(H\)-part of a congruence element]], with modulus \(1\)), so \(\iota_H(y)\in K\). Each entry of \(\iota_H(y)\) equals the corresponding entry of \(k\) or of the identity ([[?lean:New.besselH_apply_eq_or|entries of the \(H\)-part]]), so \(\iota_H(y)\) reduces to \(1\) above \(p_j\) because \(k\) does; this means that \(y\) is integral and reduces to \(1\) at the places of \(C_j\) ([[?lean:New.Filling.reduction_inclHFin_eq_one_iff|reduction of the inclusion of \(U(X_0)\)]]). By [[proofs/grh/spanning-unfolding-b/freeness-in-small-rank|freeness in rank \(k\)]], \(\delta=1\). So \(y=1\) and \(k=u'\in\mathsf{U}\).

(2) By [[proofs/grh/spanning-unfolding-b/bessel-translate-is-a-unitary-representation|the trace formula]], \(\operatorname{tr}r_\psi(s)=\nu^{-1}\sum_{c,i}A_{\mathsf{S}}(c,s^{-1},c)_{(i,i)}\).

*If \(s=\bar k\) with \(k\in K\cap\mathsf{U}\)* (the \(k\) fixed in the definition of \(\bar\psi_{\mathsf U}\)): the blocks of a stable set transform under integral unipotent elements by \(A_T(c,\bar u\,t\,\bar u'^{-1},c')=\psi_{\mathsf U}(u)^{-1}\psi_{\mathsf U}(u')\,A_T(c,t,c')\) ([[?lean:New.Filling.amplitudeSum_besselU_mul|blocks under unipotent reductions]]). With \(T=\mathsf{S}\), \(u=1\), \(u'=k\), \(t=1\): \(A_{\mathsf{S}}(c,s^{-1},c)=\psi_{\mathsf U}(k)A_{\mathsf{S}}(c,1,c)\), and \(A_{\mathsf{S}}(c,1,c)=\nu\cdot1\) ([[?lean:New.Filling.amplitudeSum_besselS_one_eq_ite|identity block]]). Summing the diagonal over \(\mathcal{C}\times I\) gives \(\dim_S\psi_{\mathsf U}(k)\).

*Otherwise* \(\bar\psi_{\mathsf U}(s)=0\), and no element of \(\mathsf{S}(E)\) is a term over \((c,s^{-1},c)\): for such a \(\gamma\), \(k=h_c^{-1}\gamma_{\mathrm{fin}}h_c\) would reduce to \(s^{-1}\), trivial above \(p_j\), so \(k\in\mathsf{U}\) by (1) and \(s=\overline{k^{-1}}\) would be the reduction of an integral unipotent element. So all the blocks vanish and the trace is \(0\).

## References

1. Lean: `New.Filling.trace_besselTranslate_eq_mul_reducedChar`, `New.Filling.mem_besselU_of_reduction_eq_one` in `src/New/Spanning/Unfolding/Moments.lean`.
