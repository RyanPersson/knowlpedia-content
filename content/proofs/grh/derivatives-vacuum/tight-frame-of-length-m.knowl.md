+++
id = "proofs/grh/derivatives-vacuum/tight-frame-of-length-m"
title = "A tight frame of length M with large multiplicities"
kind = "theorem"
summary = "For admissible data there is a tight frame in the lattice a0 of length M = p0 p1 with all multiplicities at least 6 f b, containing at every p-adic place a vector with a unit linear form."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_isTightFrame"]
lean_files = ["src/New/Derivatives/Vacuum/ShortVectors.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]], with \(M=p_0p_1\) the product of the two level primes, \(f\) the number of infinite places of \(E\) and \(b\) the weight. There are a finite set \(I\), vectors \((v_i)_{i\in I}\) in \(E\) and multiplicities \((c_i)\) such that

1. \((v_i)\) with multiplicities \((c_i)\) is a [[?lean:New.IsTightFrame|tight frame]] of length \(M\);
2. \(c_i\ge6fb\) for all \(i\);
3. for every prime \(p\) and \(p\)-adic place \(\iota_p\) of \(\mathbb{C}\), some \(v_i\) [[proofs/grh/derivatives-vacuum/unit-linear-form|has a unit linear form]] at \(\iota_p\).

## Proof

Let \(h\le b\) and \((v_i)\) be as in [[proofs/grh/derivatives-vacuum/short-coprime-tight-frame|the short coprime frame]], and \(R=\lceil6fb\rceil\). By [[proofs/grh/derivatives-vacuum/tight-frames-of-all-large-lengths|frames of all large lengths]] the powers of \(\zeta\) together with the \(v_i\) carry multiplicities \(\ge R\) making a tight frame of length \(M\), provided \(q_1h+R(q_1+h)\le M\). This inequality, with \(h\le b\), is an instance of the scale inequalities of the data (\(M\ge b^{20}\)) and is asserted here (Lean: `New.Data.nat_le_of_hasLogBound`). Property 3 holds because the vector with a unit linear form is a power of \(\zeta\) or one of the \(v_i\).

## References

1. Lean: `New.Data.exists_isTightFrame` in `src/New/Derivatives/Vacuum/ShortVectors.lean`.
