+++
id = "proofs/grh/spanning-unfolding-a/summation-by-layers"
title = "Summation by layers"
kind = "lemma"
summary = "If the total weight of the points with u <= R is at most (K R^e)^d for all R >= 1, then the weighted sum of u^(-i) is at most 2 K^d once i > 2 e d."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.tsum_mul_inv_pow_le_of_layers"]
lean_files = ["src/New/Spanning/Unfolding/AmplitudeSums.lean"]
proof_status = "full"
+++

**Lemma.** Let \(\alpha\) be a set, \(w:\alpha\to[0,\infty]\) a weight, \(u:\alpha\to\mathbb R\) with \(u\ge1\), \(K\ge0\) real and \(e,d,i\) natural numbers with \(2ed<i\). Suppose that for every real \(R\ge1\)
\[
\sum_{p:\ u(p)\le R}w(p)\le(KR^{e})^{d}.
\]
Then
\[
\sum_{p\in\alpha}w(p)\,u(p)^{-i}\le2K^{d}.
\]

## Proof

Let \(\mu\) be the measure on \(\alpha\) (all subsets measurable) with mass \(w(p)\) at \(p\); the hypothesis says \(\mu\{u\le R\}\le K^dR^{ed}\) for \(R\ge1\), and the claim is \(\int u^{-i}\,d\mu\le2K^d\). Since \(u\ge1\), for every \(p\) we have \(u(p)^{-i}=\int_{u(p)}^{\infty}iR^{-i-1}\,dR\), so by [[?c:Tonelli's theorem|Tonelli's theorem]] (the layer-cake formula)
\[
\int u^{-i}\,d\mu=\int_1^{\infty}iR^{-i-1}\,\mu\{u\le R\}\,dR\le K^{d}\int_1^{\infty}iR^{ed-i-1}\,dR=K^{d}\,\frac{i}{i-ed}\le2K^{d},
\]
because \(i>2ed\) gives \(i-ed>i/2\).

## References

1. Lean: `New.Filling.tsum_mul_inv_pow_le_of_layers` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`; it applies the general layer-cake bound `New.lintegral_rpow_neg_le_of_measure_sublevel_le`.
