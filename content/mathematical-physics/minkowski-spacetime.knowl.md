+++
id = "mathematical-physics/minkowski-spacetime"
title = "Minkowski spacetime"
kind = "definition"
summary = "The flat affine Lorentzian spacetime underlying special relativity."
aliases = ["affine Minkowski spacetime"]
domains = ["mathematical-physics", "differential-geometry", "lie-groups"]
prerequisites = ["differential-geometry/lorentzian-manifold", "linear-algebra/minkowski-vector-space", "linear-algebra/quadratic-form", "differential-geometry/time-orientation"]
dependency_review_count = 1
section_mode = "progressive"
+++

Four-dimensional **Minkowski spacetime** is the affine space underlying \(\mathbb R^4\), equipped with the translation-invariant [[differential-geometry/lorentzian-manifold|Lorentzian metric]]
\[
\eta=-dt^2+dx^2+dy^2+dz^2.
\]
After choosing an origin it is identified with [[linear-algebra/minkowski-vector-space|Minkowski vector space]], whose [[linear-algebra/quadratic-form|quadratic form]] is the same displayed \((-+++)\) form: \(q(v)=\eta(v,v)\). The affine formulation distinguishes events from displacement vectors. The coordinate field \(\partial_t\) supplies the standard [[differential-geometry/time-orientation|time orientation]].

## Causal structure

For a displacement \(v\),
\[
\eta(v,v)<0,\quad \eta(v,v)=0,\quad \eta(v,v)>0
\]
mean respectively timelike, null, and spacelike. The null cone separates the two timelike cones. Translations preserve this structure, as do linear transformations in the [[lie-groups/lorentz-group|Lorentz group]].

## Symmetry

The full affine isometry group is the [[lie-groups/poincare-group|Poincaré group]]
\[
\operatorname{ISO}(1,3)=\mathbb R^{1,3}\rtimes O(1,3).
\]
Its identity component uses the [[lie-groups/proper-orthochronous-lorentz-group|proper orthochronous Lorentz group]] and preserves both spatial orientation and time orientation. Minkowski spacetime is flat: its Levi–Civita connection has zero curvature in inertial coordinates.

## Differential operators

The scalar [[mathematical-physics/dalembert-operator|d’Alembert operator]] is
\[
\Box_\eta=\partial_t^2-\partial_x^2-\partial_y^2-\partial_z^2
\]
in the convention used in this collection. A [[fiber-bundles/spin-structure|spin structure]] and constant spin frame give the [[mathematical-physics/minkowski-dirac-operator|Minkowski Dirac operator]].

## Dimension and notation

The notation \(\mathbb R^{1,3}\) is also used for the underlying quadratic vector space. More generally, \(n\)-dimensional Minkowski spacetime has signature \((1,n-1)\), with negative directions listed first in this collection. Some physics texts instead use \(\eta=\operatorname{diag}(1,-1,-1,-1)\); all signs in wave and Clifford formulas must then be translated together.

## References

1. Barrett O'Neill, *Semi-Riemannian Geometry With Applications to Relativity*, Academic Press, 1983. [Publisher record](https://doi.org/10.1016/C2009-0-03118-3). Relevant: Chapters 1 and 14.
2. Robert M. Wald, *General Relativity*, University of Chicago Press, 1984. [Publisher record](https://press.uchicago.edu/ucp/books/book/chicago/G/bo5952261.html). Relevant: Appendix C.
