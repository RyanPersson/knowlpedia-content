+++
id = "grh-lean/landau"
title = "Eliminating poles from a one-sided exponential bound"
kind = "theorem"
summary = "A positive measure and the sign of real residues exclude poles throughout a half-plane."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/landau-laplace-singularity", "harmonic-analysis/laplace-transform"]
+++

Suppose \(E\) is measurable, \(|E(v)|\le Ce^v\) for \(v\ge0\), and its weighted [[harmonic-analysis/laplace-transform|Laplace transform]] has a [[analytic-number-theory/polar-laplace-transform|polar continuation]] to \(\Re s>0\) with only simple poles of [[complex-analysis/residue|residue]] \(r(s)\). If \(\beta>0\), \(E(v)\le e^{(\beta-1)v}\) eventually, and \(\Re r(x)\ge0\) for all real \(x>\beta\), then \(r(\rho)=0\) whenever \(\Re\rho>\beta\).

## Proof

Increase a constant \(A\) until \(Ae^{(\beta-1)v}-E(v)\) is nonnegative for all \(v\ge0\). Integrating against this density gives a positive measure. Its transform equals an explicit rational term minus the original transform. Any real singularity strictly to the right of \(\beta\) would have [[complex-analysis/residue|residue]] of the wrong sign for a transform of a positive measure approached from the right. A removable real singularity cannot be the abscissa of convergence by [[analytic-number-theory/landau-laplace-singularity|Landau’s singularity principle for positive transforms]]: expansion at a regular point, with nonnegative terms, extends exponential integrability a little to the left. Thus the transform converges and is analytic throughout the required half-plane.

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#source=Lib.Analytic.Landau:217).

## References

- [Lib/Analytic/Landau.lean, IsPolar.landau](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Landau.lean#L217)
