+++
id = "algebraic-geometry-foundations/ringed-space"
title = "Ringed space"
kind = "definition"
summary = "A topological space equipped with a sheaf of rings."
aliases = ["space with a sheaf of rings", "ringed topological space"]
domains = ["algebraic-geometry-foundations", "category-theory"]
section_mode = "progressive"
+++

A **ringed space** is a pair \((X,\mathcal O_X)\) consisting of a
[[topology/topological-space|topological space]] \(X\) and a
[[algebraic-geometry-foundations/sheaf|sheaf]] of [[algebra-rings/commutative-ring|commutative rings]]
\(\mathcal O_X\) on \(X\). The sheaf \(\mathcal O_X\) is called the
[[algebraic-geometry-foundations/structure-sheaf|structure sheaf]].

A morphism of ringed spaces
\[
(f,f^\#):(X,\mathcal O_X)\longrightarrow(Y,\mathcal O_Y)
\]
consists of a [[topology/continuous-map|continuous map]] \(f:X\to Y\) and a [[algebraic-geometry-foundations/morphism-of-sheaves|morphism of sheaves]] of rings
\[
f^\#:\mathcal O_Y\longrightarrow f_*\mathcal O_X.
\]
The arrow on functions points opposite to the map on spaces: a function near
\(f(x)\) is pulled back to a function near \(x\).

## Stalkwise form

At every \(x\in X\), the sheaf morphism induces a [[algebra-rings/ring-homomorphism|ring homomorphism]]
\[
f_x^\#:\mathcal O_{Y,f(x)}\longrightarrow\mathcal O_{X,x}
\]
between [[algebraic-geometry-foundations/stalk|stalks]]. Composition combines
the continuous maps and these pullback homomorphisms.

## Important refinements

A [[algebraic-geometry-foundations/locally-ringed-space|locally ringed
space]] additionally requires every stalk to be a [[algebra-commutative/local-ring|local ring]] and its
morphisms to induce local homomorphisms on stalks. Schemes, complex
manifolds with their holomorphic functions, and smooth manifolds with their
smooth functions carry such refinements. A bare ringed space imposes no
local-ring condition.

Sheaves of modules and locally free sheaves are defined relative to
\(\mathcal O_X\); the topological space alone is not enough to specify their
scalar multiplication.

## References

1. The Stacks Project Authors, *The Stacks Project*. [Tag 01HY](https://stacks.math.columbia.edu/tag/01HY). Relevant: ringed spaces and morphisms of ringed spaces.
2. Robin Hartshorne, *Algebraic Geometry*, Springer, 1977. [DOI record](https://doi.org/10.1007/978-1-4757-3849-0). Relevant: Chapter II, §1, sheaves and ringed spaces.
