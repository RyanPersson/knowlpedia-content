+++
id = "proofs/grh/spanning-core/scaled-poincare-map"
title = "Scaled Poincaré map and the translates of the good Poincaré map"
kind = "construction"
summary = "The Poincaré map in coordinates, scaled to be nearly isometric, and the maps #G e0 s P from source forms to target forms."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.goodPoincare", "New.Data.levelRepresentation", "New.Data.levelRepresentation_apply", "New.Data.inner_levelRepresentation", "New.Data.poincareScale", "New.Data.poincareScale_pos", "New.Data.scaledPoincare"]
lean_files = ["src/New/Spanning/SecondMoment/SpanningTheorem.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] with [[?lean:New.Data.filling|filling data]] \(S\). Let \(\Pi\colon\) [[?lean:New.Data.SourceForm|source forms]] \(\to\) [[?lean:New.Data.principalForms|forms of principal level on \(Y_0\)]] be the [[?lean:New.Data.poincare|Poincaré map]], \(\rho\) the [[?lean:New.Data.principalRep|action]] of \(\bar G=\) [[?lean:New.Data.chosenGL|\(\prod_w\mathrm{GL}_r(\mathbb{F}_w)\)]] on these forms, and \(e_0\) the [[?lean:New.Data.e₀|good idempotent]].

1. For \(s\in\bar G\) the **good Poincaré map translated by \(s\)** is the linear map from source forms to [[?lean:New.Data.targetForms|target forms]]
\[
\mathcal P_s=\lvert\bar G\rvert\cdot\rho(e_0)\,\rho(s)\,\Pi .
\]
2. The **level representation** is \(\rho\) regarded as a representation of \(\prod_{i=0,1}\prod_{w\mid p_i}\mathrm{GL}_r(\mathbb{F}_w)\) (the same group, with the chosen places sorted by the level prime below them; in Lean the type [[?lean:New.Filling.ResidueGL|`S.ResidueGL`]]). It preserves the Petersson inner product.
3. The **scale** is \(c_P=\bigl(\operatorname{vol}(J)\cdot\nu\bigr)^{-1/2}>0\), where \(J\) is the [[?lean:New.Filling.stdPrincipalLevel|principal level]] with its Haar volume and \(\nu\) is the [[?lean:New.Filling.unipotentCovolume|unipotent covolume]] of \(S\).
4. The **scaled Poincaré map** is
\[
P=c_P\cdot\Pi\circ\iota^{-1}\colon\ \mathbb{C}^{\mathcal C\times\mathcal I}\longrightarrow\text{forms of principal level on }Y_0 ,
\]
where \(\iota\) is the [[?lean:New.Data.sourceFormCoords|coordinate isomorphism]] of the source forms with the Euclidean space \(\mathbb{C}^{\mathcal C\times\mathcal I}\) (standard inner product) on pairs of a [[?lean:New.Filling.Classes|class]] \(c\in\mathcal C\) and a [[?lean:New.Filling.BesselCoord|Bessel coordinate]] \(i\in\mathcal I\). The dimension \(\lvert\mathcal C\rvert\lvert\mathcal I\rvert\) of the source is written \(D_X\) ([[?lean:New.Filling.sourceDim|`sourceDim`]]).

## References

1. Lean: `New.Data.goodPoincare`, `New.Data.levelRepresentation`, `New.Data.poincareScale`, `New.Data.scaledPoincare` in `src/New/Spanning/SecondMoment/SpanningTheorem.lean`.
