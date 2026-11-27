+++
id = "proofs/grh/spanning-unfolding-a/convergence-of-block-sums"
title = "Absolute convergence of the block sums"
kind = "theorem"
summary = "For admissible data the sums over terms of the amplitude majorants are finite, the cutoff-weighted sums of norms of Bessel functions are uniformly bounded, and the amplitudes over a block are summable."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.tsum_amplitudeMajorant_lt_top", "New.Filling.exists_tsum_classCutoff_mul_prod_enorm_le", "New.Filling.summable_amplitude", "New.Filling.tsum_lintegral_classCutoff_mul_majorant_le"]
lean_files = ["src/New/Spanning/Unfolding/AmplitudeSums.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity with \(f\) [[?c:Infinite place of a number field|infinite places]], \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], \(T\) any set of rational [[?c:Isometry of a hermitian space|isometries]], \(c\) a class, \(s\) an element of the residue group and \(\tau\) a side (full or cut). Write \(\mathcal T(c,s,d)\) for the [[?lean:New.Filling.termsOver|terms]] over \((c,s,d)\), \(i_0=r^3f\).

1. There is a finite constant \(C\) such that for all \(y\in G_\infty\)
\[
\sum_d\sum_{\gamma\in T\cap\mathcal T(c,s,d)}\beta_d(\gamma^{-1}y)\prod_v\lVert W_v^{\tau}((\gamma^{-1}y)_v)\rVert\le C .
\]
2. For decay majorants \((w_v,a_v)\) as in the lemma on [[proofs/grh/spanning-unfolding-a/cut-changes-kernel-little|pointwise bounds for the kernel]],
\[
\sum_d\sum_{\gamma}\int_{G_\infty}\beta_c(y)\beta_d(\gamma^{-1}y)\prod_vw_v(y_v)\prod_va_v\,P(\gamma^{-1}y)^{-i_0}\,dy\le\operatorname{cov}_{\mathsf U}\cdot2b^{12n^3rf}\cdot b^{400r^2f}\cdot\lvert I\rvert ,
\]
where \(\lvert I\rvert\) is the number of tuples of [[?lean:New.Filling.BesselCoord|Bessel coordinates]].
3. \(\displaystyle\sum_d\sum_{\gamma\in T\cap\mathcal T(c,s,d)}\int_{G_\infty}\beta_c(y)\beta_d(\gamma^{-1}y)\lVert\mathcal K^{\tau}_\gamma(y)\rVert\,dy<\infty\) (the sum of the [[?lean:New.Filling.amplitudeMajorant|amplitude majorants]]).
4. For every class \(c'\) the family of [[?lean:New.Filling.amplitude|amplitudes]] \(\mathcal A^{\tau}(c,c';\gamma)\), \(\gamma\in T\cap\mathcal T(c,s,c')\), is absolutely summable; its sum is the [[?lean:New.Filling.amplitudeSum|block sum]] \(A^{\tau}_T(c,s,c')\).

## Proof

Each Bessel system has a decay majorant ([[?lean:New.IsCutPair.exists_majorant|existence of decay majorants]]); fix \((w_v,a_v)\). Write \(z=\gamma^{-1}y\).

1. By item 1 of the pointwise bounds, \(\prod_v\lVert W^{\tau}_v(z_v)\rVert\le\prod_va_v\cdot P(z)^{-i_0}\). The proposition on [[proofs/grh/spanning-unfolding-a/sum-of-cutoffs-with-inverse-length-powers|sums of cutoffs]] bounds the sum by \(C=\prod_va_v\cdot2b^{12n^3rf}<\infty\).

2. All terms are nonnegative, so sum and integral may be exchanged:
the left side is \(\int\beta_c(y)\prod_vw_v(y_v)\bigl[\sum_{d,\gamma}\beta_d(z)\prod_va_vP(z)^{-i_0}\bigr]dy\le\prod_va_v\cdot2b^{12n^3rf}\int\beta_c(y)\prod_vw_v(y_v)\,dy\). By the lemma on [[proofs/grh/spanning-unfolding-a/unfolding-class-cutoff-against-invariant-weights|unfolding a class cutoff]] (the \(w_v\) are measurable and \(\mathsf U\)-invariant), the last integral is \(\operatorname{cov}_{\mathsf U}\prod_v\int_{\mathsf U\backslash G_1}w_v\). Finally \(a_v\int_{\mathsf U\backslash G_1}w_v\le b^{400r^2}\lvert I_v\rvert\) is part of the definition of a decay majorant, and \(\prod_v\lvert I_v\rvert=\lvert I\rvert\).

3. \(\lVert\mathcal K^{\tau}_\gamma(y)\rVert=\prod_v\lVert W_v^{\tau}(y_v)\rVert\prod_v\lVert W_v^{\tau}(z_v)\rVert\le\prod_vw_v(y_v)\cdot\prod_va_vP(z)^{-i_0}\) by the pointwise bounds, so 3 follows from 2.

4. \(\lVert\mathcal A^{\tau}(c,c';\gamma)\rVert\) is at most the amplitude majorant ([[proofs/grh/spanning-unfolding-a/amplitude-bounded-by-majorant|bound of the amplitude]]), and the majorants for the single class \(d=c'\) are part of the finite sum in 3.

## References

1. Lean: `New.Filling.tsum_amplitudeMajorant_lt_top` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
2. Lean: `New.Filling.exists_tsum_classCutoff_mul_prod_enorm_le` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
3. Lean: `New.Filling.summable_amplitude` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
4. Lean: `New.Filling.tsum_lintegral_classCutoff_mul_majorant_le` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
