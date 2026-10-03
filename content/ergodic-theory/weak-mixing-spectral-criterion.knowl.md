+++
id = "ergodic-theory/weak-mixing-spectral-criterion"
title = "Spectral characterization of weak mixing"
kind = "theorem"
summary = "Weak mixing is the absence of finite-dimensional invariant subspaces after constants are removed."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/weak-mixing", "ergodic-theory/reduced-koopman-representation", "ergodic-theory/koopman-eigenfunction"]
+++

For an invertible probability-preserving transformation \(T\), the following are equivalent:

1. \(T\) is weakly mixing.
2. Its reduced Koopman operator has no nonzero eigenvectors.
3. Its reduced Koopman representation has no nonzero finite-dimensional invariant subspaces.
4. Every [[ergodic-theory/koopman-spectral-measure|spectral measure]] of a mean-zero observable is atomless.

For a countable discrete group action, weak mixing is likewise equivalent to the absence of nonzero finite-dimensional invariant subspaces of the reduced Koopman representation. For a nonabelian group, checking only invariant lines is insufficient.

## Mechanism

If \(Uf=\lambda f\), then \(f(x)\overline{f(y)}\) is invariant for \(T\times T\). Conversely, the Hilbert tensor-product description of the product representation turns an invariant vector on the square into a compact intertwining operator; a nonzero eigenspace of its positive square yields a finite-dimensional invariant subspace. For one unitary operator, such a subspace has an eigenvector.

The equivalence with atomless spectral measures follows from the spectral projection at each singleton. The correlation formulation follows from Wiener's Fourier criterion for atoms.

## References

1. Jesse Peterson, [*Lecture notes on ergodic theory*](https://www.math.vanderbilt.edu/~peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf), 2011. §§1.7 and 2.2.2.
