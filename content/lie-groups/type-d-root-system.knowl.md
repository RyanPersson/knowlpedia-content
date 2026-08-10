+++
id = "lie-groups/type-d-root-system"
title = "Type D root system"
kind = "definition"
summary = "The simply laced root system D_n consisting of the vectors ±e_i±e_j in R^n."
aliases = ["type D root system", "D_n root system", "root system of type D"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

For \(n\geq4\), the **root system of type \(D_n\)** is
\[
D_n=\{\pm e_i\pm e_j:1\leq i<j\leq n\}\subset\mathbb R^n,
\]
where the two signs are chosen independently. It is an irreducible [[lie-groups/simply-laced-root-system|simply laced root system]] of rank \(n\), with \(2n(n-1)\) roots.

## Simple roots and diagram

One standard base is
\[
\alpha_i=e_i-e_{i+1}\quad(1\leq i<n),
\qquad
\alpha_n=e_{n-1}+e_n.
\]
The [[lie-groups/dynkin-diagram|Dynkin diagram]] is a chain that forks into two terminal vertices at one end. Its [[lie-groups/weyl-group|Weyl group]] consists of permutations of the coordinates together with sign changes of an even number of coordinates; it has order \(2^{n-1}n!\).

## Lie-algebra realization

Type \(D_n\) is the [[lie-groups/root-system|root system]] of the complex [[lie-groups/orthogonal-lie-algebra|orthogonal Lie algebra]]
\[
\mathfrak{so}_{2n}(\mathbb C),
\]
which has dimension \(n(2n-1)\). Thus \(D_n\) is the even-orthogonal family in the [[lie-groups/classification-simple-lie-algebras|classification of complex simple Lie algebras]].

## Low-rank coincidences

Extending the coordinate formula to small \(n\) gives reducible or coincident systems:
\[
D_2\cong A_1\sqcup A_1,
\qquad
D_3\cong A_3.
\]
The first genuinely new irreducible case is \(D_4\), whose diagram has an order-six symmetry responsible for triality.

## References

1. James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972, §§11–12. [Publisher record](https://doi.org/10.1007/978-1-4612-6398-2).
2. Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 4–6*, Springer, 2002, Chapter VI, §4. [Publisher record](https://link.springer.com/book/9783540691716).
3. John C. Baez, “Three Generations in \(E_7\),” 2026, §§5–6. [arXiv record](https://arxiv.org/abs/2608.06271).
