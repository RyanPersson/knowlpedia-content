+++
id = "algebraic-geometry-foundations/principal-g-bundle-on-scheme"
title = "Principal G-bundle on a scheme"
kind = "definition"
summary = "A G-torsor over a scheme in a specified Grothendieck topology."
aliases = ["algebraic principal G-bundle", "G-bundle on a scheme"]
domains = ["algebraic-geometry-foundations", "langlands"]
section_mode = "progressive"
+++

Let \(G\) be a group scheme over a base \(S\), and let \(X\) be an
\(S\)-scheme. A **principal \(G\)-bundle on \(X\)** is a
[[algebraic-geometry-foundations/g-torsor-on-a-site|\(G\)-torsor]] on a
specified site of \(X\), commonly the fppf or étale site. Equivalently, it is
an \(X\)-scheme \(P\to X\) with a right \(G\)-action that is locally
isomorphic to \(G\times_S X\), with \(G\) acting on itself by translation.

The torsor identity is expressed by the isomorphism
\[
P\times_S G \longrightarrow P\times_XP,\qquad (p,g)\longmapsto(p,pg).
\]

## Relation to differential geometry

When \(k=\mathbb C\), analytification produces a holomorphic principal bundle.
Its underlying smooth bundle is a
[[fiber-bundles/principal-g-bundle|smooth principal bundle]], but passing
between algebraic, holomorphic, and smooth categories requires comparison
results and can lose structure.

## Moduli

Allowing \(P\) to vary in families over test schemes gives the
[[algebraic-geometry-foundations/moduli-stack-of-g-bundles-on-a-curve|moduli
stack of \(G\)-bundles]].

## References

1. Alexander Grothendieck, “Technique de descente et théorèmes d’existence en
   géométrie algébrique. I. Généralités. Descente par morphismes fidèlement
   plats,” *Séminaire Bourbaki* 190 (1959–1960).
