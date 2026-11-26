+++
id = "arithmetic-geometry/selmer-group"
title = "Selmer group with local conditions"
kind = "definition"
summary = "The subgroup of global degree-one cohomology classes satisfying specified local restrictions."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/galois-cohomology", "arithmetic-geometry/galois-localization-kernel"]
+++

Let \(K\) be a [[algebra-fields-galois/number-field|number field]] and \(M\) a discrete Galois module. Give a subgroup \(L_v\subseteq H^1(K_v,M)\) for every place. The **Selmer group** for these local conditions is
\[
\ker\!\left(H^1(K,M)\longrightarrow
  \prod_v H^1(K_v,M)/L_v\right).
\]
The map restricts a [[arithmetic-geometry/galois-cohomology|Galois cohomology class]] at each place and passes to the quotient. Taking \(L_v=0\) at every place gives the [[arithmetic-geometry/galois-localization-kernel|kernel of localization]].

## Changing a local condition

Replacing one \(L_v\) by a smaller subgroup adds a test and can only shrink the global group. Restriction at auxiliary primes can therefore distinguish classes that satisfied all previous conditions.

## References

- [New/Congruences/Selmer/SelmerData.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/SelmerData.lean)
