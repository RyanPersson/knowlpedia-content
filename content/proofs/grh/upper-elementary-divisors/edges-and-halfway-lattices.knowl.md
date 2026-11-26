+++
id = "proofs/grh/upper-elementary-divisors/edges-and-halfway-lattices"
title = "Edges, normalised coefficients and forms in all halfway lattices"
kind = "definition"
summary = "The parahoric cosets indexing edges, the diagonal scaling by w to the depth that passes to the halfway lattice of an edge, and the module of coefficient vectors integral for the halfway lattices of all edges from a lattice."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.ParahoricCosets", "New.FrobeniusCycle.depthScaling", "New.FrobeniusCycle.allEdgesForms", "New.FrobeniusCycle.depthScaling_mulVec_mem_allEdgesForms", "New.FrobeniusCycle.depthScaling_eq_kroneckerPi", "New.monomialLattice", "New.dividedPowerLattice", "New.dividedPowerCoeff"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/Edges.lean"]
+++

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\) with \(N\ge1\), and let \(k,n,r\ge0\). Write \(w\) for the square root of \(p\) in \(O\), \(\rho_n\) for the [[proofs/grh/upper-elementary-divisors/twisted-action|twisted representation]] and \(\operatorname{depth}=\operatorname{depth}_r\) for the [[proofs/grh/upper-elementary-divisors/depth-of-monomial|depth]].

- **Edges.** Let \(\mathrm{Par}_r(W)\subseteq\mathrm{GL}_k(W)\) be the [[?lean:New.parahoric|parahoric subgroup]] for the two blocks \(\{b<r\}\), \(\{b\ge r\}\): the matrices whose entries \((i,j)\) with \(i<r\le j\) lie in the maximal ideal. The set of **edges** from the standard lattice is the set of left cosets \(\mathrm{GL}_k(W)/\mathrm{Par}_r(W)\). (Informally an edge is a pair of lattices \(L'\subseteq L\) with \(pL\subseteq L'\) and \(L/L'\) of dimension \(r\) over the residue field; \(L'\) is its origin, and \(\mathrm{Par}_r\) is the stabiliser of one edge. This interpretation is a comment in the source; only the cosets enter the statements.)
- **Depth scaling.** \(\Delta=\Delta_r\) is the diagonal matrix on \(O^{\mathcal{E}(N,k,n)}\) with entries \(w^{\operatorname{depth}(\beta)}\). It takes coefficients in the monomials \(x^{\beta}\) to coefficients in the **normalised monomials** \(w^{-\operatorname{depth}\beta}x^{\beta}\), which are regarded as a basis of the **halfway lattice** of the edge. \(\Delta=\bigotimes_s\operatorname{Sym}^n(\operatorname{diag}(w^{\delta_r(b,s)})_b)\).
- **Forms in all halfway lattices.** \(\mathcal{A}=\mathcal{A}(k,n,r)\subseteq O^{\mathcal{E}(N,k,n)}\) is the set of vectors \(v\) for which there are \(m\ge0\) and \(h\in O^{\mathcal{E}(N,k,n)}\) with
\[
w^{m}v=\Delta h\qquad\text{and}\qquad w^{m}\mid\bigl(\Delta\,\rho_n(g)\,h\bigr)_\beta\ \text{ for all }g\in\mathrm{GL}_k(W)\text{ and all }\beta .
\]
It is an \(O\)-submodule, and it contains \(\Delta h\) for every \(h\) (take \(m=0\)).

## Remarks

Two lattices of forms over an \(O\)-algebra \(K\) are also defined: \(H\), the \(O\)-span of the monomials \(x^{\beta}\), \(\beta\in\mathcal{E}(N,k,n)\), and \(H^{\circ}\subseteq H\), the \(O\)-span of the divided powers \(\frac{(n!)^{N}}{\beta!}x^{\beta}\), where \(\beta!=\prod_{s,b}\beta_s(b)!\) and \((n!)^{N}/\beta!=\prod_s\binom{n}{\beta_s}\). Both are stable under \(\mathrm{GL}_k(W)\); see [[proofs/grh/upper-elementary-divisors/lattices-of-forms-are-stable|stability]].

## References

1. Lean: `New.ParahoricCosets`, `New.FrobeniusCycle.depthScaling`, `New.FrobeniusCycle.allEdgesForms`, `New.FrobeniusCycle.depthScaling_mulVec_mem_allEdgesForms`, `New.FrobeniusCycle.depthScaling_eq_kroneckerPi`, `New.monomialLattice`, `New.dividedPowerLattice`, `New.dividedPowerCoeff` in `src/New/UpperBound/ElementaryDivisors/Edges.lean`.
