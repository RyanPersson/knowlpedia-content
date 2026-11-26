+++
id = "analytic-number-theory/entire-dirichlet-l-function"
title = "Pole-removed Dirichlet L-function"
kind = "definition"
summary = "The entire function obtained by removing the pole of the principal Dirichlet L-function."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/dirichlet-l-function", "complex-analysis/analytic-continuation"]
+++

For a [[analytic-number-theory/dirichlet-character|Dirichlet character]] \(\chi\), its **pole-removed function** \(F_\chi\) is \(L(s,\chi)\) when \(\chi\) is nonprincipal. For the [[analytic-number-theory/principal-dirichlet-character|principal character]] it is the [[complex-analysis/analytic-continuation|holomorphic extension]] of \((s-1)L(s,\chi)\) through \(s=1\). The [[analytic-number-theory/dirichlet-l-function|Dirichlet \(L\)-function]] has a simple pole there, so \(F_\chi(1)\) is its nonzero [[complex-analysis/residue|residue]].

## References

- [Lib/General/NumberTheory/ImaginaryQuadraticField.lean, entireL](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/ImaginaryQuadraticField.lean#L69)
