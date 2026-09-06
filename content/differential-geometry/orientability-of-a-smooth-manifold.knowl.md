+++
id = "differential-geometry/orientability-of-a-smooth-manifold"
title = "Orientability of a smooth manifold"
kind = "definition"
summary = "A smooth manifold is orientable when its tangent bundle admits an orientation."
aliases = ["orientable manifold"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/tangent-bundle", "fiber-bundles/orientation-of-a-real-vector-bundle", "real-analysis/jacobian-determinant"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

An \(n\)-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\) is **orientable** if its [[fiber-bundles/tangent-bundle|tangent bundle]] \(TM\) admits an [[fiber-bundles/orientation-of-a-real-vector-bundle|orientation]]. Equivalently, \(M\) has an atlas whose transition maps all have positive [[real-analysis/jacobian-determinant|Jacobian determinant]]. Orientability is an existence property: an orientable manifold need not come with a selected [[differential-geometry/orientation-of-a-smooth-manifold|orientation]]. A manifold together with such a selection is **oriented**. If no orientation exists, the manifold is **nonorientable**. These terms apply componentwise when the dimension is locally constant rather than globally fixed.

## Equivalent tests

For an ordinary second-countable smooth \(n\)-manifold, the following are equivalent:

1. \(TM\) is orientable;
2. \(M\) has an atlas with positive transition determinants; and
3. \(M\) admits a nowhere-vanishing smooth \(n\)-form.

Equivalently, the top exterior-power [[fiber-bundles/line-bundle|line bundle]] \(\bigwedge^nT^*M\) is trivial. The equivalence between compatible local choices and a global top form uses [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|smooth partitions of unity]].

## Choices on connected components

Every connected orientable manifold of positive dimension has exactly two orientations. For a disconnected manifold, orientations may be chosen independently on its [[topology/connected-component|connected components]]. A zero-dimensional manifold is orientable and has the canonical orientation determined by the unique ordered basis of each zero-dimensional [[differential-geometry/tangent-space|tangent space]].

## Examples and obstruction

[[linear-algebra/euclidean-space|Euclidean space]] and every sphere are orientable. Every [[differential-geometry/complex-manifold|complex manifold]] is canonically orientable after forgetting its complex structure. The Möbius band is nonorientable, and real projective \(n\)-space is orientable exactly when \(n\) is odd. The [[fiber-bundles/stiefel-whitney-class|first Stiefel–Whitney class]] of \(TM\) is the standard cohomological obstruction to orientability.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: the chapter on orientations.
2. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: §§4 and 9, Stiefel–Whitney classes and oriented vector bundles.
