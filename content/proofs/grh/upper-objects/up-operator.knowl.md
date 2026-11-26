+++
id = "proofs/grh/upper-objects/up-operator"
title = "The operator Up at a split level"
kind = "definition"
summary = "The operator on a representation of GL at a split level that passes to the lattice enlarged by the marked vector divided by N and sums against psi_N."
aliases = ["Up operator", "operator Up"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsSplitLevel.upOperator", "New.IsSplitLevel.lastRowColGL", "New.IsSplitLevel.exists_GL_last_col_and_row", "New.IsSplitLevel.lastRowColGL_col_and_row", "New.IsSplitLevel.mirabolic_fix_upOperator", "New.IsSplitLevel.commute_upOperator", "New.IsSplitLevel.scalar_commute_upOperator"]
lean_files = ["src/New/UpperBound/Objects/LiftLawsModuloN.lean"]
+++

Let \(P\) be a [[proofs/grh/upper-objects/split-level|split level]] for \(N\) and let \(\pi\) be a complex [[algebra-representation-theory/group-representation|representation]] of the abstract group \(\mathrm{GL}_{n^+}(E_P)\) (no continuity is assumed). For every vector \(y\in((\mathbb Z/N)^P)^{n^+}\) whose last entry \(y_\ast\) is a unit, fix a matrix \(k_y\in\mathrm{GL}_{n^+}(\mathcal O_P)\) such that modulo \(N\) both the last column and the last row of \(k_y\) equal \(y\).

**Definition.** The **operator Up** on \(\pi\) is
\[
\mathrm{Up}=\pi(D_N)\sum_{y\,:\,y_\ast\ \mathrm{unit}}\psi_N(y_\ast)\,\pi(k_y),
\]
where \(D_N=\operatorname{diag}(1,\dots,1,N^{-1})\) and \(\psi_N\) is the character of the split level.

## Properties

1. *(Existence of \(k_y\).)* Over any commutative ring \(R\), a vector \(y\in R^{n^+}\) with unit last entry \(u\) is the last column and the last row of an invertible matrix.
2. If a vector \(\varphi\in\pi\) is fixed by the [[proofs/grh/upper-objects/mirabolic-subgroup-at-split-level|mirabolic subgroup]] \(\mathrm{Mir}_n\), then so is \(\mathrm{Up}\,\varphi\). In particular \(\mathrm{Up}\,\varphi\) does not depend on the choice of the matrices \(k_y\) for such \(\varphi\).
3. Every endomorphism of \(\pi\) commuting with all \(\pi(g)\) commutes with \(\mathrm{Up}\); in particular the scalar matrices \(x\cdot1\), \(x\in\mathcal O_P^\times\), commute with \(\mathrm{Up}\).

## Proof

*1.* Let \(A\) be the identity matrix with last column replaced by \(y\) and \(B\) the identity matrix with last row replaced by \(u^{-1}y\). Then \(\det A=u\), \(\det B=1\), and \(AB\) is invertible. The last column of \(B\) is \(e_\ast\), so the last column of \(AB\) is \(Ae_\ast=y\); the last row of \(A\) is \(u\,e_\ast^{\mathsf T}\), so the last row of \(AB\) is \(u\cdot u^{-1}y=y\). Applying this over \((\mathbb Z/N)^P\) and lifting through the surjection \(\mathrm{GL}_{n^+}(\mathcal O_P)\to\mathrm{GL}_{n^+}((\mathbb Z/N)^P)\) gives \(k_y\).

*2.* Let \(g\in\mathrm{Mir}_n\). By the properties of the mirabolic subgroup, \(k:=D_N^{-1}gD_N\) is integral invertible and the last row of \(\bar k\) is \(e_\ast\); hence \((\bar ky)_\ast=y_\ast\) for all \(y\), and \(y\mapsto\bar ky\) permutes the vectors with unit last entry. For such \(y\) the matrix
\[
(D_Nk_{\bar ky})^{-1}\,g\,(D_Nk_y)=k_{\bar ky}^{-1}\,k\,k_y
\]
is integral invertible and modulo \(N\) sends \(e_\ast\mapsto y\mapsto\bar ky\mapsto e_\ast\), so it lies in \(\mathrm{Mir}_n\) and fixes \(\varphi\). Therefore \(\pi(g)\pi(D_Nk_y)\varphi=\pi(D_Nk_{\bar ky})\varphi\), and
\[
\pi(g)\,\mathrm{Up}\,\varphi=\sum_y\psi_N(y_\ast)\,\pi(D_Nk_{\bar ky})\varphi=\sum_{y}\psi_N\big((\bar ky)_\ast\big)\pi(D_Nk_{\bar ky})\varphi=\mathrm{Up}\,\varphi .
\]
The same computation with \(g=1\) and two choices of \(k_y\) shows the independence.

*3.* \(\mathrm{Up}\) is a linear combination of products of operators \(\pi(g)\). \(\square\)

## Remarks

In terms of marked lattices, \(D_N\) replaces the standard lattice \(L\) by \(L^+=L+\mathcal O e_\ast/N\), and the sum runs over the primitive vectors with unit last entry, weighted by \(\psi_N\).

## References

1. Lean: `New.IsSplitLevel.upOperator`, `mirabolic_fix_upOperator`, `commute_upOperator` in `src/New/UpperBound/Objects/LiftLawsModuloN.lean`.
