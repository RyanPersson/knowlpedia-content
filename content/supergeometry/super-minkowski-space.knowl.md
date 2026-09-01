+++
id = "supergeometry/super-minkowski-space"
title = "Super-Minkowski space"
kind = "definition"
summary = "The affine superspace of spacetime and spinor coordinates equipped with the Lie supergroup structure integrating supertranslations."
aliases = ["Minkowski superspace", "super Minkowski spacetime"]
domains = ["supergeometry", "mathematical-physics"]
prerequisites = ["supergeometry/lie-supergroup", "mathematical-physics/supertranslation-algebra", "lie-groups/baker-campbell-hausdorff-formula", "supergeometry/supertranslation-distribution"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
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

More precisely, let \(A\) be a real Grassmann algebra. On \(A\)-points, write
\(\Gamma_A(\theta,\theta')=[\theta,\theta']\) for the bracket induced from
\(\Gamma\) on \(A_{\bar1}\otimes S\). In exponential coordinates the exact
two-step
[[lie-groups/baker-campbell-hausdorff-formula|Baker–Campbell–Hausdorff
formula]] is
\[
(x,\theta)(x',\theta')
=\left(x+x'+\tfrac12\Gamma_A(\theta,\theta'),
       \theta+\theta'\right),
\]
where \(x,x'\in A_{\bar0}\otimes V\) and
\(\theta,\theta'\in A_{\bar1}\otimes S\). Defining \(\Gamma_A\) as the
induced bracket fixes the scalar sign convention in the displayed formula.
The underlying reduced Lie group is the additive translation group of \(V\).

Its odd left-invariant directions form the
[[supergeometry/supertranslation-distribution|supertranslation
distribution]], whose Levi bracket is induced by \(\Gamma\).

## Distinctions

A general [[supergeometry/superspace|superspace]] is merely a locally
superringed space. Even an affine superdomain \(V^{d|s}\) is not
super-Minkowski space until the spin representation, [[algebra-modules/bilinear-map|bilinear map]]
\(\Gamma\), and corresponding supertranslation structure have been chosen.
Curved supergravity superspaces require further torsion and connection data
and are not super-Minkowski space.

## References

1. P. Deligne and J. W. Morgan, “Notes on supersymmetry (following Joseph Bernstein),” in *Quantum Fields and Strings: A Course for Mathematicians*, Volume 1, American Mathematical Society, 1999, 41–97. Relevant: flat superspace and supertranslations.
2. D. S. Freed, *Five Lectures on Supersymmetry*, American Mathematical Society, 1999. [Publisher record](https://doi.org/10.1090/amsip/011). Relevant: superspace and super-Poincaré geometry.
