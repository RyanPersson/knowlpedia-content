+++
id = "proofs/grh/upper-divisibility/direct-lifts-lose-little"
title = "Direct lifts at N lose little"
kind = "proposition"
summary = "The lift whose datum at Sigma_N is the direct datum, in bases of L_j and L_(j+1), on a translated integral vacuum raises N-adic gauges by at most N^(f b) and commutes with the levels."
aliases = ["direct datum", "direct lift"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.schrodingerOpAtN_directDatum_mem_raises", "New.Data.schrodingerOpAt_directDatum_mem_raises", "New.Data.exists_mem_inducedPlace_one_le_norm", "New.Data.projOn_translateDatum_mem_standardData", "New.Data.omega_schrodingerOpAtN_directDatum", "New.Data.schrodingerOpAtN"]
lean_files = ["src/New/UpperBound/Divisibility/ValuationAtLevel.lean"]
proof_status = "outline"
+++

Notation of the [[proofs/grh/upper-divisibility/setup-at-the-level-prime|set-up at \(N\)]]; \(\iota\colon\mathbb{C}\to\mathbb{C}_N\). The **direct datum** is the function on matrices over \(\prod_{w\in\Sigma_N}E_w\) that is the indicator of the integral matrices whose last column is the last basis vector modulo \(N\) ([[?lean:New.IsSplitLevel.directDatum|`directDatum`]]). For a function \(\Psi\) of matrices at \(\Sigma_N\), the [[?lean:New.IsSplitLevel.schrodingerOpAt|Schrödinger operator of \(\Psi\) at \(\Sigma_N\)]] is a linear operator \(v\mapsto\Psi\otimes v\) on the data of the lift \(X_j\to X_{j+1}\); it factors through the projection of \(v\) on the vacuum at the places above \(N\) (it is a combination of Heisenberg translates of that projection), so it puts \(\Psi\) at \(\Sigma_N\) in place of the local vacuum and vanishes if the projection of \(v\) vanishes. For a datum \(v\), let \(\mathrm{Dir}_j(v)\) be the image of \(v\) under the Schrödinger operator of the direct datum, moved by the Weil action of \((\delta_j,\delta_{j+1})\): the direct datum "in bases of \(L_j\) and \(L_{j+1}\)".

**Proposition.** Let \(\vartheta\) be a tame character, \(x\) a tuple of translations and \(j<m\).

1. There is an integer \(\delta\) of \(K\) with \(\lvert\iota(\bar\delta d)\rvert_N\ge1\) that lies in every induced prime \(w_\sigma\), \(\sigma\in\Phi\).
2. The datum obtained from the translated vacuum \(\Phi^{0}_{x,j}\) by putting the direct datum at \(\Sigma_N\) [[proofs/grh/upper-divisibility/gauge-bound-for-a-chain-of-lifts|raises]] \(N\)-adic gauges by at most \(N^{fb}\) from base point \(1\) to base point \(1\); hence \(\mathrm{Dir}_j(\Phi^{0}_{x,j})\) raises gauges by at most \(N^{fb}\) from \(\delta_j\) to \(\delta_{j+1}\).
3. \(\mathrm{Dir}_j\) commutes with the Weil action of \(K_j\times K_{j+1}\).

## Proof

(1) The residue field of \(E\) at \(w_1\) has \(N\) elements, so the generator \(\beta=\frac{1+\sqrt{-d}}{2}\) of \(\mathcal O_K\) reduces to an integer \(c\); put \(\delta=\beta-c\). On \(K\) all induced primes restrict to the same prime (the kernel of reduction), so \(\delta\in w_\sigma\) for all \(\sigma\). The conjugate \(\bar\delta=1-\beta-c\) reduces to \(1-2c\), whose square is \(-d\ne0\) modulo \(N\) (as \(N\nmid d\)); so \(\bar\delta d\) is a unit at the induced prime.

(2) The direct datum depends only on the matrix modulo \(N\). By Fourier expansion modulo \(N\), \(c_0=\mathrm N(N\mathcal O_E)^{n_{j+1}n_j}=N^{2fn_{j+1}n_j}\) times the new datum \(\Theta\) is a combination, with \(N\)-integral coefficients, of Heisenberg translates of the projection of \(\Phi^{0}_{x,j}\) on the vacuum above \(N\) by vectors \(z\) with \(\bar\delta' z\) integral, where \(\delta'=\bar\delta\) lies in every place of \(\Sigma_N\) ([[?lean:New.Seesaw.isAdmissibleCombination_schrodingerOp_of_reduction|`isAdmissibleCombination_schrodingerOp_of_reduction`]], quoted). The projection of \(\Phi^{0}_{x,j}\) on the vacuum above \(N\) is either \(0\) or the translate by a vector integral above \(N\). So \(c_0\Theta\) is a [[?lean:New.Parameters.standardData|standard datum]] for \(\delta\). A standard datum for \(\delta\ne0\) raises gauges by at most a product of powers of \(\lvert\iota\overline{\bar\pi_M}\rvert\le1\) and \(\lvert\iota(\bar\delta d)\rvert^{-1}\le1\) ([[?lean:New.Parameters.mem_raises_of_standardData|`mem_raises_of_standardData`]], quoted from the chapter on derivatives of theta functions), that is, by at most \(1\). Hence \(\Theta\) raises gauges by at most \(\lvert c_0\rvert_N^{-1}=N^{2fn_{j+1}n_j}\le N^{2fn_m^2}\le N^{fb}\) (size comparison, quoted). The second statement follows since the Weil action of \((\delta_j,\delta_{j+1})\) on the datum corresponds to moving the base points ([[?lean:New.Kernel.omega_mem_raises_iff|`omega_mem_raises_iff`]]).

(3) For \(a\in K_j\), \(b\in K_{j+1}\), the components at \(\Sigma_N\) of \(\delta_j^{-1}a\delta_j\) and \(\delta_{j+1}^{-1}b\delta_{j+1}\) are [[proofs/grh/upper-divisibility/level-at-n-as-a-mirabolic-group|mirabolic]], and \(S\mapsto b'^{-1}Sa'\) with mirabolic \(a',b'\) preserves the direct datum (integrality and the last column modulo \(N\)); the Weil action of an integral pair acts on the function at \(\Sigma_N\) by this substitution ([[?lean:New.pairWeil_schrodingerOp_of_mem|`pairWeil_schrodingerOp_of_mem`]], quoted). \(\blacksquare\)

*Status.* The Fourier expansion of a datum given modulo \(N\) into translates, the gauge bound for standard data, and the formula for the Weil action on functions at \(\Sigma_N\) are quoted; the exact constants in the bound for standard data were not re-derived (the Lean proof uses only that the factor is at most \(1\) when \(\lvert\iota\bar\pi_M\rvert\le1\le\lvert\iota(\bar\delta d)\rvert\)).

## References

1. Lean: `New.Data.schrodingerOpAtN_directDatum_mem_raises`, `New.Data.schrodingerOpAt_directDatum_mem_raises`, `New.Data.omega_schrodingerOpAtN_directDatum` in `src/New/UpperBound/Divisibility/ValuationAtLevel.lean`.
2. Related work named in the head of the Lean file: Z. Liu, *Test Schwartz functions at p for theta lifts of Hida families*, arXiv:2510.21644, 2025; S. Rallis, *Langlands' functoriality and the Weil representation*, 1982.
