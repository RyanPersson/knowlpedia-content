+++
id = "lie-groups/lie-algebra"
title = "Lie algebra"
kind = "definition"
summary = "A vector space over a stated field with an alternating bilinear bracket satisfying the Jacobi identity."
aliases = ["lie-algebra", "Lie Algebra"]
domains = ["lie-groups"]
prerequisites = ["linear-algebra/vector-space", "fiber-bundles/lie-bracket"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
legacy_source_path = "lie-groups/lie-algebra.md"
section_mode = "progressive"
+++

Let \(k\) be a field. A **Lie algebra over \(k\)** is a [[linear-algebra/vector-space|vector space]] \(\mathfrak g\) over \(k\) equipped with a \(k\)-bilinear map
\[
[-,-]:\mathfrak g\times\mathfrak g\longrightarrow\mathfrak g,
\]
called the [[fiber-bundles/lie-bracket|Lie bracket]], such that \([X,X]=0\) and
\[
[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0.
\]
The first condition says that the bracket is alternating; it implies
\([X,Y]=-[Y,X]\). Over a field of characteristic different from \(2\), the
two formulations are equivalent.

## Base field and finite-dimensional convention

The base field is part of the structure and should be stated. A complex Lie
algebra can be regarded as a real Lie algebra by restricting scalars, but its
real dimension doubles and real-linear homomorphisms need not be
complex-linear.

Unless a larger category is explicitly named, the finite-dimensional category
\(\mathbf{LieAlg}^{\mathrm{fd}}_k\) has finite-dimensional Lie algebras over
\(k\) as objects and [[lie-groups/lie-algebra-homomorphism|Lie algebra
homomorphisms]] as morphisms. The characteristic-zero case, especially
\(k=\mathbb R\) or \(\mathbb C\), is the setting for the
[[formal-groups/lie-algebra-formal-group-equivalence|formal Lie
correspondence]].

## Examples

- Any associative algebra becomes a Lie algebra with commutator \([A,B]=AB-BA\), e.g. matrix Lie algebras \(\mathfrak{gl}(n,\mathbb{R})\).
- The space of [[fiber-bundles/vector-field|vector fields]] on a manifold with the commutator bracket.
- An [[lie-groups/abelian-lie-algebra|abelian Lie algebra]] is one with \([X,Y]=0\) for all \(X,Y\).

## Maps and structure

A structure-preserving map is a Lie algebra homomorphism; bijective ones are
[[lie-groups/lie-algebra-isomorphism|isomorphisms]].

Important substructures include [[lie-groups/lie-subalgebra|Lie subalgebras]], [[lie-groups/ideal-lie-algebra|ideals]], and the [[lie-groups/center-of-a-lie-algebra|center]].

Many classification notions are defined in terms of the bracket, such as
[[lie-groups/solvable-lie-algebra|solvable]],
[[lie-groups/nilpotent-lie-algebra|nilpotent]],
[[lie-groups/semisimple-lie-algebra|semisimple]],
[[lie-groups/simple-lie-algebra|simple]], and
[[lie-groups/reductive-lie-algebra|reductive]] Lie algebras.

## References

1. Nicolas Bourbaki, *Lie Groups and Lie Algebras: Chapters 1–3*, Springer, 1989. [Publisher record](https://link.springer.com/book/9783540642428). Relevant: Chapter 1, Lie algebras.
2. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, second edition, Birkhäuser, 2002. [Publisher record](https://link.springer.com/book/10.1007/978-1-4757-2453-0). Relevant: Chapter I, Lie algebras and Lie groups.
