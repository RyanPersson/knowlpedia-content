+++
id = "proofs/grh/spanning-core/coordinates-on-frames-over-a-gram-matrix"
title = "Coordinates on the tuples with given products with the frame"
kind = "lemma"
summary = "Lebesgue measure on the tuples whose products with the frame form a fixed invertible matrix Z, written in terms of their Gram matrix and the fixer of the frame."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.RealPlace.dualFrameOfGram", "New.RealPlace.gram_dualFrameOfGram", "New.RealPlace.sphereMass", "New.RealPlace.lintegral_fixerHaar", "New.RealPlace.lintegral_fixerHaar_eq_unipotentOf", "New.RealPlace.lintegral_fixerHaar_eq_inv", "New.RealPlace.lintegral_neg_single_add_freeCols_mulVec_eq", "New.RealPlace.lintegral_eq_lintegral_sphereMass_mul_dualFrameOfGram", "New.RealPlace.lintegral_eq_dualFrameOfGram_mul", "New.RealPlace.dualFrameOfGram_mul_eq_gramSection_mul", "New.RealPlace.gramCoords_dualFrameOfGram_mul", "New.RealPlace.splitLast"]
lean_files = ["src/New/Spanning/Bessel/MeanValue.lean"]
proof_status = "outline"
+++

Setting: the real unitary group \(G_1\) of the form \(h\) with Gram matrix \(J\) (see [[proofs/grh/spanning-core/bessel-length|Bessel length]]), \(k=\lvert\kappa\rvert\ge1\), the frame matrix \(F=(e_1,\dots,e_\varrho,z)\), and \(R\) the matrix with columns \(e_b\) \((b\le\varrho)\) and \(x_i\) \((i\in\kappa)\). The **fixer of the frame** is \(R^\circ=\mathsf U^0\cdot U(\kappa)\), with the measure \(ds=du\,dh\) ([[?lean:New.RealPlace.fixerHaar|`fixerHaar`]]): Lebesgue measure in the parameter \(q\) of \(u=\mathrm{unipotentOf}(q)\in\mathsf U^0\) times the Haar probability measure on \(U(\kappa)\). Hermitian \((\varrho+1)\times(\varrho+1)\) matrices \(T\) are given real coordinates \(t\) ([[?lean:New.hermOfReal|`hermOfReal`]]) with Lebesgue measure \(dt\).

**Standard dual tuple.** For a hermitian \(T\) with \(1+T_{\varrho+1,\varrho+1}\ge0\), let \(y(T)\) be the tuple of the vectors
\[
e_b^*+\tfrac12\sum_aT_{ab}e_a\quad(b\le\varrho),\qquad -z+\sum_aT_{a,\varrho+1}e_a+\sqrt{1+T_{\varrho+1,\varrho+1}}\;x_{k_0}.
\]
It is dual to the frame (\(F^*J\,y(T)=1\)) and has Gram matrix \(y(T)^*Jy(T)=T\).

**Sphere mass.** \(\sigma_k(r)=\pi^kr^{k-1}/(k-1)!\) for \(r>0\) and \(\sigma_k(r)=0\) for \(r\le0\).

**Lemma.** Let \(K\ge0\) be a measurable function of \((2\varrho+k+1)\times(\varrho+1)\) complex matrices.

1. (\(Z=1\).) \(\displaystyle\int K(JF+Rp)\,dp=\int2^{-\varrho}\,\sigma_k(1+T_{\varrho+1,\varrho+1})\int_{R^\circ}K\bigl(s\,y(T)\bigr)\,ds\,dt\), where \(p\) runs over the complex \((\varrho+k)\times(\varrho+1)\) matrices with Lebesgue measure and \(T=T(t)\).
2. For invertible \(Z\), with \(T'=(Z^{-1})^*T(t)Z^{-1}\):
\[
\int K(JFZ+Rp)\,dp=\int\lvert\det Z\rvert^{2(k-1)}\,2^{-\varrho}\,\sigma_k(1+T'_{\varrho+1,\varrho+1})\int_{R^\circ}K\bigl(s\,y(T')\,Z\bigr)\,ds\,dt .
\]
3. For \(Z\in\Omega\) and \(T_0=F^*JF=\operatorname{diag}(0,\dots,0,-1)\): \(y\bigl((Z^{-1})^*T_0Z^{-1}\bigr)Z=\gamma_ZF\), the image of the frame under the [[proofs/grh/spanning-core/gram-section|Gram section]], and \(1+\bigl((Z^{-1})^*T_0Z^{-1}\bigr)_{\varrho+1,\varrho+1}=\nu(Z)^2\).
4. The measure \(ds\) on \(R^\circ\) is invariant under inversion.

## Proof

*The Gram matrix of \(y(T)\)*: \(h\) pairs \(e_c\) with \(e_c^*\), is the identity on \(X_0\) and \(-1\) at \(z\). For \(a,b\le\varrho\) the product is \(\tfrac12T_{ab}+\tfrac12\overline{T_{ba}}=T_{ab}\); for \(a\le\varrho\) and the last vector it is \(T_{a,\varrho+1}\); and the last vector has \(h\)-square \((1+T_{\varrho+1,\varrho+1})-1\).

(3) Compare coefficients of \(e_a\), \(x_i\), \(z\), \(e_a^*\): by the definition of the Gram section, \(\gamma_ZF=(F\,Y(Z,Z^*)+F'\delta(\nu(Z)))Z\), and \((Z^{-1})^*T_0Z^{-1}=-\zeta^*\zeta\) with \(\zeta\) the last row of \(Z^{-1}\); the rows \(a\le\varrho\) of \(Y(Z,Z^*)\) are those of \(-\zeta^*\zeta\), halved in the first \(\varrho\) columns, and its last row is \((0,\dots,0,-1)\).

(1) *Outline.* The tuples \(JF+Rp\) are exactly the tuples dual to the frame. One chooses the first \(\varrho\) vectors and then the last. For the first \(\varrho\) vectors, the library change of variables `New.RealPlace.lintegral_eq_unipotent_coords` writes them as \(u\cdot(e_b^*+\frac12\sum_aT_{ab}e_a)_b\) with \(u=\mathrm{unipotentOf}(q)\) and \(T\) the hermitian \(\varrho\times\varrho\) Gram matrix, with Jacobian factor \(2^{-\varrho}\) (Lean statement, not reproved here). For the last vector \(-z+\sum a_be_b+x\), \(x\in X_0\), with \(u\) fixed: translate \(a\) (which absorbs the action of \(u\)) and use polar coordinates in \(x\in\mathbb{C}^\kappa\) (library statement `New.Floors.lintegral_eq_polar`: \(dx=\sigma_k(r)\,dr\,dh\) with \(x=h\sqrt r\,x_{k_0}\), \(h\in U(\kappa)\)), then shift \(r\) by \(1\); here \(r-1\) is the \(h\)-square of the vector. Finally a measure preserving bijection (`New.exists_measurePreserving_hermCorner`) assembles the real coordinates of \(T\) from those of its upper left block, the rest of its last column and its corner.

(2) *Outline.* Substitute \(p\mapsto pZ\) (factor \(\lvert\det Z\rvert^{2(\varrho+k)}\)), apply (1) to \(K(\,\cdot\,Z)\), and substitute \(T\mapsto Z^*TZ\) in the hermitian matrices (factor \(\lvert\det Z\rvert^{-2(\varrho+1)}\)); the two library change of variables formulas are `New.lintegral_eq_det_mul_comp_mul_mul` and `New.lintegral_eq_det_mul_comp_congruence`.

(4) \((uh)^{-1}=(h^{-1}u^{-1}h)h^{-1}\); inversion preserves \(du\) and \(dh\), and conjugation by \(h\) preserves \(du\) (library statement `New.RealPlace.measurePreserving_conj_bessel`). \(\blacksquare\)

## References

1. Lean: `New.RealPlace.dualFrameOfGram`, `New.RealPlace.gram_dualFrameOfGram`, `New.RealPlace.lintegral_eq_lintegral_sphereMass_mul_dualFrameOfGram`, `New.RealPlace.lintegral_eq_dualFrameOfGram_mul`, `New.RealPlace.dualFrameOfGram_mul_eq_gramSection_mul`, `New.RealPlace.lintegral_fixerHaar_eq_inv` in `src/New/Spanning/Bessel/MeanValue.lean`.
