+++
id = "proofs/grh/upper-objects/definite-kernel-scale"
title = "Rational equivariance, integrality and size of definite theta kernels"
kind = "theorem"
summary = "Theta kernels of a pair of standard definite spaces with a datum given by a function modulo an ideal and a homogeneous polynomial: rational points act by a two-sided substitution in the polynomial; one normalising constant makes all such kernels p-integral for p-integral input and bounds all their Galois conjugates."
aliases = ["mod kernel scale", "integrality of definite theta kernels"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Rows.modKernelStdSpace_embFin_mul", "New.Rows.IsModKernelScale", "New.Rows.exists_ne_zero_isModKernelScale", "New.Rows.modKernelScale", "New.Rows.jet_jetSeries_pairWeil_vacuumDatum", "New.Rows.blockSumOne_mem_integralAbove", "New.Rows.stdEmbFin_blockSumOne", "New.Rows.blockSumOne_mul_mem_integralAbove", "New.Rows.modKernelScale_ne_zero", "New.Rows.norm_modKernelScale_mul_modKernelStdSpace_le_one", "New.Rows.norm_modKernelScale_mul_modKernelStdSpace_le", "New.Rows.norm_map_eval_le_of_isHomogeneous", "New.Rows.norm_map_sq_div_bigOmega_mul_le", "New.Rows.hasConjugateGrowth_of_isHomogeneous", "New.Rows.M_pow_mul_card_mul_exp_le"]
lean_files = ["src/New/UpperBound/Kernels/DefiniteKernelSize.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]] with field \(E\), \(L\) and \(N\) finite index sets (here \(N\) is an index set, not the level), \(I_L,I_N\) the standard definite spaces, \(a,b\) characters of \(U(1)(\mathbb A)\) with exponents \(e,e'\) at the infinite places and tame parts, \(\mathfrak m\) a modulus, \(\Psi\) a function on \(N\times L\) matrices modulo \(\mathfrak m\), and \(Q\) a complex polynomial in the entries of matrices \(x_\tau\) (\(\tau\) an infinite place, \(N\times L\)). The [[?lean:New.modKernelStdSpace|theta kernel]] \(\Theta_{\Psi,Q}(g,h)\), for finite adelic points \(g\in U(I_L)\), \(h\in U(I_N)\), is the theta functional of the datum (Fock vector of \(Q\)) \(\otimes\) (\(\Psi\) at \(\mathfrak m\), vacuum elsewhere), moved by \((g,h)\) under the Weil representation twisted by \(a,b\).

**Theorem.**

1. *(Rational equivariance.)* For rational points \(\gamma\in U(I_L)(E^+)\), \(\gamma'\in U(I_N)(E^+)\):
\[
\Theta_{\Psi,Q}(\gamma g,\gamma'h)=\prod_\tau\tau(\det\gamma')^{-e_\tau}\,\tau(\det\gamma)^{e'_\tau}\cdot\Theta_{\Psi,Q^{\gamma,\gamma'}}(g,h),
\]
where \(Q^{\gamma,\gamma'}\) is \(Q\) after the [[?lean:New.Rows.twoSidedSubst|substitution]] \(x_\tau\mapsto\tau(\gamma'^{-1})^{\mathsf T}x_\tau\,\tau(\gamma)^{\mathsf T}\).
2. *(Jets.)* If \(Q\) is homogeneous of degree \(d\), then \(\operatorname{jet}_Q\) of the Taylor series at scale \(t\) of \(\omega_{a,b}(g,h)\big(s\cdot(\Psi\otimes\mathrm{vac})\big)\) equals \(s\,t^d\,\Theta_{\Psi,Q}(g,h)\).
3. *(Normalising constant.)* For every \(d\ge0\) the constant
\[
c=c(L,N,D,d)=(M^2)^{2f\lvert N\rvert\lvert L\rvert}\cdot\varsigma^{\lvert N\rvert\lvert L\rvert}\cdot(M^2\,d_K\,c_0)^{d}\ne0
\]
(\(\varsigma\) the vacuum scale, \(c_0\) the jet scale, \(d_K\) the prime of the parameters with \(K=\mathbb Q(\sqrt{-d_K})\), \(f\) the number of infinite places of \(E\)) is such that for all \(a,b,\mathfrak m,\Psi\) and all \(Q\) homogeneous of degree \(d\):
   * (integrality) if \(qM^2\in\mathfrak m\), the values of \(\Psi\) are integral away from \(q\), \(p\) is a prime not dividing \(q\), \(g,h\) are integral above \(p\) and the coefficients of \(Q\) are \(p\)-integral, then \(\lvert\iota_p(c\,\Theta_{\Psi,Q}(g,h))\rvert\le1\);
   * (size) if \(\lvert L\rvert,\lvert N\rvert\le\Delta\), \(d\le M\), \(M^2\in\mathfrak m\), a natural number \(A\) bounds all conjugates of the values of \(\Psi\), \(\sigma\) is an automorphism of \(\mathbb C\) and \(\lvert\sigma(Q(z))\rvert\le B\) whenever \(\lvert\sigma(z_i)\rvert\le M^4\) for all \(i\), then \(\lvert\sigma(c\,\Theta_{\Psi,Q}(g,h))\rvert\le e^{x_1}AB\) for all \(g,h\).

   Here \(M=p_0p_1\), \(\Delta=2r^8\) is the gap and \(x_1\) the second scale of the data.

## Proof

*1.* The theta functional is invariant under rational points, so translating \((g,h)\) on the left by the finite parts of \(\gamma,\gamma'\) is the same as acting by the archimedean parts of \(\gamma^{-1},\gamma'^{-1}\). The spaces are definite, so these lie in the maximal compact subgroups and act on the Fock vector of \(Q\) by a substitution and a scalar: by the formula for the real Weil representation on Fock vectors (Lean: `realPairWeil_polyVector`, cited), with all signs \(+1\) the scalar is \(\prod_\tau\tau(\det\gamma')^{-e_\tau}\tau(\det\gamma)^{e'_\tau}\) and the substitution is the stated one. The archimedean and finite actions on a datum (Fock vector) \(\otimes\) (finite datum) are independent (Lean: `pairWeil_integrated_all`, cited).

*2.* The kernel is \(\theta\) of the integrated operator of the Fock vector of \(Q\) applied to the translated finite datum, finite points commuting with this operator; and for \(Q\) homogeneous of degree \(d\) the jet at scale \(t\) is \(t^d\) times that value (Lean: `jet_jetSeries_of_isHomogeneous`, cited).

*3, integrality.* Let \(\delta=M^2\) and \(f_0=\delta^{2f\lvert N\rvert\lvert L\rvert}\varsigma^{\lvert N\rvert\lvert L\rvert}(\Psi\otimes\mathrm{vac})\). By [[proofs/grh/upper-objects/vacuum-data-of-functions-modulo-an-ideal|the lemma on vacuum data]] (with \(N_0=\delta\), using \(q\delta\in\mathfrak m\)), \(f_0\) is a standard datum for \(\delta\) at \(p\); so is \(\omega_{a,b}(g,h)f_0\) by part 1 of the [[proofs/grh/upper-objects/gauge-bounds-for-one-lift|gauge bounds]]. By 2, \(c\,\Theta_{\Psi,Q}(g,h)=\operatorname{jet}_Q\big(\operatorname{Jet}_{\bar\delta d_Kc_0}(\omega(g,h)f_0)\big)\). The Lean lemma `New.Parameters.norm_jet_jetSeries_le_one` (area on derivatives of theta functions; cited) states that for a standard datum for \(\delta\ne0\) the jets at scale \(\bar\delta\,d_K\,c_0\) along polynomials with \(p\)-integral coefficients are \(p\)-integral.

*3, size.* By 2, \(c\,\Theta_{\Psi,Q}(g,h)=(M^2)^{2f\lvert N\rvert\lvert L\rvert}\cdot J\) with \(J=\operatorname{jet}_Q\operatorname{Jet}_{M^2d_Kc_0}(\omega(g,h)f_1)\), \(f_1=\varsigma^{\lvert N\rvert\lvert L\rvert}(\Psi\otimes\mathrm{vac})\). By the lemma on vacuum data, \(f_1\) is a vacuum combination of size \(\#\{\text{matrices mod }\mathfrak m\}\cdot A\). The polynomial \(Q\) has conjugate growth \((T,d,0,B)\) with \(T=\lvert\sigma(M^2d_K)\rvert^2/\Omega\): if \(\sum\lvert\sigma z_i\rvert^2\le T(2d+2)R\) then each \(\lvert\sigma z_i\rvert\le e^RM^4\), because \(T(2d+2)\le(M^4)^2\) (sizes of the data, \(d\le M\)) and \(R\le e^{2R}\); and by homogeneity a bound \(B\) on the polydisc of radius \(M^4\) gives \(Be^{dR}\) on the polydisc of radius \(e^RM^4\) (scale \(z\) by \(\sigma^{-1}(e^{-R})\)). The [[proofs/grh/upper-objects/archimedean-bounds-for-jets|archimedean bound for jets]] gives \(\lvert\sigma J\rvert\le\#\{\text{matrices}\}\cdot A\cdot e^{C_P(q_1\lvert N\times L\rvert+1)^2}(2d+2)^{f\lvert N\rvert\lvert L\rvert}\cdot B\). Finally \(\#\{\text{matrices mod }\mathfrak m\}\le(M^2)^{2f\lvert N\rvert\lvert L\rvert}\) since \(M^2\in\mathfrak m\), and
\((M^2)^{4f\lvert N\rvert\lvert L\rvert}e^{C_P(\cdot)^2}(2d+2)^{f\lvert N\rvert\lvert L\rvert}\le e^{x_1}\) for \(\lvert L\rvert,\lvert N\rvert\le\Delta\), \(d\le M\), by the size relations of the data (in Lean: the automatic comparison of logarithmic bounds). \(\square\)

## References

1. Lean: `New.Rows.modKernelStdSpace_embFin_mul`, `New.Rows.IsModKernelScale`, `New.Rows.exists_ne_zero_isModKernelScale` in `src/New/UpperBound/Kernels/DefiniteKernelSize.lean`.
