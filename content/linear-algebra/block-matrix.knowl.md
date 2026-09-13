+++
id = "linear-algebra/block-matrix"
title = "Block matrix"
kind = "definition"
summary = "A matrix partitioned into compatible rectangular submatrices."
aliases = ["diagonal block", "block diagonal matrix"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/matrix"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **block matrix** is a [[linear-algebra/matrix|matrix]] written as an array of rectangular submatrices after partitioning its row and column indices into groups. For example,
\[
M=\begin{pmatrix}A&B\\ C&D\end{pmatrix}.
\]
Compatible block partitions permit the usual addition and multiplication rules, with matrix products in place of scalar products. Blocks on the block diagonal, such as \(A,D\), are **diagonal blocks**; they need not themselves be diagonal matrices.

## Decoupling

If all off-diagonal blocks vanish, the matrix is block diagonal. Its action preserves the corresponding coordinate subspaces, and a differential system \(y'=My\) splits into those blocks. A small off-diagonal block instead describes coupling; it is not an exact invariant decomposition.
