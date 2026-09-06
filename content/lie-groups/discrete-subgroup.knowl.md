+++
id = "lie-groups/discrete-subgroup"
title = "Discrete subgroup"
kind = "knowl"
summary = "A subgroup that is discrete in the manifold topology; its Lie algebra is zero."
aliases = ["discrete-subgroup", "Discrete subgroup"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/discrete-subgroup.md"
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]].

A subgroup \(\Gamma\le G\) is **discrete** if it is a discrete subset in the subspace topology (equivalently, every \(\gamma\in\Gamma\) is isolated in \(G\)).

## Basic Lie-theoretic consequences
- Any discrete subgroup is automatically closed; hence by the [[lie-groups/closed-subgroup-theorem|Closed Subgroup Theorem]] it is an embedded [[lie-groups/lie-subgroup|Lie subgroup]].
- The Lie algebra of a discrete subgroup is trivial:
  \[
  \mathrm{Lie}(\Gamma)=0,
  \]
  because there are no nontrivial smooth curves in \(\Gamma\) through the identity.

If \(\Gamma\) is also [[lie-groups/normal-lie-subgroup|normal]], then \(G/\Gamma\) is a Lie group and the projection \(G\to G/\Gamma\) is a [[lie-groups/covering-lie-group|covering homomorphism]].

## Examples
- \(\mathbb Z^n\) is a discrete subgroup of \(\mathbb R^n\) (additively).
- The subgroup \(\{\pm I\}\) is discrete in [[lie-groups/example-su2|\(SU(2)\)]] and is the kernel of the standard covering \(SU(2)\to SO(3)\) (compare [[lie-groups/example-so3|\(SO(3)\)]]).

**Context.** Discrete subgroups appear as “global” corrections to Lie-algebraic data: different discrete central quotients of a simply connected group yield different Lie groups with the same Lie algebra.
