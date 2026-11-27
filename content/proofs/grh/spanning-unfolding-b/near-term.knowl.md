+++
id = "proofs/grh/spanning-unfolding-b/near-term"
title = "Near term"
kind = "definition"
summary = "A rational isometry is near if it joins two boxed points of the product of the real groups."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.IsNear"]
lean_files = ["src/New/Spanning/Unfolding/Terms.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]]. A rational isometry \(\gamma\in G(E)\) is **near** if there is a point \(y\in G_\infty\) such that both \(y\) and \(\gamma_\infty^{-1}y\) are [[?lean:New.Filling.boxedPoints|boxed points]]: points that are [[proofs/grh/spanning-unfolding-b/class-cutoff|reduced]] for the fixed residue domain and whose components \(y_v\) lie in the [[?lean:New.InCut|cut]], that is, have [[?lean:New.besselLength|Bessel length]] at most \(b^{6n+2}\), at every infinite place.

## References

1. Lean: `New.Filling.IsNear` in `src/New/Spanning/Unfolding/Terms.lean`; `New.Filling.boxedPoints` in `src/New/Spanning/RemainingTerms/Box.lean`.
