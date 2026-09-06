+++
id = "lie-groups/free-action-lie"
title = "Free smooth Lie group action"
kind = "knowl"
summary = "A Lie group action is free if all stabilizers are trivial."
aliases = ["free-action-lie", "Free smooth Lie group action"]
domains = ["lie-groups"]
prerequisites = ["fiber-bundles/lie-group", "lie-groups/smooth-action-lie-group", "lie-groups/stabilizer-lie-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "lie-groups/free-action-lie.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] acting smoothly on a manifold \(M\) via a [[lie-groups/smooth-action-lie-group|smooth action]] \(G\times M\to M\), \((g,p)\mapsto g\cdot p\).

**Definition (Free action).**
The action is **free** if for every \(p\in M\), the [[lie-groups/stabilizer-lie-group|stabilizer]]
\[
G_p=\{g\in G: g\cdot p=p\}
\]
is trivial, i.e. \(G_p=\{e\}\).

## Equivalent characterizations

Equivalently, for each \(p\in M\), the orbit map \(G\to M\), \(g\mapsto g\cdot p\), is injective. It is then an injective immersion onto the [[lie-groups/orbit-lie-group|orbit]]; it is an embedding, and hence identifies the orbit diffeomorphically with \(G\), when the action is also proper.

## Remarks

**Motivation.**
Free actions are the infinitesimal starting point for principal bundles: when an action is free and proper, the orbit space \(M/G\) is a manifold and \(M\to M/G\) becomes a principal \(G\)-bundle; in the special case when the action is also transitive, \(M\) is a [[lie-groups/principal-homogeneous-space|principal homogeneous space]].
