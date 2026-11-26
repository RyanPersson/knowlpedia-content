+++
id = "proofs/grh/upper-elementary-divisors/levi-points-span-schur-algebra"
title = "Points of a Levi subgroup span its Schur algebra"
kind = "proposition"
summary = "If the residue field of the local ring W has at least d+k elements, the tensor powers of the points of a Levi subgroup of GL_k(W) span the Schur algebra of degree d."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Average.eq_top_of_schurMap_eq_leviMonomialValues", "New.Average.isHomogeneous_det_leviGeneric", "New.Average.leviGeneric_map_eval", "New.Average.schurMap_aeval"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean"]
proof_status = "full"
+++

**Proposition.** Let \(W\) be a [[algebra-commutative/local-ring|local ring]] whose residue field \(\kappa\) satisfies \(d+k\le\lvert\kappa\rvert\) (finite cardinality), \(\iota\colon W\to O\) a ring homomorphism, and \(\tau\) a labelling of \(\{0,\dots,k-1\}\). In the notation of the [[proofs/grh/upper-elementary-divisors/schur-algebra-of-levi|Schur algebra of \(L_\tau\)]], let \(V\subseteq O^{\mathcal{M}_d}\) be an \(O\)-submodule containing every \(c\) with \(S_d(c)=\iota(a)^{\otimes d}\) for some \(a\in L_\tau(W)\). Then \(V=O^{\mathcal{M}_d}\). In particular the operators \(\iota(a)^{\otimes d}\), \(a\in L_\tau(W)\), span the Schur algebra \(S_d(O^{\mathcal{M}_d})\) over \(O\).

## Proof

Apply the [[proofs/grh/upper-elementary-divisors/density-of-points-over-local-ring|density lemma]] with \(\sigma\) the set of the \(k^{2}\) entries, \(n=d\), and \(g=\det G_\tau\in W[X]\), which is homogeneous of degree \(k\) (each term of the Leibniz expansion is a product of \(k\) entries, each zero or a variable) and takes the value \(1\) at the identity matrix. It remains to see that for every point \(b\in W^{k\times k}\) with \(g(b)\in W^{\times}\) the vector \(c_b=(\iota(b^{\gamma}))_\gamma\) lies in \(V\). The matrix \(G_\tau(b)\) (the block part of \(b\), transposed) is invertible because its determinant \(g(b)\) is a unit, and vanishes off the blocks, so \(a:=G_\tau(b)\in L_\tau(W)\). Applying evaluation at \(\iota\circ b\) entrywise to \(G_\tau^{\otimes d}\) gives \(S_d(c_b)=\iota(G_\tau(b))^{\otimes d}=\iota(a)^{\otimes d}\). Hence \(c_b\in V\) by hypothesis. \(\square\)

## References

1. Lean: `New.Average.eq_top_of_schurMap_eq_leviMonomialValues`, `New.Average.isHomogeneous_det_leviGeneric`, `New.Average.leviGeneric_map_eval`, `New.Average.schurMap_aeval` in `src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean`.
2. J. A. Green, *Polynomial Representations of GL_n*, Lecture Notes in Mathematics 830, Springer, 1980; D. Benson and S. Doty, Schur–Weyl duality over finite fields, 2009 (cited in the head of the Lean file for the Schur algebra and its spanning by group elements).
