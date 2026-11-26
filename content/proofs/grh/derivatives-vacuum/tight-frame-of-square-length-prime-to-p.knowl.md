+++
id = "proofs/grh/derivatives-vacuum/tight-frame-of-square-length-prime-to-p"
title = "A tight frame whose length is a square prime to p"
kind = "lemma"
summary = "For every prime p there is a tight frame in the lattice a0 with multiplicities one whose length is b^2 for a number b prime to p."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.exists_coprime_isTightFrame_sq"]
lean_files = ["src/New/Derivatives/Vacuum/StandardDataProducts.lean"]
proof_status = "full"
+++

**Lemma.** For parameters \(P\), \(s\in\mathbb{N}\) and a prime \(p\), there are \(b\in\mathbb{N}\) with \(p\nmid b\) and a [[?lean:New.IsTightFrame|tight frame]] in \(E\) with multiplicities \(1\) and length \(b^2\).

## Proof

There is a tight frame \(v\) with multiplicities \(1\) of a length \(b\) prime to \(p\): if \(p\nmid q_1\), the powers of \(\zeta\), of length \(b=q_1\) ([[proofs/grh/derivatives-vacuum/roots-of-unity-tight-frame|roots of unity]]); if \(p\mid q_1\), the frame of [[proofs/grh/derivatives-vacuum/tight-frame-of-length-prime-to-q1|length prime to \(q_1\)]]. Repeating each vector of \(v\) \(b\) times gives multiplicities \(1\) and length \(b\cdot b\).

## References

1. Lean: `New.Parameters.exists_coprime_isTightFrame_sq` in `src/New/Derivatives/Vacuum/StandardDataProducts.lean`.
