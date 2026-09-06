+++
id = "differential-geometry/celestial-sphere"
title = "Celestial sphere"
kind = "construction"
summary = "The sphere of future null directions, naturally identified with CP¹."
aliases = ["sphere of null directions", "projectivized light cone", "celestial two-sphere"]
domains = ["differential-geometry", "mathematical-physics", "complex-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/minkowski-vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

In [[linear-algebra/minkowski-vector-space|\(\mathbb R^{1,3}\)]], let
\[
\mathcal N^+=\{v\ne0:q(v)=0,\ t>0\}
\]
be the future null cone. The **celestial sphere** is its space of positive rays,
\[
\mathscr C=\mathcal N^+/\mathbb R_{>0}.
\]
Every ray has a unique representative with \(t=1\), whose spatial part lies on \(S^2\), so \(\mathscr C\cong S^2\).

## Complex projective description

Under the [[lie-groups/hermitian-matrix-model-of-minkowski-space|Hermitian matrix model]], a future null ray is represented by \(zz^\dagger\) with \(z\in\mathbb C^2\setminus\{0\}\). Two spinors yield the same ray exactly when their complex lines agree. Therefore
\[
\mathscr C\cong\mathbb P(\mathbb C^2)=\mathbb{CP}^1
\cong\widehat{\mathbb C}.
\]
This identification equips the celestial sphere with its standard complex structure.

## Geometric meaning

At an event in Minkowski space, future null directions are possible directions of incoming or outgoing light. A choice of inertial observer identifies this abstract sphere with ordinary viewing directions; a different observer acts by a Lorentz transformation, which becomes a [[complex-analysis/mobius-transformation|Möbius transformation]] in the projective coordinate.

## References

1. Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1, Cambridge University Press, 1984, §§1.2–1.3. [Publisher record](https://doi.org/10.1017/CBO9780511564048).
2. Barrett O'Neill, *Semi-Riemannian Geometry With Applications to Relativity*, Academic Press, 1983, Chapter 5. [Publisher record](https://doi.org/10.1016/C2009-0-11874-8).
