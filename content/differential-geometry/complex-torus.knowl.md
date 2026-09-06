+++
id = "differential-geometry/complex-torus"
title = "Complex torus"
kind = "definition"
summary = "A quotient of a finite-dimensional complex vector space by a full lattice."
aliases = ["complex analytic torus"]
domains = ["differential-geometry", "lie-groups"]
prerequisites = ["linear-algebra/vector-space", "lie-groups/discrete-subgroup", "differential-geometry/complex-manifold", "fiber-bundles/lie-group"]
dependency_review_count = 1
section_mode = "progressive"
+++

A **complex torus** of complex dimension \(g\) is a quotient
\[
X=V/\Lambda,
\]
where \(V\) is a \(g\)-dimensional complex [[linear-algebra/vector-space|vector space]] and \(\Lambda\subset V\), viewed as a real vector space, is a [[lie-groups/discrete-subgroup|discrete subgroup]] of rank \(2g\) whose real span is \(V\). Translation by \(\Lambda\) acts freely and properly discontinuously, so the quotient is a compact [[differential-geometry/complex-manifold|complex manifold]]. Addition on \(V\) descends to \(X\), making it a connected compact complex [[fiber-bundles/lie-group|Lie group]]. Conversely, every connected compact complex Lie group is isomorphic to such a quotient. The lattice is part of a presentation, not additional chosen data on the abstract torus.

## Geometry and topology

As a real [[fiber-bundles/smooth-manifold|smooth manifold]], every \(g\)-dimensional complex torus is diffeomorphic to \((S^1)^{2g}\). A translation-invariant Hermitian [[linear-algebra/inner-product|inner product]] on \(V\) descends to a flat [[differential-geometry/kahler-metric|Kähler metric]] on \(X\). Translation-invariant holomorphic one-forms also descend and trivialize the [[differential-geometry/holomorphic-cotangent-bundle|holomorphic cotangent bundle]].

## Examples and algebraicity

For \(g=1\), a complex torus is an elliptic curve with the identity as base point; analytically it has the form \(\mathbb C/(\mathbb Z+\tau\mathbb Z)\) with \(\operatorname{Im}\tau>0\). In higher dimensions, not every complex torus is projective. A projective complex torus is an abelian variety, and projectivity is equivalent to the existence of a suitable positive integral \((1,1)\)-class, or Riemann form. Thus “complex torus” and “abelian variety” are not synonyms.

## References

1. Christina Birkenhake and Herbert Lange, *Complex Tori*, Progress in Mathematics 177, Birkhäuser, 1999. [Springer DOI record](https://doi.org/10.1007/978-1-4612-1566-0). Relevant: Chapter 1, quotient construction and basic geometry.
2. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Springer DOI record](https://doi.org/10.1007/b137952). Relevant: the discussion of complex tori and Kähler manifolds.
