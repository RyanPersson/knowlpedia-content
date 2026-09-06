+++
id = "algebraic-geometry-foundations/g-torsor-on-a-site"
title = "G-torsor on a site"
kind = "definition"
summary = "A sheaf with a locally trivial simply transitive action of a group sheaf."
aliases = ["G-torsor on a site", "torsor on a site", "sheaf torsor"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/site", "algebraic-geometry-foundations/sheaf-of-groups", "algebra-groups/group-action", "algebra-category-theory/terminal-object", "algebraic-geometry-foundations/covering-family", "algebraic-geometry-foundations/torsor-condition"]
dependency_review_count = 1
+++

Let \(\mathcal C\) be a [[algebraic-geometry-foundations/site|site]], let \(G\) be a [[algebraic-geometry-foundations/sheaf-of-groups|sheaf of groups]] on \(\mathcal C\), and let \(P\) be a sheaf with a right [[algebra-groups/group-action|\(G\)-action]]. The sheaf \(P\) is a **right \(G\)-torsor** if:

1. \(P\) is locally inhabited: the [[algebra-category-theory/terminal-object|terminal object]] has a [[algebraic-geometry-foundations/covering-family|covering family]] \(\{U_i\to 1\}\) for which \(P(U_i)\neq\varnothing\); and
2. the action is simply transitive, expressed by the isomorphism of sheaves

\[
P\times G \longrightarrow P\times P,
\qquad (p,g)\longmapsto(p,p\cdot g).
\]

Equivalently, there is a cover on which \(P\) is \(G\)-equivariantly isomorphic to \(G\) acting on itself by right translation. When \(P\), \(G\), and the base are represented by [[algebraic-geometry-foundations/scheme|schemes]], this becomes the geometric [[algebraic-geometry-foundations/torsor-condition|torsor condition]].

## Guiding picture

A torsor is “a group with the origin forgotten.” Once one chooses a local point \(p\in P\), every other local point can be written uniquely as \(p\cdot g\). Choosing a different point changes the coordinate system, but not the torsor.

The model to keep in mind is a finite [[algebra-fields-galois/galois-extension|Galois extension]] \(K/F\). Over \(X=\operatorname{Spec}F\), the space \(P=\operatorname{Spec}K\) has no preferred point, but after passing to the étale cover \(P\to X\), it looks like one freely movable copy of its [[algebra-fields-galois/galois-group|Galois group]] over every base point.

## Reading the torsor map

The map \((p,g)\mapsto(p,p\cdot g)\) being an isomorphism says exactly that, for any two points in the same local fiber, there is one and only one group element carrying the first to the second. It packages freeness and transitivity into a statement that continues to work for sheaves and schemes.

## Remarks

**Warning.** “Locally” refers to the chosen [[algebraic-geometry-foundations/grothendieck-topology|Grothendieck topology]] on the site. An étale torsor need not be locally trivial in the [[algebra-commutative/zariski-topology|Zariski topology]], and a torsor here is not automatically a smooth principal bundle on a manifold.
