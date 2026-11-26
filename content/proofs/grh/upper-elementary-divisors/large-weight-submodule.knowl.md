+++
id = "proofs/grh/upper-elementary-divisors/large-weight-submodule"
title = "Large weight submodule of a tensor power"
kind = "definition"
summary = "The submodule of the d-th tensor power generated under the Schur algebra of a Levi subgroup by the basis tensors of weight above a threshold; it is stable and free."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Average.largeWeightSubmodule", "New.Average.tensorOrbit", "New.Average.largeWeightRep", "New.Average.schurMap_mem_largeWeightSubmodule", "New.Average.largeWeightSubmodule_le_of_forall_leviMonomialValues", "New.Average.free_largeWeightSubmodule"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean"]
+++

In the notation of the [[proofs/grh/upper-elementary-divisors/schur-algebra-of-levi|Schur algebra of \(L_\tau\)]], let \(\rho\in\mathbb{Z}^{k}\) and \(t\in\mathbb{Z}\). The **weight** of a basis tensor \(e_j\in U_d\) is \(\sum_{l=1}^{d}\rho_{j_l}\). The **large weight submodule** is the \(O\)-[[algebra-modules/submodule|submodule]]
\[
U_+=U_+(\tau,\rho,t,d)=\sum_{j:\ \sum_l\rho_{j_l}>t}\ S_d\bigl(O^{\mathcal{M}_d}\bigr)\,e_j\ \subseteq U_d .
\]

## Properties

Let \(W\) be a local ring whose residue field has at least \(d+k\) elements (finite cardinality) and \(\iota\colon W\to O\) a ring homomorphism.

1. *Generation by group elements.* If a submodule \(N\subseteq U_d\) contains \(\iota(a)^{\otimes d}e_j\) for all \(a\in L_\tau(W)\) and all \(j\) of weight \(>t\), then \(U_+\subseteq N\). (For fixed \(j\), the set of \(c\) with \(S_d(c)e_j\in N\) is a submodule containing all \(c\) with \(S_d(c)=\iota(a)^{\otimes d}\); apply [[proofs/grh/upper-elementary-divisors/levi-points-span-schur-algebra|spanning by points]].)
2. *Stability.* Every \(S_d(c)\) maps \(U_+\) into itself. (The set of \(c\) with \(S_d(c)U_+\subseteq U_+\) is a submodule; by spanning it suffices to take \(S_d(c)=\iota(a)^{\otimes d}\), and by 1 it suffices that \(\iota(a)^{\otimes d}\iota(a')^{\otimes d}e_j=\iota(aa')^{\otimes d}e_j\in U_+\), which holds by definition.) Thus the Schur algebra acts on \(U_+\).
3. *Freeness.* If \(O\) is a valuation ring and a domain, \(U_+\) is a finitely generated torsion-free module over \(O\), hence [[algebra-modules/free-module|free]] of finite rank (finitely generated torsion-free modules over a valuation domain are free).

## References

1. Lean: `New.Average.largeWeightSubmodule`, `New.Average.tensorOrbit`, `New.Average.largeWeightRep`, `New.Average.schurMap_mem_largeWeightSubmodule`, `New.Average.largeWeightSubmodule_le_of_forall_leviMonomialValues`, `New.Average.free_largeWeightSubmodule` in `src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean`.
