+++
id = "lie-groups/lie-subgroup"
title = "Lie Subgroup"
kind = "knowl"
summary = "A subgroup of a Lie group that carries a compatible immersed submanifold structure."
aliases = ["lie-subgroup", "Lie Subgroup"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/lie-subgroup.md"
prerequisites = ["fiber-bundles/lie-group", "fiber-bundles/smooth-manifold", "algebra-groups/subgroup", "fiber-bundles/smooth-immersion"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]]. A **Lie subgroup** of \(G\) is a subgroup \(H\le G\) together with a Lie group structure such that the inclusion map
\[
i:H\hookrightarrow G
\]
is a [[fiber-bundles/smooth-immersion|smooth immersion]] and a group homomorphism.

## Embedded Lie subgroups

A Lie subgroup is called **embedded** if \(i\) is an embedding (so \(H\) is an actual submanifold of \(G\)).

## Closed subgroups
A crucial fact is the [[lie-groups/closed-subgroup-theorem|closed subgroup theorem]]: if \(H\) is a closed subgroup of \(G\) (as a subset), then \(H\) is an embedded Lie subgroup.

## Relationship to Lie algebras
The Lie algebra \(\mathfrak{h}=T_eH\) identifies with a [[lie-groups/lie-subalgebra|Lie subalgebra]] of \(\mathfrak{g}=T_eG\); see [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of a Lie group]].

## Quotients
If \(H\) is closed, the coset space \(G/H\) carries a natural smooth structure for which \(G\to G/H\) is a submersion. When \(H\) is also normal, \(G/H\) is a [[lie-groups/quotient-lie-group|quotient Lie group]].

## Examples
- \(\operatorname{SO}(n)\le \operatorname{GL}(n,\mathbb{R})\).
- The diagonal matrices form a Lie subgroup of \(\operatorname{GL}(n,\mathbb{R})\).
