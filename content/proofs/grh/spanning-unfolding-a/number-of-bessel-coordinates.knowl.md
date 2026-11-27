+++
id = "proofs/grh/spanning-unfolding-a/number-of-bessel-coordinates"
title = "The number of Bessel coordinates of admissible data"
kind = "lemma"
summary = "The Bessel system at one place has at most (k + a)^k <= b^(2k) coordinates, their tensor product at most b^(2kf), and d ((k-1)!)^f <= b^(5kf/4)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.card_besselSystem_le_add_pow", "New.Data.card_besselSystem_le_pow", "New.Data.card_besselCoord_le_pow", "New.Data.card_besselCoord_mul_factorial_le"]
lean_files = ["src/New/Spanning/Unfolding/FillingAdmissible.lean"]
proof_status = "full"
+++

**Lemma.** Let \(D\) be [[?lean:New.Data|admissible data]] with ranks \(k\) (of \(X_0\)), derivative order \(a\), scale \(b\), \(f\) [[?c:Infinite place of a number field|infinite places]], and let \(I_v\) be the index set of the [[?lean:New.BesselSystem|Bessel system]] of the [[?lean:New.Data.filling|filling data]] at the infinite place \(v\), \(I=\prod_vI_v\), \(d=\lvert I\rvert\). Then

1. \(\lvert I_v\rvert\le(k+a)^k\le b^{2k}\);
2. \(d\le b^{2kf}\);
3. \(d\cdot((k-1)!)^{f}\le b^{5kf/4}\).

## Proof

1. \(\lvert I_v\rvert\) is the dimension of the representation of \(U(X_0)\) of weight \(kw_v\) ([[proofs/grh/spanning-unfolding-a/source-forms-in-bessel-coordinates|Bessel coordinates and the Weyl module]], item 1 at one place). This weight has a single row: its column counts vanish for heights \(2,\dots,k-1\), and \(a'=kw_v(1)\le a\) (it is \(a\) at the \(a\)-places and \(0\) otherwise; [[?lean:New.Data.columnCount|column counts]]). The Schur module of a one-row weight of length \(a'\) is the [[?c:Symmetric power|symmetric power]] of degree \(a'\) ([[?lean:New.exists_equiv_schur_one_row_eq_symPowMatrix|one-row Schur modules]]), with basis the monomials of degree \(a'\) in \(k\) variables; their number is \(\binom{k+a'-1}{a'}\le\binom{k+a'}{k}\le(k+a')^k\le(k+a)^k\). Finally \(k+a\le b^2\) by the size calculus of the data ([[?lean:New.Data.le_of_hasLogBound|comparison of logarithmic bounds]]).
2. Multiply 1 over the \(f\) places.
3. \(d\le(k+a)^{kf}\) and \((k-1)!\le k^k\), so the left side is at most \(((k+a)k)^{kf}\), and \((k+a)k\le b^{5/4}\) by the size calculus.

## References

1. Lean: `New.Data.card_besselSystem_le_add_pow` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
2. Lean: `New.Data.card_besselSystem_le_pow` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
3. Lean: `New.Data.card_besselCoord_le_pow` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
4. Lean: `New.Data.card_besselCoord_mul_factorial_le` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
