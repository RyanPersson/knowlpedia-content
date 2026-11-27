+++
id = "proofs/grh/derivatives-vacuum/conjugates-of-jets-of-translates"
title = "Conjugates of the jets of the translates of a generating vector"
kind = "theorem"
summary = "Every standard space has a vector F of the finite part with theta(F) = 1 whose translates span the finite part, and each automorphism sigma of C over K maps the jet series of its translates at the jet scale to jet series of translates of another vector at a scale of squared absolute value 1/Omega, with the places permuted."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.exists_isJetConjugate_translates", "New.Parameters.IsThetaProduct.isJetConjugate_of_map_taylorAtZero_eq", "New.Parameters.map_zetaLinearSeries", "New.Parameters.exists_rational_translate_eq", "New.Parameters.norm_gal_periodFactor_div_mul_areaScale_sq", "New.Parameters.bigOmega_pos", "New.Parameters.jetScale_ne_zero"]
lean_files = ["src/New/Derivatives/Vacuum/IntegralVacuum.lean"]
proof_status = "full"
+++

Let \(P\) be [[?lean:New.Parameters|parameters]], \(s\in\mathbb{N}\), \(E=K(\zeta)\), \(\lambda\) the [[proofs/grh/derivatives-vacuum/jet-scale|jet scale]] and
\[ \Omega=e^{\gamma-\operatorname{Re}\frac{L'}{L}(1,\chi_K)}\cdot\frac{2\pi}{\mathrm{rd}_E}>0 \]
([[?lean:New.Parameters.bigOmega|the constant \(\Omega\)]]; \(\mathrm{rd}_E\) is the [[?c:Root discriminant|root discriminant]] of \(E\)). For an automorphism \(\sigma\) of \(\mathbb{C}\) over \(K\) let \(\pi_\sigma\) be the [[?lean:New.Parameters.placePerm|permutation of the infinite places]] of \(E\) induced by \(\sigma\) (\(\sigma\circ\Phi_w=\Phi_{\pi_\sigma w}\)). For vectors \(f,f'\) of a space \(V\) and scales \(t,t'\), say that the jets of \(f'\) at \(t'\) are the [[?lean:New.Space.IsJetConjugate|\(\sigma\)-conjugates]] of the jets of \(f\) at \(t\) if applying \(\sigma\) to the coefficients of \(J_t(f)\) gives \(J_{t'}(f')\) with each variable \(X_{(w,i)}\) renamed \(X_{(\pi_\sigma^{-1}w,i)}\).

**Theorem.** There is a family \((B_\sigma)\) of finite adeles of \(E\), indexed by \(\sigma\in\operatorname{Aut}(\mathbb{C}/K)\), such that for every [[?lean:New.Space.IsStd|standard]] space \(V\) over \(E\) (any finite index set \(n\)) there is \(F\) in the finite part of \(V\) with

1. \(\theta(F)=1\);
2. the finite part of \(V\) is contained in the span of the translates \(\varrho(x_f)F\), \(x\in\mathbb{A}_{E,f}^{\,n}\);
3. for every \(\sigma\) there are \(t\in\mathbb{C}\) with \(\lvert t\rvert^2=\Omega^{-1}\) and \(F'\) in the finite part of \(V\) such that for every \(x\in\mathbb{A}_{E,f}^{\,n}\) the jets of \(\varrho((B_\sigma x)_f)F'\) at scale \(t\) are the \(\sigma\)-conjugates of the jets of \(\varrho(x_f)F\) at scale \(\lambda\).

Moreover \(\lambda\ne0\).

## Proof

*Complex multiplication.* For each \(\sigma\), [[?lean:New.CMLattice.complex_multiplication_theta|complex multiplication for theta functions]] applied to the [[proofs/grh/derivatives-vacuum/cm-curve-and-period|CM curve]] \(\mathcal{E}\) (lattice \(\Omega_0\mathcal{O}_K\)) gives \(\Omega_\sigma\in\mathbb{C}^\times\), an integer \(e_\sigma\ge1\) and a finite adele \(\beta_\sigma\) of \(K\) with: \(\operatorname{area}(\mathcal{E}^\sigma)=\lvert\Omega_\sigma\rvert^2\sqrt d/2\); \(\Omega_\sigma e_\sigma\in\Lambda_{\mathcal{E}^\sigma}\); and for every \(x\in K\) a neighbourhood \(U_{\sigma,x}\) of \(\beta_\sigma x\) such that for \(x'\in K\cap U_{\sigma,x}\),
\[ \sigma\bigl(T(\tau^{(1)}_{x\Omega_0}\theta_{\mathcal{E}})\bigr)=T\bigl(\tau^{(1)}_{x'\Omega_\sigma}\theta_{\mathcal{E}^\sigma}\bigr). \tag{1}\]
Let \(B_\sigma\) be the image of \(\beta_\sigma\) in the finite adeles of \(E\).

*The vectors.* By [[proofs/grh/derivatives-vacuum/existence-of-theta-products|existence of theta products]] take \(F\) a theta product of level \(1\) for \((\mathcal{E},\Omega_0)\) and \(F'\) one of level \(e_\sigma\) for \((\mathcal{E}^\sigma,\Omega_\sigma)\). Then 1 holds by the definition, and 2 by [[proofs/grh/derivatives-vacuum/vacuum-as-sum-of-translates|the vacuum as a sum of translates]] (parts 2 and 3).

*The scale.* Put \(t=\sigma(\varpi)\,c_A/\Omega_\sigma\) with \(\varpi=s_0/u\) the period factor. Then
\[ \lvert t\rvert^2=\frac{\lvert\sigma s_0\rvert^2\,c_A^2}{\lvert\sigma u\rvert^2\lvert\Omega_\sigma\rvert^2}=\frac{\lvert\sigma s_0\rvert^2\,\pi}{\operatorname{area}(\mathcal{E}^\sigma)\lvert\sigma u\rvert^2}=\frac{(\mathrm{rd}_E/\sqrt d)\,\pi}{\pi e^{c}\,2\pi/\sqrt d}=\Omega^{-1}, \]
using \(c_A^2=2\pi/\sqrt d\), the area of \(\mathcal{E}^\sigma\), [[?lean:New.Parameters.norm_gal_vacuumRoot|\(\lvert\sigma s_0\rvert^2=\mathrm{rd}_E/\sqrt d\)]] and property 2 of the [[proofs/grh/derivatives-vacuum/chowla-selberg-unit|Chowla–Selberg unit]]. The same two facts with \(\sigma=1\) show \(s_0\ne0\) and \(u\ne0\), so \(\lambda\ne0\).

*Reduction to rational \(x\).* For \(f\) in the finite part the map \(x\mapsto\varrho(x_f)f\) on finite adelic vectors is locally constant ([[?lean:New.Space.isLocallyConstant_rho_finVec|local constancy of finite translates]]: \(f\) is fixed by an open subgroup of finite translations, and \(\varrho((x+h)_f)\) differs from \(\varrho(x_f)\varrho(h_f)\) by a value of the additive character depending on \(h\) and \(x\), which for fixed \(x\) is \(1\) for \(h\) near \(0\)). So \(x\mapsto(\varrho(x_f)F,\varrho((B_\sigma x)_f)F')\) is locally constant; the finite images \(\alpha^{-1}\gamma\) of \(\gamma\in E^n\) are dense. So it suffices to prove 3 for \(x=\alpha^{-1}\gamma\). The map \(\beta'\mapsto\varrho((\beta'\alpha^{-1}\gamma)_f)F'\) on the finite adeles of \(K\) is also locally constant and \(K\) is dense there, so there is \(x_0\in K\), arbitrarily close to \(\beta_\sigma\), with \(\varrho((B_\sigma\alpha^{-1}\gamma)_f)F'=\varrho((\alpha^{-1}x_0\gamma)_f)F'\) and \(x_0\,\kappa_k(\gamma_i)\in U_{\sigma,\kappa_k(\gamma_i)}\) for all \(k<q_1\), \(i\in n\) (finitely many open conditions). Thus we must compare the translate of \(F\) by \(\gamma\) with the translate of \(F'\) by \(\gamma'=x_0\gamma\).

*Comparison of factors.* By condition 3 of theta products,
\[ J_\lambda(\varrho(\gamma_f)F)=\prod_{k,j}T(\vartheta_{k,\gamma_j})\bigl(\ell^{\Omega_0,\lambda}_{k,j}\bigr)^{q_1},\qquad J_t(\varrho(\gamma'_f)F')=\prod_{k,j}T(\vartheta'_{k,\gamma'_j})\bigl(\ell^{\Omega_\sigma,t}_{k,j}\bigr)^{q_1}. \]
Applying \(\sigma\) to coefficients commutes with products and substitution. Since \(\kappa_k\) is \(K\)-linear, \(\kappa_k(\gamma'_j)=x_0\kappa_k(\gamma_j)\), so by (1) \(\sigma\,T(\vartheta_{k,\gamma_j})=T(\vartheta'_{k,\gamma'_j})\). For the linear forms: \(\Omega_0\lambda/(q_1c_A)=\varpi/q_1\) and \(\Omega_\sigma t/(q_1c_A)=\sigma(\varpi)/q_1\), so
\[ \sigma\bigl(\ell^{\Omega_0,\lambda}_{k,j}\bigr)=\frac{\sigma(\varpi)}{q_1}\sum_w\overline{\Phi_{\pi_\sigma w}(\zeta^k)}X_{(w,j)}, \]
which is \(\ell^{\Omega_\sigma,t}_{k,j}\) with \(X_{(w,j)}\) renamed \(X_{(\pi_\sigma^{-1}w,j)}\) (here \(\sigma\) commutes with complex conjugation on the values \(\Phi_w(\zeta^k)\), which are roots of unity). Multiplying the factors gives the claim.

## References

1. Lean: `New.Parameters.exists_isJetConjugate_translates`, `New.Parameters.IsThetaProduct.isJetConjugate_of_map_taylorAtZero_eq`, `New.Parameters.map_zetaLinearSeries`, `New.Parameters.exists_rational_translate_eq`, `New.Parameters.norm_gal_periodFactor_div_mul_areaScale_sq`, `New.Parameters.bigOmega_pos`, `New.Parameters.jetScale_ne_zero` in `src/New/Derivatives/Vacuum/IntegralVacuum.lean`.
2. The Lean statement of complex multiplication used here cites G. Shimura, Introduction to the arithmetic theory of automorphic functions, 1971, Theorem 5.4 (a case of it, without the reciprocity law).
