+++
id = "proofs/grh/derivatives-vacuum/tight-frames-of-all-large-lengths"
title = "Tight frames of every large length with large multiplicities"
kind = "lemma"
summary = "From a tight frame of length h prime to q1 and the powers of zeta one gets tight frames of every length m at least q1 h + R (q1 + h) with all multiplicities at least R."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.exists_isTightFrame_of_coprime"]
lean_files = ["src/New/Derivatives/Vacuum/ShortVectors.lean"]
proof_status = "full"
+++

**Lemma.** Let \(P\) be [[?lean:New.Parameters|parameters]], \(s\in\mathbb{N}\), and \(E=K(\zeta)\) with \(\zeta\) the chosen primitive \(q_1\)-th root of unity, so that the powers \(\zeta^i\), \(0\le i<q_1\), are a [[proofs/grh/derivatives-vacuum/roots-of-unity-tight-frame|tight frame of length \(q_1\)]] in \(\mathfrak{a}_0\). Let \((v_i)_{i\in I}\) be a tight frame in \(E\) of length \(h\) with multiplicities \(1\), \(\gcd(h,q_1)=1\), and let \(m,R\in\mathbb{N}\) with \(q_1h+R(q_1+h)\le m\). Then there are multiplicities \(c\), all \(\ge R\), such that the family consisting of \(\zeta^i\) (\(0\le i<q_1\)) and the \(v_i\), with multiplicities \(c\), is a tight frame of length \(m\).

## Proof

Since \(\gcd(q_1,h)=1\), every integer \(\ge(q_1-1)(h-1)\) is of the form \(aq_1+bh\) with \(a,b\in\mathbb{N}\) ([[?c:Frobenius coin problem for two coprime integers|the two-coin Frobenius bound]]). Apply this to \(m-R(q_1+h)\ge q_1h\): then \(m=(a+R)q_1+(b+R)h\). Take the powers of \(\zeta\) with multiplicity \(a+R\) (length \((a+R)q_1\)) and the \(v_i\) with multiplicity \(b+R\) (length \((b+R)h\)), by [[proofs/grh/derivatives-vacuum/roots-of-unity-tight-frame|scaling multiplicities]], and take the [[proofs/grh/derivatives-vacuum/tight-frame-operations|union]].

## References

1. Lean: `New.Parameters.exists_isTightFrame_of_coprime` in `src/New/Derivatives/Vacuum/ShortVectors.lean`.
