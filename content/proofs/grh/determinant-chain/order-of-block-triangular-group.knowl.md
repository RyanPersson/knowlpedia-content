+++
id = "proofs/grh/determinant-chain/order-of-block-triangular-group"
title = "Order of a group of block triangular matrices"
kind = "lemma"
summary = "The group of invertible block upper triangular matrices with one block N and j blocks T has order the product of the orders of the diagonal blocks times a power of the order of the ring, with exponent independent of the ring."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_card_parabolic_blockNumber_eq", "New.card_parabolic_blockNumber_succ", "New.blockTriangular_fromBlocks_blockNumber_succ_iff"]
lean_files = ["src/New/Determinant/Chain/TriangleNorms.lean"]
proof_status = "full"
+++

Let \(N,T\) be finite index sets and \(j\ge0\). Let \(B_j=N\sqcup T\sqcup\dots\sqcup T\) (\(j\) copies of \(T\)), with the block number \(0\) on \(N\) and \(l\) on the \(l\)-th copy of \(T\). For a [[?c:Commutative ring|commutative ring]] \(R\) let \(P_j(R)\subset\mathrm{GL}_{B_j}(R)\) be the group of invertible matrices that are block upper triangular: the entry \((x,y)\) vanishes when the block number of \(x\) exceeds that of \(y\) (the [[?lean:New.parabolic|parabolic subgroup]] of the block numbering).

**Lemma.** There is an integer \(k\ge0\), depending only on \(\#N,\#T,j\), such that for every commutative ring \(R\) (in a fixed universe)
\[
\#P_j(R)=\#\mathrm{GL}_N(R)\cdot\big(\#\mathrm{GL}_T(R)\big)^{j}\cdot(\#R)^{k}.
\]
Cardinalities are natural numbers, with the convention that an infinite set has cardinality \(0\).

## Proof

Induction on \(j\). For \(j=0\) there is one block, every matrix is block triangular, \(P_0(R)=\mathrm{GL}_N(R)\) and \(k=0\).

Write a matrix indexed by \(B_{j+1}=B_j\sqcup T\) in blocks \(\begin{pmatrix}A&B\\C&D\end{pmatrix}\). It is block upper triangular for \(B_{j+1}\) if and only if \(A\) is block upper triangular for \(B_j\) and \(C=0\): the rows of the last copy of \(T\) have the greatest block number \(j+1\), exceeded by no column and attained only on the last copy of \(T\). A matrix \(\begin{pmatrix}A&B\\0&D\end{pmatrix}\) is invertible if and only if \(A\) and \(D\) are. Hence \(u\mapsto(A,B,D)\) is a bijection
\[
P_{j+1}(R)\;\longrightarrow\;P_j(R)\times M_{B_j\times T}(R)\times\mathrm{GL}_T(R),
\]
and \(\#P_{j+1}(R)=\#P_j(R)\cdot(\#R)^{\#B_j\cdot\#T}\cdot\#\mathrm{GL}_T(R)\). With the induction hypothesis the claim holds with \(k_{j+1}=k_j+\#B_j\cdot\#T\). \(\blacksquare\)

## References

1. Lean: `New.exists_card_parabolic_blockNumber_eq` in `src/New/Determinant/Chain/TriangleNorms.lean`.
2. Lean: `New.card_parabolic_blockNumber_succ` in `src/New/Determinant/Chain/TriangleNorms.lean`.
3. Lean: `New.blockTriangular_fromBlocks_blockNumber_succ_iff` in `src/New/Determinant/Chain/TriangleNorms.lean`.
