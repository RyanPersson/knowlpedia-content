+++
id = "ergodic-theory/furstenberg-multiple-recurrence"
title = "Furstenberg multiple recurrence theorem"
kind = "theorem"
summary = "A positive-probability event has a simultaneous return along arbitrarily long arithmetic progressions of times."
aliases = ["multiple recurrence theorem"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-system", "measure-theory/indicator-function"]
+++

For a [[ergodic-theory/measure-preserving-system|probability-preserving transformation]] \(T\), a measurable set \(A\) with \(\mu(A)>0\), and any integer \(k\geq1\), there exists \(n\geq1\) such that
\[
\mu(A\cap T^{-n}A\cap T^{-2n}A\cap\cdots\cap T^{-kn}A)>0.
\]
This is **Furstenberg's multiple recurrence theorem**. Ergodicity is not required, and the statement also holds for noninvertible transformations.

## Koopman formulation

For forward composition \(Uf=f\circ T\), the measure above equals
\[
\int_X\prod_{j=0}^{k}U^{jn}1_A\,d\mu.
\]
This is a multiple correlation, involving products of evolved observables. Ordinary two-function correlations alone do not capture this statement.

## Arithmetic application

The [[ergodic-theory/furstenberg-correspondence-principle|correspondence principle]] turns positive density in the integers into positive probability in a shift system. Multiple recurrence then yields [[discrete-structures/szemeredi-theorem|Szemerédi's theorem]] on arithmetic progressions.

## References

1. Asgar Jamneshan and Henrik Kreidler, [*Ergodic Structure Theory and Applications*](https://ajamnesh.github.io/pdf/ISem28_notes.pdf), ISEM 28 lecture notes. Theorem 1.1.7 and Lecture 10.
