+++
id = "proofs/grh/derivatives-vacuum/least-valuation-zero-at-inert-primes"
title = "Nonpositive least valuation along a tight frame at an inert prime"
kind = "lemma"
summary = "At an inert prime the least valuation over six copies along a tight frame of length M is at most zero in every degree."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.leastValLE_six_zero_of_inert"]
lean_files = ["src/New/Derivatives/Sharpness/Cases.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/resolution-forms-of-a-frame|the definition of resolution forms]]. For a frame \(w\) with multiplicities \(c\) and a prime \(p\), \(\operatorname{val}_n\) denotes the [[proofs/grh/derivatives-vacuum/least-valuation-relation|least valuation]] for the [[proofs/grh/derivatives-vacuum/cm-curve-and-period|CM curve]] \(\mathcal{E}\), the resolution forms \(\mu\) of \(w\) and the exponents \(c\); degrees are exponent vectors on \(\Phi\).

**Lemma.** Let \((w,c)\) be a tight frame of length \(M\) and \(p\) inert in \(K\). Then \(\operatorname{val}_6(\nu)\le0\) for every degree \(\nu\).

## Proof

By [[proofs/grh/derivatives-vacuum/properties-of-resolution-forms|the properties of resolution forms]], \(\sum_ic_i\Phi_\tau(u_i)\,u_i^\dagger(z)=z_\tau\), so with \(a_{\tau,i}=c_i\,\iota_p(\Phi_\tau(u_i))\) — integral by part 5 — we get \(\sum_ia_{\tau,i}\mu_i(z)=\mathfrak{s}\,z_\tau\) with \(\lvert\mathfrak{s}\rvert_p=1\). Apply [[proofs/grh/derivatives-vacuum/least-valuation-zero-when-forms-span|the lemma on spanning forms]].

## References

1. Lean: `New.Data.leastValLE_six_zero_of_inert` in `src/New/Derivatives/Sharpness/Cases.lean`.
