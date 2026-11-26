+++
id = "harmonic-analysis/adelic-theta-kernel"
title = "Adelic theta kernel of a dual pair"
kind = "definition"
summary = "A theta sum evaluated after the two groups act on common test data."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/reductive-dual-pair", "harmonic-analysis/weil-representation", "harmonic-analysis/schwartz-bruhat-space-adeles"]
+++

Let \((G,H)\) be a [[harmonic-analysis/reductive-dual-pair|dual pair]] over a number field \(F\) with compatible splittings for its [[harmonic-analysis/weil-representation|Weil representation]] \(\omega\). In a Schrödinger model with position space \(X\), the **theta kernel** of a [[harmonic-analysis/schwartz-bruhat-space-adeles|Schwartz–Bruhat function]] \(\phi\) is
\[
 \theta_\phi(g,h)=\sum_{x\in X(F)}(\omega(g,h)\phi)(x).
\]
The variables \(g\) and \(h\) are adelic points of the two groups.

## Integral transform

Pairing this kernel against an automorphic form in one group variable gives its [[arithmetic-geometry/theta-lift|theta lift]] in the other, whenever the integral converges.

## References

- [Lib/Weil/DualPair/Defs.lean, pairTheta](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/Defs.lean#L187)
