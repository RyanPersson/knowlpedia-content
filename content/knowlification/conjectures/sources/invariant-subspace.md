Let \(H\) be a complex separable Hilbert space and let \(T:H\to H\) be a bounded linear operator. A linear subspace \(M\subseteq H\) is invariant under \(T\) when \(T(M)\subseteq M\). It is nontrivial when \(M\ne\{0\}\) and \(M\ne H\), and it is closed when it contains the limits of all convergent sequences of its points.

The closedness condition matters because an arbitrary invariant linear span may be too small analytically, while a closed subspace is itself a Hilbert space. Equivalently, a closed subspace is the range of an orthogonal projection.

## Open problem

If \(H\) is an infinite-dimensional complex separable Hilbert space, must every bounded linear operator \(T:H\to H\) have a nontrivial closed invariant subspace?

In symbols, must there exist a closed linear subspace \(M\) such that
\[
\{0\}\subsetneq M\subsetneq H
\qquad\text{and}\qquad
T(M)\subseteq M?
\]

An eigenvector immediately supplies such a subspace through its one-dimensional span, so the hard case includes operators without eigenvectors. The problem is specifically about Hilbert spaces over \(\mathbb C\); changing the ambient category changes the answer.

## Known boundary

Finite-dimensional complex operators have invariant subspaces by the existence of eigenvalues. Important operator classes, including normal operators, also have invariant subspaces. For general Banach spaces the corresponding assertion is false, so Hilbert-space geometry is essential.

## Formal source

This page follows `FormalConjectures/Wikipedia/InvariantSubspaceProblem.lean`, including separability, complex scalars, bounded linearity, closedness, and nontriviality.
