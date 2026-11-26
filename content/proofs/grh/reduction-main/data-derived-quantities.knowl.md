+++
id = "proofs/grh/reduction-main/data-derived-quantities"
title = "Derived quantities of the data"
kind = "notation"
summary = "The numbers k, t, n_j, the gap, a, M, f, the a-places, the shifted weights and the lift weights read off from the data."
aliases = ["a-places", "lift weight", "gap", "long order"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.x", "New.Data.x₁", "New.Data.b", "New.Data.E", "New.Data.Φ", "New.Data.q₁", "New.Data.f", "New.Data.cyclotomicConductor", "New.Data.rootDisc", "New.Data.k", "New.Data.t", "New.Data.halfGap", "New.Data.gap", "New.Data.reducedHalfGap", "New.Data.a", "New.Data.offWeight", "New.Data.placeOfInt", "New.Data.n", "New.Data.posRank", "New.Data.M", "New.Data.aPlaces", "New.Data.shiftedWeight", "New.Data.liftWeight", "New.Data.LiftIndex"]
lean_files = ["src/New/Reduction/Data/AdmissibleData.lean", "src/New/Reduction/Data/LevelAndTwists.lean"]
+++

Let \(D\) be [[proofs/grh/reduction-main/data|data]] for the parameters \(P=(q_0,d)\), with scales \(x,x_1,b\), ranks \(m,r\), tower exponent \(s\), field \(E\), places \(\Phi\), \(b\)-places \(\Phi_b\), weight \(\kappa\), primes \(p_0,p_1,N\). The following **derived quantities** are used throughout.

| Symbol | Definition | Name |
|---|---|---|
| \(q_1\) | \(q_1(s)=q_0\operatorname{towerDeg}(s)\) | order of \(\zeta\) |
| \(f\) | \(\#\Phi\) | number of infinite places of \(E\) |
| \(\mathrm{rd}_E\) | root discriminant of \(E\) | |
| \(k\) | \(r+1-m\) | rank of the source |
| \(t\) | \(5r\) | |
| \(n_j\) | \(k+j(t+1)\) | ranks of the spaces \(X_j\) |
| \(\Delta/2\) | \(r^8\) | half gap |
| \(\Delta\) | \(2r^8\) | gap between weights of consecutive lifts |
| \(a\) | \(x\,b\) | long order |
| \(a/x_1\) | \(\lfloor a/x_1\rfloor\) (exact) | weight off the \(b\)-places |
| \(M\) | \(p_0p_1\) | principal level |
| \(\Phi_a\) | \(\{\tau\in\Phi:\tau\equiv1\bmod q_0\}\) | the \(a\)-places |
| \(\kappa^{(i)}(\sigma)\) | \(\kappa(\sigma)+(i+1)\Delta/2\) | shifted weight |
| \(\kappa_j(\sigma)\) | \(\kappa^{(2j)}(\sigma)=\kappa(\sigma)+(j+\tfrac12)\Delta\) | weight of the character of lift \(j\) |
| \(-\nu\sigma\) | \(\operatorname{place}(-\nu)\cdot\sigma\) for \(\nu\in\mathbb Z\) | |

The lifts are indexed by \(1\le j\le m\). Further, \(q_1d\) is called the cyclotomic conductor (\(E\subseteq\mathbb Q(\zeta_{q_1d})\)), \(k+j-1\) is the number of plus signs of the space \(W_j\), and \(\Delta/2-(t+1)/2\) is the reduced half gap.

## Properties

1. \(a/x_1\) is an integer, \(q_1\mid\kappa(\sigma)\) for all \(\sigma\), and as real numbers \(\kappa(\sigma)=a/x\) on \(\Phi_b\), \(=a/x_1\) elsewhere. (By (R4), \(q_1x_1\mid b\mid a\).)
2. \(\kappa_j(\sigma)=\kappa(\sigma)+j\Delta+\Delta/2\).
3. \(p_0,p_1,N\equiv1\pmod{q_1d}\) (as \(q_1d\mid q_2(s)\)).
4. \(m\) is even, \(r\) and \(t\) are odd, \(r\ge3\), \(r+6\le t\). Further \(m\ge10^4\), \(m\le r+1\) so that \(r+1=k+m\), \(k\le r\le2k\), \(100m\le k\), \(k\) is even, every \(n_j\) is even and \(n_j\) increases with \(j\), and \(k+t+1\le\Delta/2\).

Properties (1)–(3) and the parities are immediate from the definition; the inequalities in (4) follow from the ranges (R1), (R2) and the largeness of \(x\) forced by (S1), (S2) (e.g. \(\log x\ge100\cdot10^{12}c_P\ge 6.4\cdot10^{15}\), so \(m\ge\sqrt x\ge10^4\), \(101m\le202\sqrt x\le x^5\le r\), and \(k+t+1\le6r+1\le r^8\)).

## References

1. Lean: the abbreviations listed in the front matter, in `src/New/Reduction/Data/AdmissibleData.lean` (`LiftIndex` in `src/New/Reduction/Data/LevelAndTwists.lean`); properties: `New.Data.cast_a`, `cast_offWeight`, `cast_weight`, `q₁_dvd_weight`, `liftWeight_eq`, `levelPrime_modEq_one`, `N_modEq_one`, `r_odd`, `m_even`, `ten_thousand_le_m`, `r_add_one`, `k_le_r`, `hundred_mul_m_le_k`, `k_pos`, `n_mono`, `k_even`, `t_odd`, `r_add_six_le_t`, `k_add_t_add_one_le_halfGap` (`src/New/Reduction/Data/Magnitudes.lean`), `r_le_two_mul_k` (`src/New/Reduction/Data/Sizes.lean`).
