+++
id = "proofs/grh/spanning-unfolding-a/poincare-map-of-admissible-data"
title = "The Poincaré map of admissible data is a Poincaré series of the Bessel function"
kind = "theorem"
summary = "For admissible data there are a real point g and a linear form t for which the form representing the Bessel period of every source form is the Poincaré series of the Bessel function with the source form coordinates as coefficients; this choice defines the Poincaré map."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.poincare_eq_poincareMap_comp", "New.Data.exists_poincareAt_eq_poincareMap_comp", "New.Data.poincare", "New.Data.besselPoint", "New.Data.besselForm"]
lean_files = ["src/New/Spanning/Unfolding/SeriesPeriod.lean"]
proof_status = "full"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]], with spaces \(X_0\), \(Y_0\), [[?lean:New.Data.filling|filling data]] \(S_D\), and for a real point \(g\) of the unitary group of \(Y_0\) and a linear form \(t\) on the [[?c:Weyl module|Weyl module]] of the values of source forms, let \(\mathcal P_{g,t}\) be the [[?lean:New.Data.poincareAt|Poincaré map at \((g,t)\)]]: the linear map from [[?lean:New.Data.SourceForm|source forms]] to [[?lean:New.Data.principalForms|principal forms]] on \(Y_0\) such that for every principal form \(y\)
\[
\langle y,\mathcal P_{g,t}\varphi\rangle=\int_{[R_0]}\mathcal W_{t,\varphi}(r)\,\overline{y(r\,(g,1))}\,dr
\]
(the Bessel period of \(\varphi\); [[?lean:New.Data.inner_poincareAt|defining property]]). Then there are \(g\) and \(t\) such that
\[
\mathcal P_{g,t}=\mathcal P\circ\operatorname{coord}_D ,
\]
where \(\operatorname{coord}_D\) are the [[proofs/grh/spanning-unfolding-a/source-form-coordinates-of-the-data|source form coordinates of the data]] and \(\mathcal P\) is the [[proofs/grh/spanning-unfolding-a/poincare-series-are-forms|Poincaré map of the fitting space]] \(Y_0\): for every source form \(\varphi\), \(\mathcal P_{g,t}\varphi\) is the Poincaré series of the Bessel function with coefficients the values, at the class representatives, of the central translate of \(\varphi\) by the lattice scale.

**Definition.** Fix such a pair: the **Bessel point** \(g_B\) and the **Bessel form** \(t_B\) of \(D\) (chosen by the axiom of choice among the pairs of the theorem). The **Poincaré map** of \(D\) is \(\mathcal P_D=\mathcal P_{g_B,t_B}\) from source forms to principal forms on \(Y_0\). By construction \(\mathcal P_D=\mathcal P\circ\operatorname{coord}_D\).

## Proof

The spaces fit ([[proofs/grh/spanning-unfolding-a/filling-data-fit-the-space-y0|fit to \(Y_0\)]]) and \(S_D\) satisfies the standing hypotheses ([[proofs/grh/spanning-unfolding-a/filling-data-of-admissible-data-are-admissible|admissibility]]). The constant of the generic character of the grading of \(Y_0\) satisfies \(\jmath\,c_Y=-(M\varpi)^{-1}\) by its definition (direct from the definitions of the grading and of the filling data, using \(\jmath\ne0\)). Let \(g,t\) be given by the theorem that the [[proofs/grh/spanning-unfolding-a/poincare-series-represents-the-bessel-period|Poincaré series represents the Bessel period]].

Two principal forms are equal if they have the same [[?c:Petersson inner product|Petersson product]] with every principal form \(y\). Fix a source form \(\varphi\) and let \(\psi\) be its central translate by the lattice scale \(u\), so that \(\eta\psi=\varphi\) (\(\eta=u^{-1}\)) and \(\operatorname{coord}_D(\varphi)\) are the fitting-space coordinates of \(\psi\). The conjugate \(\bar y\) of a principal form \(y\) is a form of type \(\overline{e_l}\) and of level \(J_M\). Hence
\[
\langle y,\mathcal P_{g,t}\varphi\rangle=\int_{[R_0]}\mathcal W_{t,\eta\psi}(r)\,\bar y(r(g,1))\,dr=\int_{\Gamma\backslash G}\bar y\cdot\mathcal P_{\operatorname{coord}_D(\varphi)}=\langle y,\mathcal P(\operatorname{coord}_D\varphi)\rangle,
\]
the last step because the Poincaré map of the fitting space is, as a function, the Poincaré series.

## References

1. Lean: `New.Data.poincare_eq_poincareMap_comp` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
2. Lean: `New.Data.exists_poincareAt_eq_poincareMap_comp` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
3. Lean: `New.Data.poincare` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
4. Lean: `New.Data.besselPoint` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
5. Lean: `New.Data.besselForm` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
