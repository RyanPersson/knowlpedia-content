+++
id = "ergodic-theory/discrete-spectrum"
title = "Discrete spectrum of a dynamical system"
kind = "definition"
summary = "The property that Koopman eigenfunctions span the full space of square-integrable observables."
aliases = ["pure point dynamical spectrum"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/koopman-eigenfunction", "linear-algebra/orthonormal-basis"]
+++

An invertible probability-preserving transformation has **discrete spectrum**, or **pure point spectrum**, if the closed linear span of its [[ergodic-theory/koopman-eigenfunction|Koopman eigenfunctions]] is all of \(L^2(X,\mu)\). Equivalently, \(L^2\) has an orthonormal basis of Koopman eigenfunctions.

## Examples

Finite permutations and translations on compact metrizable abelian groups have discrete spectrum. A nontrivial weakly mixing probability-preserving system cannot have discrete spectrum: after removing constants it has no eigenfunctions.

## Terminology

“Discrete” here describes spectral measures and the existence of an eigenfunction basis. It does not say that the eigenvalues form a discrete subset of the circle. The eigenvalues of an irrational rotation are dense there.

## References

1. Asgar Jamneshan and Henrik Kreidler, [*Ergodic Structure Theory and Applications*](https://ajamnesh.github.io/pdf/ISem28_notes.pdf), ISEM 28 lecture notes. §6.1.
