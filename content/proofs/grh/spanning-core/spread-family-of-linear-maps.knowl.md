+++
id = "proofs/grh/spanning-core/spread-family-of-linear-maps"
title = "Spread family of linear maps"
kind = "definition"
summary = "A family of linear maps V -> W such that every subspace of W has a small preimage under one of them."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsSpread"]
lean_files = ["src/New/Spanning/SecondMoment/FewTranslates.lean"]
+++

Let \(V\) and \(W\) be complex [[linear-algebra/vector-space|vector spaces]], \((B_s)_{s\in\Theta}\) a family of [[linear-algebra/linear-map|linear maps]] \(B_s\colon V\to W\) indexed by a set \(\Theta\), and \(\eta\in\mathbb{R}\). The family is **spread with error \(\eta\)** if for every linear subspace \(F\subseteq W\), with **share** \(\alpha=\dim F/\dim W\), there is \(s\in\Theta\) with
\[
\dim B_s^{-1}(F)\ \le\ \Bigl(\frac{1+\alpha}{2}+\eta\Bigr)\dim V .
\]
Here dimensions are finite ranks (zero for a space that is not finite-dimensional), and \(\alpha=0\) by convention if \(\dim W=0\).

## Remarks

Since \(\dim(F+B_s(V))=\dim F+\dim V-\dim B_s^{-1}(F)\) in finite dimension, the condition says that the image of \(B_s\) adds at least \(\bigl(\tfrac{1-\alpha}2-\eta\bigr)\dim V\) dimensions to \(F\); see [[proofs/grh/spanning-core/few-spread-maps-span-almost-everything|few spread maps span almost everything]].

## References

1. Lean: `New.IsSpread` in `src/New/Spanning/SecondMoment/FewTranslates.lean`.
