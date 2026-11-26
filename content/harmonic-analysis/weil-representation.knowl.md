+++
id = "harmonic-analysis/weil-representation"
title = "Weil representation"
kind = "definition"
summary = "The action lifting symplectic changes of variables in a Heisenberg representation."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["lie-groups/metaplectic-group", "lie-groups/heisenberg-group", "lie-groups/symplectic-group"]
+++

Fix a nontrivial additive character of a local field of characteristic zero and the irreducible unitary representation \(\pi\) of its [[lie-groups/heisenberg-group|Heisenberg group]] with that central character. The **Weil representation** is the action \(\omega\) of the [[lie-groups/metaplectic-group|metaplectic cover]] implementing symplectic automorphisms, with
\[
 \omega(\tilde g)\pi(h)\omega(\tilde g)^{-1}=\pi(g\cdot h)
\]
for every \(h\), where \(\tilde g\) projects to \(g\) in the [[lie-groups/symplectic-group|symplectic group]]. The usual metaplectic normalization acts genuinely on the cover.

## Why a cover appears

With the central character fixed, each symplectic change of variables preserves the equivalence class of \(\pi\). Its intertwiner is determined only up to a scalar. The metaplectic construction resolves those scalars into a linear action.

## References

- [Lib/Weil/Construction/HeisenbergModel.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/HeisenbergModel.lean)
