+++
id = "lie-groups/orbit-lie-group"
title = "Orbit of a Lie group action"
kind = "knowl"
summary = "The set of points reachable from x under the action; it is an immersed homogeneous space."
aliases = ["orbit-lie-group", "Orbit of a Lie group action"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/orbit-lie-group.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] acting smoothly on a manifold \(M\), and fix \(x\in M\). The **orbit of \(x\)** is
\[
G\cdot x=\{g\cdot x \mid g\in G\}\subseteq M.
\]

The **orbit map** is \(\Phi_x:G\to M\), \(\Phi_x(g)=g\cdot x\). Its stabilizer is
\[
G_x=\{g\in G:g\cdot x=x\},
\]
a closed [[lie-groups/stabilizer-lie-group|Lie subgroup]] of \(G\).

## Orbit as a homogeneous space

The orbit map descends to a smooth map
\[
\overline{\Phi}_x: G/G_x \to M
\]
from the [[lie-groups/coset-space|coset space]] \(G/G_x\), with image \(G\cdot x\). This map is an immersion, so the orbit is an immersed submanifold. If the action is [[lie-groups/proper-action-lie|proper]], it is an embedding.

Thus each orbit carries a canonical structure of a [[lie-groups/homogeneous-space|homogeneous space]] for \(G\).

## Tangent space description
The differential of the orbit map at the identity gives the infinitesimal action map
\[
d(\Phi_x)_e:\mathfrak g \to T_xM,
\]

and its image is \(T_x(G\cdot x)\).

## Remarks
The action is [[lie-groups/transitive-action-lie|transitive]] exactly when it has one orbit.
