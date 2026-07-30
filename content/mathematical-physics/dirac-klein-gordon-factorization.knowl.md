+++
id = "mathematical-physics/dirac-klein-gordon-factorization"
title = "Dirac–Klein–Gordon factorization"
kind = "theorem"
summary = "The free Minkowski Dirac factors multiply to the scalar Klein–Gordon operator up to sign."
aliases = ["Dirac factorization of the Klein-Gordon operator", "squared Dirac equation", "Dirac square factorization"]
domains = ["mathematical-physics", "partial-differential-equations"]
section_mode = "progressive"
+++

Let \(D_{\mathrm M}=\gamma^\mu\partial_\mu\) be the [[mathematical-physics/minkowski-dirac-operator|Minkowski Dirac operator]] with
\[
\{\gamma^\mu,\gamma^\nu\}=-2\eta^{\mu\nu}I,
\qquad
\Box_\eta=-\eta^{\mu\nu}\partial_\mu\partial_\nu.
\]
For every constant \(m\),
\[
(iD_{\mathrm M}-m)(iD_{\mathrm M}+m)
=(iD_{\mathrm M}+m)(iD_{\mathrm M}-m)
=-(\Box_\eta+m^2)I.
\]
Consequently every solution of either massive free [[mathematical-physics/dirac-equation|Dirac equation]] satisfies the [[mathematical-physics/klein-gordon-equation|Klein–Gordon equation]] componentwise.

## Proof

Commutativity of the constant \(m\) with \(D_{\mathrm M}\) cancels the cross terms. The Clifford relation and commutativity of partial derivatives give
\[
D_{\mathrm M}^{\,2}
=\frac12\{\gamma^\mu,\gamma^\nu\}\partial_\mu\partial_\nu
=-\eta^{\mu\nu}\partial_\mu\partial_\nu I
=\Box_\eta I.
\]
Therefore
\[
(iD_{\mathrm M})^2-m^2=-D_{\mathrm M}^{\,2}-m^2
=-(\Box_\eta+m^2)I.
\]

## What the implication does not say

The converse is false without additional data: a tuple of Klein–Gordon solutions need not satisfy a first-order Dirac equation. The factorization selects spinor solutions obeying an extra linear constraint.

## Curvature and gauge warning

On a curved spin manifold, the square of the Dirac operator contains a scalar-curvature term; coupling to a gauge field adds Clifford contraction of its curvature. Thus the free flat identity acquires lower-order corrections. The principal part remains a normally hyperbolic connection operator, but one cannot replace it by the scalar \(\Box_g\) componentwise in an arbitrary frame.

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*, Princeton University Press, 1989. [Publisher record](https://doi.org/10.1515/9781400883912). Relevant: Chapter II, §8.
2. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: §§1.3 and 3.4.
