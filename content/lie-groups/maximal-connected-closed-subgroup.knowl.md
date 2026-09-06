+++
id = "lie-groups/maximal-connected-closed-subgroup"
title = "Maximal connected closed subgroup"
kind = "definition"
summary = "A proper connected closed subgroup maximal among connected closed subgroups."
aliases = ["maximal connected subgroup", "maximal connected proper closed subgroup"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group", "algebra-groups/proper-subgroup"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]]. A **maximal connected closed subgroup** is a [[algebra-groups/proper-subgroup|proper subgroup]] \(H<G\) that is connected and closed, and for which every connected closed subgroup \(K\) satisfying
\[
H\subseteq K\subseteq G
\]
is either \(H\) or \(G\).

## What maximality does not say

The adjective “connected” restricts the competitors \(K\). Thus \(H\) can be maximal among proper connected closed subgroups while lying inside a proper **disconnected** closed subgroup of \(G\). Consequently, “maximal connected closed subgroup” is weaker than “maximal closed subgroup.”

The term also does not mean merely the [[topology/connected-component|identity component]] of some maximal subgroup; it is a maximality condition in its own right.

## Example in compact \(F_4\)

For the [[lie-groups/compact-exceptional-lie-group-f4|compact exceptional group \(F_4\)]], subgroups isomorphic to
\[
\operatorname{Spin}(9)
\qquad\text{and}\qquad
\bigl(SU(3)\times SU(3)\bigr)/\mathbb Z_3
\]
occur as maximal connected closed subgroups. In the exceptional-Jordan-algebra model, the second is the [[lie-groups/identity-component-of-a-lie-group|identity component]] of the stabilizer of a copy of \(\mathfrak h_3(\mathbb C)\). Its full stabilizer is disconnected, illustrating why connected maximality and unrestricted closed maximality differ.

## References

1. Armand Borel and Jean de Siebenthal, “Les sous-groupes fermés de rang maximum des groupes de Lie clos,” *Commentarii Mathematici Helvetici* 23 (1949), 200–221. [EuDML record](https://eudml.org/doc/139087).
2. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026. [arXiv record](https://arxiv.org/abs/2606.15235). Relevant: §3.
