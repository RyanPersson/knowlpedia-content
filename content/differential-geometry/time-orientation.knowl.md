+++
id = "differential-geometry/time-orientation"
title = "Time orientation"
kind = "definition"
summary = "A continuous choice of one component of the timelike cone on a Lorentzian manifold."
aliases = []
domains = ["differential-geometry", "mathematical-physics"]
section_mode = "progressive"
prerequisites = ["differential-geometry/lorentzian-manifold", "linear-algebra/minkowski-vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **time orientation** on a [[differential-geometry/lorentzian-manifold|Lorentzian manifold]] is a continuous choice, at every point, of one of the two connected components of the timelike cone. Equivalently, it is represented by a continuous timelike vector field; timelike vectors in the chosen component are **future-directed**, as are causal vectors in its closure. A manifold admitting such a choice is **time-orientable**.

For [[linear-algebra/minkowski-vector-space|Minkowski space]] with
\[
q(t,x,y,z)=-t^2+x^2+y^2+z^2,
\]
the standard choice declares a timelike vector future-directed when \(t>0\). Its closure contains the future-directed null cone and determines the direction used by [[differential-geometry/causal-curve|future-directed causal curves]].

## Transformations

A Lorentz transformation is **orthochronous** when it preserves the chosen future cone. This property is independent of spatial orientation. Requiring both determinant \(+1\) and preservation of time orientation selects the [[lie-groups/proper-orthochronous-lorentz-group|proper orthochronous Lorentz group]].

Time orientation is additional structure: orientability of the underlying manifold does not imply time-orientability, nor conversely.

## References

1. Barrett O'Neill, *Semi-Riemannian Geometry With Applications to Relativity*, Academic Press, 1983, §5. [Publisher record](https://doi.org/10.1016/C2009-0-11874-8).
2. Robert M. Wald, *General Relativity*, University of Chicago Press, 1984, §8.1. [Publisher record](https://doi.org/10.7208/chicago/9780226870373.001.0001).
