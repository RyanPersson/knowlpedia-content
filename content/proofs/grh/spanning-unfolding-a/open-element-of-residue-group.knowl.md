+++
id = "proofs/grh/spanning-unfolding-a/open-element-of-residue-group"
title = "Open element of the residue group"
kind = "definition"
summary = "An element s of the residue group is open if at some chosen place above p_0 all proper leading minors of the matrix of products h(f_j, s f_l) are nonzero."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.IsOpenElement"]
lean_files = ["src/New/Spanning/Unfolding/Climbing.lean"]
+++

Let \(S\) be [[?lean:New.Filling|filling data]] over a [[?c:CM field|CM field]] \(E\) and \(s=(s_w)\) an element of the [[?lean:New.Filling.ResidueGL|residue group]]. The element \(s\) is **open** if there is a chosen place \(w\) above the first level prime \(p_0\) such that, for the \((\varrho+1)\times(\varrho+1)\) matrix
\[
Z_w(s)=\bigl(h(f_j,\,s_wf_l)\bigr)_{0\le j,l\le\varrho}
\]
over the [[algebra-commutative/residue-field|residue field]] \(k_w\) (\(f\) the frame, \(h\) the [[?c:Hermitian form|hermitian form]] in the lattice basis reduced modulo \(w\); [[?lean:New.Shape.Form.frameGram|matrix of frame products]]), the [[?lean:New.leadingMinor|leading principal minors]] of orders \(0,1,\dots,\varrho\) are all nonzero.

## References

1. Lean: `New.Filling.IsOpenElement` in `src/New/Spanning/Unfolding/Climbing.lean`.
