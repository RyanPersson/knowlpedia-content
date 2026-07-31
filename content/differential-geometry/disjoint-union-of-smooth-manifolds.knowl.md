+++
id = "differential-geometry/disjoint-union-of-smooth-manifolds"
title = "Disjoint union of smooth manifolds"
kind = "definition"
summary = "A finite or countable disjoint union inherits a smooth structure component by component and is the categorical coproduct of its components."
aliases = ["coproduct manifold", "smooth coproduct"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

For a finite or countable family of [[fiber-bundles/smooth-manifold|smooth manifolds]] \((M_i)_{i\in I}\), their **smooth disjoint union** \(\bigsqcup_iM_i\) is the set-theoretic disjoint union with the disjoint-union topology and the [[fiber-bundles/smooth-atlas|smooth atlas]] formed by all component charts. Each canonical inclusion \(M_i\hookrightarrow\bigsqcup_iM_i\) is a [[fiber-bundles/smooth-embedding|smooth open embedding]]. A map \(f:\bigsqcup_iM_i\to N\) is smooth exactly when every restriction \(f|_{M_i}\) is smooth. Hence the disjoint union, with these inclusions, is the [[algebra-category-theory/coproduct|coproduct]] in the [[differential-geometry/category-of-smooth-manifolds|category of smooth manifolds]] whenever it remains an object of the chosen category.

## Universal property

Given [[fiber-bundles/smooth-map|smooth maps]] \(f_i:M_i\to N\), there is a unique set map \(f:\bigsqcup_iM_i\to N\) whose restriction to \(M_i\) is \(f_i\). Because smoothness is checked componentwise, this map is smooth. This proves the coproduct universal property directly and explains why no compatibility conditions between different components are required.

## Categorical structure

The empty manifold is the coproduct of the empty family and is an [[algebra-category-theory/initial-object|initial object]] when the convention admits it. Binary disjoint union gives the smooth-manifold category a symmetric monoidal operation whose unit is the empty manifold. Associativity, commutativity, and unit identifications are canonical diffeomorphisms.

## Countability and dimension conventions

Under the usual Hausdorff, second-countable convention, an uncountable disjoint union of nonempty manifolds is not second countable, so arbitrary coproducts need not exist. If an \(n\)-manifold must have one fixed dimension, all nonempty \(M_i\) must have that dimension. A convention allowing dimension to vary by [[topology/connected-component|connected component]] admits mixed-dimensional disjoint unions. These restrictions come from the ambient definition of manifold, not from the componentwise smooth atlas.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: the foundational conventions for smooth manifolds, atlases, and smooth maps.
2. Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed., Springer, 1998. [DOI record](https://doi.org/10.1007/978-1-4757-4721-8). Relevant: coproducts and symmetric monoidal categories.
