+++
id = "proofs/grh/spanning-unfolding-a/poincare-series-of-bessel-functions"
title = "Poincaré series of cut-off Bessel functions"
kind = "definition"
summary = "For a pair a = (class, coordinate), the cut-off Bessel function on the adelic group and the Poincaré series sum_a phi_a sum_gamma cutBessel_a(gamma g)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.cutBessel", "New.Filling.Fits.poincareSeries", "New.Filling.Fits.cutBessel_ratEquiv_mul", "New.Filling.Fits.cutBessel_eq_mul_indicator", "New.Filling.Fits.tsum_cutBessel_classUnipotent", "New.Filling.Fits.enorm_cutBessel_ratEquiv_mul_le", "New.Filling.Fits.measurable_cutBessel"]
lean_files = ["src/New/Spanning/Unfolding/PoincareSeries.lean"]
+++

Let \(V\) be a [[?c:Hermitian form|hermitian space]] [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fitting]] the [[?lean:New.Filling|filling data]] \(S\), with adelic group \(G=G_\infty\times G_f\), rational points \(\Gamma\), identifications \(\theta,\psi\), class points \(x_c\) and principal level \(J_M\). For a pair \(a=(c,i)\) of a [[?lean:New.Filling.Classes|class]] and a tuple of [[?lean:New.Filling.BesselCoord|Bessel coordinates]], the **cut-off Bessel function** is the function on \(G\)
\[
B_a(g)=\begin{cases}\beta_c(y)\,W_i(y),\quad y=\theta(g_\infty),&\text{if }x_c^{-1}g_f\in J_M,\\0&\text{otherwise,}\end{cases}
\]
where \(\beta_c\) is the [[?lean:New.Filling.classCutoff|class cutoff]] (entering through its real value) and \(W_i\) the \(i\)-th coordinate of the full [[?lean:New.Filling.besselFn|Bessel function at the infinite places]]. For a vector \(\varphi=(\varphi_a)_a\in\mathbb C^{\{a\}}\) the **Poincaré series** is
\[
\mathcal P_\varphi(g)=\sum_a\varphi_a\sum_{\gamma\in\Gamma}B_a(\gamma g).
\]

## Properties

Assume in 3 that \(E\) contains a primitive 5040-th root of unity and \(S\) satisfies the [[?lean:New.Filling.IsAdmissible|standing hypotheses]].

1. For a rational [[?c:Isometry of a hermitian space|isometry]] \(\gamma\) of \(S\) (acting on \(G\) through \(\rho\)), with \(y=\gamma\cdot\theta(g_\infty)\):
\[
B_a(\gamma g)=\beta_c(y)W_i(y)\ \text{ if }\ h_c^{-1}\gamma_f\,\iota(\eta)\psi(g_f)\in K(M),\qquad B_a(\gamma g)=0\ \text{ otherwise.}
\]
(This follows from \(\theta((\gamma g)_\infty)=\gamma\,\theta(g_\infty)\), \(\psi(\rho(\gamma)_f)=\iota(\eta)^{-1}\gamma_f\iota(\eta)\) and \(k\in J_M\iff\psi(k)\in K(M)\).)
2. \(\lvert B_a(\gamma g)\rvert\le\beta_c(y)\prod_v\lVert W_v(y_v)\rVert\); \(B_a\) is measurable and right invariant under \(J_M\).
3. \(\displaystyle\sum_{u\in\mathsf U_c(M)}B_a(u\,g)=W_i(\theta(g_\infty))\) if \(h_c^{-1}\iota(\eta)\psi(g_f)\in K(M)\), and \(=0\) otherwise. Indeed \(W\) and the finite condition are invariant under \(\mathsf U_c(M)\) (see [[proofs/grh/spanning-unfolding-a/block-sums-under-unipotent-reductions|blocks under unipotent reductions]]), and the translates of \(\beta_c\) sum to \(1\) ([[proofs/grh/spanning-unfolding-a/class-cutoff-translates-sum-to-one|class cutoffs]]).

## References

1. Lean: `New.Filling.Fits.cutBessel`, `New.Filling.Fits.poincareSeries`, `New.Filling.Fits.cutBessel_ratEquiv_mul`, `New.Filling.Fits.cutBessel_eq_mul_indicator`, `New.Filling.Fits.enorm_cutBessel_ratEquiv_mul_le`, `New.Filling.Fits.tsum_cutBessel_classUnipotent`, `New.Filling.Fits.measurable_cutBessel` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
