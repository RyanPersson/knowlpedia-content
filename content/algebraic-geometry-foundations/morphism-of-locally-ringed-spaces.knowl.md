+++
id = "algebraic-geometry-foundations/morphism-of-locally-ringed-spaces"
title = "Morphism of locally ringed spaces"
kind = "definition"
summary = "A continuous map with a compatible sheaf map that is local on every stalk."
aliases = ["morphism of locally ringed spaces", "locally ringed space morphism"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/locally-ringed-space", "topology/continuous-map", "algebraic-geometry-foundations/morphism-of-sheaves", "algebraic-geometry-foundations/direct-image-sheaf", "algebraic-geometry-foundations/stalk", "algebra-commutative/local-ring"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((X,\mathcal O_X)\) and \((Y,\mathcal O_Y)\) be [[algebraic-geometry-foundations/locally-ringed-space|locally ringed spaces]]. A **morphism of locally ringed spaces** \(f:X\to Y\) consists of

1. a [[topology/continuous-map|continuous map]] \(f:X\to Y\), and
2. a [[algebraic-geometry-foundations/morphism-of-sheaves|morphism of sheaves of rings]] into the [[algebraic-geometry-foundations/direct-image-sheaf|direct image sheaf]]

\[
f^\#:\mathcal O_Y\longrightarrow f_*\mathcal O_X,
\]

such that for every \(x\in X\), the induced map on [[algebraic-geometry-foundations/stalk|stalks]]

\[
f_x^\#:\mathcal O_{Y,f(x)}\longrightarrow\mathcal O_{X,x}
\]

is a local homomorphism of [[algebra-commutative/local-ring|local rings]]. This means that the inverse image of the maximal ideal of \(\mathcal O_{X,x}\) is the maximal ideal of \(\mathcal O_{Y,f(x)}\).

The local condition ensures that functions vanishing at \(f(x)\) pull back to functions vanishing at \(x\). A [[algebraic-geometry-foundations/morphism-of-schemes|morphism of schemes]] is precisely a morphism of locally ringed spaces between schemes.
