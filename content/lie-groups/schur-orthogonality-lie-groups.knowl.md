+++
id = "lie-groups/schur-orthogonality-lie-groups"
title = "Schur orthogonality for compact Lie groups"
kind = "knowl"
summary = "Matrix coefficients of distinct irreducible unitary representations are orthogonal in L²(G), with a sharp normalization."
aliases = ["schur-orthogonality-lie-groups", "Schur orthogonality for compact Lie groups"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/schur-orthogonality-lie-groups.md"
+++

Let $G$ be a [[lie-groups/compact-lie-group|compact Lie group]] with normalized Haar measure $dg$. Let $(\pi,V)$ and $(\sigma,W)$ be finite-dimensional continuous irreducible unitary [[lie-groups/representation-of-a-lie-group|representations]] of $G$. Choose orthonormal bases, and denote the resulting matrix coefficients by $\pi_{ij}$ and $\sigma_{kl}$.

**Schur orthogonality** asserts:
$$
\int_G \pi_{ij}(g)\,\overline{\sigma_{kl}(g)}\,dg
\;=\;
\begin{cases}
\frac{1}{\dim V}\,\delta_{ik}\delta_{jl},
  & \text{if }\pi=\sigma\text{ and the same basis is used},\\[6pt]
0, & \text{if }\pi\not\simeq \sigma.
\end{cases}
$$
In the equivalent-but-not-identical case, the first formula holds after identifying $V$ and $W$ by a unitary intertwiner and transporting the chosen basis.

This is the analytic form of Schur’s lemma and a key input in the [[lie-groups/peter-weyl-theorem|Peter–Weyl theorem]], which decomposes $L^2(G)$ into finite-dimensional isotypic pieces.

## Equivalent characterizations
Equivalently, the matrix coefficients of irreducible unitary representations form an orthogonal family in $L^2(G)$; within one irreducible representation, their squared norm is $1/\dim V$.
