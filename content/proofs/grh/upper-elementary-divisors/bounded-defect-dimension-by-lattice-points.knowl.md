+++
id = "proofs/grh/upper-elementary-divisors/bounded-defect-dimension-by-lattice-points"
title = "Forms of bounded defect are counted by flags and lattice points"
kind = "proposition"
summary = "For m a power of q, m^(kN) times the dimension of the forms of bounded defect is at most the number of flags of the Levi subgroup times the number of points of (1/m)Z^(kN) in the Pieri cone cut by a slab; in the limit the count becomes a volume."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.finrank_defectConditions_mul_pow_le", "New.FrobeniusCycle.div_mem_defectCone_inter_degreeSlab", "New.FrobeniusCycle.exists_finrank_defectConditions_le_volume"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/DefectCount.lean"]
proof_status = "full"
+++

**Proposition.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,K)\), \(N\ge1\), \(K\) a field of characteristic \(p\). Let \(a'=a+1<k\), \(n\ge0\), and \(t\in\mathbb{N}\) with \(t\ge2(k+1)\). Let \(L\) be the block diagonal subgroup of \(\mathrm{GL}_k(W)\) with blocks of sizes \(a',k-a'\), let \(\phi=[L:L\cap\mathrm{Iw}^{-}]\), and let \(S\) be the space of the [[proofs/grh/upper-elementary-divisors/translate-conditions|defect conditions]] for the root \((a,a')\), the zero ideal and the threshold \(3t\).

1. Let \(\sigma\) be as in [[proofs/grh/upper-elementary-divisors/integral-shift-into-pieri-cone|the integral shift]], \(D_s=n+k+1+4t\sum_b\sigma(b,s)\), \(Y=\mathcal{K}(a,0)\cap\mathrm{Slab}_k(D)\), and \(m=q^{j}\). Then
\[
\dim_KS\cdot m^{kN}\le\phi\cdot\#\bigl(Y\cap m^{-1}\mathbb{Z}^{k\times\mathbb{Z}/N}\bigr).
\]
2. There is \(D\colon\mathbb{Z}/N\to\mathbb{R}\) with \(1\le D_s\le n+4tP^{2a'}\) and \(\dim_KS\le\phi\cdot\operatorname{vol}\bigl(\mathcal{K}(a,0)\cap\mathrm{Slab}_k(D)\bigr)\).

## Proof

(1) Let \(R\subseteq L\) be a set of representatives as in [[proofs/grh/upper-elementary-divisors/least-height-term-at-a-flag|the lemma on least height]], \(\#R=\phi\), and \(\Lambda=Y\cap m^{-1}\mathbb{Z}^{kN}\) (finite, \(Y\) being bounded). For \(y\in\Lambda\) let \(e(y)\) be the exponent \(\max(m(y-4t\sigma),0)\) (entrywise; integral). Define the linear map
\[
\Phi\colon S^{\{\text{classes mod }m\}}\to K^{R\times\Lambda},\qquad\Phi(F)_{x,y}=\text{coefficient of }x^{e(y)}\text{ in }x\cdot\operatorname{pack}(F),
\]
with the [[proofs/grh/upper-elementary-divisors/power-packing|packing]]. There are \(m^{kN}\) classes, so it suffices to show \(\Phi\) injective. Let \(F\ne0\); then \(\operatorname{pack}(F)\ne0\), and the least-height lemma gives \(x\in R\) and \(\alpha\) occurring in \(x\cdot\operatorname{pack}(F)\) with defect \(\le0\) along the simple roots inside the two blocks, i.e. all simple roots except \((a,a')\). By the properties of the packing, \(\alpha/m\) has degrees in \([n+k,n+k+1]\) and \(\operatorname{def}_{i,a,a'}(\alpha/m)\le3t+2(k+1)\le4t\); so \(\alpha/m\in\mathcal{K}(a,4t)\cap\mathrm{Slab}_k(n+k+1)\). By the shift lemma, \(y=4t\sigma+\alpha/m\in Y\), and \(y\in m^{-1}\mathbb{Z}^{kN}\) as \(\sigma\) is integral; \(e(y)=\alpha\). Hence \(\Phi(F)_{x,y}\ne0\).

(2) With \(\sigma\) and \(D\) as in (1): \(1\le D_s\) and \(D_s\le n+k+1+4t(P^{2a'}-1)\le n+4tP^{2a'}\) since \(k+1\le t\). The set \(Y\) is bounded, measurable and convex, so its boundary is a null set, and therefore \(\#(Y\cap m^{-1}\mathbb{Z}^{kN})/m^{kN}\to\operatorname{vol}(Y)\) as \(m\to\infty\) ([[?c:Lattice point count of a Jordan measurable set|lattice point count]]). Apply (1) along \(m=q^{j}\), \(j\to\infty\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.finrank_defectConditions_mul_pow_le`, `New.FrobeniusCycle.div_mem_defectCone_inter_degreeSlab`, `New.FrobeniusCycle.exists_finrank_defectConditions_le_volume` in `src/New/UpperBound/ElementaryDivisors/DefectCount.lean`.
2. Lean (library part of the development): `tendsto_card_div_pow_atTop_volume`, the lattice point count used in part 2.
3. Related work named in the head of the Lean file: Forrester–Zhang, Corank-1 projections and the randomised Horn problem, 2021 (after Dixon, 1905; Anderson, 1991); E. Bombieri, Counting points on curves over finite fields, Séminaire Bourbaki 430, 1973; A. Okounkov, Brunn–Minkowski inequality for multiplicities, 1996.
