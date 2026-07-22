The \(n\)-sphere is
\[
S^n=\{x\in\mathbb R^{n+1}:\lVert x\rVert=1\}.
\]
A smooth \(n\)-manifold \(M\) is a topological manifold with smoothly compatible coordinate charts. Two spaces are homotopy equivalent when there are continuous maps \(f:M\to S^n\) and \(g:S^n\to M\) whose composites are homotopic to the respective identity maps. A smooth homotopy \(n\)-sphere is a closed smooth \(n\)-manifold homotopy equivalent to \(S^n\).

A diffeomorphism is a smooth bijection with smooth inverse. It is stronger data than a homeomorphism, so the smooth and topological forms of the Poincaré conjecture are genuinely different.

## Conjecture

Every smooth homotopy \(4\)-sphere is diffeomorphic to the standard sphere \(S^4\). Equivalently, if a smooth four-manifold \(M\) is homotopy equivalent to \(S^4\), then there exists a diffeomorphism \(M\cong S^4\).

The phrase “standard sphere” refers not only to the underlying topological space but to its usual smooth structure. A counterexample would be an exotic \(4\)-sphere: a manifold homeomorphic, and hence homotopy equivalent, to \(S^4\) but not diffeomorphic to it.

## Known boundary

The topological four-dimensional Poincaré conjecture is known: a topological four-manifold homotopy equivalent to \(S^4\) is homeomorphic to it. The smooth four-dimensional statement remains open. Smooth Poincaré is also known in several other dimensions, but the behavior of smooth structures is dimension-sensitive.

## Formal source

This page follows `FormalConjectures/Millenium/Poincare.lean`, which separates the topological predicate `ConjectureFor n` from the smooth predicate `SmoothConjectureFor n`.
