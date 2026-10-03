+++
id = "algebra-fields-galois/archimedean-trace-pairing"
title = "Archimedean trace pairing"
kind = "definition"
summary = "The real bilinear trace pairing on the Archimedean algebra of a number field."
aliases = []
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/archimedean-algebra", "algebra-fields-galois/trace-field"]
+++

On [[algebra-fields-galois/archimedean-algebra|\(K_\infty=\mathbb R^{r_1}\times\mathbb C^{r_2}\)]], define
\[
\operatorname{Tr}_\infty(x_1,\ldots,x_{r_1},z_1,\ldots,z_{r_2})
=\sum_jx_j+2\sum_j\operatorname{Re}z_j.
\]
The **Archimedean trace pairing** is the nondegenerate real bilinear form \((a,x)\mapsto\operatorname{Tr}_\infty(ax)\). On embedded field elements the trace agrees with \(\operatorname{Tr}_{K/\mathbb Q}\).

## It is not a Hermitian inner product

The complex-coordinate product is \(az\), without conjugation. In particular, \(2\operatorname{Re}(az)\) can be negative for \(a=z\). Nondegeneracy, rather than positive definiteness, is what identifies the dual lattice used in Fourier characters.

For vectors, write \(a\cdot x=\sum_{j=1}^d a_jx_j\) and pair by \(\operatorname{Tr}_\infty(a\cdot x)\).

## References

1. J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), version 3.08, 2020. Chapter 2, “Review of norms and traces.”
