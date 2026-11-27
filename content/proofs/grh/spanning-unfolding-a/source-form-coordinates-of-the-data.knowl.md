+++
id = "proofs/grh/spanning-unfolding-a/source-form-coordinates-of-the-data"
title = "Source form coordinates and the good projection of a translate"
kind = "definition"
summary = "For admissible data, source forms are identified with vectors indexed by classes and Bessel coordinates, and each s in the finite group G-bar gives the map translate-then-project to the good forms."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.sourceFormCoords", "New.Data.goodProjTranslate"]
lean_files = ["src/New/Spanning/Unfolding/FillingAdmissible.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] with [[?lean:New.Data.filling|filling data]] \(S_D\), which [[proofs/grh/spanning-unfolding-a/filling-data-fit-the-space-y0|fit]] the space \(Y_0\).

The **source form coordinates** of \(D\) are the linear isomorphism
\[
\{\text{source forms on }X_0\}\ \xrightarrow{\ \sim\ }\ \mathbb C^{\{\text{classes}\}\times I},
\]
from the space of [[?lean:New.Data.SourceForm|source forms]] to vectors indexed by the [[?lean:New.Filling.Classes|classes]] and the tuples \(I\) of Bessel coordinates of \(S_D\), obtained by first applying the central translation by the [[?lean:New.Data.latticeScale|lattice scale]] of \(Y_0\) ([[?lean:New.Data.centralRep|central action]], a bijection) and then the [[proofs/grh/spanning-unfolding-a/source-forms-in-bessel-coordinates|source form coordinates of the fitting space]] (values at the class representatives in the coordinates of the Bessel systems).

For \(s\) in the finite group \(\bar G=\prod_wGL_r(k_w)\) ([[?lean:New.Data.chosenGL|chosen general linear group]]), the **good projection of the translate by \(s\)** is the linear map from the forms of principal level on \(Y_0\) ([[?lean:New.Data.principalForms|principal forms]]) to the image of the good [[?c:Idempotent element|idempotent]] \(e_0\) ([[?lean:New.Data.e₀|good idempotent]]):
\[
F\longmapsto\lvert\bar G\rvert\cdot e_0\bigl(s\cdot F\bigr),
\]
the action being that of the group algebra of \(\bar G\) on principal forms ([[?lean:New.Data.principalRep|principal representation]]).

## References

1. Lean: `New.Data.sourceFormCoords` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
2. Lean: `New.Data.goodProjTranslate` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
