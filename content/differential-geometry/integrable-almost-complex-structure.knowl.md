+++
id = "differential-geometry/integrable-almost-complex-structure"
title = "Integrable almost-complex structure"
kind = "definition"
summary = "An almost-complex structure induced locally by holomorphic coordinate charts."
aliases = ["integrable almost complex structure"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

An [[differential-geometry/almost-complex-structure|almost-complex structure]] \(J\) on a smooth \(2n\)-manifold is **integrable** if every point has local coordinates in \(\mathbb C^n\) whose ordinary multiplication by \(i\) induces \(J\). Such charts have [[differential-geometry/holomorphic-map|holomorphic]] transition maps and therefore make the manifold a [[differential-geometry/complex-manifold|complex manifold]].

The [[differential-geometry/nijenhuis-tensor|Nijenhuis tensor]] measures the
failure of the \(+i\)-eigenbundle of the complexified tangent bundle to be
closed under Lie brackets. The
[[differential-geometry/newlander-nirenberg-theorem|Newlander–Nirenberg
theorem]] states that a smooth almost-complex structure is integrable exactly
when this tensor vanishes.

## Regularity scope

The displayed equivalence is stated here in the \(C^\infty\) category. There are important finite- and low-regularity refinements, but their precise hypotheses and the regularity of the resulting coordinates require separate formulations. The bare phrase “Newlander–Nirenberg” should therefore not be used to silently promote an arbitrary continuous endomorphism \(J\) to a complex structure.

In real dimension two, every smooth almost-complex structure is integrable.
In higher dimensions, vanishing of the Nijenhuis tensor is a genuine
differential constraint. Integrability is also stronger than the pointwise
relation \(J^2=-1\): the latter alone supplies complex vector spaces on
tangent spaces but not holomorphic charts.

## References

1. August Newlander and Louis Nirenberg, “Complex Analytic Coordinates in Almost Complex Manifolds,” *Annals of Mathematics* 65 (1957), 391–404. [DOI record](https://doi.org/10.2307/1970051).
2. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: Chapter 1, the Nijenhuis tensor and integrability.
