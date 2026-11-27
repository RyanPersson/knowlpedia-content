+++
id = "proofs/grh/upper-elementary-divisors/edge-conditions"
title = "Conditions on an edge"
kind = "theorem"
summary = "Under large degree there are a module C of congruence conditions modulo w^c containing the forms in all halfway lattices, an averaging map with values in C preserving the pairing up to p^(N c_0), and a small space S containing the reductions of the vectors h with w^(c-1) h in C."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.IsEdgeCondition", "New.FrobeniusCycle.exists_isEdgeCondition", "New.FrobeniusCycle.mem_translatesIn_of_pow_smul_mem", "New.FrobeniusCycle.sqrtPrime_mem_maximalIdeal", "New.FrobeniusCycle.charP_residueField"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean"]
proof_status = "full"
+++

Let \(O\) be a valuation ring and a domain with residue field \(\bar O\), \(T\) a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\), \(N\ge1\), and \(r,c\in\mathbb{N}\), \(\theta\in\mathbb{R}\), \(b\in O^{\mathcal{E}}\) (\(\mathcal{E}=\mathcal{E}(N,k,n)\)); put \(c_0=k^{2}fN\), where \(P=p^{f}\). A triple \((C,S,\mathrm{Av})\) of an \(O\)-submodule \(C\subseteq O^{\mathcal{E}}\), an \(\bar O\)-subspace \(S\subseteq\bar O^{\mathcal{E}}\) and a matrix \(\mathrm{Av}\in M_{\mathcal{E}}(O)\) is an **edge condition** for \((r,c,\theta,b)\) if

1. \(\mathcal{A}(k,n,r)\subseteq C\) ([[proofs/grh/upper-elementary-divisors/edges-and-halfway-lattices|forms in all halfway lattices]]);
2. \(w^{c}h\in C\) for all \(h\);
3. \(\mathrm{Av}\,h\in C\) for all \(h\);
4. \(\langle\mathrm{Av}\,h,h'\rangle_b\equiv p^{Nc_0}\langle h,h'\rangle_b\pmod{w^{c}}\) for all \(h\) and all \(h'\in\mathcal{A}(k,n,r)\);
5. if \(w^{\max(c-1,0)}h\in C\), then the reduction of \(h\) lies in \(S\);
6. \([\mathrm{GL}_k(W):\mathrm{Par}_r(W)]\cdot\dim_{\bar O}S\le(1+\theta)\,\#\mathcal{E}\).

**Theorem.** Assume moreover that \(O\) has characteristic \(0\), \(p\) is not a unit of \(O\), the degree is [[proofs/grh/upper-elementary-divisors/large-degree-conditions|large]] for \((k,n,r,\theta)\), and \((b,b')\) is an [[proofs/grh/upper-elementary-divisors/edge-pairing|edge pairing]]. Then an edge condition for \((r,c,\theta,b)\) exists with \(c=5Nc_0\) the congruence precision.

## Proof

Let \(a=r-1\) (so \(a<r<k\), as \(0<r\le k/2\)), \(c^{*}=3kc\); \(c>0\) since \(Nc_0\ge2\). Take

- \(C\): the [[proofs/grh/upper-elementary-divisors/translate-conditions|defect conditions]] over \(O\) for the root \((a,r)\), the ideal \((w^{c})\) and the threshold \(3c^{*}\);
- \(S\): the defect conditions over \(\bar O\) (for the base-changed cycle) for the root \((a,r)\), the zero ideal and the threshold \(3c^{*}\);
- \(\mathrm{Av}\): the matrix of [[proofs/grh/upper-elementary-divisors/averaging-map|the averaging map]], which applies because \(N=2\ell\) and \(Nk(\ell+2)n+n+k<P^{\ell}\) ([[proofs/grh/upper-elementary-divisors/consequences-of-large-degree|consequences of large degree]], 3).

Then 3 and 4 are the two properties of the averaging map; 1 is part 2 of [[proofs/grh/upper-elementary-divisors/halfway-forms-divisible-at-large-defect|the divisibility at large defect]]; 2 is clear, as \(\rho_n(g)(w^{c}h)=w^{c}\rho_n(g)h\). For 5: if \(w^{c-1}h\in C\), then for block diagonal \(g\) and \(\beta\) of defect \(>3c^{*}\), \(w^{c}\mid w^{c-1}(\rho_n(g)h)_\beta\), so \(w\mid(\rho_n(g)h)_\beta\) (cancel \(w^{c-1}\ne0\)); \(w\) lies in the maximal ideal because \(w^{2}=p\) is not a unit; hence the reduction of \(\rho_n(g)h\) vanishes at \(\beta\), and reduction commutes with \(\rho_n\). For 6: \(\bar O\) has characteristic \(p\), so the theorem that [[proofs/grh/upper-elementary-divisors/few-forms-of-bounded-defect|few forms have bounded defect]] applies with \(a'=r\), \(t=c^{*}\): its hypotheses are \(n>0\), \(c^{*}\ge3k\ge2(k+1)\) (as \(k\ge2\), \(c\ge1\)), \(\theta\le1\) and \(8Nkc^{*}P^{2r}\le\theta n\) (consequences of large degree, 6). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.IsEdgeCondition`, `New.FrobeniusCycle.exists_isEdgeCondition`, `New.FrobeniusCycle.mem_translatesIn_of_pow_smul_mem`, `New.FrobeniusCycle.sqrtPrime_mem_maximalIdeal`, `New.FrobeniusCycle.charP_residueField` in `src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean`.
