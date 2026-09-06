+++
id = "algebra-category-theory/morphism"
title = "Morphism"
kind = "knowl"
summary = "An arrow between objects in a category."
aliases = ["morphism"]
domains = ["algebra-category-theory"]
prerequisites = ["algebra-category-theory/object", "algebra-category-theory/category"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
legacy_source_path = "algebra-category-theory/morphism.md"
+++

Let \(\mathcal C\) be a [[algebra-category-theory/category|category]] and \(X,Y \in \mathrm{Ob}(\mathcal C)\).
A **morphism** \(f : X \to Y\) is an element of \(\mathrm{Hom}_{\mathcal C}(X,Y)\).

The **source** (or domain) of \(f\) is \(X\), and its **target** (or codomain) is \(Y\). Morphisms can be [[algebra-category-theory/composition-category|composed]] when targets and sources match, and each object has an [[algebra-category-theory/identity-morphism|identity morphism]].

## Special morphisms

- If \(X=Y\), then \(f\) is an [[algebra-category-theory/endomorphism-category|endomorphism]].
- If \(f\) is invertible (has a two-sided inverse), then \(f\) is an [[algebra-category-theory/isomorphism-category|isomorphism]].
- If \(f\) is left-cancellative under composition, then \(f\) is a [[algebra-category-theory/monomorphism-category|monomorphism]] (a “mono”).
- Dually, one has [[algebra-category-theory/epimorphism-category|epimorphisms]] (“epis”).

## Examples

1. In \(\mathbf{Set}\), morphisms are [[shared-foundations/function|functions]] between sets.
2. In \(\mathbf{Grp}\), morphisms are group homomorphisms.
3. In \(\mathbf{Top}\), morphisms are continuous maps.
