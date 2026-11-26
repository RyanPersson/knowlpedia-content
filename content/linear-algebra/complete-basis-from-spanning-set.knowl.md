+++
id = "linear-algebra/complete-basis-from-spanning-set"
title = "Completing an independent family from a spanning set"
kind = "theorem"
summary = "A finite-dimensional space admits a basis extending a prescribed independent family using members of any prescribed spanning set."
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/vector-space","convex-analysis/basis-hamel-basis-and-dimension"]
+++

Let \(V\) be a finite-dimensional [[linear-algebra/vector-space|vector space]], \(y_1,\ldots,y_n\) a linearly independent family, and \(S\) a spanning set for \(V\). There are \(d-n\) members of \(S\), with \(d=\dim V\), which together with \(y_1,\ldots,y_n\) form a [[convex-analysis/basis-hamel-basis-and-dimension|basis]] of \(V\).

## Proof

Start with \(Y=\operatorname{span}(y_1,\ldots,y_n)\). If \(Y\ne V\), some member of \(S\) lies outside \(Y\), since otherwise its span would be contained in \(Y\). Adjoin that member. It preserves independence, since a relation with a nonzero coefficient at the new vector would put it back in \(Y\). It raises the dimension of the span by one. Starting from dimension \(n\), after exactly \(d-n\) additions the span has dimension \(d\) and equals \(V\).

## References

- [Basis extension from a prescribed spanning set](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/GramDeterminant.lean#L34)
