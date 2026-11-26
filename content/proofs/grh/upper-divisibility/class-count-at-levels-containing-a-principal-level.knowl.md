+++
id = "proofs/grh/upper-divisibility/class-count-at-levels-containing-a-principal-level"
title = "Class count at levels containing a principal level"
kind = "proposition"
summary = "For the data, a level containing the principal congruence subgroup of level G has at most exp(x^29 (1 + log G)) classes, and at most exp(x^30) for level pi_M pi_N."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.card_stdClasses_le_exp_mul_log", "New.Data.card_stdClasses_le_exp"]
lean_files = ["src/New/UpperBound/Size/Estimates.lean"]
proof_status = "outline"
+++

**Proposition.** Let \(D\) be [[?lean:New.Data|admissible data]] with CM field \(E\), scale \(x\), number of lifts \(m\) and last rank \(n_m\). Let \(n\) be a finite index set, \(G_f\) the finite adelic unitary group over \(E\) of the form \(\sum_{i\in n}z_i\bar z_i\), \(\Gamma\) its rational points, and \(K\) a subgroup of \(G_f\).

1. If \(\lvert n\rvert\le2n_m\) and \(K\) contains the [[?c:Principal congruence subgroup|principal congruence subgroup]] of level \(G\) for an integer \(G\ge1\), then \(\lvert\Gamma\backslash G_f/K\rvert\le\exp\bigl(x^{29}(1+\log G)\bigr)\).
2. If \(\lvert n\rvert\le n_m\) and \(K\) contains the principal congruence subgroup of level \(\pi_M\pi_N\), then \(\lvert\Gamma\backslash G_f/K\rvert\le\exp(x^{30})\).

## Proof

(1) Let \(K_0\) be the standard level. Every double coset for \(K\) is represented by \(gk\) with \(g\) a representative of a class for \(K_0\) and \(k\) a coset of \(K\cap K_0\) in \(K_0\), so
\[
\lvert\Gamma\backslash G_f/K\rvert\le\lvert\Gamma\backslash G_f/K_0\rvert\cdot[K_0:K\cap K_0].
\]
The index is at most that of the principal congruence subgroup of level \(G\), which is at most \(\mathrm{N}(G\mathcal O_E)^{\lvert n\rvert^2}=G^{2f\lvert n\rvert^2}\le G^{2f(2n_m)^2}\) ([[?lean:New.relIndex_principalLevel_le|`relIndex_principalLevel_le`]], quoted). The [[proofs/grh/upper-divisibility/class-number-bound-for-the-standard-lattice|class number bound]], applied with the number \(q_1d\) of the different, gives \(\lvert\Gamma\backslash G_f/K_0\rvert\le c^{4f(2n_m)^2}\) with \(c=1+2\bigl(6q_1d(2fn_m)^2\bigr)^3\). The size comparisons \(4f(2n_m)^2\log c\le x^{29}\) and \(2f(2n_m)^2\le x^{29}\) (from [[?lean:New.Data.le_of_hasLogBound|`le_of_hasLogBound`]], quoted) give the claim.

(2) \(\pi_M\pi_N\) divides \(MN=\pi_M\bar\pi_M\pi_N\bar\pi_N\), so \(K\) contains the principal congruence subgroup of level \(MN\); apply (1) with \(G=MN\) and the comparison \(x^{29}(1+\log MN)\le x^{30}\). \(\blacksquare\)

## References

1. Lean: `New.Data.card_stdClasses_le_exp_mul_log`, `New.Data.card_stdClasses_le_exp` in `src/New/UpperBound/Size/Estimates.lean`.
