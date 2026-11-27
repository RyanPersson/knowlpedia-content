+++
id = "proofs/grh/spanning-unfolding-b/link-and-cells-are-invariant-under-the-unipotent-group"
title = "Links, discriminants and cells are invariant under the Bessel unipotent group"
kind = "theorem"
summary = "The link, the leading minors and the discriminant of an isometry do not change under multiplication on both sides by Bessel unipotent elements; hence the set of terms of a given cell rank is stable."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.link_inv_mul_mul_of_mem_besselU", "New.Filling.frameDisc_frameGram_inv_mul_mul_of_mem_besselU", "New.Filling.isStable_hasCellRank", "New.mulVec_apply_inr_of_mem_besselU"]
lean_files = ["src/New/Spanning/Unfolding/Link.lean"]
proof_status = "full"
+++

**Theorem.** Let \(F\) be a commutative ring with involution, \(J\) a split Gram matrix, \(\gamma\) an isometry of \(J\) and \(u,u'\) elements of the [[?lean:New.Shape.Form.besselU|Bessel unipotent group]] \(\mathsf{U}\).

1. The [[?lean:New.link|link]] of \(u^{-1}\gamma u'\) equals the link of \(\gamma\).
2. For every \(N\in F\), the [[?lean:New.frameDisc|frame discriminant]] \(D_{\varrho+1}\overline{D_{\varrho+1}}-N^2D_\varrho\overline{D_\varrho}\) of the frame products is the same for \(u^{-1}\gamma u'\) and \(\gamma\).
3. For a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] \(S\) and \(0\le j\le\varrho+1\), the set of \(\gamma\in G(E)\) of [[proofs/grh/spanning-unfolding-b/cell-rank-of-a-term|cell rank]] \(j\) is [[proofs/grh/spanning-unfolding-b/unipotent-character-agreement-stability|stable]].

## Proof

(1) An element \(v\in\mathsf{U}\) is block upper unitriangular, with identity middle block; so if \(t_{e^*}=0\), then \(vt\) has the same middle and \(e^*\) blocks as \(t\). It suffices to show \(\operatorname{link}(g)\subset\operatorname{link}(vgw^{-1})\) for \(v,w\in\mathsf{U}\); applying this to \((v,w,g)=(u,u',u^{-1}\gamma u')\) and to \((u^{-1},u'^{-1},\gamma)\) gives both inclusions. Let \(t\) define an element of the link of \(g\): \(t_{e^*}=0\), \((g^{-1}t)_{e^*}=0\) ([[proofs/grh/spanning-unfolding-b/link-in-coordinates|the link in coordinates]]). Then \(vt\) has \((vt)_{e^*}=0\) and \((vt)_{\mathrm{mid}}=t_{\mathrm{mid}}\); and \((vgw^{-1})^{-1}vt=w\,g^{-1}t\) has vanishing \(e^*\)-block and the same middle block as \(g^{-1}t\). So \(vt\) defines the same pair in the link of \(vgw^{-1}\).

(2) All leading minors of the frame products are unchanged under \(\gamma\mapsto u^{-1}\gamma u'\) ([[?lean:New.Filling.leadingMinor_frameGram_besselU_mul|invariance of the leading minors]]), in particular \(D_\varrho\) and \(D_{\varrho+1}=\det\).

(3) By [[proofs/grh/spanning-unfolding-b/norm-one-pairs-under-inversion-and-unipotent-multiplication|the behaviour of norm-one pairs]], the condition "a norm-one pair occurs from \(j\)" is preserved by inversion and by left multiplication with \(\mathsf{U}\), hence also by right multiplication (\(\gamma u'=(u'^{-1}\gamma^{-1})^{-1}\)); applying this with \(u,u'\) and with their inverses shows that it holds for \(u^{-1}\gamma u'\) if and only if it holds for \(\gamma\). The minor \(D_j\) and the discriminant are unchanged by (2) and its proof. So the three conditions of cell rank \(j\) hold for \(u^{-1}\gamma u'\) if and only if they hold for \(\gamma\).

## References

1. Lean: `New.Filling.link_inv_mul_mul_of_mem_besselU`, `New.Filling.frameDisc_frameGram_inv_mul_mul_of_mem_besselU`, `New.Filling.isStable_hasCellRank` in `src/New/Spanning/Unfolding/Link.lean`.
