+++
id = "algebraic-geometry-foundations/principal-g-bundle-on-scheme"
title = "Principal G-bundle on a scheme"
kind = "definition"
summary = "A G-torsor over a scheme in a specified Grothendieck topology."
aliases = ["algebraic principal G-bundle", "G-bundle on a scheme"]
domains = ["algebraic-geometry-foundations", "langlands"]
prerequisites = ["algebraic-geometry-foundations/group-scheme", "algebraic-geometry-foundations/g-torsor-on-a-site"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[algebraic-geometry-foundations/group-scheme|group scheme]] over a base \(S\), and let \(X\) be an
\(S\)-scheme. A **principal \(G\)-bundle on \(X\)** is a
[[algebraic-geometry-foundations/g-torsor-on-a-site|\(G_X\)-torsor]] on a
specified site of \(X\), commonly the fppf or étale site, whose underlying
torsor is represented by an \(X\)-scheme \(P\). Thus \(P\to X\) has a right
action of \(G_X=G\times_SX\) and is locally \(G_X\)-equivariantly isomorphic
to \(G_X\), with \(G_X\) acting on itself by translation.

The torsor identity is expressed by the isomorphism
\[
P\times_S G \longrightarrow P\times_XP,\qquad (p,g)\longmapsto(p,pg).
\]

## Relation to differential geometry

When \(S=\operatorname{Spec}\mathbb C\), \(G\) is a complex [[algebraic-geometry-foundations/algebraic-group|algebraic group]],
and \(X\) is a complex algebraic variety, analytification produces a
holomorphic principal \(G(\mathbb C)\)-bundle. Its underlying smooth bundle is
a
[[fiber-bundles/principal-g-bundle|smooth principal bundle]], but passing
between algebraic, holomorphic, and smooth categories requires comparison
results and can lose structure.

## Moduli

When \(X\) is a fixed curve, allowing \(P\) to vary in families over test
schemes gives the
[[algebraic-geometry-foundations/moduli-stack-of-g-bundles-on-a-curve|moduli
stack of \(G\)-bundles]].

## References

1. Alexander Grothendieck, “Technique de descente et théorèmes d’existence en
   géométrie algébrique. I. Généralités. Descente par morphismes fidèlement
   plats,” *Séminaire Bourbaki* 190 (1959–1960).
