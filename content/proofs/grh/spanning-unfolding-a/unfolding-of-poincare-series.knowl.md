+++
id = "proofs/grh/spanning-unfolding-a/unfolding-of-poincare-series"
title = "Unfolding of the Poincaré series"
kind = "theorem"
summary = "The integral over Gamma backslash G of a form times the Poincaré series of phi is sum_a phi_a times the integral over G of the form times the cut-off Bessel function."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.integrable_and_integral_mul_poincareSeries", "New.Filling.Fits.integral_mul_poincareSeries", "New.Filling.Fits.integrable_mul_poincareSeries", "New.Filling.Fits.integral_mul_tsum_cutBessel", "New.Filling.Fits.integrable_mul_tsum_cutBessel"]
lean_files = ["src/New/Spanning/Unfolding/PoincareSeries.lean"]
proof_status = "full"
+++

**Theorem (unfolding).** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], \(V\) a space [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fitting]] \(S\) with rational points \(\Gamma\subseteq G\), and \(y\) a [[?lean:New.Space.IsForm|form]] on \(V\) of any type (a bounded automorphic function). For every \(\varphi\in\mathbb C^{\{a\}}\), the function \(y\cdot\mathcal P_\varphi\) (with \(\mathcal P_\varphi\) the [[proofs/grh/spanning-unfolding-a/poincare-series-of-bessel-functions|Poincaré series]]) is integrable on \(\Gamma\backslash G\), and
\[
\int_{\Gamma\backslash G}y(g)\,\mathcal P_\varphi(g)\,d\dot g=\sum_a\varphi_a\int_Gy(g)\,B_a(g)\,dg .
\]

## Proof

It suffices to treat one \(a\). Since \(y\) is left \(\Gamma\)-invariant, \(y(g)\sum_\gamma B_a(\gamma g)=\sum_\gamma(yB_a)(\gamma g)\). The function \(yB_a\) is integrable on \(G\) by the proposition on [[proofs/grh/spanning-unfolding-a/convergence-of-poincare-series|convergence]]. For an integrable function \(F\) on \(G\) and the discrete subgroup \(\Gamma\), the series \(\sum_\gamma F(\gamma g)\) is integrable on \(\Gamma\backslash G\) with integral \(\int_GF\) ([[?lean:New.integral_quotMeasure_tsum_eq|unfolding over a discrete subgroup]], with [[?lean:New.integrable_quotMeasure_tsum|its integrability]]). Summing over the finitely many \(a\) with the coefficients \(\varphi_a\) gives the statement.

## Remarks

The source classes this as a known result: the unfolding of Poincaré series along a Bessel subgroup.

## References

1. Lean: `New.Filling.Fits.integrable_and_integral_mul_poincareSeries` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
2. Lean: `New.Filling.Fits.integral_mul_poincareSeries` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
3. Lean: `New.Filling.Fits.integrable_mul_poincareSeries` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
4. Lean: `New.Filling.Fits.integral_mul_tsum_cutBessel` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
5. Lean: `New.Filling.Fits.integrable_mul_tsum_cutBessel` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
