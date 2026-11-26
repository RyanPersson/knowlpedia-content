+++
id = "proofs/grh/upper-divisibility/level-at-n-as-a-mirabolic-group"
title = "The level at N as a mirabolic group in a basis of L_j"
kind = "lemma"
summary = "In a basis of L_j, the components at Sigma_N of the level of stage j are integral invertible matrices with last column that of 1 modulo N, and conversely such matrices supported above N lie in the level."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.atPlaces_conj_mem_mirabolic", "New.Data.mem_levelX_of_mem_mirabolic", "New.Data.directDatum_conj_ne_zero_iff", "New.Data.directDatum_ne_zero_iff", "New.Data.conjEmbedGL_mem_levelX", "New.Data.conjEmbedGL_mem_supportedOn"]
lean_files = ["src/New/UpperBound/Divisibility/SetupAtLevel.lean"]
proof_status = "outline"
+++

Notation of the [[proofs/grh/upper-divisibility/setup-at-the-level-prime|set-up at \(N\)]]. The **mirabolic group** is the group of matrices over \(\prod_{w\in\Sigma_N}\mathcal O_w\) that are invertible and whose last column is \((0,\dots,0,1)^{T}\) modulo \(N\) ([[?lean:New.mirabolic|`mirabolic`]]).

**Lemma.** Let \(k\in G_f(X_j)\).

1. The matrix of \(\delta_j^{-1}k\delta_j\) at \(\Sigma_N\) is integral with last column that of \(1\) modulo \(N\) if and only if for each \(w\in\Sigma_N\): \(k_w\) is integral; if \(\bar w\mid\pi_N\), the last row of \((k^{-1})_{\bar w}\) is that of \(1\) modulo \(\bar w\); and if \(w\mid\pi_N\), the last row of \(k_w\) is that of \(1\) modulo \(w\).
2. If \(k\) lies in the [[?lean:New.Data.levelX|level \(K_j\) of stage \(j\)]], the components of \(\delta_j^{-1}k\delta_j\) at \(\Sigma_N\) lie in the mirabolic group.
3. Conversely, if \(k\) is trivial away from \(\Sigma_N\cup\overline{\Sigma_N}\) and the components of \(\delta_j^{-1}k\delta_j\) at \(\Sigma_N\) lie in the mirabolic group, then \(k\in K_j\). In particular \(\langle a\rangle_j\in K_j\) for mirabolic \(a\).

## Proof

(1) Fix \(w\in\Sigma_N\); exactly one of \(w,\bar w\) divides \(\pi_N\). Conjugation by \(\delta_j\) multiplies the last column by \(t\) and divides the last row by \(t\), where \(t=N\) if \(w\mid\pi_N\) and \(t=1\) otherwise. Since \(k\) is unitary, the last row of \((k^{-1})_{\bar w}\) is the conjugate of the last column of \(k_w\). If \(w\nmid\pi_N\) (so \(\bar w\mid\pi_N\)), both sides say: \(k_w\) integral and its last column is that of \(1\) modulo \(w\). If \(w\mid\pi_N\): integrality of the conjugate says that the upper block is integral, the last row off the corner is divisible by \(N\), \(N\) times the last column off the corner is integral and the corner is integral; the congruence on the last column of the conjugate says that the last column of \(k_w\) off the corner is integral and the corner is \(1\) modulo \(w\). Together this is: \(k_w\) integral, with last row that of \(1\) modulo \(w\).

(2) For \(k\in K_j\): \(k\) is integral, and the last rows of \(k\) and of \(k^{-1}\in K_j\) are those of \(1\) modulo every prime dividing \(\pi_N\) ([[proofs/grh/upper-divisibility/scaling-generator|description of the level]]). By (1) the matrix of the conjugate of \(k\), and likewise that of \(k^{-1}\), is integral with the required last column; so it is invertible over the integers.

(3) By (1) for \(k\) and \(k^{-1}\), \(k\) is integral with integral inverse at \(\Sigma_N\), hence everywhere (it is unitary and trivial elsewhere); it lies in the principal congruence subgroup at the chosen places because it is trivial away from \(N\); and for \(w\mid\pi_N\) either \(w\in\Sigma_N\), where (1) gives the congruence for the last row of \(k_w\), or \(\bar w\in\Sigma_N\), where (1) applied to \(k^{-1}\) at \(\bar w\) gives it. \(\blacksquare\)

*Status.* The Lean proof phrases (1) through the non-vanishing of a "direct datum" (the indicator of integral matrices with prescribed last column, [[?lean:New.directDatum|`directDatum`]]); the entrywise case analysis above follows its proof. The passage between "integral with last column of 1" for \(k\) and \(k^{-1}\) and membership in the mirabolic group uses [[?lean:New.exists_inclGL_eq|`exists_inclGL_eq`]], quoted.

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Divisibility/SetupAtLevel.lean`.
