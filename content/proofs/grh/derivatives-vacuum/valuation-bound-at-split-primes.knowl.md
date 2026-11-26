+++
id = "proofs/grh/derivatives-vacuum/valuation-bound-at-split-primes"
title = "The valuation bound on twelve copies at a split prime"
kind = "lemma"
summary = "At a split prime, if one frame vector has a unit linear form, then v(l!) + val_12(l) <= 0 = S_p in every degree."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.leastValLE_twelve_of_split"]
lean_files = ["src/New/Derivatives/Sharpness/Cases.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/least-valuation-zero-at-inert-primes|the lemma at inert primes]]; \(S_p\) is the [[?lean:New.Data.localPrimeSumTotal|predicted valuation]].

**Lemma.** Let \(p\) split in \(K\), let \(w\) be a family in \(E\) with multiplicities \(c\), and suppose \(\lvert\mu_{i_0,\tau}\rvert_p=1\) for some \(i_0\) and all \(\tau\). Then \(S_p=0\) and \(\operatorname{val}_{12}(l)\le S_p-v_p(l!)\) for every degree \(l\).

## Proof

For split \(p\) the set \(I_p\) is empty, so \(S_p=0\), and \(\gamma_p=0\). By [[proofs/grh/derivatives-vacuum/least-valuation-with-a-unit-form|the bound with a unit form]], \(\operatorname{val}_6(l)\le-v_p(l!)\); add six copies in degree \(0\) ([[proofs/grh/derivatives-vacuum/least-valuation-rules|rule 1]]).

## References

1. Lean: `New.Data.leastValLE_twelve_of_split` in `src/New/Derivatives/Sharpness/Cases.lean`.
