+++
id = "proofs/grh/spanning-unfolding-a/bessel-function-paired-with-a-form-value"
title = "The integral formula of the Bessel function paired with the value of a form"
kind = "theorem"
summary = "The value of a form psi at a class representative, paired with the Bessel function at x, is the integral over R(F_infinity) of the conjugate kernel at g_0^-1 s^-1 x times the source function at (s, x_c)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.exists_dotProduct_besselFn_eq_integral"]
lean_files = ["src/New/Spanning/Unfolding/SeriesPeriod.lean"]
proof_status = "full"
+++

**Theorem.** Let \(V\) with grading \(Y\) [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fit]] the [[?lean:New.Filling|filling data]] \(S\) over a [[?c:CM field|CM field]] \(E\), and assume \(\jmath\,c_Y=-(M\varpi)^{-1}\) (notation of [[proofs/grh/spanning-unfolding-a/bessel-character-extends-generic-character|the Bessel character and the generic character]]). There are a real point \(g_0\in G_\infty\) and a linear form \(t\) on the [[?c:Weyl module|Weyl module]] such that for every [[?c:Algebraic modular form|algebraic form]] \(\psi\) on \(H\) of weight \((kw,0)\), every class \(c\) and every \(x\in G_\infty\)
\[
\bigl\langle A(\psi(c_{\mathrm{out}})),\,W(\theta(x))\bigr\rangle=\int_{R(F_\infty)}\overline{e_l\bigl(g_0^{-1}s^{-1}x\bigr)}\;\mathcal W_{t,\eta\psi}(s,x_c)\,ds,
\]
where \(A\) is the identification of the Weyl module with the dual of the Bessel coordinates, \(W\) the full Bessel function, \(e_l\) the type kernel, and \(\mathcal W_{t,\eta\psi}\) the [[?lean:New.Grading.sourceFn|source function]] of the translate of \(\psi\) by \(\eta\) at the [[proofs/grh/spanning-unfolding-a/class-sections-and-class-weights|class section]].

## Proof

Take \(g_0,t\) from the theorem on the [[proofs/grh/spanning-unfolding-a/bessel-function-as-one-integral|Bessel function as one integral]], applied with \(y=x\), \(\zeta=\psi(c_{\mathrm{out}})\):
\[
\langle A(\zeta),W(\theta(x))\rangle=\int_{R(F_\infty)}\overline{e_l(g_0^{-1}sx)}\,\chi_R(s,1)^{-1}\,t(\check a(s)\zeta)\,ds .
\]
The group \(R(F_\infty)\) is unimodular ([[?lean:New.Grading.isMulRightInvariant_haar_besselReal_besselFin|unimodularity of the real Bessel group]]), so we may replace \(s\) by \(s^{-1}\). Since \(\chi_R\) is a character on \(R(\mathbb A)\), \(\chi_R(s^{-1},1)^{-1}=\chi_R(s,1)\), and \(a(s^{-1})=a(s)^{-1}\). The integrand becomes \(\overline{e_l(g_0^{-1}s^{-1}x)}\,\chi_R(s,1)\,t(\check a(s)^{-1}\zeta)\), and by item 4 of the proposition on the Bessel character the last two factors are \(\mathcal W_{t,\eta\psi}(s,x_c)\).

## References

1. Lean: `New.Filling.Fits.exists_dotProduct_besselFn_eq_integral` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
