+++
id = "proofs/grh/spanning-unfolding-a/rigidity-of-frames"
title = "Rigidity of frames"
kind = "theorem"
summary = "A term that moves the frame vectors of a point in a box by less than 1/(N rho) at every infinite place fixes the frame."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.frameImage_eq_frameImage_one_of_close", "New.Filling.frameVector_sub_eq_sum", "New.Filling.frameImage_inr_eq_of_frameProducts_eq", "New.Filling.norm_Φ_frameProducts_sub_le", "New.Filling.termsOver.isIntegral_inl_besselFrame", "New.Filling.one_le_pow_mul_norm_basisScale_div", "New.Filling.norm_Φ_sub_mul_norm_basisScale_div_le"]
lean_files = ["src/New/Spanning/Unfolding/Packing.lean"]
proof_status = "full"
+++

**Theorem (rigidity of frames).** Let \(E\) be a [[?c:CM field|CM field]] and \(S\) [[?lean:New.Filling|filling data]] over \(E\) satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], with parameter \(b\), prime \(N\), \(n=\varrho+1\). Let \(g\) be a [[?lean:New.Filling.termsOver|term]] over some block \((d,r,d')\): a rational [[?c:Isometry of a hermitian space|isometry]] of \(V\) with \(h_d^{-1}gh_{d'}\) integral and of reduction \(r\). Let \(R\ge1\), \(\rho=b^{37n}R\), and let \(z\in G_\infty\) be such that at every [[?c:Infinite place of a number field|infinite place]] \(v\)

- the [[?lean:New.besselLength|Bessel length]] of \(z_v\) is at most \(b^{6n+2}R\);
- the [[?lean:New.frameVector|frame vectors]] \(z_v^{-1}f_a\) (\(a=0,\dots,\varrho\); \(f=(e_1,\dots,e_\varrho,z)\)) have Euclidean norm at most \(\rho\);
- for every \(a\), \(\bigl\lVert (g^{-1}z)_v^{-1}f_a-z_v^{-1}f_a\bigr\rVert<(N\rho)^{-1}\), where \(g\) acts through the [[?lean:New.Filling.ratToInf|rescaled embedding]].

Then \(g\) fixes the frame: \(g f_a=f_a\) for all \(a\).

## Proof

Write \(\delta_v(a)\) for the distance in the third hypothesis, \(\sigma_v\) for the [[?lean:New.Filling.basisScale|basis scales]] and \(\kappa_v\) for the [[?lean:New.Filling.realM|real number \(\kappa_v\)]]; by the standing hypotheses \(1\le\lvert\kappa_v\rvert\le b^{23}\).

**Rigidity principle.** Let \(\phi\) be a function on rational isometries with values in \(E\) that is an [[?c:Algebraic integer|algebraic integer]] on every term, and suppose \(\lvert\Phi_v(\phi(g)-\phi(1))\rvert\le N\rho\,\delta_v(a)\) for some \(a\) and all \(v\). Then \(\phi(g)=\phi(1)\). Indeed \(1\) is a term (over \((d,1,d)\)), so \(\phi(g)-\phi(1)\) is an algebraic integer all of whose archimedean absolute values are \(<1\); such an integer is \(0\) ([[?lean:New.eq_zero_of_forall_norm_lt_one|small algebraic integers vanish]]; its norm is an integer of absolute value \(<1\)).

**Step 1: the frame products.** Let \(Z(\gamma)_{ba}=h(f_b,\gamma f_a)\) be the [[?lean:New.Filling.frameProducts|frame products]]; they are algebraic integers for terms ([[?lean:New.Filling.isIntegral_frameProducts|integrality of frame products]]). For rational \(\gamma,\gamma'\), \(y\in G_1\) and a place \(v\),
\[
\lvert\Phi_v(Z(\gamma)_{ba}-Z(\gamma')_{ba})\rvert\le N\,\lVert y^{-1}f_b\rVert\;\bigl\lVert(\gamma^{-1}y)^{-1}f_a-(\gamma'^{-1}y)^{-1}f_a\bigr\rVert .\tag{1}
\]
Indeed, since \(y\) is an isometry of the normalised form \(h_1\) of \(G_1\), \(h_1(y^{-1}f_b,(\gamma^{-1}y)^{-1}f_a)\) is the \((b,a)\) frame product of the image of \(\gamma\) in \(G_1\), which equals \(\frac tN\Phi_v(Z(\gamma)_{ba})\) with \(t=\kappa_v^{\varrho-b}\kappa_v^{\varrho-a}\) ([[?lean:New.Filling.realFrameGram_ratToInf|frame products at an infinite place]]). As \(\lvert t\rvert\ge1\), the left side of (1) is at most \(N\,\lvert h_1(y^{-1}f_b,\,F_\gamma-F_{\gamma'})\rvert\) with \(F_\gamma=(\gamma^{-1}y)^{-1}f_a\), and \(\lvert h_1(x,w)\rvert\le\lVert x\rVert\lVert w\rVert\) ([[?lean:New.norm_inner_J₁_le|Cauchy–Schwarz for the normalised form]]).
Applying (1) with \(\gamma=g,\gamma'=1,y=z_v\) and \(\lVert z_v^{-1}f_b\rVert\le\rho\), the rigidity principle gives \(Z(g)_{ba}=Z(1)_{ba}\) for all \(a,b\).

**Step 2: \(gf_a-f_a\) lies in the span of the \(e_i\).** Fix \(a\) and write \(gf_a-f_a=\sum_i\alpha_ie_i+x+\zeta z+\sum_i\alpha_i^{*}e_i^{*}\) with \(x\in X_0\). From \(h(e_i,gf_a)=h(e_i,f_a)\) we get \(\alpha_i^{*}=0\), and from \(h(z,gf_a)=h(z,f_a)\) and \(N\ne0\) we get \(\zeta=0\). Since \(g\) is an isometry, \(h(gf_a,gf_a)=h(f_a,f_a)\); expanding with \(gf_a=f_a+\sum\alpha_ie_i+x\), and using that the \(e_i\) are isotropic, mutually orthogonal and orthogonal to \(X_0\oplus Ez\), this gives \(h(x,x)=0\). The form on \(X_0\) is the standard one over a CM field, hence anisotropic ([[?lean:New.Filling.eq_zero_of_ratMiddle_form_eq_zero|anisotropy of the middle form off \(z\)]]), so \(x=0\).

**Step 3: the coordinates along the \(e_a\).** We show \(g_{e_a,f_b}=1_{e_a,f_b}\) for all \(b\) by downward induction on \(a\in\{1,\dots,\varrho\}\). The function \(\phi(\gamma)=\gamma_{e_a,f_b}\) is integral on terms, because this entry is unchanged by the passage to the lattice bases of the two classes, where the matrix of a term is integral. By Step 2, for \(y\in G_1\),
\[
(g^{-1}y)^{-1}f_b-y^{-1}f_b=\sum_{x=1}^{\varrho}\Phi_v\bigl((g-1)_{e_x,f_b}\bigr)\frac{\sigma_v(f_b)}{\sigma_v(e_x)}\;y^{-1}e_x ,\tag{2}
\]
and by the induction hypothesis the coefficients with \(x>a\) vanish. Since the Bessel length of \(z_v\) is at most \(b^{6n+2}R\), there is \(w\) in the real unipotent group \(\mathsf U\) with [[?c:Operator norm|operator norm]] \(\lVert wz_v\rVert\le b^{6n+2}R\) ([[?lean:New.RealPlace.exists_norm_le_of_besselLength_le|small unipotent translate]]). Apply row \(e_a\) of \(w\) to the combination \(\sum_xc_xe_x\) of the coefficients \(c_x\) of (2): as \(w\) is [[?c:Unitriangular matrix|unitriangular]], \(w_{e_a,e_x}=\delta_{ax}\) for \(x\le a\), so the result is \(c_a\); on the other hand it is bounded by \(\lVert wz_v\rVert\cdot\lVert\sum_xc_x\,z_v^{-1}e_x\rVert\) ([[?lean:New.norm_sum_le_mul_norm_sum_frameVector|norm of a row applied to a frame combination]]). Hence
\[
\lvert\Phi_v((g-1)_{e_a,f_b})\rvert\,\Bigl\lvert\frac{\sigma_v(f_b)}{\sigma_v(e_a)}\Bigr\rvert\le b^{6n+2}R\,\delta_v(b).
\]
The quotient of scales has absolute value \(\lvert\kappa_v\rvert^{\varrho-b}/\lvert\kappa_v\rvert^{\varrho-a}\ge b^{-23\varrho}\). Therefore \(\lvert\Phi_v((g-1)_{e_a,f_b})\rvert\le b^{23\varrho+6n+2}R\,\delta_v(b)\le b^{37n}R\,\delta_v(b)\le N\rho\,\delta_v(b)\), and the rigidity principle gives \(g_{e_a,f_b}=1_{e_a,f_b}\).

Steps 2 and 3 together give \(gf_b=f_b\) for all \(b\).

## References

1. Lean: `New.Filling.frameImage_eq_frameImage_one_of_close` in `src/New/Spanning/Unfolding/Packing.lean`.
2. Lean: `New.Filling.frameVector_sub_eq_sum` in `src/New/Spanning/Unfolding/Packing.lean`.
3. Lean: `New.Filling.frameImage_inr_eq_of_frameProducts_eq` in `src/New/Spanning/Unfolding/Packing.lean`.
4. Lean: `New.Filling.norm_Φ_frameProducts_sub_le` in `src/New/Spanning/Unfolding/Packing.lean`.
5. Lean: `New.Filling.termsOver.isIntegral_inl_besselFrame` in `src/New/Spanning/Unfolding/Packing.lean`.
6. Lean: `New.Filling.one_le_pow_mul_norm_basisScale_div` in `src/New/Spanning/Unfolding/Packing.lean`.
7. Lean: `New.Filling.norm_Φ_sub_mul_norm_basisScale_div_le` in `src/New/Spanning/Unfolding/Packing.lean`.
