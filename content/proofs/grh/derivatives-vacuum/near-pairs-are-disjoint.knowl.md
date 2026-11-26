+++
id = "proofs/grh/derivatives-vacuum/near-pairs-are-disjoint"
title = "No place occurs twice among the starts and ends of near pairs"
kind = "lemma"
summary = "For a non-split prime p at most k, a place is the start of at most one near pair, the end of at most one near pair, and never both a start and an end."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsNearPair.exponent_unique", "New.Data.IsNearPair.eq_and_eq_of_partner_eq", "New.Data.IsNearPair.end_ne_start"]
lean_files = ["src/New/Derivatives/Sharpness/NearPairs.lean"]
proof_status = "full"
+++

**Lemma.** Let \(p\le k\) be a prime with \(\chi_K(p)\ne1\), and let \((\tau,e)\), \((\tau',e')\) be [[proofs/grh/derivatives-vacuum/near-pair|near pairs]] at \(p\).

1. If \(\tau=\tau'\), then \(e=e'\).
2. If the ends agree, \([-p^e]\tau=[-p^{e'}]\tau'\), then \(\tau=\tau'\) and \(e=e'\).
3. The end of \((\tau,e)\) is not the start \(\tau'\).

## Proof

Each case produces three \(b\)-places forbidden by [[proofs/grh/derivatives-vacuum/sparseness-along-powers-of-minus-p|sparseness]]; note \(e,e'<l_0/2\).

1. If \(e<e'\): \(\tau\), \([-p]^e\tau\), \([-p]^{e'}\tau\) with \(0<e<e'<l_0\).

2. If \(e<e'\): then \(\tau=[-p]^{e'-e}\tau'\), and \(\tau'\), \([-p]^{e'-e}\tau'\), \([-p]^{e'}\tau'\) are \(b\)-places with \(0<e'-e<e'<l_0\) (as \(e>0\)). So \(e=e'\), and then \(\tau=\tau'\) by cancellation.

3. If \([-p]^e\tau=\tau'\): \(\tau\), \([-p]^e\tau\), \([-p]^{e+e'}\tau\) are \(b\)-places with \(0<e<e+e'<l_0\).

## References

1. Lean: `New.Data.IsNearPair.exponent_unique`, `New.Data.IsNearPair.eq_and_eq_of_partner_eq`, `New.Data.IsNearPair.end_ne_start` in `src/New/Derivatives/Sharpness/NearPairs.lean`.
