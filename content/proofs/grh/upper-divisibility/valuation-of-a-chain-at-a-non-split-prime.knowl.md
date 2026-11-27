+++
id = "proofs/grh/upper-divisibility/valuation-of-a-chain-at-a-non-split-prime"
title = "Valuation of the restricted chain on the image of the scaled Hecke operators"
kind = "theorem"
summary = "On the m-th power of the product of the scaled Hecke operators applied to an integral source form, the restricted chain has p-adic gauge at most p to the sum over the stages of the transfer exponents plus the lift losses."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsWeakChainDatum.gaugeLe_scaledHeckeOperator_pow", "New.Data.IsWeakChainDatum.exists_lift_eq_chain_scaledHeckeOperator", "New.Data.IsMarked.ω_heckeSplit_mem_raises", "New.Data.liftKernel_omega_heckeSplit", "New.Data.liftKernel_lift_heckeSplit", "New.Data.liftTargetRep"]
lean_files = ["src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]], \(\vartheta\) a twist, \(\Psi\) a [[?lean:New.Data.IsWeakChainDatum|weak chain datum]] for \(\vartheta\), \(p\) a prime not dividing the norm of the modulus of \(\vartheta\), \(\iota\colon\mathbb{C}\to\mathbb{C}_p\), and \(\Lambda\) a [[proofs/grh/upper-divisibility/marked-set-of-primes|marked set]]. Let \(Y=\prod_{\mathfrak l\in\Lambda}\widetilde T_{\mathfrak l}\) be the product (in a fixed order) of the [[proofs/grh/upper-divisibility/scaled-hecke-operator|scaled Hecke operators]], and \(v\) an integral source form. Then the [[?lean:New.Data.restrictedChain|restricted chain]] of \(Y^{m}v\) (the \(\Psi\)-combination of the chains of \(m\) lifts with translated vacua, restricted to \(Y_m\)) has gauge at base point \(1\) at most
\[
p^{\ \sum_{j<m}\bigl(\lvert\Lambda\rvert\,\nu_p+\operatorname{ll}_\Lambda(j)\bigr)},
\]
with \(\nu_p\) the transfer exponent and \(\operatorname{ll}_\Lambda(j)\) the [[proofs/grh/upper-divisibility/neighbor-exponents-and-lift-loss|lift loss]].

## Proof

*Step 1 (moving the operators onto the data).* Fix \(j\) and a list \(L\) of distinct primes of \(\Lambda\). We construct a linear operator \(t=t_{j,L}\) on the data of the lift \(X_j\to X_{j+1}\) such that for every \(x\in\operatorname{supp}\Psi\), with \(\Phi'=t\,\Phi^{0}_{x,j}\):

(a) \(\omega(a,b)\Phi'=t\,\omega(a,b)\Phi^{0}_{x,j}\) for all \(a\) and all integral \(b\);

(b) for every source form \(y\): \(\Theta_{\Phi'}\bigl(F_{x,j}y\bigr)=F_{x,j+1}\bigl(\prod_{\mathfrak l\in L}\widetilde T_{\mathfrak l}\,y\bigr)\), where \(\Theta_{\Phi'}\) is the lift with datum \(\Phi'\) and \(F_{x,e}\) the chain of the first \(e\) lifts;

(c) if \(j<m\) and \(g\) is the unitary adelic element attached to a tuple \((g_{\mathfrak l})_{\mathfrak l\in\Lambda}\) of matrices at the primes of \(\Lambda\) (so \(g\) is determined at the conjugate primes by unitarity and is \(1\) outside \(\Lambda\cup\bar\Lambda\)), with \(g_{\mathfrak l}=1\) for \(\mathfrak l\in L\) and \(g_{\mathfrak l}\) in the double coset of some \(\operatorname{diag}(\varpi1_i,1)\), \(i\le\mathfrak r\), for the other \(\mathfrak l\in\Lambda\), then \(\omega(1,g)\Phi'\) raises gauges by at most \(p^{\beta_L}\), \(\beta_L=\sum_{\mathfrak l\in L}(\nu_p-A_{\mathfrak l})+\sum_{\mathfrak l\in\Lambda}A_{\mathfrak l}+\operatorname{ll}_\Lambda(j)\).

Induction on \(L\). For \(L=\emptyset\), \(t=1\): (a), (b) are trivial; \(\Phi^{0}_{x,j}\) is a standard datum of level one because \(p\ne N\) and \(p\nmid M\) ([[proofs/grh/upper-divisibility/data-of-a-weak-chain-datum-are-standard|standard data]]), and (c) is the theorem on [[proofs/grh/upper-divisibility/one-lift-evaluated-at-a-neighbor|one lift evaluated at a neighbour]]. For \(L'=\mathfrak l::L\), let \(c_i\) be the coefficients of the [[proofs/grh/upper-divisibility/hecke-transfer-through-the-chain|Hecke transfer]] at \(\mathfrak l\) for the chain of \(j+1\) lifts, \(s=p^{A_{\mathfrak l}-\nu_p}\), and
\[
t_{L'}=\Bigl(\sum_{i\le\mathfrak r}c_is\,T^{\mathrm{data}}_{\mathfrak l,i}\Bigr)\circ t_L,
\]
where \(T^{\mathrm{data}}_{\mathfrak l,i}\) is the Hecke operator at \(\mathfrak l\) of the group of \(X_{j+1}\) acting on the data through \(b\mapsto\omega(1,b)\). The datum \(t_L\Phi^{0}_{x,j}\) is spherical at \(\mathfrak l\) by (a) for \(L\) and part 2 of the Hecke transfer. Then: (a) the Hecke operator at \(\mathfrak l\) on a vector spherical at \(\mathfrak l\) commutes with \(\omega(a,b)\), \(b\) integral; (b) the lift intertwines the Hecke operator on the data with the Hecke operator on the lifted forms, so \(\Theta_{t_{L'}\Phi^0}(F_{x,j}y)=\sum_ic_is\,T_i\,F_{x,j+1}(\prod_Ly)=s\,p^{\nu_p}F_{x,j+1}(T_{\mathfrak r}\prod_Ly)=F_{x,j+1}(\widetilde T_{\mathfrak l}\prod_Ly)\) by the Hecke transfer (the form \(\prod_Ly\) is a source form, hence spherical at \(\mathfrak l\)); (c) \(T^{\mathrm{data}}_{\mathfrak l,i}\) is a sum over representatives \(u\) of the left cosets \(uK_{\mathfrak l}\) in the double coset of index \(i\le\mathfrak r\), and \(\omega(1,g)\omega(1,u)=\omega(1,g\cdot u_{\mathfrak l})\), where \(g\cdot u_{\mathfrak l}\) differs from \(g\) only in the component at \(\mathfrak l\) (and \(\bar{\mathfrak l}\)), is trivial on \(L\) and of Hecke type at \(\mathfrak l\) and at the other primes of \(\Lambda\setminus L'\), so (c) for \(L\) applies to each term; the scalar has \(\lvert\iota(c_is)\rvert\le p^{\nu_p-A_{\mathfrak l}}\) since \(c_i\) is \(p\)-integral for \(j<m\); gauges are ultrametric.

*Step 2 (the chain).* Take \(L=\Lambda\) and \(g=1\): operators \(t_j\) with \(\Theta_{t_j\Phi^0_{x,j}}F_{x,j}=F_{x,j+1}Y\) on source forms, commuting with the levels at the data, and \(t_j\Phi^{0}_{x,j}\) raising gauges by at most \(p^{\lvert\Lambda\rvert\nu_p+\operatorname{ll}_\Lambda(j)}\) for \(j<m\) (the sums of \(A_{\mathfrak l}\) cancel). By induction on \(j\), the chain of \(j\) lifts with data \(t_e\Phi^{0}_{x,e}\) applied to \(v\) equals \(F_{x,j}(Y^{j}v)\). Hence the restricted chain of \(Y^{m}v\) is the restriction to \(Y_m\) of the \(\Psi\)-combination of chains with the modified data applied to \(v\).

*Step 3 (the bound).* \(v\) has gauge at most \(1\). The [[proofs/grh/upper-divisibility/gauge-bound-for-a-chain-of-lifts|gauge bound for a chain with modified data]] gives the bound on \(X_m\), and [[proofs/grh/upper-divisibility/gauge-and-size-of-the-restriction-to-y-m|restriction to \(Y_m\)]] keeps it because \(p\ne N\). \(\blacksquare\)

*Status.* Complete relative to the cited knowls; the commutation of Hecke operators with the Weil action and with the lift ([[?lean:New.map_heckeSplit|`map_heckeSplit`]], [[?lean:New.heckeSplit_comm_of_atPlace_mem|`heckeSplit_comm_of_atPlace_mem`]]) is quoted.

## References

1. Lean: `New.Data.IsWeakChainDatum.gaugeLe_scaledHeckeOperator_pow`, `New.Data.IsWeakChainDatum.exists_lift_eq_chain_scaledHeckeOperator` in `src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean`.
