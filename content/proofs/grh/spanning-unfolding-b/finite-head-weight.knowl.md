+++
id = "proofs/grh/spanning-unfolding-b/finite-head-weight"
title = "Weight of a head at the finite places"
kind = "definition"
summary = "For a sequence of units of a semilocal field, the product over initial partial products D of the K-th power of the square root of the generalised index of D, or zero if some partial product is not integral."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.finHeadWeight"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
+++

Let \(A\) be a [[?lean:New.SemilocalField|semilocal field]] (a locally compact ring with Haar measure and a compact open subring \(O\) of volume one, as for a finite product of nonarchimedean local fields), let \(K,i\ge0\) be integers and \(p=(p_0,p_1,\dots)\) a sequence of units of \(A\). For \(l<i\) put \(D_l=p_0p_1\cdots p_l\). The **weight of the head \(p_0,\dots,p_{i-1}\) at the finite places** is
\[
w^{\mathrm{fin}}_{K,i}(p)=\prod_{l=0}^{i-1}
\begin{cases}\bigl(\sqrt{\operatorname{ind}(D_l)}\bigr)^{K} & D_l\in O,\\ 0 & D_l\notin O,\end{cases}
\]
where \(\operatorname{ind}(D)\) is the [[?lean:New.genIndex|generalised index]] of \(D\): the inverse of the factor by which multiplication by the unit \(D\) scales the [[harmonic-analysis/haar-measure|Haar measure]] of \(A\).

## Remarks

For integral \(D\) the generalised index is the index \([O:DO]\). The weight vanishes unless all partial products \(D_0,\dots,D_{i-1}\) are integral.

## References

1. Lean: `New.finHeadWeight` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`.
