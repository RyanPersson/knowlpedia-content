+++
id = "fiber-bundles/invariant-function"
title = "Invariant function"
kind = "knowl"
summary = "A smooth function constant along the orbits of a Lie group action."
aliases = ["invariant-function", "Invariant function"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/invariant-function.md"
+++

Let \(G\) act smoothly on a manifold \(M\).

A smooth function \(f:M\to \mathbb{R}\) is **\(G\)-invariant** if
\[
f(g\cdot x)=f(x)\qquad\text{for all }g\in G,\ x\in M.
\]

## Equivalent characterizations

Equivalently, \(f\) is constant on each [[fiber-bundles/orbit-of-a-group-action|orbit]]. It therefore factors uniquely as a set map through the quotient:
\[
f=\bar f\circ\pi,\qquad \pi:M\to M/G,\quad \bar f:M/G\to\mathbb R.
\]
When \(M/G\) has a smooth structure for which \(\pi\) is a submersion, \(\bar f\) is smooth.

## Examples
1. **Radial functions.** For the \(SO(n)\)-action on \(\mathbb{R}^n\), the norm \(x\mapsto \|x\|\) and any function of \(\|x\|\) are invariant.
2. **Pullbacks from a quotient.** If \(\pi:P\to B\) is a principal bundle, then any smooth \(h:B\to\mathbb{R}\) gives an invariant function \(h\circ \pi\) on \(P\).
3. **Transitive actions.** If the action is transitive (one orbit), for instance \(\mathbb{R}^n\) acting on itself by translations, then every invariant smooth function is constant.
