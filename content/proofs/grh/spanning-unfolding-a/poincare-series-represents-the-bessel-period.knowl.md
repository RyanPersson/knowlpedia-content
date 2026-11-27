+++
id = "proofs/grh/spanning-unfolding-a/poincare-series-represents-the-bessel-period"
title = "The Poincaré series represents the Bessel period"
kind = "theorem"
summary = "For a fitting space and admissible filling data there are g_0 and t such that the pairing of a form y of the conjugate type with the Poincaré series of a source form psi is the Bessel period of the source function against y(. g_0)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.exists_integral_poincareSeries_eq_period", "New.Filling.Fits.sourceFormCoords_apply"]
lean_files = ["src/New/Spanning/Unfolding/SeriesPeriod.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity (with fixed Weil data), \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], and \(V\) with grading \(Y\) a space [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fitting]] \(S\) with \(\jmath\,c_Y=-(M\varpi)^{-1}\). There are a real point \(g_0\in G_\infty\) and a linear form \(t\) on the [[?c:Weyl module|Weyl module]] such that for every [[?c:Algebraic modular form|algebraic form]] \(\psi\) on \(H=U(X_0)\) of weight \((kw,0)\) fixed by the source level, and every [[?lean:New.Space.IsForm|form]] \(y\) on \(V\) of type \(\overline{e_l}\) (the complex conjugate of the type kernel) that is right invariant under the principal level \(J_M\),
\[
\int_{\Gamma\backslash G}y(g)\,\mathcal P_{\operatorname{coord}(\psi)}(g)\,d\dot g=\int_{[R]}\mathcal W_{t,\eta\psi}(r)\;y\bigl(r\,(g_0,1)\bigr)\,dr,
\]
where \(\operatorname{coord}(\psi)\in\mathbb C^{\{(c,i)\}}\) are the [[proofs/grh/spanning-unfolding-a/source-forms-in-bessel-coordinates|source form coordinates]] of \(\psi\) (the coordinates \(A(\psi(c_{\mathrm{out}}))_i\) of its values at the class representatives), \(\mathcal P\) is the [[proofs/grh/spanning-unfolding-a/poincare-series-of-bessel-functions|Poincaré series]], \([R]=R(F)\backslash R(\mathbb A)\) and \(\mathcal W_{t,\eta\psi}\) is the [[?lean:New.Grading.sourceFn|source function]] of the translate of \(\psi\) by \(\eta\).

## Proof

Let \(g_0,t_0\) be given by the theorem on the [[proofs/grh/spanning-unfolding-a/bessel-function-paired-with-a-form-value|Bessel function paired with a form value]], \(\operatorname{vol}_{J'}\) by the theorem on the [[proofs/grh/spanning-unfolding-a/bessel-quotient-as-union-of-class-quotients|decomposition of \([R]\)]], and \(\operatorname{vol}_J\) the [[harmonic-analysis/haar-measure|Haar measure]] of \(J_M\). We prove the formula with \(t=(\operatorname{vol}_J/\operatorname{vol}_{J'})\,t_0\); write \(\mathcal W=\mathcal W_{t_0,\eta\psi}\).

*Properties of \(\mathcal W\).* It is continuous and left \(R(F)\)-invariant ([[?lean:New.Grading.isEquivariant_sourceFn|equivariance of the source function]]), right \(J'\)-invariant (item 4 of the decomposition theorem), hence integrable on the compact quotient \([R]\) ([[?lean:New.Grading.isCocompact_ratBessel|compactness of \([R]\)]]); by item 3 of that theorem each \(s\mapsto\beta_c(\theta(s))\mathcal W(s,x_c)\) is integrable. Moreover \(\mathcal W(u_\infty s,x_c)=\mathcal W(s,x_c)\) for \(u\in\mathsf U_c(M)\), by property 3 of [[proofs/grh/spanning-unfolding-a/class-sections-and-class-weights|class sections]] and the two invariances.

*Step 1 (folding).* By the theorem on [[proofs/grh/spanning-unfolding-a/folding-of-poincare-series|folding]], with \(\varphi=\operatorname{coord}(\psi)\), and since \(\sum_i\varphi_{(c,i)}W_i=\langle A(\psi(c_{\mathrm{out}})),W\rangle\):
\[
\int_{\Gamma\backslash G}y\,\mathcal P_\varphi=\operatorname{vol}_J\sum_c\int_{G_\infty}\beta_c(\theta(x))\,\bigl\langle A(\psi(c_{\mathrm{out}})),W(\theta(x))\bigr\rangle\,y(x,x_c)\,dx .
\]
*Step 2 (integral formula).* Replace the pairing by \(\int_{R(F_\infty)}\overline{e_l(g_0^{-1}s^{-1}x)}\,\mathcal W(s,x_c)\,ds\).

*Step 3 (moving the quotient).* Apply the lemma on [[proofs/grh/spanning-unfolding-a/moving-the-quotient-to-the-bessel-group|moving the quotient]] with \(e=\overline{e_l}\) (continuous and integrable, as \(e_l\) is an [[?c:Idempotent element|idempotent]] kernel) and \(W(s)=\mathcal W(s,x_c)\):
\[
=\operatorname{vol}_J\sum_c\int_{R(F_\infty)}\beta_c(\theta(s))\,\mathcal W(s,x_c)\,y(sg_0,x_c)\,ds .
\]
*Step 4 (the period).* The function \(F(r)=\mathcal W(r)\,y(r(g_0,1))\) on \(R(\mathbb A)\) is left \(R(F)\)-invariant, right \(J'\)-invariant (\((g_0,1)\) commutes with finite points) and integrable on \([R]\) ([[?lean:New.Grading.IsEquivariant.integrable_mul|integrability of an equivariant function times an automorphic function]]); and \(F(s,x_c)=\mathcal W(s,x_c)y(sg_0,x_c)\). By item 3 of the decomposition theorem the last sum is \(\operatorname{vol}_{J'}^{-1}\int_{[R]}F\). So the left side equals \((\operatorname{vol}_J/\operatorname{vol}_{J'})\int_{[R]}\mathcal W_{t_0,\eta\psi}(r)y(r(g_0,1))\,dr\), and the source function is linear in \(t\).

## References

1. Lean: `New.Filling.Fits.exists_integral_poincareSeries_eq_period` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
2. Lean: `New.Filling.Fits.sourceFormCoords_apply` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
