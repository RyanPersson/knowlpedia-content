+++
id = "algebraic-geometry-foundations/locally-topologically-ringed-space"
title = "Locally topologically ringed space"
kind = "definition"
summary = "A topological space with a sheaf of topological rings whose underlying ringed space is locally ringed."
aliases = ["locally topological ringed space", "locally ringed space with topological structure sheaf"]
domains = ["algebraic-geometry-foundations", "algebra-topological"]
section_mode = "progressive"
prerequisites = ["topology/topological-space", "algebraic-geometry-foundations/locally-ringed-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **locally topologically ringed space** is a pair
\((X,\mathcal O_X)\) consisting of a
[[topology/topological-space|topological space]] \(X\) and a sheaf
\(\mathcal O_X\) of commutative topological rings such that:

1. every restriction map
   \(\mathcal O_X(U)\to\mathcal O_X(V)\), for \(V\subseteq U\), is continuous;
2. after forgetting the topologies on the rings,
   \((X,\mathcal O_X)\) is a
   [[algebraic-geometry-foundations/locally-ringed-space|locally ringed
   space]].

In the adic formal-scheme setting, the topologies on local sections are
linear topologies defined by ideals, and the structure sheaf is complete for
those topologies.

## Morphisms

A morphism
\[
(f,f^\#):(X,\mathcal O_X)\longrightarrow(Y,\mathcal O_Y)
\]
consists of a continuous map \(f:X\to Y\) and a morphism of structure sheaves
\[
f^\#:\mathcal O_Y\longrightarrow f_*\mathcal O_X
\]
whose maps on sections are continuous and whose induced homomorphisms on
stalks are local. [[algebraic-geometry-foundations/formal-scheme|Formal schemes]] use morphisms of this kind.

## References
The Stacks Project Authors, “Formal schemes à la EGA.”
[Section 87.2, Tag 0AHY](https://stacks.math.columbia.edu/tag/0AHY).
