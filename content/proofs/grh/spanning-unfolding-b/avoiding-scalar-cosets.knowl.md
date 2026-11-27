+++
id = "proofs/grh/spanning-unfolding-b/avoiding-scalar-cosets"
title = "Sets avoiding the scalar cosets of the reduced Bessel group"
kind = "definition"
summary = "A set of residues that is disjoint from the cosets of the reduced Bessel group by all integral scalars of norm one other than one."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.AvoidsScalarCosets"]
lean_files = ["src/New/Spanning/Unfolding/SquareExpansion.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\), with residue group \(\bar G\) and [[proofs/grh/spanning-unfolding-b/filling-level-and-reduction|reduced image]] \(\bar R_0\) of the Bessel subgroup. For an integral finite adele \(\zeta\in\widehat{\mathcal{O}}\), an element \(s\in\bar G\) lies **in the scalar coset \(\zeta\bar R_0\)** if there is \(t\in\bar R_0\) with \(s_w=(\zeta\bmod w)\cdot t_w\) at every chosen place \(w\) ([[?lean:New.Filling.InScalarCoset|scalar coset]]).

A set \(\Omega\subset\bar G\) **avoids the scalar cosets** if for every \(\zeta\in E\) that is integral at all finite places, satisfies \(\zeta\bar\zeta=1\) and \(\zeta\ne1\), no \(s\in\Omega\) lies in the scalar coset \(\zeta\bar R_0\).

## Remarks

By [[?c:Kronecker's theorem on roots of unity|Kronecker's theorem]] such \(\zeta\) are the roots of unity of \(E\); the Lean development does not use this.

## References

1. Lean: `New.Filling.AvoidsScalarCosets` in `src/New/Spanning/Unfolding/SquareExpansion.lean`; `New.Filling.InScalarCoset` in `src/New/Spanning/Unfolding/Climbing.lean`.
