+++
id = "ergodic-theory/number-field-torus"
title = "Number-field torus"
kind = "construction"
summary = "The compact additive quotient of the Archimedean algebra by its integral lattice."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/minkowski-embedding", "harmonic-analysis/haar-measure", "topology/flat-torus"]
+++

For a number field \(K\) of degree \(m\), the **number-field torus** is the compact additive group
\[
\mathbb T_K=K_\infty/\iota(\mathcal O_K).
\]
Its \(d\)-fold power is \(X=K_\infty^d/\iota(\mathcal O_K)^d\), a real torus of dimension \(md\), endowed with normalized [[harmonic-analysis/haar-measure|Haar measure]] and, when needed, the completed Borel sigma-algebra.

## Why all Archimedean embeddings are needed

The integral lattice has full real rank in \(K_\infty\). An integral basis identifies this quotient as a topological group with \((\mathbb R/\mathbb Z)^m\). These are quotients of additive groups; the integral lattice is not an ideal in the Archimedean algebra, so no quotient-ring structure is being asserted.

## Torsion points

Regard the additive torus as a \(\mathbb Z\)-module. Its [[algebra-modules/torsion-element|torsion elements]], called torsion points, are exactly the points killed by a nonzero integer.

The smaller quotient \(K/\mathcal O_K\cong(\mathbb Q/\mathbb Z)^m\) is exactly the torsion subgroup inside \(\mathbb T_K\): \(N[x]=0\) implies \(Nx\in\mathcal O_K\), hence \(x\in K\), and the converse follows by clearing denominators. Thus \(K/\mathcal O_K\) is not the full torus. An increment from \(K^d\) produces a periodic translation.

## References

1. J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), version 3.08, 2020. Chapter 4, lattice embedding; the quotient and torsion assertions follow from the displayed integral-basis calculation.
