+++
id = "functional-analysis/spectral-theorem-unitary-operator"
title = "Spectral theorem for a unitary operator"
kind = "theorem"
summary = "A unitary operator is the integral of the circle coordinate against a unique projection-valued measure."
aliases = []
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/unitary-operator", "functional-analysis/projection-valued-measure", "functional-analysis/spectral-integral"]
+++

For a unitary operator \(U\) on a complex Hilbert space \(H\), there is a unique normalized [[functional-analysis/projection-valued-measure|projection-valued measure]] \(E\) on the Borel sets of \(\mathbb S^1=\{z:|z|=1\}\) such that
\[
U=\int_{\mathbb S^1}z\,dE(z),\qquad
U^n=\int_{\mathbb S^1}z^n\,dE(z)\quad(n\in\mathbb Z).
\]
Moreover, \(E(\{\lambda\})\) projects onto \(\ker(U-\lambda I)\).

## Eigenvectors need not span

The measure may have a continuous part. Thus spectral resolution is more general than diagonalization in an eigenvector basis. Applied to a Koopman operator, it resolves the possible temporal frequencies of observables.

## Averaging

The mean ergodic projection is \(E(\{1\})\): the scalar averages \(N^{-1}\sum_{n=0}^{N-1}z^n\) converge to \(1\) at \(z=1\) and to \(0\) otherwise. Dominated convergence for the scalar spectral measures gives the Hilbert-space limit.

## References

1. [*The Spectral Theorem*](https://math.berkeley.edu/~ltomczak/notes/SpecThm.pdf), UC Berkeley-hosted notes, p. 1, spectral theorem (ii)–(iii). Apply the normal-operator theorem to a unitary, whose spectrum lies on the unit circle.
