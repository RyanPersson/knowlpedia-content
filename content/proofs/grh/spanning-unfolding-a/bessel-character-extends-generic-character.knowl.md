+++
id = "proofs/grh/spanning-unfolding-a/bessel-character-extends-generic-character"
title = "The Bessel character is a character of R(A) extending the generic character"
kind = "proposition"
summary = "The Bessel character of a fitting space is multiplicative on R(A), trivial on H(A), and equals the generic character psi_U on U(A) when j c = -(M varpi)^-1; hence the source function is the Bessel character times a coefficient of the Levi part."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.besselChar_eq_unipotentChar", "New.Filling.Fits.besselChar_mul", "New.Filling.Fits.besselChar_inclX", "New.Filling.Fits.besselChar_mul_inv_inclX", "New.Filling.Fits.shift_eq_smul_besselCharMatrix", "New.Filling.Fits.sourceFn_eq_besselChar_mul", "New.Filling.Fits.sourceFn_classSection", "New.Filling.Fits.adelicEquiv_inclX", "New.Filling.Fits.ratEquiv_mem_unipotent", "New.Filling.Fits.mem_besselS_of_ratEquiv_mem_besselGroup"]
lean_files = ["src/New/Spanning/Unfolding/SeriesPeriod.lean"]
proof_status = "outline"
+++

**Proposition.** Let \(V\) with grading \(Y\) [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fit]] the [[?lean:New.Filling|filling data]] \(S\) over a [[?c:CM field|CM field]] \(E\) (with fixed [[?lean:New.WeilData|Weil data]], in particular a purely imaginary \(\jmath\in E\)). Let \(R(\mathbb A)=U(\mathbb A)\rtimes H(\mathbb A)\) be the [[?lean:New.Grading.besselGroup|Bessel group of the grading]], \(\chi_R\) the [[proofs/grh/spanning-unfolding-a/bessel-character-of-fitting-space|Bessel character]], \(\psi_U\) the [[?lean:New.Grading.unipotentChar|generic character]] of \(U(\mathbb A)\) with constant \(c_Y\) ([[?lean:New.Grading.genericConst|generic constant]]).

1. \(\chi_R(rr')=\chi_R(r)\chi_R(r')\) for \(r,r'\in R(\mathbb A)\); \(\chi_R\) is trivial on the image of \(H(\mathbb A)\); hence \(\chi_R(r\,a^{-1})=\chi_R(r)\) for \(a\in H(\mathbb A)\).
2. If \(\jmath\,c_Y=-(M\varpi)^{-1}\), then \(\chi_R(u)=\psi_U(u)\) for all \(u\in U(\mathbb A)\).
3. Under the hypothesis of 2, for a linear form \(t\) on the [[?c:Weyl module|Weyl module]] and an [[?c:Algebraic modular form|algebraic form]] \(\varphi\) on \(H\), the [[?lean:New.Grading.sourceFn|source function]] \(\mathcal W_{t,\varphi}(ua)=\psi_U(u)\,t\bigl(\check a_\infty^{-1}\varphi(a_f)\bigr)\) on \(R(\mathbb A)\) satisfies \(\mathcal W_{t,\varphi}(r)=\chi_R(r)\cdot t\bigl(\check a(r)_\infty^{-1}\varphi(a(r)_f)\bigr)\), with \(a(r)\) the Levi part of \(r\) and \(\check a\) the action by the conjugate Weyl representation.
4. Under the same hypothesis, for a class \(c\) with representative \(c_{\mathrm{out}}\), a real point \(s\in R(F_\infty)\) and the point \((s,x_c)\in R(\mathbb A)\) (\(x_c\) the class point), for the translate \(\eta\cdot\psi\) of an algebraic form \(\psi\):
\[
\mathcal W_{t,\eta\psi}(s,x_c)=\chi_R(s,1)\cdot t\bigl(\check a(s)_\infty^{-1}\,\psi(c_{\mathrm{out}})\bigr).
\]

Also: a rational point of \(S\) in \(\mathsf U\) maps into \(U(\mathbb A)\), and a rational \(\sigma\) whose image lies in \(R(\mathbb A)\) lies in the Bessel subgroup of \(S\) (the defining equations descend from the adeles to \(E\)).

## Proof

1. Under \(\alpha\) the Bessel group corresponds to the Bessel subgroup of \(S\) ([[proofs/grh/spanning-unfolding-a/groups-of-a-graded-fitting-space|groups of a graded fitting space]]), on which the simple root sum is additive ([[?lean:New.simpleRootSum_mul|additivity of the simple root sum]]); the [[?c:Additive character|additive character]] turns sums into products. The image of \(H(\mathbb A)\) is the block embedding, whose simple root sum is \(0\).

2. *(Outline.)* The generic character is \(\psi_U(u)=\psi\bigl(\tfrac{\jmath}{2}\operatorname{tr}(\mathfrak e\cdot u)\bigr)\) with \(\mathfrak e\) the [[?lean:New.Grading.shift|shift of the grading]]. For a fitting space \(\mathfrak e=c_Y\cdot C\), where \(C\) is the [[?lean:New.Filling.besselCharMatrix|matrix of the Bessel character]] attached to the middle block of the form of \(S\); **this matrix identity is asserted** (it is the declaration named in the last reference, proved in the source by comparing entries block by block with an automated case analysis). Then \(\operatorname{tr}(Cu)=\sigma-\bar\sigma\) for the simple root sum \(\sigma\) of \(\alpha(u)\) ([[?lean:New.Filling.trace_besselCharMatrix_mul|trace against the Bessel character matrix]], with \(\sigma(u^{-1})=-\sigma(u)\)), so \(\tfrac\jmath2\operatorname{tr}(\mathfrak eu)=\tfrac12\bigl(\jmath c_Y\sigma+\overline{\jmath c_Y\sigma}\bigr)\) because \(\bar\jmath=-\jmath\) and \(\bar c_Y=c_Y\). The standard character depends only on this real part: \(\psi(\tfrac12(x+\bar x))=\psi(x)\) in the normalisation of the source ([[?lean:New.stdAddChar_inv_two_mul_add_star|the standard character and conjugation]]). With \(x=\jmath c_Y\sigma=-(M\varpi)^{-1}\sigma\) this is \(\chi_R(u)\).

3. By definition \(\mathcal W(r)=\psi_U\bigl(r\,a(r)^{-1}\bigr)\cdot t(\dots)\), and by 2 and 1, \(\psi_U(ra(r)^{-1})=\chi_R(ra(r)^{-1})=\chi_R(r)\).

4. The class point is the image in \(R(\mathbb A_f)\) of \(c_{\mathrm{out}}\eta^{-1}\) (centrality of \(\eta\)), so \((s,x_c)=(s,1)\cdot j_Y(1,c_{\mathrm{out}}\eta^{-1})\). Right translation of the argument by an element of \(H(\mathbb A_f)\) translates the form ([[?lean:New.Grading.sourceFn_mul_inclX|source function under translation in \(H\)]]): \(\mathcal W_{t,\eta\psi}((s,1)j_Y(1,c_{\mathrm{out}}\eta^{-1}))=\mathcal W_{t,\,c_{\mathrm{out}}\psi}(s,1)\), and by 3 this is \(\chi_R(s,1)\,t(\check a(s)_\infty^{-1}\psi(c_{\mathrm{out}}))\), the Levi part of \((s,1)\) having trivial finite component.

## References

1. Lean: `New.Filling.Fits.besselChar_eq_unipotentChar` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
2. Lean: `New.Filling.Fits.besselChar_mul` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
3. Lean: `New.Filling.Fits.besselChar_inclX` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
4. Lean: `New.Filling.Fits.besselChar_mul_inv_inclX` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
5. Lean: `New.Filling.Fits.shift_eq_smul_besselCharMatrix` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
6. Lean: `New.Filling.Fits.sourceFn_eq_besselChar_mul` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
7. Lean: `New.Filling.Fits.sourceFn_classSection` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
8. Lean: `New.Filling.Fits.adelicEquiv_inclX` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
9. Lean: `New.Filling.Fits.ratEquiv_mem_unipotent` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
10. Lean: `New.Filling.Fits.mem_besselS_of_ratEquiv_mem_besselGroup` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
11. The step asserted without proof above is proved in Lean by `New.Filling.Fits.shift_eq_smul_besselCharMatrix`.
