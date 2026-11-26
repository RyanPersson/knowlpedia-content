+++
id = "proofs/grh/derivatives-vacuum/legendre-bounds-for-the-data"
title = "Legendre bounds up to O(log b)"
kind = "lemma"
summary = "For p at least 3 and n at most 2b, the valuation of n! lies between n/(p-1) - (log b + 2) and n/(p-1); hence a trinomial coefficient with top at most 2b has valuation at most 3(log b + 2)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.padicValNat_factorial_mem_Icc_of_le", "New.Data.padicValNat_factorial_add_add_le"]
lean_files = ["src/New/Derivatives/Sharpness/NearPairs.lean"]
proof_status = "full"
+++

**Lemma.** Let \(D\) be admissible data with size parameter \(b\), and \(p\ge3\) a prime.

1. If \(n\le2b\), then \(\dfrac{n}{p-1}-(\log b+2)\le v_p(n!)\le\dfrac{n}{p-1}\).
2. If \(n_1+n_2+n_3\le2b\), then \(v_p((n_1+n_2+n_3)!)\le v_p(n_1!)+v_p(n_2!)+v_p(n_3!)+3(\log b+2)\).

## Proof

1. By [[?c:Legendre's formula|Legendre's formula]], \(v_p(n!)=(n-s_p(n))/(p-1)\) with \(s_p(n)\) the digit sum; if \(n<p^D\) then \(1\le s_p(n)\le D(p-1)\) for \(n\ge1\), giving \(n/(p-1)-D\le v_p(n!)\le n/(p-1)\) (Mathlib: `padicValNat_factorial_mem_Icc`). Here \(n\le2b<e\cdot e^{\log b}\le3^{\lceil\log b\rceil+1}\le p^{\lceil\log b\rceil+1}\), so \(D=\lceil\log b\rceil+1\le\log b+2\).

2. Apply the upper bound to \(n_1+n_2+n_3\) and the lower bound to each \(n_i\); the main terms cancel.

## References

1. Lean: `New.Data.padicValNat_factorial_mem_Icc_of_le`, `New.Data.padicValNat_factorial_add_add_le` in `src/New/Derivatives/Sharpness/NearPairs.lean`.
