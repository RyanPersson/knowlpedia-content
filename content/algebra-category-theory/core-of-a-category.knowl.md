+++
id = "algebra-category-theory/core-of-a-category"
title = "Core of a category"
kind = "construction"
summary = "The maximal subgroupoid of a category, retaining all objects but only the isomorphisms."
aliases = ["maximal subgroupoid", "underlying groupoid of a category"]
domains = ["algebra-category-theory"]
section_mode = "progressive"
+++

The **core** of a [[algebra-category-theory/category|category]] \(\mathcal C\), written \(\mathcal C^\simeq\) or \(\operatorname{Core}(\mathcal C)\), is the [[algebra-category-theory/groupoid|groupoid]] with the same objects as \(\mathcal C\) and with
\[
\operatorname{Hom}_{\mathcal C^\simeq}(X,Y)
=\{f\in\operatorname{Hom}_{\mathcal C}(X,Y):f\text{ is an isomorphism}\}.
\]
It is the largest subcategory of \(\mathcal C\) containing every object and only invertible morphisms.

## Functoriality

Every [[algebra-category-theory/functor|functor]] \(F:\mathcal C\to\mathcal D\) preserves isomorphisms, so restriction gives a functor
\[
F^\simeq:\mathcal C^\simeq\longrightarrow\mathcal D^\simeq.
\]
Consequently, taking the core is functorial.

## Interpretation

Passing to the core forgets all noninvertible maps but retains automorphism groups. Passing further to isomorphism classes forgets those automorphisms too. For example, the [[differential-geometry/diffeomorphism-groupoid-of-smooth-manifolds|core of the category of smooth manifolds]] has diffeomorphisms as its morphisms, while the original category also contains arbitrary smooth maps.

## References

1. Emily Riehl, *Category Theory in Context*, Dover, 2016. [Author-hosted text](https://math.jhu.edu/~eriehl/context.pdf). Relevant: §1.1, categories and their maximal subgroupoids.
