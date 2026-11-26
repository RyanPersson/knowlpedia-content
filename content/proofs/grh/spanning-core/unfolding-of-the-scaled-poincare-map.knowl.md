+++
id = "proofs/grh/spanning-core/unfolding-of-the-scaled-poincare-map"
title = "Unfolding: the blocks of P* s P are amplitude sums"
kind = "theorem"
summary = "The matrix coefficients of the translates of the scaled Poincaré map are the amplitude sums of the filling data divided by the unipotent covolume."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.hasAmplitudeBlocks_scaledPoincare"]
lean_files = ["src/New/Spanning/SecondMoment/SpanningTheorem.lean"]
proof_status = "outline"
+++

**Theorem (unfolding).** Let \(D\) be admissible data, \(S\) its [[?lean:New.Data.filling|filling data]], \(\rho\) the level representation and \(P\) the [[proofs/grh/spanning-core/scaled-poincare-map|scaled Poincaré map]]. Then \(P\) [[?lean:New.Filling.HasAmplitudeBlocks|has amplitude blocks]]: for every \(s\) in the finite group, all classes \(c,c'\) and Bessel coordinates \(i,j\), with \(e_{(c,i)}\) the standard basis vectors of the source,
\[
\bigl\langle\rho(s)\,Pe_{(c',j)},\ Pe_{(c,i)}\bigr\rangle=\frac1\nu\,A(c,s,c')_{(i,j)},
\]
where \(\nu\) is the [[?lean:New.Filling.unipotentCovolume|unipotent covolume]] and \(A(c,s,c')\) is the [[?lean:New.Filling.amplitudeSum|amplitude sum]] of the uncut Bessel function over all terms: the sum over the rational \(\gamma\) such that \(h_c^{-1}\gamma h_{c'}\) is integral with reduction \(s\) of the [[?lean:New.Filling.amplitude|amplitudes]] \(\int\beta_c(y)\beta_{c'}(\gamma^{-1}y)\,W_i(y)\overline{W_j(\gamma^{-1}y)}\,dy\).

## Proof

*Outline.* By `New.Data.poincare_eq_poincareMap_comp` (Lean statement of the area of `New/Spanning/Unfolding/SeriesPeriod`) the Poincaré map is \(\Pi=\mathcal P\circ\iota\), where \(\mathcal P\) is the [[?lean:New.Filling.Fits.poincareMap|Poincaré series map]] of the filling data fitted to \(Y_0\); hence \(\Pi\circ\iota^{-1}=\mathcal P\) and \(P=c_P\mathcal P\). The [[?lean:New.Filling.Fits.petersson_poincare|Petersson product formula for Poincaré series]] states that for \(k\) in the standard maximal level with reduction \(s\) at the chosen places,
\[
\langle k\,\mathcal Pe_{(c',j)},\mathcal Pe_{(c,i)}\rangle=\operatorname{vol}(J)\cdot A(c,s,c')_{(i,j)} ;
\]
it applies to the integral lift of \(s\) through which \(\rho(s)\) acts, whose reduction is \(s\). Multiplying both arguments by the real number \(c_P=(\operatorname{vol}(J)\nu)^{-1/2}\) multiplies the product by \(c_P^2=1/(\operatorname{vol}(J)\nu)\) (`New.Filling.hasAmplitudeBlocks_smul_of_inner_eq`), which gives the claim. \(\blacksquare\)

## References

1. Lean: `New.Data.hasAmplitudeBlocks_scaledPoincare` in `src/New/Spanning/SecondMoment/SpanningTheorem.lean`.
