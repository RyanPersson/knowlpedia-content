+++
id = "fiber-bundles/serre-swan-theorem"
title = "Serre–Swan theorem"
kind = "theorem"
summary = "On a compact smooth manifold, taking smooth sections gives an equivalence between vector bundles and finitely generated projective modules."
aliases = ["Serre-Swan correspondence", "Serre-Swan duality", "vector bundles versus projective modules", "categorical Serre-Swan equivalence"]
domains = ["fiber-bundles", "algebra-category-theory"]
section_mode = "progressive"
+++

Let \(M\) be a compact [[fiber-bundles/smooth-manifold|smooth manifold]] and \(\mathbb F=\mathbb R\) or \(\mathbb C\). The **smooth Serre–Swan theorem** states that the functor
\[
E\longmapsto\Gamma^\infty(M,E)
\]
from finite-rank smooth [[fiber-bundles/vector-bundle|\(\mathbb F\)-vector bundles]] with [[fiber-bundles/vector-bundle-morphism|bundle morphisms covering \(\operatorname{id}_M\)]] to finitely generated projective \(C^\infty(M,\mathbb F)\)-modules with module homomorphisms is an [[algebra-category-theory/equivalence-of-categories|equivalence of categories]]. Thus every [[fiber-bundles/section-module-is-finitely-generated-projective|section module is finitely generated projective]], every such module is the [[fiber-bundles/module-of-smooth-sections|module of smooth sections]] of a vector bundle, and module homomorphisms arise uniquely from vector-bundle maps over \(M\). The compactness hypothesis is part of this formulation.

## The two constructions

A vector bundle \(E\) embeds as a direct summand of a trivial bundle. Taking sections then expresses \(\Gamma^\infty(M,E)\) as a direct summand of a finite-rank free \(C^\infty(M)\)-module, hence as a finitely generated projective module.

Conversely, a finitely generated projective module is represented by an idempotent matrix \(p\in M_N(C^\infty(M))\). Evaluating \(p\) pointwise gives a smoothly varying family of projections, whose images form a [[fiber-bundles/vector-subbundle|vector subbundle]] of \(M\times\mathbb F^N\). This [[fiber-bundles/projective-module-bundle-reconstruction|idempotent reconstruction]] is inverse to taking sections up to natural isomorphism [Swan, §§1–3](https://doi.org/10.1090/S0002-9947-1962-0143225-6).

## Categorical content

The theorem is stronger than a bijection of isomorphism classes. It identifies
morphisms covering \(\operatorname{id}_M\) and their compositions, so direct
sums, direct summands, and isomorphisms agree on the geometric and algebraic
sides. In particular, bundle automorphisms over \(M\) correspond exactly to
invertible \(C^\infty(M)\)-linear endomorphisms of the section module.

This equivalence explains why vector bundles define classes in topological \(K\)-theory and why finitely generated projective modules play the role of vector bundles in noncommutative geometry.

## Variants and scope

**Warning.** Several results are called the Serre–Swan theorem. For compact Hausdorff \(X\), complex vector bundles correspond to finitely generated projective modules over \(C(X)\). The displayed theorem is its smooth compact-manifold version over \(C^\infty(M)\). For noncompact manifolds, one must modify the finiteness conditions or the function algebra; the unqualified compact statement cannot simply be copied.

“Serre–Swan duality” is common terminology, but the result is a covariant equivalence produced by the section functor, not a contravariant duality.

## References

1. Richard G. Swan, “Vector Bundles and Projective Modules,” *Transactions of the American Mathematical Society* 105 (1962), 264–277. [DOI record](https://doi.org/10.1090/S0002-9947-1962-0143225-6). Relevant: §§1–3, finite-type bundles, projective section modules, and reconstruction.
2. José M. Gracia-Bondía, Joseph C. Várilly, and Héctor Figueroa, *Elements of Noncommutative Geometry*, Birkhäuser, 2001. [DOI record](https://doi.org/10.1007/978-1-4612-0005-5). Relevant: chapter 2, projective modules as noncommutative vector bundles and the Serre–Swan correspondence.
