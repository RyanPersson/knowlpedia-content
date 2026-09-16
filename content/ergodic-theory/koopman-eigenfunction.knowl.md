+++
id = "ergodic-theory/koopman-eigenfunction"
title = "Koopman eigenfunction"
kind = "definition"
summary = "A nonzero observable that changes by a fixed scalar phase under one step of the dynamics."
aliases = ["Koopman eigenvalue"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/koopman-operator"]
+++

A **Koopman eigenfunction** of an invertible [[ergodic-theory/measure-preserving-transformation|probability-preserving transformation]] is a nonzero \(f\in L^2(X,\mu)\) satisfying
\[
U_Tf=\lambda f,\qquad\text{that is, }f(Tx)=\lambda f(x)\text{ almost everywhere}.
\]
Unitarity forces \(|\lambda|=1\), and \(f(T^nx)=\lambda^nf(x)\).

## Ergodic systems

In an ergodic system, \(|f|\) is invariant and hence constant almost everywhere. Normalize it to one. Such an eigenfunction is a measurable circle-valued observable that extracts a rotation from the dynamics. Any two normalized eigenfunctions with the same eigenvalue have invariant product \(f\overline h\), so the eigenspace is one-dimensional.

Products and conjugates of normalized eigenfunctions are eigenfunctions with eigenvalues \(\lambda\eta\) and \(\overline\lambda\). Thus the eigenvalues of an ergodic system form a subgroup of the circle.

## References

1. Asgar Jamneshan and Henrik Kreidler, [*Ergodic Structure Theory and Applications*](https://ajamnesh.github.io/pdf/ISem28_notes.pdf), ISEM 28 lecture notes. §5.1.
