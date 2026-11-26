+++
id = "proofs/grh/upper-divisibility/full-mark-exists"
title = "Existence of full marks, and vanishing of collisions outside a full mark"
kind = "proposition"
summary = "For an exceptional prime below x_1 a full mark exists, and there are no collisions outside the places inducing it."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_isFullMark", "New.Data.IsFullMark.collisionSum_placesInducing_eq_zero", "New.Data.IsMarked.neg_pow_mul_mem_placesInducing_iff", "New.Data.IsMarked.neg_pow_mul_mem_placesInducingConj_iff"]
lean_files = ["src/New/UpperBound/Divisibility/MarkedPrimes.lean"]
proof_status = "full"
+++

**Proposition.** Let \(D\) be [[?lean:New.Data|admissible data]], \(p\) a prime and \(\iota\colon\mathbb{C}\to\mathbb{C}_p\) an embedding.

1. If \(p<x_1\) and \(p\) is exceptional, there is a [[proofs/grh/upper-divisibility/marked-set-of-primes|full mark]] \(\Lambda\).
2. If \(\Lambda\) is a full mark, then there is no [[proofs/grh/upper-divisibility/collisions|collision]] outside \(\Phi_\Lambda\), and \(\operatorname{coll}_p(\Phi_\Lambda)=0\).

## Proof

(1) Fix a linear order on the set of primes of \(E\) and let \(\Lambda\) be the set of primes \(\mathfrak l=w_\tau\), \(\tau\in\Phi_a\), with \(\mathfrak l<\bar{\mathfrak l}\). It is finite, disjoint from its conjugate (if \(\mathfrak l<\bar{\mathfrak l}\) then not \(\bar{\mathfrak l}<\mathfrak l\)), consists of primes induced by a-places, and \(p\) is exceptional (hence \(\chi_K(p)=-1\ne1\)) and below \(x_1\); so \(\Lambda\) is marked. Let \(\tau\) be an a-place. By the [[proofs/grh/upper-divisibility/orbits-at-an-exceptional-prime|theorem on orbits]], \(\bar w_\tau\ne w_\tau\), and \(\tau'=u(-p^{o_0})\tau\) induces \(\bar w_\tau\) because \(o_0\) is odd; moreover \(\tau'\) is an a-place because \(o_0\mid o_0\) ([[proofs/grh/upper-divisibility/collision-sum-bound|criterion]]). So both \(w_\tau\) and \(\bar w_\tau\) are induced by a-places, and the smaller of the two lies in \(\Lambda\).

(2) Let \((\tau,e)\) be a collision outside \(\Phi_\Lambda\). Then \(e\) is odd, \(\tau\) is an a-place with \(w_\tau\notin\Lambda\), hence \(\bar w_\tau\in\Lambda\) as \(\Lambda\) is full. Since \(e\) is odd and \(p\) is inert, the partner \(u(-p^{e})\tau\) induces \(\bar w_\tau\in\Lambda\), so it lies in \(\Phi_\Lambda\), contradicting the definition of a collision outside \(\Phi_\Lambda\). \(\blacksquare\)

## References

1. Lean: `New.Data.exists_isFullMark`, `New.Data.IsFullMark.collisionSum_placesInducing_eq_zero` in `src/New/UpperBound/Divisibility/MarkedPrimes.lean`.
