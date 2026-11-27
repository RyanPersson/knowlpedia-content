+++
id = "proofs/grh/spanning-unfolding-a/class-sections-and-class-weights"
title = "Class sections and class weights on the Bessel group"
kind = "definition"
summary = "For a class c: the point (s, x_c) of R(A) attached to a real point s, the real image of the unipotent congruence subgroup, and the weight beta_c(r_infinity) on R(F_infinity) x x_c J."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.classSection", "New.Filling.Fits.classUnipotentToReal", "New.Filling.Fits.classWeight", "New.Filling.Fits.classPoint_eq_inclXFin", "New.Filling.Fits.classPoint_mem_besselFin", "New.Filling.Fits.inv_classPoint_mul_mem_iff", "New.Filling.Fits.exists_ratEquiv_mul_classPoint", "New.Filling.Fits.tsum_classCutoff_realHomeomorph", "New.Filling.Fits.measurable_classWeight", "New.Filling.Fits.ratEquiv_classUnipotent_mem_besselGroup"]
lean_files = ["src/New/Spanning/Unfolding/SeriesPeriod.lean"]
+++

Let \(V\) with grading \(Y\) [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fit]] the [[?lean:New.Filling|filling data]] \(S\) over a [[?c:CM field|CM field]] \(E\); \(R(\mathbb A)\) is the Bessel group of the grading, \(R(F_\infty)\) and \(R(\mathbb A_f)\) its real and finite points, \(J_M\) the principal level, and \(x_c\) the class point of a [[?lean:New.Filling.Classes|class]] \(c\). For a class \(c\):

- the **class section** is the map \(R(F_\infty)\to R(\mathbb A)\), \(s\mapsto(s,x_c)\);
- the **real image** of the [[?lean:New.Filling.classUnipotent|unipotent congruence subgroup]] is the homomorphism \(\mathsf U_c(M)\to R(F_\infty)\), \(u\mapsto u_\infty\) (the infinite component of the image of \(u\) in \(\Gamma\));
- the **class weight** is the function on \(R(\mathbb A)\)
\[
\omega_c(r)=\begin{cases}\beta_c(\theta(r_\infty))&\text{if }x_c^{-1}r_f\in J_M,\\0&\text{otherwise,}\end{cases}
\]
with \(\beta_c\) the [[?lean:New.Filling.classCutoff|class cutoff]] and \(\theta\) the identification of \(G_\infty\) with \(\prod_vG_1\).

## Properties

1. \(x_c=j_Y(c_{\mathrm{out}}\eta^{-1})\in R(\mathbb A_f)\), where \(c_{\mathrm{out}}\) is the chosen representative of \(c\) (because \(\psi(j_Y(a))=\iota(a)\) and \(\eta\) is central); so the class section takes values in \(R(\mathbb A)\).
2. A finite point \(t\) lies in \(x_cJ_M\) if and only if \(h_c^{-1}\iota(\eta)\psi(t)\in K(M)\).
3. For \(u\in\mathsf U_c(M)\) there is \(k\in R(\mathbb A_f)\cap J_M\) (namely \(k=x_c^{-1}u_fx_c\)) with \(u\cdot(x,x_c)=(u_\infty x,\,x_c)\cdot(1,k)\) for all \(x\in G_\infty\).
4. If \(S\) satisfies the standing hypotheses, \(\sum_{u\in\mathsf U_c(M)}\beta_c(\theta(u_\infty x))=1\) for all \(x\in G_\infty\) (as \(\theta(u_\infty x)=u\,\theta(x)\); see [[proofs/grh/spanning-unfolding-a/class-cutoff-translates-sum-to-one|class cutoffs]]), and \(\omega_c\) is measurable.

## References

1. Lean: `New.Filling.Fits.classSection`, `New.Filling.Fits.classUnipotentToReal`, `New.Filling.Fits.classWeight`, `New.Filling.Fits.classPoint_eq_inclXFin`, `New.Filling.Fits.inv_classPoint_mul_mem_iff`, `New.Filling.Fits.exists_ratEquiv_mul_classPoint`, `New.Filling.Fits.tsum_classCutoff_realHomeomorph` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
