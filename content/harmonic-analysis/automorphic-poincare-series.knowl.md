+++
id = "harmonic-analysis/automorphic-poincare-series"
title = "Automorphic Poincaré series"
kind = "definition"
summary = "Periodization of a seed function over a quotient by rational symmetries."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["langlands/automorphic-form", "algebra-groups/coset"]
+++

Let \(\Gamma\) be a [[lie-groups/discrete-subgroup|discrete subgroup]] of \(G\), \(\Gamma_0\subseteq\Gamma\), and \(f\) a left \(\Gamma_0\)-invariant function on \(G\). Its **Poincaré series** is \(P_f(g)=\sum_{\gamma\in\Gamma_0\backslash\Gamma} f(\gamma g)\) wherever the sum over [[algebra-groups/coset|cosets]] converges absolutely. Right multiplication permutes the indexing cosets, so \(P_f\) is left \(\Gamma\)-invariant. With the appropriate regularity, growth, and transformation law this construction yields an [[langlands/automorphic-form|automorphic form]].

## Why the sum can be unfolded

When pairing \(P_f\) against a \(\Gamma\)-invariant integrable function, translate the integration variable separately in each summand. Under absolute convergence the translates of a fundamental domain assemble into a fundamental domain for \(\Gamma_0\).

## References

- [New/UpperBound/Objects/PoincareMap.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/PoincareMap.lean)
