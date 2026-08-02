+++
id = "differential-geometry/homotopy-invariance-of-de-rham-cohomology"
title = "Homotopy invariance of de Rham cohomology"
kind = "theorem"
summary = "Smoothly homotopic maps induce the same pullback homomorphism on de Rham cohomology."
aliases = ["smooth-homotopy invariance of de Rham cohomology"]
domains = ["differential-geometry", "topology"]
section_mode = "progressive"
+++

Let \(f_0,f_1:M\to N\) be [[fiber-bundles/smooth-map|smooth maps]] between [[fiber-bundles/smooth-manifold|smooth manifolds]]. If \(f_0\) and \(f_1\) are joined by a [[differential-geometry/smooth-homotopy|smooth homotopy]], then their pullbacks induce the same homomorphism on every [[fiber-bundles/de-rham-cohomology-group|de Rham cohomology group]]:
\[
f_0^*=f_1^*:H_{\mathrm{dR}}^k(N)\longrightarrow H_{\mathrm{dR}}^k(M).
\]
Indeed, the associated [[differential-geometry/de-rham-homotopy-operator|de Rham homotopy operator]] \(K\) satisfies
\[
f_1^*-f_0^*=dK+Kd.
\]
Hence the difference of the endpoint pullbacks is cochain-homotopic to zero and vanishes on cohomology.
The conclusion holds in every degree and is natural with respect to composition by smooth maps.

## Consequences

A smooth [[topology/homotopy-equivalence|homotopy equivalence]] induces an isomorphism on de Rham cohomology. In particular, a smooth deformation retract has the same de Rham cohomology as the retract. This makes \(H_{\mathrm{dR}}^*\) a [[algebra-category-theory/contravariant-functor|contravariant functor]] on the smooth homotopy category, not merely on the [[differential-geometry/category-of-smooth-manifolds|category of smooth manifolds]].

## Canonical example

The radial homotopy \(F(x,t)=tx\) contracts \(\mathbb R^n\) to the origin. Homotopy invariance therefore gives
\[
H_{\mathrm{dR}}^0(\mathbb R^n)\cong\mathbb R,\qquad
H_{\mathrm{dR}}^k(\mathbb R^n)=0\quad(k>0).
\]
At the level of forms, the same homotopy operator supplies primitives for closed forms of positive degree, which is the usual star-shaped-domain proof of the [[differential-geometry/poincare-lemma|Poincaré lemma]].

## Scope

The theorem concerns smooth homotopies and ordinary de Rham cohomology. A continuous homotopy between smooth maps can be replaced by a smooth one under the standard smoothing theorem, but that extra step is not part of the chain-homotopy formula. Compact-support, relative, and boundary-condition variants require the homotopy operator to preserve the relevant support or restriction conditions.

## References

1. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [Springer DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: Chapter I, §4, homotopy operators and homotopy invariance.
2. Loring W. Tu, *An Introduction to Manifolds*, 2nd ed., Springer, 2011. [Springer DOI record](https://doi.org/10.1007/978-1-4419-7400-6). Relevant: Chapter 17, homotopy operator and induced maps on de Rham cohomology.
