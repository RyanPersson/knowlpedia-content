+++
id = "proofs/grh/derivatives-vacuum/near-pair"
title = "Near pairs of b-places"
kind = "definition"
summary = "A b-place tau and an exponent e in I_p below l0/2 such that the partner -p^e tau is again a b-place; they occur only at inert primes and odd exponents."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsNearPair", "New.Data.IsNearPair.ne_d", "New.Data.IsNearPair.inert_and_odd", "New.Data.IsNearPair.inert", "New.Data.IsNearPair.odd", "New.Data.IsNearPair.pos", "New.Data.IsNearPair.partner_eq", "New.Data.IsNearPair.pow_mul_mem"]
lean_files = ["src/New/Derivatives/Sharpness/NearPairs.lean"]
+++

Notation as in [[proofs/grh/derivatives-vacuum/sparseness-along-powers-of-minus-p|the sparseness lemma]]. For a prime \(p\) let \(I_p\) be the [[?lean:New.positivePartnerExponents|set of positive partner exponents]]: the odd natural numbers if \(p\) is inert in \(K\), all \(e\ge1\) if \(p=d\), empty if \(p\) splits. The [[?lean:New.Parameters.partner|partner]] of \(\tau\in\Phi\) at the exponent \(e\) is \([-p^e]\tau\).

A pair \((\tau,e)\in\Phi\times\mathbb{N}\) is a **near pair** at \(p\), with **start** \(\tau\) and **end** \([-p^e]\tau\), if

1. \(e\in I_p\);
2. \(2e<l_0\);
3. \(\tau\in\Phi_b\) and \([-p^e]\tau\in\Phi_b\).

## Properties

All \(b\)-places have the same class modulo \(q_0\) ([[?lean:New.Data.placeClass_of_mem_bPlaces|class of a \(b\)-place]]), so by part 2 of the sparseness lemma there are no near pairs for \(p=d\). Hence a near pair exists only for \(p\) inert, \(e\) is odd and positive, and its end is \([-p]^e\tau\).

## References

1. Lean: `New.Data.IsNearPair`, `New.Data.IsNearPair.ne_d`, `New.Data.IsNearPair.inert_and_odd`, `New.Data.IsNearPair.inert`, `New.Data.IsNearPair.odd`, `New.Data.IsNearPair.pos`, `New.Data.IsNearPair.partner_eq`, `New.Data.IsNearPair.pow_mul_mem` in `src/New/Derivatives/Sharpness/NearPairs.lean`.
