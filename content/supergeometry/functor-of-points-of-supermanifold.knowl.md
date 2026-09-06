+++
id = "supergeometry/functor-of-points-of-supermanifold"
title = "Functor of points of a supermanifold"
kind = "definition"
summary = "The contravariant functor sending each test supermanifold to its family of points in a given supermanifold."
aliases = ["functor of points in supergeometry", "S-points of a supermanifold"]
domains = ["supergeometry", "algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["supergeometry/supermanifold", "algebra-category-theory/contravariant-functor", "algebra-category-theory/natural-transformation", "algebra-category-theory/yoneda-lemma"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For a [[supergeometry/supermanifold|supermanifold]] \(X\), its **functor of
points** is the [[algebra-category-theory/contravariant-functor|contravariant functor]]
\[
h_X:\mathbf{SMan}_{\mathbb R}^{\mathrm{sm},\mathrm{op}}
\longrightarrow\mathbf{Set},
\qquad
h_X(S)=\operatorname{Hom}_{\mathbf{SMan}}(S,X).
\]
An element of \(h_X(S)\) is an **\(S\)-point** of \(X\), or equivalently a
family of points of \(X\) parametrized by the test supermanifold \(S\).
A morphism \(X\to Y\) induces a [[algebra-category-theory/natural-transformation|natural transformation]] \(h_X\to h_Y\).

By the [[algebra-category-theory/yoneda-lemma|Yoneda lemma]], \(X\mapsto h_X\) is fully faithful. Consequently, a
supermanifold and every one of its morphisms can be characterized by all
\(S\)-points and their naturality in \(S\).

## Why generalized points matter

Maps from the ordinary one-point manifold detect only the reduced points
\(|X|\); odd coordinates vanish there. Maps from test objects with odd
nilpotents, such as purely odd affine supermanifolds, detect the odd and
nilpotent directions. Coordinate formulas used in physics become ordinary
formulas with Grassmann-valued coefficients after evaluation on suitable test
objects.

Restricting tests to finite Grassmann algebras can be effective, but a bare
collection of sets of Grassmann-valued points is not automatically equivalent
to a supermanifold. One must retain naturality and, depending on the chosen
formalism, the smooth or enriched structure on those point sets.

## References

1. P. Deligne and J. W. Morgan, “Notes on supersymmetry (following Joseph Bernstein),” in *Quantum Fields and Strings: A Course for Mathematicians*, Volume 1, American Mathematical Society, 1999, 41–97. Relevant: functor-of-points conventions.
2. C. Carmeli, L. Caston, and R. Fioresi, *Mathematical Foundations of Supersymmetry*, EMS, 2011. [Publisher record](https://doi.org/10.4171/097). Relevant: Chapters 4 and 10.
