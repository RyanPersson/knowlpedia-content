+++
id = "lie-groups/global-cartan-decomposition"
title = "Global Cartan decomposition"
kind = "theorem"
summary = "The decomposition of a real reductive group as K exp(p), refined to the KAK decomposition."
aliases = ["KAK decomposition", "polar decomposition of G"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/real-reductive-lie-group", "lie-groups/cartan-decomposition-real-reductive-lie-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[lie-groups/real-reductive-lie-group|real reductive Lie
group]], let \(K\) be the fixed subgroup of a global Cartan involution, and let
\(\mathfrak g=\mathfrak k\oplus\mathfrak p\) be the associated
[[lie-groups/cartan-decomposition-real-reductive-lie-algebra|Cartan
decomposition]]. The **global Cartan decomposition** states that
\[
K\times\mathfrak p\longrightarrow G,\qquad (k,X)\longmapsto k\exp X,
\]
is a diffeomorphism. If \(\mathfrak a\subseteq\mathfrak p\) is maximal
abelian and \(\overline{\mathfrak a^+}\) is a closed positive Weyl chamber,
then every \(g\in G\) can be written
\[
g=k_1\exp(H)k_2,\qquad
k_1,k_2\in K,\quad H\in\overline{\mathfrak a^+}.
\]
This refinement is the **\(KAK\) decomposition**.

## Uniqueness

The polar coordinates \(g=k\exp X\) are unique. In a \(KAK\) expression the
two compact factors need not be unique, but the chamber element \(H\) is
unique. Without restricting \(H\) to a closed chamber, its orbit under the
[[lie-groups/restricted-weyl-group|restricted Weyl group]] is the invariant
datum.

## Geometric meaning

The decomposition identifies \(G/K\) with \(\mathfrak p\) by
\(X\mapsto\exp(X)K\), providing global normal coordinates on the associated
[[lie-groups/riemannian-symmetric-space-noncompact-type|Riemannian symmetric
space]]. Passing from \(\mathfrak p\) to a chamber in \(\mathfrak a\) is the
analogue of diagonalizing a positive-definite matrix. The resulting radial
coordinate controls invariant integration formulas.

## Example and applications

For \(G=\mathrm{GL}_n(\mathbb R)\) and \(K=\mathrm O(n)\), the theorem is the
matrix polar decomposition \(g=k\exp X\) with \(X\) symmetric. Orthogonally
diagonalizing \(X\) gives \(KAK\), with \(A\) the positive diagonal matrices.
In representation theory, the size of \(H\) governs decay and growth estimates
for matrix coefficients.

## References

1. A. W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002. [Publisher record](https://link.springer.com/book/9780817642594). Relevant: Chapter VI, §4 and Chapter VII, §8.
2. S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, American Mathematical Society, 2001. [DOI record](https://doi.org/10.1090/gsm/034). Relevant: Chapter IX on global decompositions.
