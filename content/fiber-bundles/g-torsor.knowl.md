+++
id = "fiber-bundles/g-torsor"
title = "G-torsor"
kind = "definition"
summary = "A nonempty set or smooth space with a free and transitive action of a group G."
aliases = ["principal homogeneous G-space", "G-principal homogeneous space", "right G-torsor"]
domains = ["fiber-bundles", "group-theory"]
prerequisites = ["algebra-groups/group", "algebra-groups/group-action", "fiber-bundles/lie-group"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[algebra-groups/group|group]]. A **right \(G\)-torsor** is a
nonempty set \(T\) with a right [[algebra-groups/group-action|action]] of \(G\)
that is free and transitive. Equivalently, for every \(t,t'\in T\), there is a
unique \(g\in G\) such that \(t'=tg\). In the smooth setting, \(G\) is a
[[fiber-bundles/lie-group|Lie group]], \(T\) is a smooth manifold, and the
action is smooth.

## A copy of a group without an origin

Choosing \(t_0\in T\) gives a \(G\)-equivariant bijection

\[
G\longrightarrow T,
\qquad
g\longmapsto t_0g.
\]

Thus a torsor becomes a copy of \(G\) after choosing a basepoint, but it has no
preferred identity element. If \(t_1=t_0h\) is chosen instead, the resulting
coordinates differ by left multiplication by \(h^{-1}\).

## Relation to principal bundles

For a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]]
\(\pi:P\to M\), every fiber \(P_x=\pi^{-1}(x)\) is canonically a right
\(G\)-torsor. A [[fiber-bundles/section-of-a-fiber-bundle|local section]]
chooses one point in each fiber over an open set and therefore identifies those
torsors smoothly with copies of \(G\). The absence of a global compatible
choice is one way to express the twisting of a nontrivial principal bundle.

## Morphisms and automorphisms

A morphism of right \(G\)-torsors is a \(G\)-equivariant map. Every such map
between nonempty torsors is an isomorphism. After choosing a point of a right
torsor, its \(G\)-equivariant automorphisms identify with left translations by
\(G\); changing the chosen point changes this identification by conjugation.

## References

1. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: principal bundles and principal homogeneous spaces.
2. Norman Steenrod, *The Topology of Fibre Bundles*, Princeton University Press, 1951. [Publisher record](https://press.princeton.edu/books/paperback/9780691005485/the-topology-of-fibre-bundles). Relevant: principal bundles and coordinate bundles.
