+++
id = "differential-geometry/diffeomorphism-group"
title = "Diffeomorphism group"
kind = "definition"
summary = "The group of all smooth self-diffeomorphisms of a smooth manifold under composition."
aliases = ["group of diffeomorphisms", "Diff(M)"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]]. The **diffeomorphism group** of \(M\), denoted \(\operatorname{Diff}(M)\), is the set of all [[fiber-bundles/diffeomorphism|diffeomorphisms]] \(f:M\to M\), with composition as multiplication, the identity map as identity element, and functional inverse as group inverse. It is the automorphism group of \(M\) in the [[differential-geometry/category-of-smooth-manifolds|category of smooth manifolds]]. This algebraic definition does not by itself specify a topology or an infinite-dimensional smooth structure on \(\operatorname{Diff}(M)\); those require additional choices and hypotheses.

## Actions and important subgroups

The group acts on points, tensor fields, [[fiber-bundles/differential-k-form|differential forms]], and geometric structures by pushforward or pullback. Common subgroups preserve an [[differential-geometry/orientation-of-a-smooth-manifold|orientation]], a volume form, a Riemannian metric, or a symplectic form. The quotient by the identity component gives a mapping class group when the chosen topology makes that component meaningful.

## Topological and smooth structures

For compact \(M\), the \(C^\infty\) topology gives \(\operatorname{Diff}(M)\) the structure of an infinite-dimensional Lie group modeled on smooth [[fiber-bundles/vector-field|vector fields]]. Noncompact manifolds require more care: compact-open and strong Whitney topologies behave differently, and support conditions may be imposed. These analytic structures are not part of the underlying group definition.

## Examples

\(\operatorname{Diff}(\{\ast\})\) is trivial. Every invertible linear map of \(\mathbb R^n\) is a diffeomorphism, so \(\mathrm{GL}(n,\mathbb R)\) is a subgroup of \(\operatorname{Diff}(\mathbb R^n)\). For the circle, rotations form a subgroup, but the full diffeomorphism group also contains nonlinear reparametrizations.

## References

1. Augustin Banyaga, *The Structure of Classical Diffeomorphism Groups*, Mathematics and Its Applications 400, Kluwer, 1997. [DOI record](https://doi.org/10.1007/978-1-4757-6800-8). Relevant: Chapter 1, diffeomorphism groups and structure-preserving subgroups.
2. Peter W. Michor, *Manifolds of Differentiable Mappings*, Shiva Mathematics Series 3, Shiva Publishing, 1980. [Author-hosted scan](https://www.mat.univie.ac.at/~michor/manifolds_of_differentiable_mappings.pdf). Relevant: differentiable mapping spaces and diffeomorphism groups.
