+++
id = "proofs/grh/upper-divisibility/colength-of-the-up-integral-forms"
title = "The prime N: colength of the up-integral forms"
kind = "theorem"
summary = "Every finite family of N-integral source forms is carried into the module A' by a matrix whose determinant divides N^e with e at most m f b times the dimension of the source forms."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_colengthDvd_upIntegralForms_pow", "New.Data.colengthDvd_comap_upOperator_pow", "New.Data.colengthDvd_integralFormsAt_diagPointN", "New.Data.upOperator_mem_integralFormsAt", "New.Data.integralFormsAt_one_le", "New.Data.exists_mul_dualPointN_mem_integralAbove"]
lean_files = ["src/New/UpperBound/Divisibility/ColengthAtLevel.lean"]
proof_status = "outline"
+++

Notation of the [[proofs/grh/upper-divisibility/setup-at-the-level-prime|set-up at \(N\)]]. Let \(\mathcal A_\iota\), \(\mathcal A^{L}\), \(\mathcal A^{\vee}\) be the \(O_\iota\)-modules of source forms that are integral at the base points \(1\), \(\delta_0\), \(\delta_0^{\vee}\) (values integral for the standard lattice, for \(L_0\), for \(L_0^{\vee}\) at \(\Sigma_N\)). For submodules \(M,M'\) and \(z\in O_\iota\), "the [[?lean:New.ColengthDvd|colength]] of \(M'\) in \(M\) divides \(z\)" means: every finite family \(\varphi_1,\dots,\varphi_n\in M\) is carried into \(M'\) by an \(n\times n\) matrix over \(O_\iota\) whose determinant divides \(z\).

**Theorem.** There is a natural number \(e\le m\,f\,b\,\dim_{\mathbb{C}}\mathcal S\) such that the colength of \(\mathcal A'\) in \(\mathcal A_\iota\) divides \(N^{e}\).

More precisely, with \(l\) the [[proofs/grh/upper-divisibility/mean-degree-in-one-variable|summed degree]] in the last variable of \(X_0\):

1. \(\mathcal A_\iota\subset\mathcal A^{\vee}\).
2. The colength of \(\mathcal A^{L}\) in \(\mathcal A^{\vee}\) divides \(N^{l}\).
3. \(U\mathcal A^{L}\subset\mathcal A^{\vee}\).
4. For every \(i\ge0\), the colength in \(\mathcal A_\iota\) of \(\{\varphi:U^{i}\varphi\in\mathcal A^{L}\}\) divides \(N^{l(i+1)}\).

## Proof

(1) \((\delta_0^{\vee})^{-1}=\delta_0(\Sigma_N\setminus\{w\mid\pi_N\})\) acts at each \(\tau\) by a diagonal matrix with entries \(1\) or \(N\), hence integral; the weight of \(X_0\) is polynomial (no determinant twist), and a Schur matrix of an integral matrix does not increase norms ([[?lean:New.Rows.norm_schur_mulVec_le|`norm_schur_mulVec_le`]], quoted). So the gauge at \(g\delta_0^{\vee}\) is at most the gauge at \(g\).

(2) By weak approximation above \(N\) ([[?lean:New.exists_mul_mem_integralAbove|`exists_mul_mem_integralAbove`]], quoted) choose for each class \(c\) a representative \(r_c\) such that \(r_c\delta_0^{\vee}\) and \(\delta_0(\Sigma_N)^{-1}r_c\delta_0\) are integral above \(N\). For \(\varphi\in\mathcal A^{\vee}\) the coordinates of \(\varphi(r_c)\) are integral. Conversely let \(\varphi\) be a source form with \(\varphi(r_c)_i=N^{\deg_{\mathrm{last}}(i)}y_{c,i}\), \(y_{c,i}\in O_\iota\), where \(\deg_{\mathrm{last}}(i)\) is the degree of the basis vector \(i\) in the last variable summed over the places. For \(g=\eta r_ck\) (\(\eta\) rational, \(k\in K_0\)): the gauge of \(\varphi(g)\) at \(g\delta_0\) equals the gauge of \(\varphi(r_c)\) at \(r_ck\delta_0\); the element \(\delta_0(\Sigma_N)^{-1}r_ck\delta_0\) is integral above \(N\) (as \(\delta_0^{-1}k\delta_0\) is, by the [[proofs/grh/upper-divisibility/level-at-n-as-a-mirabolic-group|mirabolic description]]), so this is the gauge at \(\delta_0(\Sigma_N)\), where the inverse acts at every \(\tau\) by \(\operatorname{diag}(1,\dots,1,N)^{-1}\), dividing the coordinate \(i\) by \(N^{\deg_{\mathrm{last}}(i)}\). The result \((y_{c,i})\) is integral, so \(\varphi\in\mathcal A^{L}\). Thus, in the coordinates \(\varphi\mapsto(\varphi(r_c)_i)\), the diagonal matrix with entries \(N^{\deg_{\mathrm{last}}(i)}\), of determinant \(N^{l}\), carries the lattice of all integral families into the image of \(\mathcal A^{L}\); this gives the colength bound (pulled back along evaluation, [[?lean:New.ColengthDvd.comap|`ColengthDvd.comap`]]).

(3) \((U\varphi)(g)\) is a sum of roots of unity times values \(\varphi(gg'_y)\), where \(g'_y=\delta_0^{\vee}k_y\delta_0^{-1}\) with \(k_y\) integral above \(N\). So the gauge of each term at \(g\delta_0^{\vee}\), which equals the gauge at \(g\delta_0^{\vee}k_y=gg'_y\delta_0\), is at most \(1\) for \(\varphi\in\mathcal A^{L}\); the gauge is ultrametric. \(U\varphi\) is a source form by the [[proofs/grh/upper-divisibility/up-operator-preserves-source-forms|preceding proposition]].

(4) Induction on \(i\). For \(i=0\) combine (1) and (2). If \(U^{i}\varphi\in\mathcal A^{L}\) then \(U^{i+1}\varphi\in\mathcal A^{\vee}\) by (3); pulling (2) back along \(U^{i+1}\) shows that the colength of \(\{U^{i+1}\varphi\in\mathcal A^{L}\}\) in \(\{U^{i}\varphi\in\mathcal A^{L}\}\) divides \(N^{l}\). Colengths multiply along chains.

*Conclusion.* Take \(i=\varrho+1\): \(e=l(\varrho+2)\). By the [[proofs/grh/upper-divisibility/mean-degree-in-one-variable|mean degree]], \(k\,l\le\dim\mathcal S\cdot fa\), and \((\varrho+2)a\le m\,b\,k\) is a size comparison of the data (quoted). Hence \(k\,e\le k\cdot mfb\dim\mathcal S\). \(\blacksquare\)

*Status.* Weak approximation, the Schur-matrix bound, the explicit form of \(U\) as a sum of translates with roots of unity (unfolded in Lean from the definition of `upOperator`) and the final size comparison are quoted.

## References

1. Lean: `New.Data.exists_colengthDvd_upIntegralForms_pow` and the lemmas listed in the front matter, in `src/New/UpperBound/Divisibility/ColengthAtLevel.lean`.
