+++
id = "proofs/grh/spanning-unfolding-a/change-of-weight-in-block-sums"
title = "Change of weight in a block sum"
kind = "theorem"
summary = "For a stable set T, the product of the two class cutoffs in the amplitudes may be replaced by any measurable weight whose sums over the orbits of the two unipotent congruence subgroups are 1."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.hasSum_amplitudeSum_of_cutoff", "New.Filling.lintegral_mul_eq_of_isCutoff", "New.Filling.mul_mul_inv_mem_inter_termsOver"]
lean_files = ["src/New/Spanning/Unfolding/AmplitudeSums.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], and \(T\) a [[?lean:New.Filling.IsStable|stable]] set of rational [[?c:Isometry of a hermitian space|isometries]] (\(u^{-1}\gamma u'\in T\iff\gamma\in T\) for rational \(u,u'\in\mathsf U\)). Fix classes \(c,c'\), an element \(s\) of the residue group and a side \(\tau\); put \(X=T\cap\mathcal T(c,s,c')\) ([[?lean:New.Filling.termsOver|terms]]) and \(\Delta=\mathsf U_c(M)\times\mathsf U_{c'}(M)\). Let \(\varphi(\gamma,y)\in[0,\infty]\) be defined for rational \(\gamma\) and \(y\in G_\infty\), measurable in \(y\), such that for all \(\gamma\in X\), \(y\in G_\infty\)
\[
\sum_{(u,u')\in\Delta}\varphi\bigl(u\gamma u'^{-1},\,u\,y\bigr)=1 .
\]
Then:

(a) the integrals \(\int_{G_\infty}\varphi(\gamma,y)\,\mathcal K^{\tau}_\gamma(y)\,dy\), \(\gamma\in X\), are summable with sum the [[?lean:New.Filling.amplitudeSum|block sum]] \(A^{\tau}_T(c,s,c')\);

(b) for each \(\gamma\in X\) the integrand \(y\mapsto\varphi(\gamma,y)\mathcal K^{\tau}_\gamma(y)\) is integrable;

(c) \(\displaystyle\sum_{\gamma\in X}\int_{G_\infty}\varphi(\gamma,y)\,\lVert\mathcal K^{\tau}_\gamma(y)-\mathcal K^{\flat}_\gamma(y)\rVert\,dy\le\tfrac12\operatorname{cov}_{\mathsf U}\,b^{-k^3f}\).

(As in the definition of the amplitude, \(\varphi\) enters vector-valued integrals through its real value.)

## Proof

*The action.* \(\Delta\) acts on \(X\times G_\infty\) by \((u,u')\cdot(\gamma,y)=(u\gamma u'^{-1},uy)\). This preserves \(X\): \(T\) is stable, and \(u,u'\) are terms over \((c,1,c)\) and \((c',1,c')\), so \(u\gamma u'^{-1}\) is again a term over \((c,s,c')\). It preserves the measure \(\rho=\)(counting measure)\(\otimes\)([[harmonic-analysis/haar-measure|Haar measure]]). The kernel \(\mathcal K^{\sigma}(\gamma,y)=\mathcal K^{\sigma}_\gamma(y)\) is invariant for both sides \(\sigma\): \((u\gamma u'^{-1})^{-1}uy=u'\gamma^{-1}y\), and \(W(uy)=W(y)\) for \(u\in\mathsf U_c(M)\), because \(W\) transforms under rational unipotent elements by the inverse of the [[?lean:New.Filling.unipotentChar|unipotent character]] of the finite image ([[?lean:New.Filling.besselFn_ratToInf_mul|transformation of the Bessel function]]), which is trivial on elements conjugate into \(K(M)\).

*Cutoffs.* Call a measurable \(\beta\ge0\) on \(X\times G_\infty\) a cutoff if its sum over every \(\Delta\)-orbit (with multiplicity, i.e. over \(\Delta\)) is \(1\). By hypothesis \(\varphi\) is a cutoff. So is \(\beta_0(\gamma,y)=\beta_c(y)\beta_{c'}(\gamma^{-1}y)\): its sum over \(\Delta\) is \(\sum_u\beta_c(uy)\sum_{u'}\beta_{c'}(u'\gamma^{-1}y)=1\) by the proposition on [[proofs/grh/spanning-unfolding-a/class-cutoff-translates-sum-to-one|class cutoffs]].

*Independence of the cutoff.* For a countable group acting measurably and preserving an s-finite measure, and two cutoffs \(\beta,\beta'\), every invariant measurable \(F\ge0\) has \(\int\beta F\,d\rho=\int\beta'F\,d\rho\): both are the integral of \(F\) over the quotient ([[?lean:New.identDistrib_orbitMeasure|law of an invariant function under a cutoff measure]]). (Directly: \(\int\beta F=\int\beta F\sum_\delta\beta'(\delta p)=\sum_\delta\int\beta(\delta^{-1}p)F(p)\beta'(p)=\int\beta'F\).) The same holds for integrable invariant vector-valued functions ([[?lean:New.IsCutoff.integral_orbitMeasure|integral over the quotient through a cutoff]]).

*Conclusion.* For any cutoff \(\beta\) and invariant \(F\ge0\): \(\int\beta F\,d\rho=\int\beta_0F\,d\rho=\sum_{\gamma\in X}\int\beta_0(\gamma,y)F(\gamma,y)\,dy\). With \(F=\lVert\mathcal K^{\tau}\rVert\) the right side is finite by the theorem on [[proofs/grh/spanning-unfolding-a/convergence-of-block-sums|convergence of block sums]]; so \(\beta\,\mathcal K^{\tau}\) is \(\rho\)-integrable, which gives (b) for \(\beta=\varphi\), and by [[?c:Fubini's theorem|Fubini's theorem]] the integrals over \(y\) sum over \(\gamma\) to \(\int\beta\,\mathcal K^{\tau}d\rho\), which is the integral of \(\mathcal K^{\tau}\) over the quotient and does not depend on \(\beta\). For \(\beta=\beta_0\) the summands are the amplitudes, so this common value is the block sum; for \(\beta=\varphi\) this is (a). With \(F=\lVert\mathcal K^{\tau}-\mathcal K^{\flat}\rVert\) and the [[proofs/grh/spanning-unfolding-a/tail-bound-for-the-cut|tail bound]] (restricted to the class \(d=c'\)) we get (c).

## References

1. Lean: `New.Filling.hasSum_amplitudeSum_of_cutoff` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
2. Lean: `New.Filling.lintegral_mul_eq_of_isCutoff` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
3. Lean: `New.Filling.mul_mul_inv_mem_inter_termsOver` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
