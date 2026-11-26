+++
id = "proofs/grh/spanning-core/restricting-maps-to-a-subspace"
title = "Restricting finitely many maps to a subspace"
kind = "lemma"
summary = "Restricting maps to a subspace U lowers the dimension of the span of their images by at most the codimension of U per map."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.finrank_biSup_range_le", "New.finrank_biSup_map_le"]
lean_files = ["src/New/Spanning/SecondMoment/FewTranslates.lean"]
proof_status = "full"
+++

**Lemma.** Let \(V,W\) be finite-dimensional complex vector spaces, \((B_s)_{s\in\Theta}\) linear maps \(V\to W\), \(t\subseteq\Theta\) a finite set, and \(U\subseteq V\) a subspace. Then
\[
\dim\sum_{s\in t}B_s(V)\ \le\ \dim\sum_{s\in t}B_s(U)+\lvert t\rvert\,(\dim V-\dim U).
\]

## Proof

For a subspace \(C\subseteq V\), \(\dim\sum_{s\in t}B_s(C)\le\lvert t\rvert\dim C\), since each \(B_s(C)\) has dimension at most \(\dim C\) and dimensions of sums are subadditive. Choose a complement \(C\) of \(U\) in \(V\), so \(\dim C=\dim V-\dim U\) and \(B_s(V)=B_s(U)+B_s(C)\). Then \(\sum_{s\in t}B_s(V)=\sum_{s\in t}B_s(U)+\sum_{s\in t}B_s(C)\), and the claim follows by subadditivity. \(\blacksquare\)

## Remarks

In [[?lean:New.Data.enough_forms|Theorem B (enough forms)]] this passes from all source forms to the [[?lean:New.Data.ramifiedSourceForms|ramified source forms]].

## References

1. Lean: `New.finrank_biSup_range_le`, `New.finrank_biSup_map_le` in `src/New/Spanning/SecondMoment/FewTranslates.lean`.
