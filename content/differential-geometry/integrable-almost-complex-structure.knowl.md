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

## The Nijenhuis criterion

The **Nijenhuis tensor** of \(J\) is
\[
N_J(X,Y)
=[JX,JY]-J[JX,Y]-J[X,JY]-[X,Y].
\]
It measures the failure of the \(+i\)-eigenbundle of the complexified tangent bundle to be closed under Lie brackets. Every integrable almost-complex structure has \(N_J=0\).

The smooth Newlander–Nirenberg theorem gives the converse:
\[
J\text{ is integrable}\quad\Longleftrightarrow\quad N_J=0.
\]
Consequently, a smooth almost-complex manifold with vanishing Nijenhuis tensor has compatible local holomorphic coordinates. This is a local theorem; it does not assert that the resulting complex manifold has global complex coordinates.

## Regularity scope

The displayed equivalence is stated here in the \(C^\infty\) category. There are important finite- and low-regularity refinements, but their precise hypotheses and the regularity of the resulting coordinates require separate formulations. The bare phrase “Newlander–Nirenberg” should therefore not be used to silently promote an arbitrary continuous endomorphism \(J\) to a complex structure.

In real dimension two, every smooth almost-complex structure is integrable. In higher dimensions, \(N_J=0\) is a genuine differential constraint. Integrability is also stronger than the pointwise relation \(J^2=-1\): the latter alone supplies complex vector spaces on tangent spaces but not holomorphic charts.

## References

1. August Newlander and Louis Nirenberg, “Complex Analytic Coordinates in Almost Complex Manifolds,” *Annals of Mathematics* 65 (1957), 391–404. [DOI record](https://doi.org/10.2307/1970051).
2. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: Chapter 1, the Nijenhuis tensor and integrability.
