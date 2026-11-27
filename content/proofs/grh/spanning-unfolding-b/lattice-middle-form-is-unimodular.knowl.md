+++
id = "proofs/grh/spanning-unfolding-b/lattice-middle-form-is-unimodular"
title = "The form in the lattice basis is unimodular"
kind = "lemma"
summary = "The Gram matrix of the middle space in the lattice basis is hermitian with an integral inverse over every subring containing N, and the whole Gram matrix in the lattice basis is symmetric."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.isUnimodular_latticeMiddleGram", "New.Filling.isUnimodular_latticeMiddle", "New.Filling.transpose_splitGram", "New.frameImage_one_mulVec", "New.frameImage_mulVec", "New.exists_star_vecMul_eq"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
proof_status = "full"
+++

**Lemma.** Let \(A\) be a commutative ring with involution, \(R\subset A\) a subring, \((\varrho,\kappa,k_0)\) a shape and \(N\in R\) with \(\bar N=N\). Let \(T^{\mathrm{lat}}_N\) be the [[?lean:New.latticeMiddleGram|lattice middle Gram matrix]], indexed by \(\kappa\sqcup\{z\}\): diagonal entries \(1\) at \(i\in\kappa\setminus\{k_0\}\), \(0\) at \(k_0\), \(-N\) at \(z\); entries \(-1\) at \((k_0,z)\) and \((z,k_0)\); zero elsewhere. Then \(T^{\mathrm{lat}}_N\) is [[?lean:New.IsUnimodular|unimodular over \(R\)]]: it is hermitian, and it and its inverse have entries in \(R\).

In particular, for a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] \(S\) and any commutative ring \(F\) with involution, the lattice middle form of \(S\) over \(F\) is unimodular over every subring, the Gram matrix \(J^{\mathrm{lat}}\) of the whole space in the lattice basis is hermitian and invertible, and (for the trivial involution) it is symmetric.

## Proof

The inverse is \(T^{\mathrm{lat}}_0+N\,E_{k_0k_0}\), where \(E_{k_0k_0}\) is the matrix unit: on the complement of \(\{k_0,z\}\) both matrices are the identity, and on the plane indexed by \((k_0,z)\)
\[
\begin{pmatrix}0&-1\\-1&-N\end{pmatrix}\begin{pmatrix}N&-1\\-1&0\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}.
\]
All entries of both matrices are among \(0,\pm1,\pm N\), which lie in \(R\) and are fixed by the involution; since both matrices are symmetric, \(T^{\mathrm{lat}}_N\) is hermitian. For the filling datum, \(N\) is a natural number, hence lies in every subring and is fixed by every involution. The whole Gram matrix is built from \(T^{\mathrm{lat}}\) and identity blocks pairing \(e_a\) with \(e_a^*\), so it is hermitian and invertible as well; applying this with the trivial involution on \(F\) shows that it is symmetric.

## References

1. Lean: `New.isUnimodular_latticeMiddleGram`, `New.Filling.isUnimodular_latticeMiddle`, `New.Filling.transpose_splitGram` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`.
