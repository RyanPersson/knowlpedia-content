+++
id = "proofs/grh/spanning-core/near-isometry-in-mean-square"
title = "Near isometry in mean square"
kind = "definition"
summary = "A linear map whose squared Hilbert–Schmidt norm on every subspace is at least the dimension of the subspace, up to a fixed share of the dimension of the source."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsNearIsometry", "New.IsNearIsometry.mono", "New.IsNearIsometry.finrank_range_pos"]
lean_files = ["src/New/Spanning/SecondMoment/FewTranslates.lean"]
+++

Let \(S,T\) be finite-dimensional complex [[linear-algebra/inner-product-space|inner product spaces]], \(A\colon S\to T\) a [[linear-algebra/linear-map|linear map]] and \(\varepsilon\in\mathbb{R}\). The map \(A\) is a **near isometry (from below, in mean square) with error \(\varepsilon\)** if for every linear subspace \(U\subseteq S\)
\[
\dim U-\varepsilon\,\dim S\ \le\ \lVert A\,\mathrm{pr}_U\rVert_{\mathrm{HS}}^2 ,
\]
where \(\mathrm{pr}_U\) is the orthogonal projection onto \(U\) and \(\lVert\cdot\rVert_{\mathrm{HS}}\) is the [[proofs/grh/spanning-core/hilbert-schmidt-norm-of-a-linear-map|Hilbert–Schmidt norm]].

## Properties

1. A near isometry with error \(\varepsilon\) is one with every error \(\varepsilon'\ge\varepsilon\).
2. Let \(S\neq0\), let \(p\colon T\to T\) be any linear map and \(B\colon S\to T\) linear. If \(pB\) is a near isometry with error \(\varepsilon<1\), then \(p\neq0\), that is, \(\dim p(T)>0\).

## Proof

(1) is clear. (2) If \(p=0\), the definition with \(U=S\) gives \((1-\varepsilon)\dim S\le0\), which is false.

## References

1. Lean: `New.IsNearIsometry`, `New.IsNearIsometry.mono`, `New.IsNearIsometry.finrank_range_pos` in `src/New/Spanning/SecondMoment/FewTranslates.lean`.
