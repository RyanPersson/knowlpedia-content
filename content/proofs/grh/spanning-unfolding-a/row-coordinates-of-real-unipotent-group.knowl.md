+++
id = "proofs/grh/spanning-unfolding-a/row-coordinates-of-real-unipotent-group"
title = "Row coordinates on the real unipotent group"
kind = "construction"
summary = "The free entries of the rows e_a and the imaginary parts of the entries at (e_a, e_a*) are injective coordinates on the real unipotent group that carry its Haar measure to Lebesgue measure."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.rowCoords", "New.Filling.freeRowCoords", "New.Filling.imRowCoords", "New.Filling.classUnipotentToInf", "New.Filling.measurePreserving_rowCoords", "New.Filling.rowCoords_injective", "New.Filling.classUnipotentToInf_injective"]
lean_files = ["src/New/Spanning/Unfolding/CutoffIntegral.lean"]
+++

Let \(E\) be a [[?c:CM field|CM field]] and \(\mathsf U_\infty=\prod_v\mathsf U\) the product, over the [[?c:Infinite place of a number field|infinite places]] \(v\) of \(E\), of the [[?lean:New.Shape.Form.besselU|Bessel unipotent group]] \(\mathsf U\) of [[?lean:New.Shape.G₁|\(G_1\)]]. The **row coordinates** of \(u=(u_v)_v\in\mathsf U_\infty\) are, for each \(a\in\{1,\dots,\varrho\}\):

- the **free entries** of the row \(e_a\): the complex numbers \((u_v)_{e_a,j}\) for all places \(v\) and all columns \(j\) with \((a,j)\) [[?lean:New.RealPlace.IsFreeEntry|free]] (that is, \(j\) in the middle block \(X_0\oplus\mathbb Cz\), or \(j=e_b\), \(j=e_b^{*}\) with \(b>a\)); there are \(2(\varrho-a)+k+1\) such columns;
- the **imaginary parts** \(\operatorname{Im}(u_v)_{e_a,e_a^{*}}\in\mathbb R\) for all places \(v\).

For [[?lean:New.Filling|filling data]] \(S\) and a class \(c\), the map \(\mathsf U_c(M)\to\mathsf U_\infty\), \(\gamma\mapsto(\gamma_v)_v\), given by the [[?lean:New.Filling.ratToInf|rescaled embedding]] of the [[?lean:New.Filling.classUnipotent|unipotent congruence subgroup]], is an injective group homomorphism; its image is denoted \(\Gamma_c\).

## Properties

1. The row coordinates are injective on \(\mathsf U_\infty\) and vanish at the identity ([[?lean:New.RealPlace.injective_freeEntries_besselU|injectivity of the free-entry coordinates]] at each place).
2. The row-coordinate map carries the product of the [[harmonic-analysis/haar-measure|Haar measures]] [[?lean:New.Shape.besselHaar|\(\mu_{\mathsf U}\)]] on the factors to [[?c:Lebesgue measure|Lebesgue measure]] on \(\prod_a\mathbb C^{\{\text{free }j\}\times\{v\}}\times\prod_a\mathbb R^{\{v\}}\). At each place this is [[?lean:New.RealPlace.measurePreserving_freeEntries_besselHaar|the normalisation of the Haar measure by the free entries]]; regrouping the coordinates by rows instead of places preserves Lebesgue measure.
3. \(\gamma\mapsto(\gamma_v)_v\) is injective because an entry of \(\gamma\) is determined by its image under one embedding \(\Phi_v\) and the scales are nonzero.

## References

1. Lean: `New.Filling.rowCoords`, `New.Filling.freeRowCoords`, `New.Filling.imRowCoords`, `New.Filling.classUnipotentToInf`, `New.Filling.measurePreserving_rowCoords`, `New.Filling.rowCoords_injective`, `New.Filling.classUnipotentToInf_injective` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
