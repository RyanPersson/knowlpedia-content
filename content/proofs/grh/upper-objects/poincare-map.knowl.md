+++
id = "proofs/grh/upper-objects/poincare-map"
title = "The Poincaré map from source forms to forms on Y_0"
kind = "construction"
summary = "The linear map sending a source form on X_0 to the form of principal level on Y_0 that represents, in the Petersson product, the Bessel period of the source form."
aliases = ["Poincaré map", "Poincaré series", "Bessel period of a source form", "level trace"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.poincareAt", "New.Data.inner_poincareAt", "New.Data.poincareAt_smul", "New.Data.integral_mul_poincareAt", "New.Data.besselPeriod", "New.Data.besselPeriod_apply", "New.Data.isEquivariant_sourceFn", "New.rieszMap", "New.inner_rieszMap", "New.bijective_flip_innerₛₗ", "New.Space.Form.levelTrace", "New.Space.Form.levelTrace_apply", "New.Space.Form.hasLevel_levelTrace", "New.Space.Form.integral_levelTrace_mul", "New.Grading.IsEquivariant.integrable_mul"]
lean_files = ["src/New/UpperBound/Objects/PoincareMap.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]]. Let \(\mathcal A(X_0)\) be the [[proofs/grh/upper-objects/source-form|source forms]] with values in the Weyl module \(\mathcal V_0\) (action \(\rho\) through the conjugate matrices), \(\mathcal A(Y_0)\) the [[proofs/grh/upper-objects/target-form|forms of principal level]] on \(Y_0\) (a finite-dimensional space with the Petersson inner product), \(G_0=U(Y_0)(\mathbb A)\), and \(R_0\) the adelic [[?lean:New.Grading.besselGroup|Bessel subgroup]] of the grading \(Y_0=X_0\oplus\) string: \(R_0=U^{\ge2}\rtimes U(X_0)\), where \(U^{\ge2}\) is the unipotent group of the elements \(u\) such that \(u-1\) raises the grading by at least \(2\), with its [[?lean:New.Grading.besselMeasure|invariant measure]] on \([R_0]=R_0(E^+)\backslash R_0(\mathbb A)\), which is compact. Fix an archimedean point \(g\in G_{0,\infty}\) and a linear form \(t\) on \(\mathcal V_0\).

For a source form \(\varphi\) put \(\mathcal W_\varphi(uh)=\psi_U(u)\,t\big(\rho(h_\infty^{-1})\varphi(h_f)\big)\) for \(u\) unipotent and \(h\in U(X_0)(\mathbb A)\), with \(\psi_U\) the generic character ([[?lean:New.Grading.sourceFn|source function]]).

**Construction.**

* The **Bessel period** is the pairing, linear in \(\varphi\) and conjugate linear in \(y\in\mathcal A(Y_0)\),
\[
B_{g,t}(\varphi,y)=\int_{[R_0]}\mathcal W_\varphi(r)\,\overline{y(r\,g)}\,dr .
\]
* The **Poincaré map** \(\mathcal P=\mathcal P_{g,t}\colon\mathcal A(X_0)\to\mathcal A(Y_0)\) is the unique linear map with
\[
\langle y,\mathcal P\varphi\rangle=B_{g,t}(\varphi,y)\qquad\text{for all }y\in\mathcal A(Y_0),
\]
the inner product being linear in the second variable.

## Properties

1. \(\mathcal P_{g,ct}=c\,\mathcal P_{g,t}\); so a change of the Haar measure on \(R_0(\mathbb A)\) can be absorbed in \(t\).
2. Let \(J\) be a subgroup of the finite adelic points with \([J_M:J\cap J_M]<\infty\), \(J_M\) the [[proofs/grh/upper-objects/chosen-places-and-chosen-group-order|chosen level]], and let \(z\) be a form on \(G_0\), right invariant under \(J\), of the archimedean type conjugate to that of \(\mathcal A(Y_0)\). Then
\[
[J_M:J\cap J_M]\int_{[G_0]}z\cdot\mathcal P\varphi=\sum_{\gamma\in J_M/(J\cap J_M)}\int_{[R_0]}\mathcal W_\varphi(r)\,z(r\,g\,\gamma)\,dr .
\]

## Proof

*Well-definedness.* \(\mathcal W_\varphi\) is continuous, left invariant under \(R_0(E^+)\) and transforms by \(\psi_U\) under the unipotent part; hence \(r\mapsto\mathcal W_\varphi(r)\overline{y(rg)}\) is continuous on the compact quotient \([R_0]\) and integrable. On a finite-dimensional inner product space every conjugate linear form is \(y\mapsto\langle y,v\rangle\) for a unique \(v\) ([[?c:Riesz representation theorem|Riesz representation theorem]]); apply this to \(y\mapsto B_{g,t}(\varphi,y)\).

*1.* \(\mathcal W_\varphi\) is linear in \(t\).

*2.* Let \(\operatorname{tr}z=\sum_{\gamma}R(\gamma)z\) over representatives of \(J_M/(J\cap J_M)\); it is right \(J_M\)-invariant, and for \(J_M\)-invariant \(y\), \(\int\operatorname{tr}z\cdot y=[J_M:J\cap J_M]\int z\cdot y\) by the invariance of the measure. The conjugate of \(\operatorname{tr}z\) lies in \(\mathcal A(Y_0)\), so the left side is \(\int\operatorname{tr}z\cdot\mathcal P\varphi=\langle\overline{\operatorname{tr}z},\mathcal P\varphi\rangle=B_{g,t}(\varphi,\overline{\operatorname{tr}z})\), which is the right side. (The identification of the integral with the inner product and the membership of \(\overline{\operatorname{tr}z}\) in \(\mathcal A(Y_0)\) are as in the Lean proof `integral_mul_poincareAt`, read in outline.) \(\square\)

## Remarks

The normalised Poincaré map of the main inequality and the translates used in the spanning theorem are built from \(\mathcal P_{g,t}\) in other areas ([[?lean:New.Data.poincare|`poincare`]]).

## References

1. Lean: `New.Data.poincareAt`, `New.Data.inner_poincareAt`, `New.Data.integral_mul_poincareAt` in `src/New/UpperBound/Objects/PoincareMap.lean`.
