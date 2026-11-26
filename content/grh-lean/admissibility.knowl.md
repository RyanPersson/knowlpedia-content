+++
id = "grh-lean/admissibility"
title = "Constructing admissible data at every large integer"
kind = "theorem"
summary = "Sparse infinite places, levels and compatible scales can be chosen for a prescribed cutoff."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["grh-lean/arithmetic-data", "analytic-number-theory/prime-number-theorem-progressions"]
+++

For fixed arithmetic parameters and \(0<\delta<1/100\), every sufficiently large integer \(x\) has [[grh-lean/arithmetic-data|admissible data]] with that exact cutoff, \(m\ge\sqrt x\), \(\log b\le2x^\delta\), and \(\log x_1\ge x^{\delta/12}\).

## Proof

Choose a dyadic chain length between \(\sqrt x\) and \(2\sqrt x\). Choose the field in a [[algebra-fields-galois/cyclotomic-extension|cyclotomic tower]], so its infinite places are indexed by [[complex-analysis/residue|residue]] classes. A [[discrete-structures/behrend-progression-free-set|Behrend construction]] chooses many \(b\)-places while avoiding prescribed triples under multiplication by powers of a small prime. Points on a common sphere in a box give a set with no prohibited weighted three-term progression. Encoding the box in residue classes transfers this property to the places.

The [[analytic-number-theory/prime-number-theorem-progressions|prime number theorem in progressions]] supplies level primes in the required ranges. The scale inequalities allow these choices and the sparsity requirements to hold simultaneously. The construction starts from the prescribed integer \(x\), which supplies the quantifier needed for the [[grh-lean/real-cutoffs|real-cutoff estimate]].

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#source=New.Reduction.Data.Existence:898).

## References

- [New/Reduction/Data/Existence.lean, eventually_exists_data](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L898)
- [New/Reduction/Data/Existence.lean, exists_three_term_free](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L80)
- [New/Reduction/OneSidedBound.lean, eventually_exists_data_scales](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L74)
