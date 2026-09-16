+++
id = "lie-groups/smooth-vector-frechet-topology"
title = "Fréchet topology on smooth vectors"
kind = "definition"
summary = "The complete topology that controls every finite iterated representation derivative."
aliases = ["smooth-vector topology", "smooth-vector Fréchet space"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/derived-representation-on-smooth-vectors", "functional-analysis/frechet-space", "functional-analysis/topology-generated-by-seminorms"]
+++

Let \(\pi\) be a strongly continuous unitary representation of a finite-dimensional Lie group on \(H\), and choose a real Lie-algebra basis \(X_1,\ldots,X_m\). The **smooth-vector topology** on \(H^\infty\) is the [[functional-analysis/topology-generated-by-seminorms|topology generated]] by the norms
\[
p_k(v)^2=\sum_{r=0}^k\ \sum_{j_1,\ldots,j_r=1}^m
\|d\pi(X_{j_1})\cdots d\pi(X_{j_r})v\|_H^2,
\qquad k\geq0,
\]
where the \(r=0\) term is \(\|v\|_H^2\). The operators are the [[lie-groups/derived-representation-on-smooth-vectors|derived action]] on smooth vectors. This topology makes \(H^\infty\) a [[functional-analysis/frechet-space|Fréchet space]] and is independent of the chosen basis.

## Convergence and completeness

Convergence means convergence in \(H\) of the vectors and of every ordered representation derivative. Equivalently, the topology is defined by \(v\mapsto\|d\pi(D)v\|\) for all elements \(D\) of the [[lie-groups/universal-enveloping-algebra|universal enveloping algebra]], including its unit.

Completeness follows by realizing smooth vectors as the closed subspace of smooth equivariant maps in \(C^\infty(G,H)\) through their orbit maps. Finite-dimensional changes of Lie-algebra basis express each word of length at most \(k\) as a finite linear combination of words of the same maximal length, proving equivalence of the norm families.

## Continuous infinitesimal action

The estimate
\[
p_k(d\pi(X_j)v)\leq p_{k+1}(v)
\]
shows that every derived operator is continuous on \(H^\infty\). By linearity this holds for every \(X\in\mathfrak g\), and compositions remain continuous. The group action on this Fréchet space is smooth.

## Hilbert norm versus smooth-vector topology

The inclusion \(H^\infty\hookrightarrow H\) is continuous because \(p_0=\|\cdot\|_H\). Its inherited inner product generally makes it an incomplete pre-Hilbert space; completeness above refers to the stronger topology. An operator may be continuous for the smooth-vector topology while being unbounded in the Hilbert norm.

## References

1. Gerrit van Dijk, Karl-Hermann Neeb, Hadi Salmasian, and Christoph Zellner, [*On the characterization of trace class representations and Schwartz operators*](https://arxiv.org/abs/1512.02451). §1, opening description of the smooth-vector Fréchet topology.
2. Karl-Hermann Neeb, [*On Differentiable Vectors for Representations of Infinite Dimensional Lie Groups*](https://arxiv.org/abs/1002.1602). Theorem 4.4 and Proposition 5.4.
