+++
id = "algebraic-geometry-foundations/blue-scheme"
title = "Blue scheme"
kind = "definition"
summary = "A locally blueprinted space covered by spectra of blueprints."
aliases = ["blueprint scheme", "blue scheme over F1"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/locally-blueprinted-space", "topology/open-cover", "algebraic-geometry-foundations/affine-blue-scheme"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A **blue scheme** is a [[algebraic-geometry-foundations/locally-blueprinted-space|locally blueprinted space]] \(X\) that admits an [[topology/open-cover|open cover]] by [[algebraic-geometry-foundations/affine-blue-scheme|affine blue schemes]]
\[
U_i\simeq\operatorname{Spec}B_i.
\]
Morphisms are local morphisms of the corresponding sheaves of blueprints.

## Construction by gluing

As with ordinary schemes, spectra are glued along open affine subspaces. The local coordinate objects are [[algebraic-geometry-foundations/blueprint|blueprints]], and the [[algebraic-geometry-foundations/structure-sheaf|structure sheaf]] records their [[algebraic-geometry-foundations/localization-of-blueprint|localizations]].

The framework simultaneously contains geometric objects induced by [[algebra-groups/commutative-monoid|commutative monoids]], semirings, and rings. Base extension sends suitable blue schemes to semiring schemes or ordinary schemes, but it can forget the monomial skeleton and additive-relation data.

## Distinguish ordered blue schemes

An [[algebraic-geometry-foundations/ordered-blue-scheme|ordered blue scheme]] is locally modeled on [[algebraic-geometry-foundations/ordered-blueprint|ordered blueprints]] and is the setting used for scheme-theoretic tropicalization and matroid moduli. It generalizes this construction, but “blue scheme” and “ordered blue scheme” are not interchangeable labels.

There are also functor-of-points approaches to relative blue schemes. Their comparison with blue schemes as locally blueprinted spaces is subtle and is not an unrestricted equivalence.

## References

- Oliver Lorscheid, [*The geometry of blueprints, Part I*, §3](https://arxiv.org/abs/1103.1745).
- Oliver Lorscheid, [*Blue schemes, semiring schemes, and relative schemes after Toën and Vaquié*](https://arxiv.org/abs/1212.3261).
