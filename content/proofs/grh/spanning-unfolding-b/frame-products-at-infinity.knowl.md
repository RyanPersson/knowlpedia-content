+++
id = "proofs/grh/spanning-unfolding-b/frame-products-at-infinity"
title = "Frame products of a rational term at the infinite places"
kind = "lemma"
summary = "The frame products of the rescaled real image of a rational isometry are the embedded rational frame products times explicit powers of the scales, and likewise for their minors."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.realFrameGram_ratToInf", "New.Filling.det_submatrix_realFrameGram_ratToInf", "New.Filling.basisScale_besselFrame"]
lean_files = ["src/New/Spanning/Unfolding/Setup.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]], \(\gamma\in G(E)\) with [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|frame products]] \(Z(\gamma)\), and \(v\) an infinite place. Let \(Z_1(g)=\bigl(h_1(f_a,gf_b)\bigr)_{a,b}\) denote the [[?lean:New.realFrameGram|frame products in \(G_1\)]]. Then for \(0\le a,b\le\varrho\)
\[
Z_1\bigl((\gamma_\infty)_v\bigr)_{ab}=\frac{\kappa_v^{\varrho-a}\,\kappa_v^{\varrho-b}}{N}\ \Phi_v\bigl(Z(\gamma)_{ab}\bigr),
\]
and for every map \(e\) from a finite set \(m\) to \(\{0,\dots,\varrho\}\)
\[
\det\Bigl(Z_1\bigl((\gamma_\infty)_v\bigr)_{e(i)e(j)}\Bigr)_{i,j\in m}=\Bigl(\prod_{i\in m}\frac{\kappa_v^{2(\varrho-e(i))}}{N}\Bigr)\ \Phi_v\Bigl(\det\bigl(Z(\gamma)_{e(i)e(j)}\bigr)_{i,j\in m}\Bigr).
\]

## Proof

By [[proofs/grh/spanning-unfolding-b/filling-unitary-groups|the definition of \(\gamma_\infty\)]], \((\gamma_\infty)_v=D_v^{-1}\Phi_v(\gamma)D_v\) and \(D_v^*J_{\mathbb{C}}D_v=J_1\) with \(D_v\) real diagonal. Hence \(J_1(\gamma_\infty)_v=D_v\,J_{\mathbb{C}}\,\Phi_v(\gamma)\,D_v\), and the \((f_a,f_b)\) entry is \(\sigma_v(f_a)\sigma_v(f_b)\,\Phi_v(Z(\gamma)_{ab})\). Since \(\sigma_v(f_a)=\kappa_v^{\varrho-a}/\sqrt N\) for all frame indices, the first formula follows.

For the minors, expand both determinants by the Leibniz formula. In the term of a permutation \(\tau\), the factor for \(i\) is \(\kappa_v^{\varrho-e(i)}\kappa_v^{\varrho-e(\tau i)}N^{-1}\Phi_v(Z(\gamma)_{e(i)e(\tau i)})\); the product over \(i\) of the scalar factors is \(\prod_i\kappa_v^{2(\varrho-e(i))}/N\), independent of \(\tau\), because \(\tau\) permutes \(m\).

## References

1. Lean: `New.Filling.realFrameGram_ratToInf`, `New.Filling.det_submatrix_realFrameGram_ratToInf` in `src/New/Spanning/Unfolding/Setup.lean`.
