+++
id = "analytic-number-theory/landau-laplace-singularity"
title = "Landau’s theorem for positive Laplace transforms"
kind = "theorem"
summary = "The finite real abscissa of convergence of a positive Laplace transform is a singularity."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/laplace-transform", "analytic-number-theory/landau-singularity-theorem"]
+++

Let \(\mu\) be a positive measure on \([0,\infty)\). Suppose its [[harmonic-analysis/laplace-transform|Laplace integral]] \(F(s)=\int_0^\infty e^{-st}\,d\mu(t)\) converges for \(\Re s>\sigma_c\) and diverges for real \(s<\sigma_c\), with \(\sigma_c\) finite. Then \(F\) has no holomorphic continuation to a neighborhood of \(\sigma_c\).

## Proof

At a real \(a>\sigma_c\), the derivatives of \(F\) give the moments \(\int t^n e^{-at}\,d\mu(t)\) with alternating signs. If \(F\) extended across \(\sigma_c\), one could center its Taylor series at a nearby \(a\) and evaluate it at a point \(a-h<\sigma_c\) in its disk of convergence. Every term of the moment expansion there is nonnegative. Monotone convergence sums them inside the integral, giving \(\int e^{-(a-h)t}\,d\mu<\infty\), a contradiction.

## Positive Dirichlet series

Putting a mass \(a_n\ge0\) at \(t=\log n\) recovers the [[analytic-number-theory/landau-singularity-theorem|Dirichlet-series theorem]].

## References

- [Lib/Analytic/Landau.lean, exists_Ioi_subset_integrableExpSet_of_analyticAt](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Landau.lean#L160)
