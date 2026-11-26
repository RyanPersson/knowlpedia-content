+++
id = "grh-lean/enough-forms"
title = "Theorem B · Few translates span nearly the entire target"
kind = "theorem"
summary = "A second moment gives rank gain and iteration turns it into a spanning estimate."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["grh-lean/second-moment", "harmonic-analysis/automorphic-poincare-series"]
+++

For [[grh-lean/arithmetic-data|admissible data]], the target has dimension \(d_T\ge1\). A set \(T\) of translates of the normalized [[harmonic-analysis/automorphic-poincare-series|Poincaré map]] on the ramified source \(S\) has
\[
 |T|\dim S\le5d_T\log(1+2b^2),\qquad
 \dim\sum_{g\in T} g\mathcal P S\ge(1-4/b^2)d_T .
\]

## Proof

Begin with the zero subspace in the target. Given the span already reached, the [[grh-lean/second-moment|second-moment estimate]] finds a translate that adds a controlled fraction of the remaining dimension, measured in units of the source dimension. Add this translate and repeat. First apply this to the full source to leave a deficit of at most \(2d_T/b^2\). Restricting to the ramified source costs at most its codimension per translate. The level bounds make the combined deficit at most \(4d_T/b^2\). Summing the rank gains gives the logarithm in the bound on \(|T|\dim S\). This latter bound pays for the index accumulated in [[grh-lean/short-forms|Theorem A]].

## References

- [New/Reduction/ShortAndEnough.lean, enough_forms](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L448)
- [New/Reduction/ShortAndEnough.lean, exists_le_finrank_iSup_range_normalizedPoincare](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L410)
