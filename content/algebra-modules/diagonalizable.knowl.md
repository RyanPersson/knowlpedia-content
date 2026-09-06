+++
id = "algebra-modules/diagonalizable"
title = "Diagonalizable operator"
kind = "knowl"
summary = "A linear operator that has a basis of eigenvectors."
aliases = ["diagonalizable", "Diagonalizable operator"]
domains = ["algebra-modules"]
prerequisites = ["linear-algebra/linear-map", "linear-algebra/vector-space", "linear-algebra/eigenvector", "convex-analysis/basis-hamel-basis-and-dimension"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "algebra-modules/diagonalizable.md"
+++


A [[linear-algebra/linear-map|linear operator]] \(T:V\to V\) on a finite-dimensional [[linear-algebra/vector-space|vector space]] \(V\) over a field \(K\) is **diagonalizable over \(K\)** if \(V\) has a basis consisting of [[linear-algebra/eigenvector|eigenvectors]] of \(T\).

## Equivalent characterizations

Equivalently, \(T\) is diagonalizable iff its [[algebra-modules/matrix-representation|matrix representation]] in some basis is diagonal.

The following are also equivalent:

1. \(T\) is diagonalizable.
2. \(V = \bigoplus_{\lambda} E_\lambda\) where \(E_\lambda\) is the eigenspace for eigenvalue \(\lambda\).
3. The sum of geometric multiplicities equals \(\dim V\).
4. The [[linear-algebra/minimal-polynomial|minimal polynomial]] of \(T\) splits into distinct linear factors.

## Criteria

If the [[linear-algebra/characteristic-polynomial|characteristic polynomial]] splits over \(K\) and has distinct roots, then \(T\) is diagonalizable. More generally, when the characteristic polynomial splits over \(K\), \(T\) is diagonalizable if and only if each eigenvalue's geometric multiplicity equals its algebraic multiplicity.

## Examples
- Any operator with \(n\) distinct eigenvalues (where \(\dim V = n\)).
- Self-adjoint operators on finite-dimensional real or complex inner product spaces.
- Projections.

## Non-example

The matrix \(\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}\) is not diagonalizable (only one eigenvector).
