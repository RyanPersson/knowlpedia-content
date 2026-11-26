+++
id = "proofs/grh/upper-elementary-divisors/halfway-forms-divisible-at-large-defect"
title = "Forms in all halfway lattices are divisible at monomials of large defect"
kind = "theorem"
summary = "A vector integral for the halfway lattices of all edges has block diagonal translates whose coefficient at a monomial of defect at least 3j along a root across the blocks is divisible by w^j; the same for the edge pairing with such monomials."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.pow_dvd_letterRep_mulVec_of_mem_allEdgesForms", "New.FrobeniusCycle.pow_add_dvd_of_le_defect", "New.FrobeniusCycle.allEdgesForms_le_defectConditions", "New.FrobeniusCycle.IsEdgePairing.pow_dvd_pairing_letterRep", "New.pow_sub_dvd_of_pow_dvd_pow_mul"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/Edges.lean"]
proof_status = "full"
+++

**Theorem.** Let \(O\) be an integral domain of characteristic \(0\) and \(T\) a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\), \(N\ge1\). Let \(a<r<k\) be indices (so \(a\) lies in the block \(\{b<r\}\) and \(r\) in the block \(\{b\ge r\}\)), and let \(\operatorname{def}_i=\operatorname{def}_{i,a,r}\) be the [[proofs/grh/upper-elementary-divisors/defect-of-monomial|defect]] along the root \((a,r)\). Let \(v\in\mathcal{A}(k,n,r)\) ([[proofs/grh/upper-elementary-divisors/edges-and-halfway-lattices|forms in all halfway lattices]]), and let \(g\in\mathrm{GL}_k(W)\) be block diagonal for \(\{b<r\},\{b\ge r\}\).

1. If \(\operatorname{def}_i(\beta)\ge3j\) for some letter \(i\) and \(j\in\mathbb{N}\), then \(w^{j}\mid(\rho_n(g)v)_\beta\).
2. For every \(c\in\mathbb{N}\), \(\mathcal{A}(k,n,r)\) is contained in the [[proofs/grh/upper-elementary-divisors/translate-conditions|defect conditions]] for the root \((a,r)\), the ideal \((w^{c})\) and the threshold \(h=3c^{*}\), \(c^{*}=3kc\).
3. If \((b,b')\) is an [[proofs/grh/upper-elementary-divisors/edge-pairing|edge pairing]] and \(\operatorname{def}_i(\beta)>c^{*}=3kc\) for some \(i\), then \(w^{c}\) divides \(\langle\rho_n(g)e_\beta,v\rangle_b=\sum_\alpha v_\alpha b_\alpha\rho_n(g)_{\alpha\beta}\).

## Proof

*Key step.* Let \(F\in O^{\mathcal{E}}\) and \(m\ge0\) with \(w^{m}\mid w^{\operatorname{depth}\delta}(\rho_n(\gamma)F)_\delta\) for all \(\gamma,\delta\). Then \(w^{m+j}\mid w^{\operatorname{depth}\beta}(\rho_n(\gamma)F)_\beta\) whenever \(\operatorname{def}_i(\beta)\ge3j\). Indeed, for the root \((a,r)\) the variable \(Y_s\) is deep and \(X_s\) is not, in every letter, so the weights \(\delta_r\) rise by \(1\) from \(X_s\) to \(Y_s\). Cancelling \(w^{\operatorname{depth}\delta}\) (\(w\ne0\) in the domain \(O\)), the hypothesis says that every translate of the form of \(\rho_n(\gamma)F\) lies in the [[proofs/grh/upper-elementary-divisors/gauss-filtration|Gauss level]] \(m\) for the weights \(\delta_r\). By [[proofs/grh/upper-elementary-divisors/large-defect-forces-divisibility|the theorem on large defect]] (only translates by the \(\mathrm{SL}_2\) of the root are needed), \((\rho_n(\gamma)F)_\beta\) is divisible by \(w^{e}\), \(e=\lceil m-\operatorname{depth}\beta+\tfrac13\operatorname{def}_i(\beta)\rceil_+\), and \(\operatorname{depth}\beta+e\ge m+j\).

(1) Let \(w^{m}v=\Delta h\) with \(w^{m}\mid\Delta\rho_n(\gamma)h\) for all \(\gamma\). As \(g\) is block diagonal, \(\rho_n(g)\) commutes with \(\Delta\) ([[proofs/grh/upper-elementary-divisors/parahoric-preserves-halfway-lattice|commutation]]), so \(w^{m}(\rho_n(g)v)_\beta=w^{\operatorname{depth}\beta}(\rho_n(g)h)_\beta\), which is divisible by \(w^{m+j}\) by the key step with \(F=h\). Cancel \(w^{m}\).

(2) If \(\operatorname{def}_i(\beta)>3c^{*}\ge 9c\) (note \(k\ge1\)), then (1) with \(j=c\) applies (\(3c\le c^{*}\)).

(3) The transpose \({}^tg\) is block diagonal, and by adjointness \(\sum_\alpha v_\alpha b_\alpha\rho_n(g)_{\alpha\beta}=b_\beta(\rho_n({}^tg)v)_\beta\). Since \(\operatorname{def}_i(\beta)>c^{*}\ge3c\), apply (1) to \({}^tg\) with \(j=c\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.pow_dvd_letterRep_mulVec_of_mem_allEdgesForms`, `New.FrobeniusCycle.pow_add_dvd_of_le_defect`, `New.FrobeniusCycle.allEdgesForms_le_defectConditions`, `New.FrobeniusCycle.IsEdgePairing.pow_dvd_pairing_letterRep`, `New.pow_sub_dvd_of_pow_dvd_pow_mul` in `src/New/UpperBound/ElementaryDivisors/Edges.lean`.
