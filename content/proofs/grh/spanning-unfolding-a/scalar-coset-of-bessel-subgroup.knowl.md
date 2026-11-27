+++
id = "proofs/grh/spanning-unfolding-a/scalar-coset-of-bessel-subgroup"
title = "Scalar coset of the reduced Bessel subgroup"
kind = "definition"
summary = "An element s of the residue group lies in the scalar coset of an integral adele zeta if s is zeta times an element of the reduction of the Bessel subgroup."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.InScalarCoset"]
lean_files = ["src/New/Spanning/Unfolding/Climbing.lean"]
+++

Let \(S\) be [[?lean:New.Filling|filling data]] over a [[?c:CM field|CM field]] \(E\), \(\zeta\in\widehat{\mathcal O}\) an integral finite adele and \(s=(s_w)\) an element of the [[?lean:New.Filling.ResidueGL|residue group]]. Then \(s\) is **in the scalar coset of \(\zeta\)** if there is \(t\) in the [[?lean:New.Filling.reducedImage|reduced image]] \(\bar{\mathsf S}\) of the [[?lean:New.Shape.Form.besselS|Bessel subgroup]] such that for every chosen place \(w\) (above \(p_0\) or \(p_1\))
\[
s_w=(\zeta\bmod w)\cdot t_w
\]
as matrices over the [[algebra-commutative/residue-field|residue field]] at \(w\).

## References

1. Lean: `New.Filling.InScalarCoset` in `src/New/Spanning/Unfolding/Climbing.lean`.
