+++
id = "proofs/grh/spanning-core/bessel-systems-exist-at-the-real-places"
title = "Bessel systems exist at the real places"
kind = "theorem"
summary = "For admissible data and each infinite place there is a Bessel system on the real group of Y_0, of discrete series type given by the parameter and the weight of the data at that place."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_besselSystem", "New.Data.unitarySignFrameY", "New.Data.exists_unitary_schur_rep", "New.Data.weylDimensionPoly_paramW_le", "New.Data.volU_div_volU_le", "New.Data.scaledVolumeRatio_le", "New.Data.weylDimensionPoly_mul_scaledVolumeRatio_le", "New.Data.abs_paramW_le", "New.Data.exists_lowestKType_eq_ite", "New.Data.realPlaceSizes", "New.Data.exponent_add_le_mul_sq_r", "New.Data.liftWeight_add_columnCount_le", "New.Data.rank_add_le_cube", "New.Data.rank_sq_mul_log_le", "New.IsBesselFunction.integral_dsKernel_mul_eq_of_convolve_eq", "New.Data.card_X₀"]
lean_files = ["src/New/Spanning/Bessel/FillingData.lean"]
proof_status = "outline"
+++

**Theorem (Bessel functions at a real place).** Let \(D\) be [[?lean:New.Data|admissible data]], \(\mathfrak s=\) [[?lean:New.Data.shape|the shape of \(Y_0\)]] (\(\varrho\) hyperbolic planes, \(X_0\) of rank \(k\), one negative line; rank \(r\)), \(b\) the scale and \(f\) the number of infinite places of \(E\). For every infinite place \(v\) there is a [[proofs/grh/spanning-core/bessel-system|Bessel system]] \(B\) for \((\mathfrak s,b,f)\) which is [[proofs/grh/spanning-core/bessel-system-of-discrete-series-type|of discrete series type]] \(\bigl(2\varsigma_v,\ \mathrm{cc}_v\bigr)\), where \(2\varsigma_v=\) [[?lean:New.Data.paramW|`D.paramW v`]] is the doubled parameter (for a fixed unitary frame with the signs of \(Y_0\)) and \(\mathrm{cc}_v=\) [[?lean:New.Data.columnCount|`D.columnCount v`]] the weight on \(U(X_0)\). Its degree is the formal degree \(\deg_\lambda\) of \(l=2\varsigma_v\), equal to Weyl's dimension polynomial.

## Proof

*Outline; the numerical hypotheses of the quoted theorems are size inequalities of the data, proved in Lean by `le_of_hasLogBound` and not reproduced.*

1. *Frame.* A unitary matrix diagonalising the form of \(Y_0\) to its signs exists (`New.Seesaw.exists_conjTranspose_mul_gradedGram_mul_eq_signMatrix`).
2. *Parameter.* \(l=2\varsigma_v\) has entries of modulus \(\le3a\), large gap with excess \(r^7\) (from the gap instance of the data), and \(\deg_\lambda=\) Weyl's polynomial (Harish-Chandra's formal degree formula, `New.Orbital.harish_chandra_degree_and_orbital`).
3. *Type.* Let \(u\) be the doubled Harish-Chandra parameter of the weight \(\mathrm{cc}_v\) of \(U(\kappa)\). The Schur matrices of this weight, conjugated by \(B_0\) where the positive definite Gram form of the Weyl module is \(B_0^*B_0\), give a continuous unitary representation \(\mathrm{rep}\); it is conjugate to the transposed Schur matrices of transposes, only scalars commute with it (Schur's lemma for Schur modules, library), and for \(e=B_0x\), \(x\) the highest weight vector, \(\langle e,\mathrm{rep}(k)e\rangle=c_u(k)\) (both are the product of principal minors of weight the highest weight). In particular \(\lVert e\rVert=1\). The lowest \(K\)-type of \(u\) is \(\mathrm{cc}_v(1)\) at one index and \(0\) elsewhere.
4. *Point.* The parameters \(2\varsigma_v\) are steep (`New.Data.exists_isSteep`, other area). The [[proofs/grh/spanning-core/stationary-point-with-large-period|stationary point theorem]] with \(B=\) [[?lean:New.Data.liftWeight|the weight of lift \(0\) at \(v\)]], \(a=\mathrm{cc}_v(1)\), \(\beta=b^3\), \(L=3a\), excess \(r^7\) gives \(x\) with \(\ell(x)\le b^{5n}\) and ball volume \(\le b^{60(r+k)^2}\lvert\text{period}\rvert\); by [[proofs/grh/spanning-core/bessel-average-properties|part 5 of the properties of the Bessel average]], \(\mathrm{vol}_x\le b^{60(r+k)^2}\deg_\lambda\int\lVert\mathcal W_{x,e}\rVert^2d\mu\).
5. *Cut pair.* Since \(60(r+k)^2+99r^2\le400r^2\) (\(k\le r\)), the [[proofs/grh/spanning-core/cut-pair-from-the-bessel-average|cut pair theorem]] gives \(F=c\,\mathcal W_{x,e}\) with \(F*(\deg_\lambda c_\lambda)=F\) and a cut pair \((F,F^\flat)\) for \((b,f,\mathrm{rep})\), \(\int\lVert F\rVert^2d\mu=\lvert I\rvert\).
6. *Schur bound.* For \(P\ge b^5\ge(r+1)^4(3a+r+1+2n^2)\), [[proofs/grh/spanning-core/schur-bound-holds-for-functions-fixed-by-the-kernel|Schur's bound]] holds with constants \(P\) and \(\lvert I\rvert/\deg_\lambda\).
7. *Local bounds.* The theorem `New.Floors.exists_hasLocalBounds_of_isCutBessel` (area of `New/Spanning/Frames/RealBandLimits`) produces forms \(J\) such that \(F^\flat\) [[proofs/grh/spanning-core/local-bounds-of-a-bessel-function|has local bounds]] \((b,\deg_\lambda,J)\), from: the cut pair, the size conditions `RealPlaceSizes` (radius \(b^{6n+2}\), \(k>10^9n^3+3n+6\), …), irreducibility of the type, \(\int_{G_1}\lvert\int\langle F(y),F(yg)\rangle d\mu\rvert^2dg\le\lvert I\rvert^2/\deg_\lambda\) (the matrix coefficient formula of the Schur bound knowl), \(\deg_\lambda\Theta\le b^{4r^2}\) (\(\Theta\) the scaled volume ratio; Weyl's polynomial is \(\le b^{2r^2}\) as its \(\le r^2\) factors are \(\le3a\le b^2\), and \(\Theta\le b^{2r^2}\)), and the ball volume bound \(\deg_\lambda\operatorname{vol}\{\lVert g\rVert\le T\}\le T^{9r^2}b^{99r^2}\) (Chebyshev with the tail bound of the coefficient).
8. *Type clauses.* \(F*(\deg_\lambda c_\lambda)=F\) is clause 3 of the discrete series type (rewritten with \(e_\lambda(g)=\deg_\lambda c_\lambda(g^{-1})\)); clause 4 is \(F=c\,\mathcal W_{x,e}\) with absolute convergence. \(\blacksquare\)

## References

1. Lean: `New.Data.exists_besselSystem`, `New.Data.exists_unitary_schur_rep` in `src/New/Spanning/Bessel/FillingData.lean`.
2. Related work named in the Lean file head: Petersson (1932); NIST DLMF §10.22; Baruch, Bessel distributions on the open cell (2001–2004); Comtat et al. (2025).
