+++
id = "grh-lean/second-moment"
title = "A rank gain from the translated Poincaré maps"
kind = "theorem"
summary = "The average of squared matrix norms prevents every translate from lying mostly in a prescribed subspace."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/automorphic-poincare-series", "functional-analysis/hilbert-schmidt-operator"]
+++

Let \(S_0\) be the full space of source forms and let \(F\) occupy a fraction \(\alpha\) of the good target. The translates of the projected [[harmonic-analysis/automorphic-poincare-series|Poincaré series]] form a [[linear-algebra/spread-family-of-linear-maps|spreading family]]. For some translate \(B_s\),
\[
 \dim B_s^{-1}(F)\le\frac{1+\alpha+3/(8b^2)}{2}\dim S_0 .
\]

## Proof

Unfold pairings of translates into finite blocks. Bound the part removed by the two level projections and establish near-isometry for the projected map. A bound on the sum of squared [[functional-analysis/hilbert-schmidt-operator|Hilbert–Schmidt norms]] controls the second moment of these blocks. If every translate mapped too much of the source into the prescribed subspace, its first-moment contribution and this second-moment bound would be incompatible by [[linear-algebra/cauchy-schwarz-inequality|Cauchy–Schwarz]]. A translate with the required rank gain must exist.

## References

- [New/Spanning/SecondMoment/SpanningTheorem.lean, isSpread_goodPoincare](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean#L339)
