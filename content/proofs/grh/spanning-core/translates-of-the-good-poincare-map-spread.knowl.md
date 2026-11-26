+++
id = "proofs/grh/spanning-core/translates-of-the-good-poincare-map-spread"
title = "One good translate of the Poincaré map"
kind = "theorem"
summary = "The translates #G e0 s P of the Poincaré map from source forms to target forms form a spread family with error (3/2) b^-2 / 8."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.isSpread_goodPoincare", "New.Data.comap_scaledPoincare_eq_comap_goodPoincare"]
lean_files = ["src/New/Spanning/SecondMoment/SpanningTheorem.lean"]
proof_status = "full"
+++

**Theorem (one translate of the Poincaré map).** Let \(D\) be [[?lean:New.Data|admissible data]] with scale \(b\), and for \(s\) in the finite group \(\bar G\) let \(\mathcal P_s=\lvert\bar G\rvert\,e_0\,s\,\Pi\) be the [[proofs/grh/spanning-core/scaled-poincare-map|translates of the good Poincaré map]], from the [[?lean:New.Data.SourceForm|source forms]] to the [[?lean:New.Data.targetForms|target forms]]. The family \((\mathcal P_s)_{s\in\bar G}\) is [[proofs/grh/spanning-core/spread-family-of-linear-maps|spread]] with error \(\tfrac32\varepsilon_0\), \(\varepsilon_0=\tfrac1{8b^2}\): for every space \(F\) of target forms, with share \(\alpha=\dim F/d_{\mathrm{tar}}\), there is \(s\in\bar G\) with
\[
\dim\mathcal P_s^{-1}(F)\ \le\ \frac{1+\alpha+3\varepsilon_0}{2}\,D_X ,
\]
where \(D_X\) is the dimension of the space of source forms.

## Proof

Apply the [[proofs/grh/spanning-core/one-translate-from-second-moment|one-translate theorem]] with \(\Gamma=\bar G\), \(T\) the forms of principal level on \(Y_0\) with the Petersson product (finite-dimensional), \(\rho\) the action of \(\bar G\), which is unitary, \(\mathrm{pr}_0=\rho(e_0)\), \(B=P\) the scaled Poincaré map, and \(\varepsilon=\varepsilon_0\).

* \(\rho(e_0)\) is an orthogonal projection commuting with \(\rho\): \(e_0\) is a central idempotent of \(\mathbb{C}[\bar G]\) ([[?lean:New.Data.isCentralProj_e₀|`New.Data.isCentralProj_e₀`]]), so it commutes with every group element, and a central idempotent acts in a unitary representation as a self-adjoint idempotent (`New.IsCentralProj.isSymmetricProjection`). Its image is the space of target forms.
* Hypothesis 1: \(\rho(e_0)P\) is a [[proofs/grh/spanning-core/good-poincare-map-is-a-near-isometry|near isometry with error \(5b^{-4}\)]], and \(5b^{-4}\le\varepsilon_0\) (size inequality).
* Hypothesis 2: by the [[proofs/grh/spanning-core/second-moment-of-the-poincare-map|second moment bound]] and \(9b^{-4}\le\varepsilon_0\) (size inequality), \(d_{\mathrm{tar}}\sum_s\lVert P^*\rho(s)P\rVert_{\mathrm{HS}}^2\le\lvert\bar G\rvert(1+\varepsilon_0)D_X^2\); the source \(\mathbb{C}^{\mathcal C\times\mathcal I}\) of \(P\) has dimension \(D_X\).

Hence for every \(F\) there is \(s\) with \(\dim(\rho(e_0)\rho(s)P)^{-1}(F)\le\frac{1+\alpha+3\varepsilon_0}2D_X\). Finally, for \(\varphi\) in the source of \(P\), \(\rho(e_0)\rho(s)P\varphi=c_P\,y\) and \(\mathcal P_s(\iota^{-1}\varphi)=\lvert\bar G\rvert\,y\) with \(y=\rho(e_0)\rho(s)\Pi\iota^{-1}\varphi\); as \(c_P\ne0\) and \(\lvert\bar G\rvert\neq0\), the preimage of \(F\) under \(\rho(e_0)\rho(s)P\) is the image under the coordinate isomorphism \(\iota\) of \(\mathcal P_s^{-1}(F)\), and has the same dimension. \(\blacksquare\)

## Remarks

The two size inequalities \(5b^{-4}\le(8b^2)^{-1}\) and \(9b^{-4}\le(8b^2)^{-1}\) are proved in Lean by `New.Data.le_of_hasLogBound`. The spanning theorem itself, [[?lean:New.Data.enough_forms|Theorem B (enough forms)]], is deduced from this theorem and [[proofs/grh/spanning-core/few-spread-maps-span-almost-everything|few spread maps span almost everything]] in `New/Reduction/ShortAndEnough`.

## References

1. Lean: `New.Data.isSpread_goodPoincare` in `src/New/Spanning/SecondMoment/SpanningTheorem.lean`.
2. Related work named in the Lean file head: H. Petersson (1932); Benedetto–Fickus, Finite normalized tight frames (2003); G. Muić (2010).
