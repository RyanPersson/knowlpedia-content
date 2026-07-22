Let \(H=\mathbb C^d\). A normalized state vector is a vector \(\psi\in H\) with \(\lVert\psi\rVert=1\). It determines the rank-one orthogonal projector \(\Pi_\psi=|\psi\rangle\langle\psi|\).

A positive operator-valued measure (POVM) with finitely many outcomes is a family of positive semidefinite operators \((E_i)\) on \(H\) satisfying \(\sum_iE_i=I\). It is symmetric informationally complete when it has \(d^2\) rank-one outcomes with equal pairwise Hilbert–Schmidt overlaps. In vector form, this asks for normalized vectors \(\psi_1,\ldots,\psi_{d^2}\) such that
\[
|\langle\psi_i,\psi_j\rangle|^2=\frac1{d+1}\qquad(i\ne j).
\]
Then \(E_i=\Pi_{\psi_i}/d\) form a POVM. The vectors are defined only up to phase; geometrically, they determine \(d^2\) equiangular complex lines.

## Conjecture

For every integer \(d\ge1\), a SIC-POVM exists in \(\mathbb C^d\). Equivalently, every finite complex dimension admits \(d^2\) normalized vectors with the overlap relation above.

“Informationally complete” means that the outcome probabilities \(\operatorname{Tr}(\rho E_i)\) determine every density operator \(\rho\). Symmetry makes the reconstruction especially uniform.

## Known boundary

Exact and numerical constructions are known in many dimensions, but no proof covers all positive integers. The formal source records direct low-dimensional examples and leaves the universal existence statement open.

## Formal source

This page follows `FormalConjectures/OpenQuantumProblems/23.lean`, whose primary predicate uses normalized state vectors and constant pairwise squared overlaps.
