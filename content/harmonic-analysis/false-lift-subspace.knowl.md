+++
id = "harmonic-analysis/false-lift-subspace"
title = "False lifts at a split place"
kind = "definition"
summary = "A local Hecke condition cuts out a subspace in the unwanted summand."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/hecke-operator", "arithmetic-geometry/integral-automorphic-form"]
+++

For a space \(V\) of [[langlands/automorphic-form|automorphic forms]], fix a type operator \(e\), a subspace \(Z\subseteq V\), and a split place \(w\) off the level with [[harmonic-analysis/unramified-hecke-polynomial|Hecke polynomial operator]] \(H_w(\lambda_w)\) evaluated at the proposed lift eigenvalue. The **false lifts at \(w\)** for these data form
\[
 Z\cap\operatorname{im}(e)\cap\ker H_w(\lambda_w).
\]
A common choice for \(Z\) is the orthogonal complement of the genuine lifted space.

## Testing integral forms

A vector orthogonal to these local subspaces at every allowed place can still pair with a genuine lift. Requiring this vector to be an [[arithmetic-geometry/integral-automorphic-form|integral form]] at a given prime permits a bound on denominators from its pairing.

## References

- [New/OneLift/TestedForms.lean, falseLiftsAt](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean#L373)
