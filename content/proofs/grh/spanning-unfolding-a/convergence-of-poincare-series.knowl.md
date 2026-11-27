+++
id = "proofs/grh/spanning-unfolding-a/convergence-of-poincare-series"
title = "Uniform convergence of the Poincaré series and integrability of the cut-off Bessel functions"
kind = "proposition"
summary = "The sums over Gamma of the absolute values of a cut-off Bessel function are bounded uniformly on the adelic group, and the function is integrable."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.exists_tsum_enorm_cutBessel_le", "New.Filling.Fits.integrable_cutBessel", "New.Filling.Fits.integrable_mul_cutBessel"]
lean_files = ["src/New/Spanning/Unfolding/PoincareSeries.lean"]
proof_status = "full"
+++

**Proposition.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], \(V\) a space [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fitting]] \(S\), and \(B_a\) the [[proofs/grh/spanning-unfolding-a/poincare-series-of-bessel-functions|cut-off Bessel function]] of \(a=(c,i)\).

1. There is a finite constant \(C\) with \(\sum_{\gamma\in\Gamma}\lvert B_a(\gamma g)\rvert\le C\) for all \(g\in G\).
2. \(B_a\) is integrable on \(G\); and for every [[?lean:New.Space.IsForm|form]] \(y\) on \(V\) (of any type: a bounded automorphic function), \(y\cdot B_a\) is integrable on \(G\).

## Proof

1. By the theorem on [[proofs/grh/spanning-unfolding-a/convergence-of-block-sums|convergence of block sums]] (item 1, with \(T\) everything, \(s=1\), restricted to the class \(d=c\)) there is \(C\) with \(\sum_{\gamma\in\mathcal T(c,1,c)}\beta_c(\gamma^{-1}y)\prod_v\lVert W_v((\gamma^{-1}y)_v)\rVert\le C\) for all \(y\in\prod_vG_1\). Fix \(g\). Say that a rational \(\delta\) is *in the level* if \(h_c^{-1}\delta_f\iota(\eta)\psi(g_f)\in K(M)\); otherwise \(B_a(\delta g)=0\). If no \(\delta\) is in the level the sum is \(0\). Otherwise fix such a \(\delta\) and substitute \(\gamma\mapsto\gamma^{-1}\delta\) in the sum over \(\Gamma\cong G_S(E)\): if \(\gamma^{-1}\delta\) is in the level too, then \(h_c^{-1}\gamma_fh_c\in K(M)\), i.e. \(\gamma\in\mathcal T(c,1,c)\). By property 2 of \(B_a\), \(\lvert B_a(\gamma^{-1}\delta g)\rvert\le\beta_c(\gamma^{-1}y)\prod_v\lVert W_v((\gamma^{-1}y)_v)\rVert\) with \(y=\delta\,\theta(g_\infty)\), and the sum over \(\gamma\in\mathcal T(c,1,c)\) is at most \(C\).

2. \(\int_G\lvert B_a\rvert=\int_{\Gamma\backslash G}\sum_\gamma\lvert B_a(\gamma g)\rvert\,d\dot g\le C\operatorname{vol}(\Gamma\backslash G)<\infty\), since the quotient has finite volume ([[?lean:New.Space.quotMeasure|quotient measure on \(\Gamma\backslash G\)]] is finite; unfolding by [[?lean:New.lintegral_orbitMeasure_lintegral|integration over orbits]]). A form is bounded and measurable, so \(y\cdot B_a\) is integrable.

## References

1. Lean: `New.Filling.Fits.exists_tsum_enorm_cutBessel_le` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
2. Lean: `New.Filling.Fits.integrable_cutBessel` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
3. Lean: `New.Filling.Fits.integrable_mul_cutBessel` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
