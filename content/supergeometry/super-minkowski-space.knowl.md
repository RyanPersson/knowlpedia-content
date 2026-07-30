+++
id = "supergeometry/super-minkowski-space"
title = "Super-Minkowski space"
kind = "definition"
summary = "The affine superspace of spacetime and spinor coordinates equipped with the Lie supergroup structure integrating supertranslations."
aliases = ["Minkowski superspace", "super Minkowski spacetime", "flat superspace"]
domains = ["supergeometry", "mathematical-physics"]
section_mode = "progressive"
+++

Fix supertranslation data
\((V,S,\Gamma)\), where
\(\Gamma:\operatorname{Sym}^2S\to V\). **Super-Minkowski space** is the
affine supermanifold
\[
\mathbb M^{V|S}=(V,\ C^\infty_V\otimes\Lambda S^*)
\]
equipped with the [[supergeometry/lie-supergroup|Lie supergroup]] structure
integrating the
[[mathematical-physics/supertranslation-algebra|supertranslation algebra]]
\(V_{\bar0}\oplus S_{\bar1}\).

In exponential coordinates, the two-step
[[lie-groups/baker-campbell-hausdorff-formula|Baker–Campbell–Hausdorff
formula]] has the schematic form
\[
(x,\theta)(x',\theta')
=\left(x+x'+\tfrac12\Gamma(\theta,\theta'),
       \theta+\theta'\right),
\]
with the precise displayed signs depending on the convention for
Grassmann-valued points and left versus right actions. The underlying reduced
Lie group is the additive translation group of \(V\).

## Geometric structure used in physics

The odd left-invariant directions define a distinguished distribution
\(\mathcal D\) whose bracket generates translations according to
\[
[\mathcal D,\mathcal D]\longrightarrow \operatorname{im}\Gamma\subseteq TV,
\qquad (s,t)\longmapsto\Gamma(s,t).
\]
When \(\Gamma\ne0\), this distribution is nonintegrable; when \(\Gamma\) is
surjective, it is bracket-generating in all translation directions. Together
with the super-Poincaré action, this structure is part of what makes the
affine supermanifold into flat physical superspace. Superfields are functions
or sections on this space, often constrained by operators built from the
invariant odd directions.

## Distinctions

A general [[supergeometry/superspace|superspace]] is merely a locally
superringed space. Even an affine superdomain \(V^{d|s}\) is not
super-Minkowski space until the spin representation, bilinear map
\(\Gamma\), and corresponding supertranslation structure have been chosen.
Curved supergravity superspaces require further torsion and connection data
and are not super-Minkowski space.

## References

1. P. Deligne and J. W. Morgan, “Notes on supersymmetry (following Joseph Bernstein),” in *Quantum Fields and Strings: A Course for Mathematicians*, Volume 1, American Mathematical Society, 1999, 41–97. Relevant: flat superspace and supertranslations.
2. D. S. Freed, *Five Lectures on Supersymmetry*, American Mathematical Society, 1999. [Publisher record](https://doi.org/10.1090/amsip/011). Relevant: superspace and super-Poincaré geometry.
