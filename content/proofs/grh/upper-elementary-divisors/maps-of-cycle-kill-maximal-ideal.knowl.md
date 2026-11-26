+++
id = "proofs/grh/upper-elementary-divisors/maps-of-cycle-kill-maximal-ideal"
title = "The maps of a Frobenius cycle send the maximal ideal into pR"
kind = "lemma"
summary = "Each map of a Frobenius cycle sends the maximal ideal of W into pR; hence parahoric elements have twisted matrices that are block triangular modulo p."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.p_dvd_embedding_of_mem_maximalIdeal", "New.FrobeniusCycle.p_dvd_letterMatrix_of_mem_parahoric", "New.FrobeniusCycle.p_dvd_letterMatrix_of_mem_parahoric_of_isEven", "New.FrobeniusCycle.p_dvd_letterMatrix_of_mem_parahoric_of_not_isEven"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/TwistingData.lean"]
proof_status = "full"
+++

**Lemma.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,R)\) with \(N\ge1\), and let \(\mathfrak{m}\) be the [[algebra-rings/maximal-ideal|maximal ideal]] of \(W\).

1. For every letter \(s\) and every \(y\in\mathfrak{m}\), \(p\) divides \(\iota_s(y)\) in \(R\).
2. Let \(\tau\colon\{0,\dots,k-1\}\to\mathbb{N}\) be a labelling and let \(g\in\mathrm{GL}_k(W)\) lie in the [[?lean:New.parahoric|parahoric subgroup]] of \(\tau\), i.e. \(g_{ij}\in\mathfrak{m}\) whenever \(\tau(i)<\tau(j)\). Let \(g_s\) be the matrix of the [[proofs/grh/upper-elementary-divisors/twisted-action|twisted action]]. If \(s\) is even and \(\tau(i)<\tau(j)\), or \(s\) is odd and \(\tau(j)<\tau(i)\), then \(p\mid (g_s)_{ij}\).

## Proof

(1) By the iterated congruence of a Frobenius cycle, \(p\mid\iota_s(y)-\iota_s(y)^{q}=\iota_s(y)\,\iota_s(1-y^{q-1})\). Since \(q>1\), \(y^{q-1}\in\mathfrak{m}\), so \(1-y^{q-1}\) is a unit of the local ring \(W\) and \(\iota_s(1-y^{q-1})\) is a unit of \(R\). Hence \(p\mid\iota_s(y)\).

(2) If \(s\) is even, \((g_s)_{ij}=\iota_s(g_{ij})\) with \(g_{ij}\in\mathfrak{m}\); apply (1). If \(s\) is odd, \((g_s)_{ij}=\iota_s\bigl((g^{-1})_{ji}\bigr)\); the parahoric subgroup is a group, so \(g^{-1}\) lies in it and \((g^{-1})_{ji}\in\mathfrak{m}\) because \(\tau(j)<\tau(i)\); apply (1). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.p_dvd_embedding_of_mem_maximalIdeal`, `New.FrobeniusCycle.p_dvd_letterMatrix_of_mem_parahoric`, `New.FrobeniusCycle.p_dvd_letterMatrix_of_mem_parahoric_of_isEven`, `New.FrobeniusCycle.p_dvd_letterMatrix_of_mem_parahoric_of_not_isEven` in `src/New/UpperBound/ElementaryDivisors/TwistingData.lean`.
