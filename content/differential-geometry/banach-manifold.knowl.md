+++
id = "differential-geometry/banach-manifold"
title = "Smooth Banach manifold"
kind = "definition"
summary = "A manifold modeled on a Banach space, with smooth transition maps in the norm derivative sense."
aliases = ["Banach manifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["linear-algebra/banach-space", "topology/hausdorff-space", "topology/homeomorphism", "real-analysis/frechet-derivative"]
+++

A **smooth Banach manifold** modeled on a real [[linear-algebra/banach-space|Banach space]] \(E\) is a [[topology/hausdorff-space|Hausdorff space]] \(M\) with a maximal atlas of [[topology/homeomorphism|homeomorphisms]]
\[
\phi_i:U_i\longrightarrow V_i\subseteq E,
\]
where the \(U_i\) cover \(M\), the \(V_i\) are open, and all transition maps \(\phi_j\circ\phi_i^{-1}\) are \(C^\infty\). Here \(C^\infty\) means that all iterated [[real-analysis/frechet-derivative|Fréchet derivatives]] exist and depend continuously on the point in the corresponding operator norms.

## Smooth maps and Hilbert-valued orbit maps

A map between Banach manifolds is smooth when its expressions in charts are smooth. A Hilbert space is itself a Banach manifold. Thus a map from a finite-dimensional Lie group to a Hilbert space has an unambiguous notion of norm smoothness, even when its range is infinite-dimensional.

This is the smoothness used for the orbit maps defining [[lie-groups/smooth-vector-unitary-representation|smooth vectors]]. It does not ask that an operator-valued representation be smooth in operator norm.

## Conventions

When \(E=\mathbb R^n\), this recovers the local chart definition of a finite-dimensional smooth manifold. Global countability and paracompactness assumptions are imposed separately here; neither is part of the displayed local definition. Complex Banach spaces may be used as real model spaces; holomorphic transition maps are an additional condition.

## References

1. Karl-Hermann Neeb, [*On Differentiable Vectors for Representations of Infinite Dimensional Lie Groups*](https://arxiv.org/abs/1002.1602). §2, Definition 2.1 and the ensuing manifold construction, specialized to Banach spaces.
