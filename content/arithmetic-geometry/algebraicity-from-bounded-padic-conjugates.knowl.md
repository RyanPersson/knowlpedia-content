+++
id = "arithmetic-geometry/algebraicity-from-bounded-padic-conjugates"
title = "Algebraicity from bounded p-adic conjugates"
kind = "theorem"
summary = "Bounding a complex number at every comparison over one prime forces it to be algebraic over the rationals."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/prime-number","arithmetic-geometry/padic-comparison-place","algebra-fields-galois/algebraic-element","algebra-fields-galois/transcendental-element","algebra-fields-galois/p-adic-field","shared-foundations/countable-set","algebra-fields-galois/algebraic-closure","algebra-fields-galois/extend-embedding-of-countable-subfield"]
+++

Fix a [[analytic-number-theory/prime-number|prime]] \(p\). If \(x\in\mathbb C\) and \(|\iota(x)|_p\le M\) for every [[arithmetic-geometry/padic-comparison-place|comparison]] \(\iota:\mathbb C\to\overline{\mathbb Q_p}\) over \(p\), then \(x\) is [[algebra-fields-galois/algebraic-element|algebraic]] over \(\mathbb Q\).

## Proof

Suppose \(x\) is [[algebra-fields-galois/transcendental-element|transcendental]]. There are only countably many numbers algebraic over \(\mathbb Q\), since there are countably many rational polynomials and each nonzero one has finitely many roots. The [[algebra-fields-galois/p-adic-field|field \(\mathbb Q_p\)]] has continuum cardinality by its expansions in base \(p\). Choose a transcendental \(u\in\mathbb Q_p\). For a sufficiently large positive integer \(k\), the element \(v=p^{-k}u\) still is transcendental and satisfies \(|v|_p=p^k|u|_p>M\).

Evaluation on rational functions gives an isomorphism \(\mathbb Q(x)\to\mathbb Q(v)\) sending \(x\) to \(v\). Both subfields are [[shared-foundations/countable-set|countable]]. The [[algebra-fields-galois/algebraic-closure|algebraic closure]] of \(\mathbb Q_p\) still has continuum cardinality, by counting its polynomials and their finitely many roots. The [[algebra-fields-galois/extend-embedding-of-countable-subfield|extension theorem for countable subfields]] therefore gives a comparison \(\iota\) sending \(x\) to \(v\). Its size contradicts the bound.

## References

- [The p-adic algebraicity criterion](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/PadicLimitsValuation.lean#L50)
- [Cardinality of the algebraic closure of the p-adic field](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/PeriodRings/Ainf.lean#L53)
