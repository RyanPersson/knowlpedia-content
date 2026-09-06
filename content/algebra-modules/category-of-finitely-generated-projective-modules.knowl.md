+++
id = "algebra-modules/category-of-finitely-generated-projective-modules"
title = "Category of finitely generated projective modules"
kind = "definition"
summary = "The fixed-ring category whose objects are finitely generated projective modules and whose morphisms are module homomorphisms."
aliases = ["Proj A", "category of finite projective modules", "finite projective module category"]
domains = ["algebra-modules", "category-theory"]
prerequisites = ["algebra-modules/projective-module", "algebra-modules/module-homomorphism", "algebra-category-theory/full-subcategory", "algebra-category-theory/zero-object", "linear-algebra/matrix"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a commutative unital ring. The **category of finitely generated
projective \(A\)-modules**, denoted \(\mathbf{Proj}(A)\), has
[[algebra-modules/projective-module|finitely generated projective
\(A\)-modules]] as objects and
[[algebra-modules/module-homomorphism|\(A\)-linear maps]] as morphisms.

This is a [[algebra-category-theory/full-subcategory|full subcategory]] of the category of \(A\)-modules. It is additive:
the zero module is a [[algebra-category-theory/zero-object|zero object]] and finite direct sums are biproducts. Every
object is isomorphic to the image of an idempotent matrix
\(p\in M_n(A)\), or equivalently to a direct summand of \(A^n\).

## Exactness and fixed scalars

The category \(\mathbf{Proj}(A)\) is generally not abelian. For example, the
cokernel of a map between projective modules need not be projective. It does
carry the standard split exact structure, and direct sums and direct
summands remain inside the category.

The ring \(A\) is fixed. A homomorphism \(A\to B\) leads to extension and
[[algebra-commutative/restriction-of-scalars|restriction of scalars]] between different module categories, but it is not
itself a morphism in \(\mathbf{Proj}(A)\).

For a noncommutative ring one must instead specify left or right modules and
use the compatible matrix convention. That handed version is not part of the
notation on this page.

## Geometric example

For a connected finite-dimensional Hausdorff second-countable smooth
manifold \(M\), the
[[fiber-bundles/serre-swan-theorem|Serre–Swan theorem]] gives a covariant
equivalence
\[
\mathbf{Vect}_{\mathbb F}(M)\simeq
\mathbf{Proj}\bigl(C^\infty(M,\mathbb F)\bigr).
\]
Both sides use morphisms over one fixed base or one fixed ring. This is not
the contravariant reconstruction of maps between different manifolds from
their smooth-function algebras. No compactness hypothesis is needed here;
on a disconnected base the matching bundle category has globally bounded
rank.

## References

1. T. Y. Lam, *Lectures on Modules and Rings*, Springer, 1999. [DOI record](https://doi.org/10.1007/978-1-4612-0525-8). Relevant: projective modules, finite generation, and idempotent matrices.
2. Richard G. Swan, “Vector Bundles and Projective Modules,” *Transactions of the American Mathematical Society* 105 (1962), 264–277. [DOI record](https://doi.org/10.1090/S0002-9947-1962-0143225-6). Relevant: finite projective modules and vector bundles.
