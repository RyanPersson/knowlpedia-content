+++
id = "proofs/grh/spanning-core/dimension-of-the-target"
title = "Dimension of the target"
kind = "theorem"
summary = "The space of target forms has dimension at most the order of the finite group times the Bessel degree times the mass of the standard lattice of rank r."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.targetDim_le_card_mul_besselDegree_mul_mass", "New.Data.finrank_principalForms_spaceW", "New.Data.decreasingPosition_paramW"]
lean_files = ["src/New/Spanning/SecondMoment/SpanningTheorem.lean"]
proof_status = "outline"
+++

**Theorem (dimension of the target).** Let \(D\) be [[?lean:New.Data|admissible data]], \(\bar G\) the finite group [[?lean:New.Data.chosenGL|\(\prod_w\mathrm{GL}_r(\mathbb{F}_w)\)]] over the chosen places \(w\) above \(p_0,p_1\), and \(d_{\mathrm{tar}}=\dim\) of the [[?lean:New.Data.targetForms|target forms]] (the [[?lean:New.Data.goodForms|good forms]] on \(Y_0\)). Then
\[
d_{\mathrm{tar}}\ \le\ \lvert\bar G\rvert\cdot\deg\cdot\mathrm{mass}_r ,
\]
where \(\deg\) is the [[?lean:New.Filling.besselDegree|Bessel degree]] of the [[?lean:New.Data.filling|filling data of \(D\)]] (the product over the infinite places of \(E\) of the degree constants of the local Bessel systems) and \(\mathrm{mass}_r\) is the [[?lean:New.mass|mass]] of the genus of the standard hermitian lattice of rank \(r\) over \(E\).

More precisely, on the definite space \(W_m\) ([[?lean:New.Data.spaceW|\(W_j\)]] for \(j=m\)),
\[
\dim\bigl(\text{forms of principal level on }W_m\bigr)=\lvert\bar G\rvert\cdot\mathrm{mass}_r\cdot\prod_{v}\deg{}^{c}_v ,
\]
where \(\deg^c_v\) is the [[?lean:New.HCParam.formalDegree|formal degree]] of the doubled parameter [[?lean:New.Data.paramW|\(2\varsigma_v\)]] for the all-positive signs (the compact group \(U(r)\)).

## Proof

*Outline; the steps marked (L) are Lean statements of other areas, used as stated.*

1. (L) [[proofs/grh/spanning-core/equal-multiplicities-of-eigensystems|Equality of dimensions]]: \(d_{\mathrm{tar}}=\dim\) of the good forms on \(W_m\). These are a subspace of the [[?lean:New.Data.principalForms|forms of principal level]] on \(W_m\).
2. (L) Since the parameter has a gap for the signs of \(Y_0\) (`New.Data.hasGap_signsY_paramW`), it is twice the Harish-Chandra parameter of an algebraic weight \((\kappa,e)\) (`New.Exchange.exists_isHCParam_of_hasGap`), and on the definite (standard) space \(W_m\) the forms of principal level are isomorphic to the algebraic modular forms of weight \((\kappa,e)\) fixed by the principal level \(J_M\) (`New.Space.algFormEquiv`).
3. (L) The principal level is small: every stabiliser \(\Gamma\cap gJ_Mg^{-1}\) in the rational points \(\Gamma\) of the definite unitary group is trivial (`New.Data.classAut_eq_bot_of_le_chosenLevel`, using a size inequality for \(r\)). For such a level the space of algebraic forms has dimension (number of double cosets \(\Gamma\backslash G_f/J_M\)) \(\times\) (dimension of the weight) (`New.finrank_levelSpace_smoothFormRep`), and the number of double cosets is the class sum of \(1\) (`New.card_classes_eq_classSum`).
4. (L) The class sum of \(1\) for \(J_M\) is the index \([K_0:J_M]=\lvert\bar G\rvert\) times the class sum for the maximal level \(K_0\) (`classSum_one_of_le`, `relIndex_levelOf`), which is \(\mathrm{mass}_r\) (`New.classSum_stdRatPoints_eq_mass`).
5. (L) The dimension of the weight \((\kappa,e)\), a product over the infinite places, is \(\prod_v\deg^c_v\) (`IsHCParam.prod_formalDegree`). This gives the displayed formula.
6. (L) \(\prod_v\deg^c_v=\deg\): the degree constant of the Bessel system at \(v\) is the formal degree of the parameter for the signs of \(Y_0\) (`New.Filling.Fits.isDiscreteSeriesBessel`, field `deg_eq`), and by Harish-Chandra's formal degree formula (`New.Orbital.harish_chandra_degree_and_orbital`, valid for parameters with a large gap) the formal degree equals Weyl's dimension polynomial of the parameter, which does not depend on the signs.

Combining 1, the inclusion, 5 and 6 gives the theorem. \(\blacksquare\)

## References

1. Lean: `New.Data.targetDim_le_card_mul_besselDegree_mul_mass`, `New.Data.finrank_principalForms_spaceW` in `src/New/Spanning/SecondMoment/SpanningTheorem.lean`.
