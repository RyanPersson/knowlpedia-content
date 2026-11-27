+++
id = "proofs/grh/upper-objects/archimedean-bounds-for-jets"
title = "Archimedean bounds for the conjugates of jets of theta kernels"
kind = "theorem"
summary = "For a combination of translates of the integral vacuum with coefficients of total size B, every Galois conjugate of a jet along a polynomial of controlled growth, and of the Schur jet matrix of a lift weight, is bounded by B times an explicit factor."
aliases = ["size of jets", "vacuum combination", "jet size bound", "conjugate growth"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.HasConjugateGrowth", "New.Parameters.IsVacuumCombination", "New.Parameters.jetSizeBound", "New.Parameters.jetSizeBound_eq", "New.Parameters.norm_jet_le_of_isVacuumCombination", "New.Parameters.sqrt_weylNormSq_schurJet_le_of_isVacuumCombination", "New.Parameters.norm_jet_translate_le", "New.Parameters.map_jet_eq_integral", "New.Parameters.jet_jetSeries_mul", "New.Parameters.isVacuumCombination_of_isAdmissibleCombination", "New.Parameters.isVacuumCombination_finHeisenbergOp", "New.Parameters.norm_map_pairChar", "New.schurGrowthExponent", "New.Parameters.hasConjugateGrowth_schurCoeffPoly", "New.sqrt_prod_pow_le_exp", "New.FitsRanks.sum_diagramWeight_eq_boxes", "New.integral_exp_neg_inv_mul_normalizedVolume", "New.norm_integral_normalizedVolume_le", "New.norm_realVac"]
lean_files = ["src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean"]
proof_status = "outline"
+++

Notation of [[proofs/grh/upper-objects/jet-conjugation|jet conjugation]]: \(E=E_s\) (so the statements concern the field \(E_s\) of the parameters for any \(s\)), \(f_E\) its number of infinite places, \(\Omega\), jet scale \(c_0\), \(q_1=q_1(s)\). Let \(n,n'\) be finite index sets and \(V=\operatorname{Hom}(I_n,I_{n'})\) the standard space of \(n'\times n\) matrices, with [[?lean:New.Parameters.intVacuum|integral vacuum]] \(v^{\mathrm{int}}\). For a polynomial \(Q\) in variables indexed by (infinite place, \(n'\), \(n\)) and a power series \(F\), \(\operatorname{jet}_Q(F)=Q(\partial)F(0)\).

**Definitions.**

* \(f\in\mathcal S(V)\) is a **vacuum combination of size \(B\)** if \(f=\sum_xr_x\,\varrho^{\mathrm{fin}}(x)v^{\mathrm{int}}\), a finite sum over finite adelic vectors \(x\) of [[?lean:New.Space.finHeisenbergOp|normalised Heisenberg translates]] of the integral vacuum, with \(\sum_x\lvert\sigma(r_x)\rvert\le B\) for every field automorphism \(\sigma\) of \(\mathbb C\). (An [[?lean:New.Seesaw.IsAdmissibleCombination|admissible combination]] with the size condition switched on is one; a single translate has size \(1\).)
* For \(\sigma\colon\mathbb C\to\mathbb C\), a polynomial \(Q\), \(T\in\mathbb R\), \(L\in\mathbb N\), \(w,A\in\mathbb R\): \(Q\) **has conjugate growth** \((T,L,w,A)\) if \(\lvert\sigma(Q(z))\rvert\le A\exp(w+LR)\) whenever \(\sum_i\lvert\sigma(z_i)\rvert^2\le T(2L+2)R\).
* The **jet size bound** is \(\mathcal B(B,L,w)=B\cdot\exp\big(C_P\,(q_1\lvert n'\times n\rvert+1)^2+w\big)\cdot(2L+2)^{f_E\lvert n'\rvert\lvert n\rvert}\), with \(C_P\) the [[?lean:New.Parameters.constantBound|constant bound]] of the parameters.

**Theorem.** Let \(f\) be a vacuum combination of size \(B\) on \(V\); let \(a,b\) be [[?lean:New.AutChar|automorphic characters of \(U(1)\)]] (continuous characters of the norm-one adeles of \(E\) with values of absolute value \(1\), trivial on the rational norm-one elements) having weights and tame parts, \(g\in U(I_n)(\mathbb A_f)\), \(h\in U(I_{n'})(\mathbb A_f)\), \(\sigma\) any field automorphism of \(\mathbb C\) (not necessarily over \(K\)), \(c\in\mathbb C\), and \(F=\operatorname{Jet}_{c\,c_0}\big(\omega_{a,b}(g,h)f\big)\).

1. If \(A\ge0\), \(\lvert\sigma(c)\rvert^2/\Omega\le T\) and \(Q\) has conjugate growth \((T,L,w,A)\) for \(\sigma\), then \(\lvert\sigma(\operatorname{jet}_Q(F))\rvert\le\mathcal B(B,L,w)\cdot A\).
2. Let \(\kappa\) be a [[?lean:New.IsLiftWeight|lift weight]] from rank \(\lvert n\rvert\) to \(\lvert n'\rvert\) and \(\operatorname{SJ}_\kappa(F)\) the [[?lean:New.schurJet|Schur jet matrix]] (entries \(\operatorname{jet}_Q(F)\) for \(Q\) the polynomial entries of the Schur matrix of \(\kappa\)). For every integer \(L\ge1\) and every vector \(\xi\) of the Weyl module of rank \(n\):
\[
\big\lVert\sigma\big(\operatorname{SJ}_\kappa(F)\,\xi\big)\big\rVert\le\mathcal B\big(B,L,w_L\big)\cdot\lVert\sigma(\xi)\rVert,\qquad w_L=\tfrac12\sum_{l}\Big(\tfrac lL+\log l!+l\log\tfrac{\lvert\sigma(c)\rvert^2}{\Omega}\Big),
\]
where \(\lVert\cdot\rVert\) is the Gram norm of the Weyl modules, \(\sigma\) is applied coordinatewise, and \(l\) runs over the lengths of the first \(\lvert n\rvert\) rows, at all infinite places, of the diagram formed by the columns of \(\kappa\) of height below \(\lvert n'\rvert\).

## Proof

Cited from other areas and not reproved: the identity \(\operatorname{jet}_Q(\operatorname{Jet}_a F)=\theta(\text{integrated operator of }Q(a\,\cdot)\text{ applied to }F)\) and its Gaussian integral form (Lean: `jet_jetSeries_eq_theta`, `theta_integrated`); the bound \(\lVert S_\kappa(Z)\eta\rVert^2\le\prod_{\tau,i}\rho_{\tau,i}^{\,l_{\tau,i}}\lVert\eta\rVert^2\) for the Schur matrix with \(\sum_i\rho_{\tau,i}\le\sum_{j,i}\lvert Z_{\tau,j,i}\rvert^2\) (Lean: `weylNormSq_schur_le`); duality for the Gram norm (`sqrt_weylNormSq_le_of_dual`); and that every automorphism of \(\mathbb C\) has the same absolute values, on the relevant numbers, as some automorphism over \(K\) (`New.Parameters.exists_algEquiv_norm_eq`).

*(a) Conjugate jets as Gaussian integrals.* Let \(\sigma\in\operatorname{Aut}(\mathbb C/K)\) and let \(\operatorname{Jet}_t(F')\) be the jet conjugate of \(\operatorname{Jet}_{c_0}(F)\). Then \(\sigma(\operatorname{jet}_Q\operatorname{Jet}_{c_0}F)=\operatorname{jet}_{Q'}\operatorname{Jet}_t(F')\), where \(Q'\) is \(Q\) with conjugated coefficients and places renamed by \(\pi_\sigma\); and the latter equals
\[
\int Q'(t\bar y)\,\mathrm{vac}_\infty(y)\,F'(\mathrm{rv}(y))\,d\mu(y),\qquad\lvert\mathrm{vac}_\infty(y)\rvert=e^{-\lvert y\rvert^2/2},
\]
over \(y\in\mathbb C^{\Phi\times n'\times n}\), with \(\mu\) Lebesgue measure divided by \(\pi\) in each complex coordinate, and \(\mathrm{rv}(y)\) the adelic vector with zero finite part whose coordinates at the place \(\tau\) are \((2\pi\operatorname{Im}\tau(\jmath))^{-1/2}y_\tau\) (Lean: `realVec`; \(y\) are Fock coordinates). A factor in the scale moves into the operator: \(\operatorname{jet}_Q\operatorname{Jet}_{ca}=\operatorname{jet}_{Q(c\,\cdot)}\operatorname{Jet}_a\).

*(b) One translate.* Let \(F=\varrho(\hat x)\omega(g)v^{\mathrm{int}}\) and take a [[proofs/grh/upper-objects/existence-of-jet-conjugation|jet conjugation]] \(\Lambda\) for \(\sigma\), with scale \(t\), \(\lvert t\rvert^2=1/\Omega\). By (a) applied to \(Q(c\,\cdot)\), \(\sigma(\operatorname{jet}_Q\operatorname{Jet}_{cc_0}F)=\int Q'(t\bar y)\mathrm{vac}_\infty(y)(\Lambda F)(\mathrm{rv}(y))d\mu\) with \(Q'(t\bar y)=\sigma(Q(z))\) for the point \(z\) with \(\sigma(z_i)=\sigma(c)\,t\,\bar y_{\pi_\sigma i}\). Then \(\sum_i\lvert\sigma(z_i)\rvert^2=\frac{\lvert\sigma c\rvert^2}{\Omega}\lvert y\rvert^2\le T(2L+2)R\) with \(R=\lvert y\rvert^2/(2L+2)\), so the growth hypothesis gives \(\lvert Q'(t\bar y)\rvert\le Ae^{w+L\lvert y\rvert^2/(2L+2)}\). With \(\lvert(\Lambda F)(v)\rvert\le e^{M}\) at every adelic vector \(v\), \(M=C_P(q_1\lvert n'\times n\rvert+1)^2\) ([[proofs/grh/upper-objects/bounds-for-the-vacuum-and-its-conjugates|bound for the conjugates of the vacuum]]), the integrand is at most \(Ae^{M+w}e^{-\lvert y\rvert^2/(2L+2)}\), because \(\frac{L}{2L+2}-\frac12=-\frac1{2L+2}\). Since \(\int e^{-\lvert y\rvert^2/a}d\mu=a^{\#\text{variables}}\), we get \(\lvert\sigma(\operatorname{jet}_Q\operatorname{Jet}_{cc_0}F)\rvert\le Ae^{M+w}(2L+2)^{f_E\lvert n'\rvert\lvert n\rvert}\).

*(c) Statement 1.* Replace \(\sigma\) by \(\sigma'\in\operatorname{Aut}(\mathbb C/K)\) with the same absolute values. Write \(f=\sum_xr_x\varrho^{\mathrm{fin}}(x)v^{\mathrm{int}}\). The operator \(\omega_{a,b}(g,h)\) is the character value \(a(\det h)b(\det g)^{-1}\) times \(\omega(k)\) for the finite point \(k\) of \(U(\operatorname{Hom})\) induced by \((g,h)\); \(\omega(k)\varrho^{\mathrm{fin}}(x)=\varrho^{\mathrm{fin}}(kx)\omega(k)\); and \(\varrho^{\mathrm{fin}}(kx)\) is a root of unity times \(\varrho(\widehat{kx})\). The conjugates of the character value have absolute value \(1\): for an automorphic character with a weight, every field automorphism of \(\mathbb C\) maps its values at finite points to numbers of absolute value \(1\) (Lean: `New.AutChar.HasWeight.norm_map_eq_one`, cited; it uses that the base change is an algebraic Hecke character, and it would fail for a character that is not trivial on rational points). The conjugates of the root of unity have absolute value \(1\). So each term is bounded by (b), and \(\sum_x\lvert\sigma(r_x)\rvert\le B\).

*(d) Statement 2.* By duality it suffices to bound \(\lvert\sigma(y\cdot\operatorname{SJ}_\kappa(F)\xi)\rvert\) for covectors \(y\) with \(\lvert\sigma(y\cdot\eta)\rvert\le\lVert\sigma\eta\rVert\) for all \(\eta\); and \(y\cdot\operatorname{SJ}_\kappa(F)\xi=\operatorname{jet}_{Q_{y,\xi}}(F)\) with \(Q_{y,\xi}(z)=y\cdot S_\kappa(z)\xi\). This polynomial has conjugate growth \((e^u,L,w_L(u),\lVert\sigma\xi\rVert)\) for every real \(u\): \(\sigma(Q_{y,\xi}(z))\) is bounded by \(\lVert S_\kappa(\sigma z)\sigma\xi\rVert\le\sqrt{\prod\rho^{l}}\,\lVert\sigma\xi\rVert\) with \(\sum\rho\le\sum\lvert\sigma z_i\rvert^2\le e^u(2L+2)R\), and
\[
\sqrt{\textstyle\prod\rho_{\tau,i}^{\,l_{\tau,i}}}\le\exp\Big(\tfrac12\sum\big(\tfrac lL+\log l!+lu\big)+LR\Big):
\]
indeed \(\rho^l\le l!\,e^{lv+\rho e^{-v}}\) with \(v=u+1/L\), and \(\sum\rho\,e^{-v}\le e^u(2L+2)R/(e^u(1+1/L))=2LR\) since \(e^{1/L}\ge1+1/L\). Apply statement 1 with \(T=e^u\), \(u=\log(\lvert\sigma c\rvert^2/\Omega)\) (if \(\sigma c=0\) the convention \(\log0=0\) of the Lean text still gives \(\lvert\sigma c\rvert^2/\Omega\le e^u\)). \(\square\)

## References

1. Lean: `New.Parameters.norm_jet_le_of_isVacuumCombination`, `New.Parameters.sqrt_weylNormSq_schurJet_le_of_isVacuumCombination`, `New.Parameters.IsJetConjugation.norm_map_intVacuum_le` in `src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean`.
