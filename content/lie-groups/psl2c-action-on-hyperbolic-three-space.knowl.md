+++
id = "lie-groups/psl2c-action-on-hyperbolic-three-space"
title = "PSL(2,C) action on hyperbolic three-space"
kind = "theorem"
summary = "PSL(2,C) is the orientation-preserving isometry group of hyperbolic three-space."
aliases = ["PSL2C hyperbolic action", "orientation-preserving isometries of H3"]
domains = ["lie-groups", "differential-geometry"]
section_mode = "progressive"
+++

On the positive-definite Hermitian-matrix model of [[differential-geometry/hyperbolic-three-space|\(\mathbb H^3\)]], the formula
\[
H\longmapsto AHA^\dagger,\qquad A\in SL(2,\mathbb C),
\]
is isometric and has kernel \(\{\pm I\}\). It induces an isomorphism of real Lie groups
\[
PSL(2,\mathbb C)_{\mathbb R}
\xrightarrow{\;\sim\;}
\operatorname{Isom}^+(\mathbb H^3).
\]

## Relation to the Lorentz model

Under the determinant-one hyperboloid model, this is the restriction of the [[lie-groups/sl2c-spin-cover-of-lorentz-group|spin-cover action]] to the sheet \(q(v)=-1,\ t>0\). Consequently,
\[
\operatorname{Isom}^+(\mathbb H^3)
\cong SO^+(1,3)
\cong PSL(2,\mathbb C)_{\mathbb R}.
\]
These isomorphisms are in the category of real Lie groups.

## Boundary action and quotients

The action extends continuously to \(\partial_\infty\mathbb H^3\cong\mathbb{CP}^1\), where it is the [[lie-groups/celestial-sphere-and-mobius-action|Möbius action]]. Thus a [[lie-groups/discrete-subgroup|discrete subgroup]] \(\Gamma<PSL(2,\mathbb C)\) acts simultaneously on \(\mathbb H^3\) and its sphere at infinity. The quotient \(\Gamma\backslash\mathbb H^3\) is a hyperbolic orbifold, and is a manifold when \(\Gamma\) acts freely. Arithmetic choices of \(\Gamma\) connect this geometry with automorphic forms and representation theory.

## References

1. John G. Ratcliffe, *Foundations of Hyperbolic Manifolds*, 3rd ed., Springer, 2019, §§3.2–3.3 and 4.5. [Publisher record](https://doi.org/10.1007/978-3-030-31597-9).
2. Alan F. Beardon, *The Geometry of Discrete Groups*, Springer, 1983, Chapters 4 and 7. [Publisher record](https://doi.org/10.1007/978-1-4612-1146-4).
