+++
id = "proofs/grh/upper-divisibility/valuation-of-chains-at-unmarked-primes"
title = "Valuation of the restricted chain without Hecke operators"
kind = "proposition"
summary = "Away from N and d the chain keeps integrality; at a small non-split prime it has valuation at least gain minus loss minus m times the collision sum, and after multiplication by p^(j_p) at least gain minus loss."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsWeakChainDatum.gaugeLe_restrictedChain_one", "New.Data.IsWeakChainDatum.gaugeLe_restrictedChain_collisionSum", "New.Data.IsWeakChainDatum.gaugeLe_pow_collisionExponent_smul", "New.Data.IsWeakChainDatum.gaugeLe_restrictedChain_of_mem_raises", "New.GaugeLe.rpow_mono", "New.GaugeLe.add", "New.GaugeLe.smul", "New.GaugeLe.zpow_neg_smul"]
lean_files = ["src/New/UpperBound/Divisibility/LocalDivisibility.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]], \(p\) a prime, \(\iota\colon\mathbb{C}\to\mathbb{C}_p\), \(\vartheta\) a twist with modulus of norm prime to \(p\), \(\Psi\) a [[?lean:New.Data.IsWeakChainDatum|weak chain datum]] for \(\vartheta\), and \(v\) an integral source form. A form has **valuation at least \(\beta\)** if its gauge at base point \(1\) is at most \(p^{-\beta}\). Let \(R_\Psi\) be the [[?lean:New.Data.restrictedChain|restricted chain]].

**Proposition.**

0. If \(p\ne N\) and, for all \(x\in\operatorname{supp}\Psi\) and all \(j\), the translated vacuum \(\Phi^{0}_{x,j}\) raises gauges by at most \(p^{r_j}\) (base points \(1\)), then \(R_\Psi(v)\) has gauge at most \(p^{\sum_{j<m}r_j}\).
1. If \(p\ne N\) and \(p\ne d\), then \(R_\Psi(v)\) is integral (gauge at most \(1\)).
2. If \(p<x_1\) and \(\chi_K(p)\ne1\), then \(R_\Psi(v)\) has valuation at least \(\operatorname{gain}(p)-\operatorname{loss}(p)-m\operatorname{coll}_p(\emptyset)\).
3. If \(p<x_1\) and \(\chi_K(p)\ne1\), then \(R_\Psi(p^{j_p}v)\) has valuation at least \(\operatorname{gain}(p)-\operatorname{loss}(p)\), where \(j_p=\lceil2mfa/p\rceil\) is the collision exponent.

Gauge bounds are stable under sums (ultrametric), are multiplied by \(\lvert\iota a\rvert_p\) under multiplication by \(a\in\mathbb{C}\), and may be weakened.

## Proof

(0) The [[proofs/grh/upper-divisibility/gauge-bound-for-a-chain-of-lifts|gauge bound for chains]] with \(t_j=1\), \(d_j=1\), followed by [[proofs/grh/upper-divisibility/gauge-and-size-of-the-restriction-to-y-m|restriction to \(Y_m\)]] for \(p\ne N\).

(1) The data are [[proofs/grh/upper-divisibility/data-of-a-weak-chain-datum-are-standard|standard]] for \(\delta=\bar\pi_M\). A standard datum for \(\delta\), with jets scaled by \(\overline{\bar\pi_M}\), raises gauges by at most \(\bigl(\lvert\iota\overline{\bar\pi_M}\rvert/\lvert\iota(\overline{\bar\pi_M}d)\rvert\bigr)^{\text{boxes}}\) ([[?lean:New.Parameters.mem_raises_of_standardData|`mem_raises_of_standardData`]], quoted), which is \(1\) because \(\lvert d\rvert_p=1\) for \(p\ne d\). Apply (0) with \(r_j=0\).

(2) \(p\nmid M\) and \(p\ne N\) ([[proofs/grh/upper-divisibility/orbits-at-an-exceptional-prime|last assertion there]]), so the data are standard of level one, and each raises gauges by at most \(p^{-\operatorname{db}_{p,j}(\emptyset)}\) ([[proofs/grh/upper-divisibility/one-lift-evaluated-at-a-neighbor|last statement there]]). By the theorem that [[proofs/grh/upper-divisibility/only-collisions-lose|only collisions lose]] with \(S=\emptyset\), and \(f(\log b)^2a/p\le\operatorname{loss}(p)\):
\[
-\operatorname{db}_{p,j}(\emptyset)\le\operatorname{coll}_p(\emptyset)+\frac{\operatorname{loss}(p)-\operatorname{gain}(p)}{m}.
\]
Sum over \(j<m\) and apply (0).

(3) Every collision has \(e\ge1\), so \(m\operatorname{coll}_p(\emptyset)\le2mfa/p\le j_p\) ([[proofs/grh/upper-divisibility/collision-sum-bound|bound for the collision sum]]). Multiply (2) by \(p^{j_p}\), of absolute value \(p^{-j_p}\). \(\blacksquare\)

*Status.* The gauge bound for standard data is quoted; the rest is complete relative to the cited knowls.

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Divisibility/LocalDivisibility.lean`.
