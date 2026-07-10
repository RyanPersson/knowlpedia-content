+++
id = "algebraic-geometry-foundations/group-scheme"
title = "Group scheme"
kind = "definition"
summary = "A scheme over a base whose multiplication, identity, and inverse are morphisms of schemes."
aliases = ["group scheme", "group object in schemes"]
domains = ["algebraic-geometry-foundations"]
+++

Fix a base [[algebraic-geometry-foundations/scheme|scheme]] \(S\). A **group scheme over \(S\)** is an [[algebraic-geometry-foundations/scheme-over-a-base|\(S\)-scheme]] \(G\to S\) equipped with [[algebraic-geometry-foundations/morphism-of-schemes|morphisms of schemes]] over \(S\)

\[
m:G\times_S G\longrightarrow G,
\qquad e:S\longrightarrow G,
\qquad i:G\longrightarrow G,
\]

called multiplication, identity, and inverse, satisfying the usual [[algebra-groups/group|group]] axioms. The product in the multiplication map is a [[algebraic-geometry-foundations/fiber-product-of-schemes|fiber product over the base]].

## Functor-of-points viewpoint

For every \(S\)-scheme \(T\), the set of \(T\)-valued points

\[
G(T)=\operatorname{Hom}_S(T,G)
\]

is a group, functorially in \(T\). This viewpoint exposes the group law on points defined over every test scheme, including points carrying nilpotent or family-valued information that ordinary geometric points may miss.

## Actions

A right [[algebra-groups/group-action|action]] of \(G\) on an \(S\)-scheme \(P\) is a morphism

\[
P\times_S G\longrightarrow P
\]

over \(S\) satisfying the identity and associativity axioms. Such actions appear in the [[algebraic-geometry-foundations/torsor-condition|torsor condition]].

## Remarks

**Warning.** A group scheme is not merely an abstract group whose elements happen to be scheme points. Its multiplication, identity, and inverse include scheme structure and must be defined over the chosen base \(S\).
