+++
id = "algebraic-geometry-foundations/torsor-condition"
title = "Torsor condition"
kind = "definition"
summary = "The condition that two points in the same fiber differ by a unique group element."
aliases = ["torsor condition", "principal homogeneous space condition"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/group-scheme", "algebra-groups/group-action", "algebraic-geometry-foundations/fiber-product-of-schemes"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
+++

Let \(G\to X\) be a [[algebraic-geometry-foundations/group-scheme|group scheme]] and let \(P\to X\) carry a right [[algebra-groups/group-action|\(G\)-action]]. The **torsor condition** is that \(P\to X\) is a cover in the chosen topology and the morphism

\[
P\times_X G\longrightarrow P\times_X P,
\qquad (p,g)\longmapsto(p,p\cdot g)
\]

is an isomorphism. Thus an ordered pair in one fiber is uniquely a first point together with the group element carrying it to the second. The repeated products are [[algebraic-geometry-foundations/fiber-product-of-schemes|fiber products of schemes]].

## Local triviality

After a covering [[algebraic-geometry-foundations/base-change|base change]] \(U\to X\) admitting a section of \(P_U\to U\), the chosen section supplies an equivariant isomorphism

\[
P_U\cong U\times_X G.
\]

## Remarks

Checking that an action is free and transitive merely on ordinary topological points is generally too weak. Scheme structure, residue fields, and nilpotents are detected by the displayed isomorphism but may be invisible on the underlying point set.
