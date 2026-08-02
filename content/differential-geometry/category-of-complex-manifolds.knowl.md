+++
id = "differential-geometry/category-of-complex-manifolds"
title = "Category of complex manifolds"
kind = "definition"
summary = "The category whose objects are finite-dimensional complex manifolds and whose morphisms are holomorphic maps."
aliases = ["complex-manifold category", "category of complex manifolds and holomorphic maps", "ComplexMan"]
domains = ["differential-geometry", "complex-analysis", "category-theory"]
section_mode = "progressive"
+++

The **category of complex manifolds**, denoted here by
\(\mathbf{CMan}\), has finite-dimensional
Hausdorff second-countable
[[differential-geometry/complex-manifold|complex manifolds]] as objects and
[[differential-geometry/holomorphic-map|holomorphic maps]] as morphisms.
Identity maps and composites of holomorphic maps are holomorphic, so these
data form a [[algebra-category-theory/category|category]]. This is the house
convention; disconnected objects are allowed when their component dimensions
are globally bounded.

An isomorphism in \(\mathbf{CMan}\) is exactly a
[[differential-geometry/biholomorphism|biholomorphism]]: a holomorphic map
with a holomorphic inverse. Merely requiring a map to be a bijection is not
enough in arbitrary geometric categories; the inverse must also be
holomorphic.

## Relation to smooth manifolds

Forgetting the [[differential-geometry/complex-coordinate-chart|complex charts]] gives a functor
\[
U:\mathbf{CMan}\longrightarrow\mathbf{Man}.
\]
Here \(\mathbf{Man}\) is the
[[differential-geometry/category-of-smooth-manifolds|category of smooth
manifolds]]. The functor sends a complex \(n\)-manifold to its underlying real \(2n\)-manifold and
a holomorphic map to its underlying smooth map. This functor is faithful but
not full: most smooth maps between underlying manifolds are not holomorphic.
It is also not essentially surjective, because not every even-dimensional
smooth manifold admits a complex structure.

## Products and categorical conventions

The product \(X\times Y\), with product complex charts, is a categorical
product, and a point is terminal.

The [[algebra-category-theory/core-of-a-category|maximal subgroupoid]] of \(\mathbf{CMan}\) retains all complex manifolds but
only biholomorphisms. It should not be confused with \(\mathbf{CMan}\) itself,
which contains noninvertible holomorphic maps such as constant maps and
branched maps.

## References

1. Otto Forster, *Lectures on Riemann Surfaces*, Springer, 1981. [DOI record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: holomorphic maps, biholomorphisms, and products of complex manifolds.
2. Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Vol. II, Wiley, 1969. Relevant: Chapter IX, complex manifolds and holomorphic mappings.
