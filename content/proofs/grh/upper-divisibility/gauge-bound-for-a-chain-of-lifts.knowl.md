+++
id = "proofs/grh/upper-divisibility/gauge-bound-for-a-chain-of-lifts"
title = "Gauge bound for a chain of lifts with modified data"
kind = "proposition"
summary = "If each datum of a weak chain datum, changed by an operator commuting with the levels, raises p-adic gauges by at most p^(r_j), the combination of chains raises the gauge of a source form by at most p to the sum of the r_j."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsWeakChainDatum.gaugeLe_chain", "New.Data.gaugeLe_chainCombination", "New.Data.norm_star_piMBar_le_one"]
lean_files = ["src/New/UpperBound/Divisibility/ChainValuation.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]], \(p\) a prime, \(\iota\colon\mathbb{C}\to\mathbb{C}_p\). For a point \(d\) and a real \(c\), a form \(\varphi\) has **gauge at most \(c\) at base point \(d\)** if the [[?lean:New.weylGauge|gauge]] of \(\varphi(g)\) at \(gd\) is at most \(c\) for all \(g\) ([[?lean:New.GaugeLe|`GaugeLe`]]). A datum \(\Phi\) for the kernel \(\mathcal K_j\) **raises** gauges by at most \(C\) from \(d\) to \(d'\) if for all points \(g,g'\) and vectors \(v\), the gauge at \(g'd'\) of \(\mathcal K_j(\Phi;g,g')v\) is at most \(C\) times the gauge of \(v\) at \(gd\) ([[?lean:New.Kernel.raises|`Kernel.raises`]]).

**Proposition.** Let \(\vartheta\) be a twist whose modulus has norm prime to \(p\), and \(\Psi\) a [[?lean:New.Data.IsWeakChainDatum|weak chain datum]] for \(\vartheta\) (the tensor of the [[?lean:New.Data.translateDatum|translated vacua]] \(\Phi^{0}_{x,j}\), \(x\in\operatorname{supp}\Psi\), weighted by \(\Psi\), is jointly invariant under the levels of the stages below \(m\); the coefficients \(\Psi(x)\) are integral at every prime not dividing the norm of the modulus of \(\vartheta\); the support consists of admissible translations). For each \(j\) let \(t_j\) be a linear operator on the data of stage \(j\), and \(d_j\in G_f(X_j)\), \(r_j\in\mathbb{R}\). Suppose:

(a) for \(x\in\operatorname{supp}\Psi\), \(t_j\) commutes with the action of \(K_j\times K_{j+1}\) on \(\Phi^{0}_{x,j}\);

(b) for \(x\in\operatorname{supp}\Psi\) and \(j<m\), the datum \(t_j\Phi^{0}_{x,j}\) raises gauges by at most \(p^{r_j}\) from \(d_j\) to \(d_{j+1}\);

(c) the source form \(\varphi\) has gauge at most \(1\) at base point \(d_0\).

Then the combination \(C_\Psi(\varphi)\) of the chains with data \(t_j\Phi^{0}_{x,j}\) has gauge at most \(p^{\sum_{j<m}r_j}\) at base point \(d_m\).

## Proof

By (a) the modified data are still jointly invariant: apply the invariance of the original tensor to the functionals composed with \(t_{m-1}\otimes\cdots\otimes t_0\). By the theorem that [[proofs/grh/upper-divisibility/chain-of-lifts-as-a-sum-over-classes|a chain of lifts is a plain sum]], \(C_\Psi(\varphi)(g_m)\) is a finite sum of terms \(\Psi(x)\cdot\mathcal K_{m-1}\cdots\mathcal K_0\varphi(h_0)\). By (b), applied \(m\) times, and (c), each product of kernels applied to \(\varphi(h_0)\) has gauge at most \(\prod_{j<m}p^{r_j}\) at \(g_md_m\). The coefficient satisfies \(\lvert\iota\Psi(x)\rvert_p\le1\). The gauge is a maximum of \(p\)-adic absolute values of coordinates, hence ultrametric, so the sum obeys the same bound. \(\blacksquare\)

*Status.* Complete given the quoted theorem on the sum over classes; the precise definition of a weak chain datum belongs to another area and is paraphrased.

## References

1. Lean: `New.Data.IsWeakChainDatum.gaugeLe_chain`, `New.Data.gaugeLe_chainCombination` in `src/New/UpperBound/Divisibility/ChainValuation.lean`.
