+++
id = "ergodic-theory/furstenberg-correspondence-principle"
title = "Furstenberg correspondence principle"
kind = "theorem"
summary = "Positive upper Banach density can be modeled by an event in a probability-preserving shift system."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["discrete-structures/upper-banach-density", "ergodic-theory/measure-preserving-system"]
+++

For \(E\subseteq\mathbb Z\), there exist an invertible [[ergodic-theory/measure-preserving-system|probability-preserving system]] \((X,\mu,T)\) and a measurable event \(A\) with \(\mu(A)=d^*(E)\) such that, for every finite list \(n_1,\ldots,n_k\in\mathbb Z\),
\[
\mu(A\cap T^{-n_1}A\cap\cdots\cap T^{-n_k}A)
\leq d^*\bigl(E\cap(E-n_1)\cap\cdots\cap(E-n_k)\bigr).
\]
Here \(E-n=\{m:m+n\in E\}\).

## Construction

Encode \(E\) by its binary indicator sequence in \(\{0,1\}^{\mathbb Z}\). On the closure of its shift orbit, average point masses over intervals where the density approaches \(d^*(E)\), and take a weak limit. Boundary terms vanish relative to interval length, so the limit is shift invariant. The coordinate event \(x_0=1\) gives \(A\); finite-coordinate intersections give the inequality.

## Scope

This version preserves the density exactly but does not promise an ergodic model. It is sufficient for arithmetic recurrence because the multiple recurrence theorem does not require ergodicity.

## References

1. Asgar Jamneshan and Henrik Kreidler, [*Ergodic Structure Theory and Applications*](https://ajamnesh.github.io/pdf/ISem28_notes.pdf), ISEM 28 lecture notes. Theorem 4.2.9, specialized to interval averages in the integers.
