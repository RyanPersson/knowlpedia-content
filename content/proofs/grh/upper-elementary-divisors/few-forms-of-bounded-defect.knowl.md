+++
id = "proofs/grh/upper-elementary-divisors/few-forms-of-bounded-defect"
title = "Few forms have bounded defect"
kind = "theorem"
summary = "In large degree n, the index of the two-block parahoric subgroup times the dimension of the forms whose block diagonal translates have defect at most 3t along the root between the blocks is at most (1 + theta) times the number of exponents."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.index_mul_finrank_defectConditions_le", "New.volume_degreeSlab_le", "New.volume_sum_mem_Icc_le", "New.pow_div_factorial_le_card_monomials"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/DefectCount.lean"]
proof_status = "full"
+++

**Theorem.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,K)\), \(N\ge1\), with \(K\) a field of characteristic \(p\). Let \(a'=a+1<k\), \(n>0\), \(t\in\mathbb{N}\) with \(t\ge2(k+1)\), and \(\theta\le1\) real with
\[
8\,N\,k\,t\,P^{2a'}\le\theta\,n .
\]
Let \(S\) be the space of coefficient vectors \(F\colon\mathcal{E}(N,k,n)\to K\) such that for every block diagonal \(g\) (blocks of sizes \(a',k-a'\)) the translate \(\rho_n(g)F\) vanishes at every \(\beta\) with \(\operatorname{def}_{i,a,a'}(\beta)>3t\) for some letter \(i\) ([[proofs/grh/upper-elementary-divisors/translate-conditions|defect conditions]]). Then
\[
[\mathrm{GL}_k(W):\mathrm{Par}_{a'}(W)]\cdot\dim_KS\ \le\ (1+\theta)\cdot\#\mathcal{E}(N,k,n).
\]

## Proof

By [[proofs/grh/upper-elementary-divisors/bounded-defect-dimension-by-lattice-points|the count by flags and volume]] there is \(D\) with \(D_s\le n+E\), \(E=4tP^{2a'}\), and \(\dim S\le\phi\operatorname{vol}(\mathcal{K}(a,0)\cap\mathrm{Slab}_k(D))\). By [[proofs/grh/upper-elementary-divisors/number-of-flags-bound|the bound on flags]] and the [[proofs/grh/upper-elementary-divisors/defect-of-steps|share of the cone in the slab]],
\[
[\mathrm{GL}_k(W):\mathrm{Par}_{a'}]\dim S\le\Bigl(\prod_{l<k}\tfrac{q^{l+1}-1}{q-1}\Bigr)\operatorname{vol}\bigl(\mathcal{K}(a,0)\cap\mathrm{Slab}_k(D)\bigr)=\operatorname{vol}\mathrm{Slab}_k(D).
\]
*Volume of the slab.* Write \(k=k'+1\). The set \(\{y\in\mathbb{R}_{\ge0}^{k'+1}:d-1\le\sum y\le d\}\), \(d\le B\), has volume at most \(B^{k'}/k'!\) (induction on \(k'\): slice along the first coordinate \(x\in[0,B]\) and integrate \((B-x)^{k'-1}/(k'-1)!\)). The slab is contained in a product of such sets over the letters, so with \(B=n+E\le e^{E/n}n\): \(\operatorname{vol}\mathrm{Slab}_k(D)\le e^{x}(n^{k'}/k'!)^{N}\), \(x=Nk'E/n\). The hypothesis gives \(2x\le2NkE/n\le\theta\le1\), so \(e^{x}\le1+2x\le1+\theta\) (\(0\le x\le1\)). Finally \(n^{k'}/k'!\le\binom{n+k'}{k'}\), the number of monomials of degree \(n\) in \(k\) variables, and \(\#\mathcal{E}(N,k,n)=\binom{n+k'}{k'}^{N}\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.index_mul_finrank_defectConditions_le`, `New.volume_degreeSlab_le`, `New.volume_sum_mem_Icc_le`, `New.pow_div_factorial_le_card_monomials` in `src/New/UpperBound/ElementaryDivisors/DefectCount.lean`.
2. Related work named in the head of the Lean file: Forrester–Zhang, Corank-1 projections and the randomised Horn problem, 2021 (after Dixon, 1905; Anderson, 1991); E. Bombieri, Counting points on curves over finite fields, Séminaire Bourbaki 430, 1973; A. Okounkov, Brunn–Minkowski inequality for multiplicities, 1996.
