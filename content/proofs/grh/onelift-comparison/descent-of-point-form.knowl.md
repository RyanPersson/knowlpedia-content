+++
id = "proofs/grh/onelift-comparison/descent-of-point-form"
title = "The descent of a point form is a conjugate theta kernel"
kind = "lemma"
summary = "The normalized descent of a point form is the complex conjugate of the theta kernel whose finite datum is the indicator of Y at the chosen places times tame characters of row determinants."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Rows.pointFormDatum", "New.Rows.normalizedDescent_classForm", "New.Rows.residueBlockDatum_inv_pointLift_mul", "New.Rows.normalizedDescent_pointForm"]
lean_files = ["src/New/OneLift/TestedForms.lean"]
proof_status = "full"
+++

In the setting of [[proofs/grh/onelift-comparison/point-form|point forms]], fix [[?c:Weil representation|Weil data]] for \(E\) and let \(\mathcal{D}=\mathcal{D}_O\) be the [[?lean:New.DescentPair.normalizedDescent|normalized descent]], the linear map from forms on \(V\) to functions on \(U(W)(\mathbb{A})\) adjoint to the [[?c:Theta lift|theta lift]] from \(W\). Let \(\mathfrak{m}\) be the level modulus \(O.\mathrm{levelModulus}(2)\), and for a matrix \(T\in(\mathcal{O}_E/\mathfrak m)^{n\times r}\) let \(T_w\in k_w^{n\times r}\) be its reduction at \(w\in M\cup Q\).

The **point-form datum** of \((Y,e)\) is the function of a family \(X=(X_w)_{w\in M\cup Q}\), \(X_w\in k_w^{n\times r}\),
\[
\Psi_{Y,e}(X)=\begin{cases}\prod_{w\in Q}\psi_w\bigl(\det (X_w)_{e}\bigr)&\text{if }X_w=Y_w\text{ for all }w\in M,\\ 0&\text{otherwise,}\end{cases}
\]
where \((X_w)_e\) is the \(r\times r\) matrix of the rows \(e\) of \(X_w\). The block datum \(\Psi_O\) of the pair ([[?lean:New.DescentPair.residueBlockDatum|residue block datum]]) is the case \(Y_w=\iota_{\operatorname{incl}}\), \(e=\operatorname{incl}\).

**Lemma.** For \(h\in U(V)(\mathbb{A}_f)\), \(v\in\mathbb{C}^{\mathcal I}\), \(g\in U(W)(\mathbb{A})\):

1. \(\mathcal{D}(\delta_h(v))(g)=\overline{\Theta_{\Psi_O,\,P_{\bar v}}(g,h)}\), where \(\Theta_{\Psi,P}\) is the [[?lean:New.modKernel|theta kernel modulo \(\mathfrak m\)]] of the pair \((W,V)\), twisted by the characters \(\chi_W,\chi_V\) of the pair, with finite datum \(T\mapsto\Psi((T_w)_w)\) and polynomial \(P_{\bar v}\) in the Fock variables attached linearly to the conjugate vector \(\bar v\).
2. For \(Y\) of full column rank and any \(X\): \(\Psi_O\bigl((\bar A_w^{-1}X_w)_w\bigr)=\Psi_{Y,e}(X)\) with \(A=A_{Y,e}\).
3. \(\mathcal{D}(\delta_{h,Y,e}(v))(g)=\overline{\Theta_{\Psi_{Y,e},\,P_{\bar v}}(g,h)}\).

## Proof

1. By definition \(\mathcal{D}(\Xi)(g)\) is the class sum over \(h\) of the conjugate kernel \(\overline{\Theta_{\Psi_O,P}(g,h)}\) applied to \(\Xi(h)\); this kernel has the equivariance in \(h\) required by the [[?lean:New.classSum_deltaForm|class-sum lemma for class forms]] ([[?lean:New.DescentPair.conjKernel_equivariant|equivariance of the conjugate kernel]]), which therefore evaluates the sum at the point \(h\).

2. For \(w\in M\): \(\bar A_w^{-1}X_w=\iota_{\operatorname{incl}}\iff X_w=\bar A_w\iota_{\operatorname{incl}}=Y_w\), by property 2 of the [[proofs/grh/onelift-comparison/point-lift|point lift]]. For \(w\in Q\): rows are selected by transposed inclusion matrices, and property 3 gives \(\iota_{\operatorname{incl}}^{\mathsf T}=\iota_e^{\mathsf T}\bar A_w\), so \((\bar A_w^{-1}X_w)_{\operatorname{incl}}=\iota_{\operatorname{incl}}^{\mathsf T}\bar A_w^{-1}X_w=\iota_e^{\mathsf T}X_w=(X_w)_e\). Substituting in the definition of \(\Psi_O\) gives \(\Psi_{Y,e}\).

3. Apply 1 at the point \(hA\). Right translation of the second variable of the kernel by an element \(A\) of the integral level replaces the datum \(T\mapsto\Psi(T)\) by \(T\mapsto\Psi(\bar A^{-1}T)\) and multiplies by \(\chi_W(\det A)\) ([[?lean:New.modKernel_mul_stdLevel_right|translation of the kernel by the integral level]]); here \(\chi_W(\det A)=1\). Reduction commutes with the product, so 2 applies.

## References

1. Lean: `New.Rows.pointFormDatum`, `New.Rows.normalizedDescent_classForm`, `New.Rows.residueBlockDatum_inv_pointLift_mul`, `New.Rows.normalizedDescent_pointForm` in `src/New/OneLift/TestedForms.lean`.
