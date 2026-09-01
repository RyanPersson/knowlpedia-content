+++
id = "lie-groups/effective-action"
title = "Effective action"
kind = "knowl"
summary = "A Lie group action whose only element fixing every point is the identity."
aliases = ["effective-action", "Effective action"]
domains = ["lie-groups"]
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "lie-groups/effective-action.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] acting smoothly on a manifold \(M\). The **kernel of the action** is
\[
\ker(G\curvearrowright M) := \{g\in G : g\cdot x = x \text{ for all }x\in M\}.
\]
The action is **effective** if \(\ker(G\curvearrowright M)=\{e\}\).

## Basic structure
- The kernel is a closed [[lie-groups/normal-lie-subgroup|normal Lie subgroup]] of \(G\).
- Every action factors through an effective action of the quotient group:
  the induced action of \(G/\ker(G\curvearrowright M)\) on \(M\) is effective and has the same [[lie-groups/orbit-lie-group|orbits]].

## Motivation
An ineffective action contains group elements that are invisible on \(M\); passing to the quotient by the kernel removes this redundancy.
