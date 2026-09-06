+++
id = "lie-groups/transitive-action-lie"
title = "Transitive Lie group action"
kind = "knowl"
summary = "A smooth Lie group action is transitive when it has a single orbit, making the manifold a homogeneous space."
aliases = ["transitive-action-lie", "Transitive Lie group action"]
domains = ["lie-groups"]
prerequisites = []
dependency_review_count = 1
legacy_source_path = "lie-groups/transitive-action-lie.md"
+++

Let \(G\) be a Lie group acting smoothly on a manifold \(M\). The action is **transitive** if, for every \(x,y\in M\), there exists \(g\in G\) such that
\[
g\cdot x = y.
\]

## Homogeneous space description
Fix \(x_0\in M\), and let \(H=G_{x_0}\) be its [[lie-groups/stabilizer-lie-group|stabilizer subgroup]]. The subgroup \(H\) is closed, and the orbit map induces
\[
G/H \to M,\quad gH\mapsto g\cdot x_0.
\]

For a smooth transitive action, this map is a diffeomorphism, so \(M\) is the [[lie-groups/homogeneous-space|homogeneous space]] \(G/H\).

## Context
Transitive actions encode geometries with a large symmetry group. Many classical manifolds arise as homogeneous spaces, and invariants on \(M\) can often be studied through the stabilizer \(H\).

## Equivalent characterizations
Equivalently, for some—and hence every—\(x\in M\), the [[lie-groups/orbit-lie-group|orbit]] \(G\cdot x\) is all of \(M\).
