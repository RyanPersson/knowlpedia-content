+++
id = "proofs/grh/reduction-main/normalized-poincare"
title = "The normalised Poincaré maps from the source to the target"
kind = "definition"
summary = "The translates s p of the map p = c_B c_ss^{-1} #G e_0 P from ramified source forms to target forms, and the set of ramified source forms integral at every finite place."
aliases = ["normalizedPoincare", "projectedPoincare", "seesawConst", "integralRamified", "scaledInclusion"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.seesawConst", "New.Data.scaledInclusion", "New.Data.projectedPoincare", "New.Data.normalizedPoincare", "New.Data.coe_normalizedPoincare", "New.Data.integralRamified", "New.Data.exists_lowerChain_poincare_eq", "New.Data.normSqAt_normalizedPoincare", "New.Data.range_normalizedPoincare"]
lean_files = ["src/New/Reduction/ShortAndEnough.lean"]
+++

Let \(D\) be [[proofs/grh/reduction-main/data|data]]. Notation from other chapters: \(\mathcal S_X\) is the space of [[?lean:New.Data.SourceForm|source forms]] on \(\mathrm U(X_0)\), of dimension \(D_X\); \(\mathcal S\subseteq\mathcal S_X\) the [[?lean:New.Data.ramifiedSourceForms|ramified source forms]] (the **source**); \(\mathcal T\) the [[?lean:New.Data.targetForms|target forms]] (the **target**), of dimension \(d_T\); \(\bar G\) the finite group [[?lean:New.Data.chosenGL|\(\prod_w\mathrm{GL}_r(k_w)\)]] over the chosen places, acting on the forms of principal level on \(Y_0\); \(e_0\) the [[?lean:New.Data.e₀|central idempotent]] of \(\mathbb C[\bar G]\) projecting onto the good forms; \(\mathcal P\) the [[?lean:New.Data.poincare|Poincaré map]] from source forms to forms on \(Y_0\); and \(\iota_\vartheta\) the [[?lean:New.Data.lowerChain|lower chain of \(m\) lifts]] \(Y_0\to Y_m\) for a twist \(\vartheta\).

- **Seesaw constant.** By the [[?lean:New.Data.seesaw_identity|seesaw identity]] there is \(c_{ss}\in\mathbb C^\times\) such that every twist \(\vartheta\) has a [[?lean:New.Data.IsChainDatum|chain datum]] \(\Psi\) with \(\iota_\vartheta(\mathcal P\varphi)=c_{ss}\,B_{\vartheta,\Psi}\varphi\) for all \(\varphi\in\mathcal S\), \(B_{\vartheta,\Psi}\) being the [[?lean:New.Data.compositeLift|composite lift]]. One such \(c_{ss}\) is fixed (by choice).
- For \(s\in\bar G\), the **normalised Poincaré map** is
\[
s\mathfrak p:\ \mathcal S\to\mathcal T,\qquad s\mathfrak p(\varphi):=c_B\cdot\#\bar G\cdot e_0\,s\,\bigl(c_{ss}^{-1}\mathcal P\varphi\bigr),
\]
with [[proofs/grh/reduction-main/gain-normalisation|\(c_B\)]]. Equivalently \(s\mathfrak p=c_B\,c_{ss}^{-1}\cdot\mathrm{gp}_s|_{\mathcal S}\), where \(\mathrm{gp}_s=\#\bar G\,e_0\,s\,\mathcal P:\mathcal S_X\to\mathcal T\) is the [[?lean:New.Data.goodPoincare|good Poincaré map]]. We write \(\mathfrak p=1\mathfrak p\).
- The set \(\mathcal S^{\mathrm{int}}\subseteq\mathcal S\) of **integral ramified source forms** consists of the \(\varphi\in\mathcal S\) that are [[?lean:New.Data.integralSourceForms|integral]] at every [[proofs/grh/reduction-main/prime-padic-iso|finite place \(\iota\) of \(\mathbb C\)]].

## Properties

1. \(s\mathfrak p(\varphi)=s\cdot\mathfrak p(\varphi)\) (action of \(s\) on forms on \(Y_0\)), because \(e_0\) is central.
2. For every twist \(\vartheta\) there is a chain datum \(\Psi\) with \(\iota_\vartheta(c_{ss}^{-1}\mathcal P\varphi)=B_{\vartheta,\Psi}\varphi\) for all \(\varphi\in\mathcal S\).
3. For \(\sigma\in\operatorname{Aut}(\mathbb C)\): \(\lVert\Theta_1\,s\mathfrak p\varphi\rVert_\sigma^2=c_B^{\,2}\,\lVert\Theta_1(c_B^{-1}s\mathfrak p\varphi)\rVert_\sigma^2\), as \(c_B\) is a positive rational number.
4. The image of \(s\mathfrak p\) is \(\mathrm{gp}_s(\mathcal S)\), as \(c_B,c_{ss}^{-1}\ne0\).

## References

1. Lean: the declarations in the front matter, in `src/New/Reduction/ShortAndEnough.lean`. The Lean `D.poincare` is the Poincaré map at the fixed linear form `D.besselForm` and archimedean point `D.besselPoint`, without the factor `poincareScale`, which \(c_{ss}\) absorbs.
