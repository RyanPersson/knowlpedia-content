+++
id = "proofs/grh/spanning-unfolding-a/lattices-of-unipotent-row-coordinates"
title = "The lattices of row coordinates of the arithmetic unipotent group"
kind = "proposition"
summary = "The free entries of a row of the unipotent congruence subgroup fill an explicit lattice, and the imaginary parts at (e_a, e_a*) fill the lattice of rescaled imaginary parts of skew integers; both lattices are attained by elements with trivial later coordinates."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.freeLattice", "New.Filling.freeBlock", "New.Filling.exists_classBasis_eq_fromBlocks", "New.Filling.classUnipotent_sub_one_div_M_row_integral", "New.Filling.rowCoords_fst_mem_freeLattice", "New.Filling.exists_rowCoords_fst_eq", "New.Filling.rowCoords_snd_mem_imSkewLattice", "New.Filling.exists_rowCoords_snd_eq", "New.Filling.star_inv_mul_apply_eStar_eq_neg", "New.Filling.isIntegral_inv_mul_apply_eStar", "New.Filling.exists_fundamental_domain_freeLattice", "New.Filling.prod_norm_basisScale_sq_div_eq"]
lean_files = ["src/New/Spanning/Unfolding/CutoffIntegral.lean"]
proof_status = "full"
+++

**Proposition.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity with \(f\) [[?c:Infinite place of a number field|infinite places]], \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], with level \(M\) and prime \(N\); let \(c\) be a class and \(a\in\{1,\dots,\varrho\}\). Let \(\sigma_v\) be the [[?lean:New.Filling.basisScale|basis scales]] and \(\lambda_v(a)=\sigma_v(e_a)^2=\kappa_v^{2(\varrho-a)}/N\) (with \(a\) counted from \(0\) as in the source; [[?lean:New.Filling.frameScaleSq|squared frame scale]]). Let \(\mathcal F_a\) be the set of columns \(j\) with \((a,j)\) free, of cardinality \(n_a=2(\varrho-1-a)+k+1\) (again with \(a\) from \(0\)).

**(i) Class basis.** The [[?lean:New.Filling.classBasis|class basis]] \(B_c\) is the identity except on the middle block \(X_0\oplus Ez\), where it is a matrix \(B_c^{\mathrm{mid}}\) over the [[catalog/arithmetic/adeles-number-field-finite|finite adeles]]; multiplication by \(\det B_c^{\mathrm{mid}}\) scales [[harmonic-analysis/haar-measure|Haar measure]] of the finite adeles by \(N^{f}\), i.e. its [[?lean:New.genIndex|index]] is \(N^{-f}\).

**(ii) Free lattice.** Define the **free lattice** \(L_a\subseteq\mathbb C^{\mathcal F_a\times\{v\}}\) as the set of vectors \(\bigl(\tfrac{M}{\sigma_v(e_a)}\sigma_v(j)\,\Phi_v(x_j)\bigr)_{j,v}\), for \(x\in E^{\mathcal F_a}\) such that the row vector \(x\) (extended by \(0\)) times \(B_c\) has entries in \(\widehat{\mathcal O}\) at the columns of \(\mathcal F_a\). Then:

- for every \(\gamma\in\mathsf U_c(M)\), the free entries of the row \(e_a\) of its real image lie in \(L_a\);
- every \(l\in L_a\) is the vector of free entries of the row \(e_a\) of the image of some \(\gamma\in\mathsf U_c(M)\) all of whose [[proofs/grh/spanning-unfolding-a/row-coordinates-of-real-unipotent-group|row coordinates]] in the rows \(e_d\), \(d>a\), vanish;
- \(L_a\) has a measurable strict fundamental domain (a set containing exactly one translate of every vector) of [[?c:Lebesgue measure|Lebesgue volume]]
\[
\Bigl(\frac{\prod_vM^2/\lambda_v(a)}{\operatorname{vol}(\widehat{\mathcal O})}\Bigr)^{n_a}.
\]

**(iii) Imaginary lattice.** Let \(L'_a\subseteq\mathbb R^{\{v\}}\) be the group of vectors \(\bigl(\tfrac{M}{\lambda_v(a)}\operatorname{Im}\Phi_v(s)\bigr)_v\), \(s\in\mathcal O_E\), \(\bar s=-s\) ([[?lean:New.Filling.imSkewLattice|lattice of imaginary parts of skew integers]]). Then:

- if \(\gamma\in\mathsf U_c(M)\) is such that at some place \(v\) right multiplication by \(\gamma_v\) adds its \((e_a,e_a^{*})\) entry to that of every \(x\in\mathsf U\), then the vector of imaginary parts of the \((e_a,e_a^{*})\) entries of the image of \(\gamma\) lies in \(L'_a\);
- every \(l\in L'_a\) is the vector of imaginary parts at \((e_a,e_a^{*})\) of the image of some \(\gamma\in\mathsf U_c(M)\) whose free entries all vanish and whose imaginary coordinates in the rows \(d\ne a\) vanish;
- \(L'_a\) has a measurable strict fundamental domain of volume \(\prod_v\lvert M/\lambda_v(a)\rvert\cdot\lvert\operatorname{disc}E\rvert^{1/4}\) ([[?lean:New.Filling.exists_fundamental_domain_im_skew|covolume of the skew lattice]]).

## Proof

**(i)** \(B_c\) is the product of the image of the class representative, which acts on \(X_0\) only, and the lattice basis, which changes one basis vector of \(X_0\oplus Ez\); so it has the stated block form, with middle determinant \(\det(h)\cdot\bar\pi^{-1}\) up to a unit, \(h\) the unitary representative. From \(h^{*}h=1\) the index of \(\det h\) has square \(1\), hence is \(1\); from \(\pi\bar\pi=N\) the index of \(\pi\) has square the index \(N^{2f}\) of \(N\), hence is \(N^{f}\). This gives index \(N^{-f}\) for the determinant.

**Integrality of rows.** For \(\gamma\in\mathsf U_c(M)\), \(h_c^{-1}\gamma h_c\in K(M)\) means that \(M^{-1}(\gamma'-1)\) is integral in the lattice basis ([[?lean:New.Filling.principalLevel_eq_unitaryLevel|description of the principal level]]); conjugating back, \(M^{-1}(\gamma-1)\cdot B_c=B_c\cdot M^{-1}(\gamma'-1)\), and since the row \(e_a\) of \(B_c\) is that of the identity, the row \(e_a\) of \(M^{-1}(\gamma-1)\) times \(B_c\) is integral.

**(ii)** By (i), for a row vector \(l\) the entries of \(l\cdot B_c\) at the columns of \(\mathcal F_a\) depend only on the entries of \(l\) at \(\mathcal F_a\), through the square block \(B_c^{(a)}\) of \(B_c\) on \(\mathcal F_a\), and \(\det B_c^{(a)}=\det B_c\). *Membership:* with \(x_j=M^{-1}\gamma_{e_a,j}\), the real image has entry \(\Phi_v(\gamma_{e_a,j})\sigma_v(j)/\sigma_v(e_a)\) at \((e_a,j)\), and \(x\) satisfies the integrality condition by the previous paragraph. *Attainment:* given \(x\), extend it by \(0\); the row vector \(x\cdot B_c\) is integral (at the non-free columns it vanishes by the block form), and \(x\) vanishes at the non-free positions, so the lemma on [[proofs/grh/spanning-unfolding-a/eichler-element-with-prescribed-row|a prescribed row]] (with \(s=0\)) gives \(\gamma\in\mathsf U_c(M)\) with row \(Mx\) at \(e_a\) and identity rows at the other \(e_d\), outside the column \(e_a^{*}\). The free columns of the row \(e_a\) are not \(e_a^{*}\), so the free entries of the row \(e_a\) are \(l\); for \(d>a\) the free columns of the row \(e_d\) are not \(e_a^{*}\) either, and \(e_d^{*}\ne e_a^{*}\), so all coordinates in the rows \(d>a\) vanish. *Volume:* by the general [[?lean:New.exists_fundamental_domain_classLattice|covolume of a class lattice]], the lattice of vectors \((t_{j,v}\Phi_v(x_j))\) with \(m\,x\) integral has a fundamental domain of volume \(\prod_v\lvert\prod_jt_{j,v}\rvert^2/\operatorname{index}(\det m)/\operatorname{vol}(\widehat{\mathcal O})^{n}\). Here \(t_{j,v}=M\sigma_v(j)/\sigma_v(e_a)\); the scales of \(e_b\) and \(e_b^{*}\) are inverse, those of \(X_0\) are \(1\) and that of \(z\) is \(N^{-1/2}\), so \(\lvert\prod_jt_{j,v}\rvert^2=(M^2/\lambda_v(a))^{n_a}/N\). The factor \(N^{-f}\) from the places cancels against the index \(N^{-f}\) of (i).

**(iii)** *Membership:* \(s=M^{-1}\gamma_{e_a,e_a^{*}}\) is an [[?c:Algebraic integer|algebraic integer]] by the integrality of rows and (i) (the column \(e_a^{*}\) of \(B_c\) is that of the identity). Applying the additivity hypothesis to \(x=\gamma_v^{-1}=J\gamma_v^{*}J\) gives \(0=(\gamma_v)_{e_a,e_a^{*}}+\overline{(\gamma_v)_{e_a,e_a^{*}}}\); as \((\gamma_v)_{e_a,e_a^{*}}=\Phi_v(Ms)/\lambda_v(a)\) with \(\lambda_v(a)\) real and \(\Phi_v\) injective and compatible with conjugation, \(\bar s=-s\). The imaginary part at each place \(w\) is \(\tfrac{M}{\lambda_w(a)}\operatorname{Im}\Phi_w(s)\). *Attainment:* apply the lemma on a prescribed row with \(l=0\) and the skew integer \(s\): the rows \(e_d\) of \(\gamma-1\) vanish except for the entry \(Ms\) at \((e_a,e_a^{*})\).

## References

1. Lean: `New.Filling.freeLattice` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
2. Lean: `New.Filling.freeBlock` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
3. Lean: `New.Filling.exists_classBasis_eq_fromBlocks` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
4. Lean: `New.Filling.classUnipotent_sub_one_div_M_row_integral` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
5. Lean: `New.Filling.rowCoords_fst_mem_freeLattice` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
6. Lean: `New.Filling.exists_rowCoords_fst_eq` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
7. Lean: `New.Filling.rowCoords_snd_mem_imSkewLattice` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
8. Lean: `New.Filling.exists_rowCoords_snd_eq` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
9. Lean: `New.Filling.star_inv_mul_apply_eStar_eq_neg` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
10. Lean: `New.Filling.isIntegral_inv_mul_apply_eStar` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
11. Lean: `New.Filling.exists_fundamental_domain_freeLattice` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
12. Lean: `New.Filling.prod_norm_basisScale_sq_div_eq` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
