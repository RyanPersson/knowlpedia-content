+++
id = "discrete-structures/szemeredi-theorem"
title = "Szemerédi theorem"
kind = "theorem"
summary = "Every positive-density subset of the integers contains arithmetic progressions of arbitrary finite length."
aliases = ["Szemeredi theorem"]
domains = ["discrete-structures"]
section_mode = "progressive"
prerequisites = ["discrete-structures/upper-banach-density"]
+++

If \(E\subseteq\mathbb Z\) has positive [[discrete-structures/upper-banach-density|upper Banach density]], then for every \(k\geq1\) there exist integers \(a\) and \(r\geq1\) such that
\[
a,a+r,\ldots,a+kr\in E.
\]
In particular, the conclusion holds for a subset of \(\mathbb N\) with positive ordinary upper density. This is **Szemerédi's theorem**.

## Ergodic proof route

Use the [[ergodic-theory/furstenberg-correspondence-principle|correspondence principle]] to obtain an event of positive probability. [[ergodic-theory/furstenberg-multiple-recurrence|Multiple recurrence]] gives a positive intersection of its translates at \(0,r,\ldots,kr\). The correspondence inequality forces a nonempty intersection \(E\cap(E-r)\cap\cdots\cap(E-kr)\), and any element of it is the required starting point.

The common difference is positive, so the progression is nonconstant. Positive density is a sufficient hypothesis; many zero-density sets also contain long progressions.

## References

1. Asgar Jamneshan and Henrik Kreidler, [*Ergodic Structure Theory and Applications*](https://ajamnesh.github.io/pdf/ISem28_notes.pdf), ISEM 28 lecture notes. Theorem 1.1.8 and Lecture 10.
