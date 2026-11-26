+++
id = "proofs/grh/spanning-unfolding-a/size-of-different-generator-at-infinite-places"
title = "Size of the generator of the different at the infinite places"
kind = "lemma"
summary = "At every infinite place the generator of the different has absolute value between 2 and b."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.apply_deltaE_mem_Icc", "New.Data.two_div_and_inv_sqrt_deltaE_mem_Icc"]
lean_files = ["src/New/Spanning/Unfolding/FrameMass.lean"]
proof_status = "full"
+++

**Lemma.** Let \(D\) be [[?lean:New.Data|admissible data]], with [[?c:CM field|CM field]] \(E\), scale \(b\), and let \(\varpi\) be the purely imaginary [[?lean:New.Parameters.deltaE|generator of the different]] of \(E\) fixed by the parameters (so \(\varpi\mathcal{O}_E\) is the [[?c:Different of a number field|different]] of \(E\)). For every [[?c:Infinite place of a number field|infinite place]] \(v\) of \(E\), writing \(\lvert\varpi\rvert_v\) for the ordinary complex absolute value of \(\varpi\) at \(v\),
\[
2\le \lvert\varpi\rvert_v\le b .
\]
Consequently
\[
b^{-1}\le \frac{2}{\lvert\varpi\rvert_v}\le 1,\qquad b^{-1}\le \lvert\varpi\rvert_v^{-1/2}\le 1 .
\]

## Proof

The two bounds \(2\le\lvert\varpi\rvert_v\) and \(\lvert\varpi\rvert_v\le b\) are comparisons of magnitudes of quantities attached to the data; they are instances of the size calculus of the data, [[?lean:New.Data.le_of_hasLogBound|comparison of logarithmic bounds]], which reduces them to the [[?lean:New.Data.scale_inequalities|scale inequalities]].

Put \(w=\lvert\varpi\rvert_v\). From \(2\le w\) we get \(2/w\le 1\), and from \(w\le b\) we get \(b^{-1}\le w^{-1}\le 2/w\). Since \(w\ge 1\) we have \(\sqrt w\ge 1\), so \(w^{-1/2}\le 1\). Finally \(b\ge w\ge 2\) gives \(w\le b\le b^2\), hence \(\sqrt w\le b\) and \(b^{-1}\le w^{-1/2}\).

## References

1. Lean: `New.Data.apply_deltaE_mem_Icc` in `src/New/Spanning/Unfolding/FrameMass.lean`.
2. Lean: `New.Data.two_div_and_inv_sqrt_deltaE_mem_Icc` in `src/New/Spanning/Unfolding/FrameMass.lean`.
