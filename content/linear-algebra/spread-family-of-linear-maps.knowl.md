+++
id = "linear-algebra/spread-family-of-linear-maps"
title = "A spreading family of linear maps"
kind = "definition"
summary = "Every target subspace has a controlled inverse image under at least one member of the family."
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/linear-map", "linear-algebra/vector-space"]
+++

Let \(V,W\) be finite-dimensional complex [[linear-algebra/vector-space|vector spaces]] with \(\dim W>0\). A family of [[linear-algebra/linear-map|linear maps]] \(B_s:V\to W\) **spreads with error \(\eta\)** if for every subspace \(F\subseteq W\), some \(s\) satisfies
\[
 \dim B_s^{-1}(F)\le\left(\frac{1+\dim F/\dim W}{2}+\eta\right)\dim V .
\]

## Rank gained outside a subspace

For this \(s\), composing \(B_s\) with the quotient map to \(W/F\) gives rank \(\dim V-\dim B_s^{-1}(F)\) by the [[linear-algebra/rank-nullity-theorem|rank–nullity theorem]].

## References

- [New/Spanning/SecondMoment/FewTranslates.lean, IsSpread](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean#L41)
