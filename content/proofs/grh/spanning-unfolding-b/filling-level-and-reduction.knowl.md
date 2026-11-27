+++
id = "proofs/grh/spanning-unfolding-b/filling-level-and-reduction"
title = "Lattice stabiliser, reduction and principal level of a filling datum"
kind = "definition"
summary = "The integral subgroup K of the finite adelic unitary group, its reduction to the product of GL over the residue fields of the chosen places, the kernel K(M), and reduced images of subgroups."
aliases = ["principal level K(M)", "ResidueGL", "reduced image"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.latticeStabilizer", "New.Filling.ResidueGL", "New.Filling.reduction", "New.Filling.principalLevel", "New.Filling.reducedImage"]
lean_files = ["src/New/Spanning/Unfolding/Setup.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] with chosen places \(C_0,C_1\), and let \(G_{\mathrm{fin}}\) be its [[proofs/grh/spanning-unfolding-b/filling-unitary-groups|finite adelic unitary group in the lattice basis]]. Write \(\mathbb{F}_w\) for the [[algebra-commutative/residue-field|residue field]] at a finite place \(w\).

* The **lattice stabiliser** \(K\subset G_{\mathrm{fin}}\) is the subgroup of the elements \(g\) such that \(g\) and \(g^{-1}\) have all entries in the integral finite adeles \(\widehat{\mathcal{O}}\).
* The **residue group** is the finite group
\[
\bar G=\prod_{i\in\{0,1\}}\ \prod_{w\in C_i}\mathrm{GL}_r(\mathbb{F}_w),
\]
where \(\mathrm{GL}_r(\mathbb{F}_w)\) is the [[?c:General linear group|general linear group]] of matrices indexed by the basis of \(V\).
* The **reduction** \(K\to\bar G\), \(g\mapsto\bar g\), reduces the entries of \(g\) modulo each chosen place. It is a [[algebra-groups/group-homomorphism|group homomorphism]].
* The **principal level** \(K(M)\subset G_{\mathrm{fin}}\) is the [[?c:Kernel of a group homomorphism|kernel]] of the reduction.
* For a subgroup \(A\subset G_{\mathrm{fin}}\), the **reduced image** \(\bar A\subset\bar G\) is the image of \(A\cap K\) under the reduction.

## Remarks

The reduction takes no account of the unitary structure: the target is a product of full linear groups, one for each chosen place, and conjugate places are not chosen. By condition 4 of a filling datum, an integral adele vanishes modulo the chosen places and their conjugates exactly when \(M\) divides it, which is why the kernel is written \(K(M)\).

## References

1. Lean: `New.Filling.latticeStabilizer`, `New.Filling.ResidueGL`, `New.Filling.reduction`, `New.Filling.principalLevel`, `New.Filling.reducedImage` in `src/New/Spanning/Unfolding/Setup.lean`.
