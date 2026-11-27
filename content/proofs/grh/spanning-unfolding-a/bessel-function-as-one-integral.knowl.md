+++
id = "proofs/grh/spanning-unfolding-a/bessel-function-as-one-integral"
title = "The Bessel function as an integral over the real Bessel group"
kind = "theorem"
summary = "For a fitting space, the pairing of the tensor product of the local Bessel functions with a vector of the Weyl module is one integral over R(F_infinity) of the conjugate type kernel, the inverse Bessel character and a linear form on the translated vector."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.exists_besselFn_eq_integral", "New.Filling.Fits.prod_besselIntegrand", "New.Filling.Fits.conj_typeKernel", "New.Filling.Fits.weylBesselEquiv_conjWeylRep", "New.Filling.Fits.prod_formalDegree_ne_zero", "New.dotProduct_prod_integral"]
lean_files = ["src/New/Spanning/Unfolding/BesselFormula.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] and let \(V\) with grading \(Y\) [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fit]] the [[?lean:New.Filling|filling data]] \(S\), with parameters \(l=(l_v)\) and weights \(kw\). Let \(A:\mathcal W_{kw}\to\mathbb C^{I}\) be the identification of the [[?c:Weyl module|Weyl module]] with the dual of the values of the Bessel function ([[proofs/grh/spanning-unfolding-a/source-forms-in-bessel-coordinates|source forms in Bessel coordinates]]), \(e_l\) the [[?lean:New.typeKernel|type kernel]], \(\chi_R\) the [[proofs/grh/spanning-unfolding-a/bessel-character-of-fitting-space|Bessel character]], and \(a(s)\) the Levi part of \(s\in R(F_\infty)\), acting on \(\mathcal W_{kw}\) by the Schur matrix of the complex conjugate of \(a(s)\) ([[?lean:New.conjWeylRep|conjugate Weyl representation]], without determinant twist). Then there are a point \(g\in G_\infty\) and a linear form \(t\) on \(\mathcal W_{kw}\) such that for all \(y\in G_\infty\) and \(\zeta\in\mathcal W_{kw}\)
\[
\bigl\langle A(\zeta),\,W(\theta(y))\bigr\rangle=\int_{R(F_\infty)}\overline{e_l(g^{-1}s\,y)}\;\chi_R(s,1)^{-1}\;t\bigl(a(s)\cdot\zeta\bigr)\,ds,
\]
where \(W=\bigotimes_vW_v\) is the tensor product of the full local Bessel functions, \(\langle\cdot,\cdot\rangle\) the bilinear pairing of coordinates, and \(ds\) a [[harmonic-analysis/haar-measure|Haar measure]] on \(R(F_\infty)\) (its normalisation is absorbed in \(t\)).

## Proof

*Local formula.* At each [[?c:Infinite place of a number field|infinite place]] \(v\), the hypothesis that the Bessel system has type \((l_v,kw_v)\) gives a real constant \(a_v\), a point \(x_v\in G_1\) and a vector \(u_v\) of the value space such that for all \(y\in G_1\)
\[
W_v(y)=a_v\int_{R_{\mathrm{loc}}}c_{l_v}(x_v^{-1}r\,y)\;\operatorname{wave}(-\sigma(r))\;\operatorname{rep}_v(a^{-1})u_v\;d\mu_R(r,a),
\]
with integrable integrand, where \(c_{l_v}\) is the coefficient of the [[?c:Discrete series representation|discrete series]] of parameter \(l_v\) carried to \(G_1\) ([[?lean:New.Filling.IsDiscreteSeriesBessel.exists_eq_besselAverage|the Bessel function as a local average]]). Choose \(g\in G_\infty\) with \(\theta(g)=(x_v)_v\).

*Product.* A tensor product of finitely many integrals of integrable vector-valued functions, paired with a fixed vector, is one integral over the product space. So, with \(w=\bigotimes_vu_v\),
\[
\langle A(\zeta),W(\theta(y))\rangle=\Bigl(\prod_va_v\Bigr)\int_{\prod_vR_{\mathrm{loc}}}\Bigl\langle A(\zeta),\bigotimes_v\bigl[c_{l_v}(x_v^{-1}r_v\theta(y)_v)\operatorname{wave}(-\sigma(r_v))\operatorname{rep}_v(a_v^{-1})u_v\bigr]\Bigr\rangle .
\]
By the proposition on the [[proofs/grh/spanning-unfolding-a/real-bessel-group-is-product-of-local-groups|real Bessel group]] this is \(c_0\prod_va_v\) times the integral over \(s\in R(F_\infty)\) of the integrand at \((c(s)_v,a(s)_v)_v\).

*The three factors.* At such a point: (i) \(c(s)_v\theta(y)_v=\theta(sy)_v\), and \(\overline{e_l(g^{-1}sy)}=\prod_vd_{l_v}\cdot\prod_vc_{l_v}\bigl(\theta(g)_v^{-1}\theta(sy)_v\bigr)\), where \(d_{l_v}\) is the [[?c:Formal degree|formal degree]] — the type kernel is the product of the formal degrees times the conjugate coefficients, and \(\theta\) is at each place the inverse frame followed by a fixed left translation; (ii) \(\prod_v\operatorname{wave}(-\sigma(c(s)_v))=\chi_R(s,1)^{-1}\); (iii) the tensor product of the \(\operatorname{rep}_v(a(s)_v^{-1})u_v\) is \(\bigl(\bigotimes_v\operatorname{rep}_v(a(s)_v^{-1})\bigr)w\), and by the intertwining property of \(A\), \(\langle A(\zeta),(\bigotimes_v\operatorname{rep}_v(a(s)_v^{-1}))w\rangle=\langle A(a(s)\cdot\zeta),w\rangle\), because the transpose of the inverse of a unitary matrix is its complex conjugate.

*Conclusion.* The product of the formal degrees is nonzero (the [[?c:Idempotent element|idempotent]] kernel \(e_l\) does not vanish at \(1\)). Put \(C=c_0\prod_va_v/\prod_vd_{l_v}\) and \(t(\xi)=C\,\langle A(\xi),w\rangle\). Combining the three factors gives the formula.

## References

1. Lean: `New.Filling.Fits.exists_besselFn_eq_integral` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
2. Lean: `New.Filling.Fits.prod_besselIntegrand` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
3. Lean: `New.Filling.Fits.conj_typeKernel` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
4. Lean: `New.Filling.Fits.weylBesselEquiv_conjWeylRep` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
5. Lean: `New.Filling.Fits.prod_formalDegree_ne_zero` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
6. Lean: `New.dotProduct_prod_integral` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
