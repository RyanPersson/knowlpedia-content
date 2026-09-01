+++
id = "lie-groups/rank-of-a-semisimple-lie-algebra"
title = "Rank of a semisimple Lie algebra"
kind = "definition"
summary = "The dimension of a Cartan subalgebra, equivalently the rank of the associated root system."
aliases = ["rank of a Lie algebra", "semisimple Lie algebra rank"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/semisimple-lie-algebra", "algebraic-geometry-foundations/algebraically-closed-field", "lie-groups/cartan-subalgebra", "lie-groups/root-system"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(\mathfrak g\) be a finite-dimensional [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]] over an
[[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed field]] of characteristic zero. Its **rank** is
\[
\operatorname{rank}\mathfrak g=\dim\mathfrak h,
\]
where \(\mathfrak h\subseteq\mathfrak g\) is any
[[lie-groups/cartan-subalgebra|Cartan subalgebra]]. All Cartan subalgebras of
\(\mathfrak g\) are conjugate, so this dimension is independent of the choice
of \(\mathfrak h\). It is also the rank of the associated
[[lie-groups/root-system|root system]].

## Examples

The classical complex [[lie-groups/lie-algebra|Lie algebras]] satisfy
\[
\operatorname{rank}\mathfrak{sl}_n(\mathbb C)=n-1,
\qquad
\operatorname{rank}\mathfrak{so}_{2n}(\mathbb C)=n.
\]
For \(\mathfrak{sl}_n\), the diagonal trace-zero matrices form a Cartan
subalgebra. The exceptional complex Lie algebras of types \(E_6,E_7,E_8,F_4\),
and \(G_2\) have ranks \(6,7,8,4\), and \(2\), respectively.

## Relation to rank in other settings

For a compact [[lie-groups/connected-lie-group|connected Lie group]] \(G\), the rank of \(G\) is the dimension of
a maximal torus. Its Lie algebra has the same rank after complexification. For
a general real [[lie-groups/reductive-lie-algebra|reductive Lie algebra]], **complex rank** and **real rank** are
different invariants: complex rank is the rank of its complexification,
whereas real rank is the dimension of a maximal abelian subspace in the
noncompact part of a Cartan decomposition. The unqualified definition above is
the complex semisimple one used in root-system arguments.

## Why rank matters for subalgebras

A subalgebra has **maximal rank** when it contains a Cartan subalgebra of the
ambient semisimple algebra. This is stronger than merely having large
dimension. It permits both algebras to be described using roots in one common
Cartan subalgebra and underlies root-removal constructions.

## References

1. James E. Humphreys, *Introduction to Lie Algebras and Representation
   Theory*, Springer, 1972, §§8–10. [Publisher
   record](https://doi.org/10.1007/978-1-4612-6398-2).
2. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed.,
   Birkhäuser, 2002, Chapters IV–V. [Publisher
   record](https://doi.org/10.1007/978-1-4757-2453-0).
