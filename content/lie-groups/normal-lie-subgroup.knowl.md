+++
id = "lie-groups/normal-lie-subgroup"
title = "Normal Lie subgroup"
kind = "knowl"
summary = "A Lie subgroup invariant under conjugation; infinitesimally, it corresponds to an ideal."
aliases = ["normal-lie-subgroup", "Normal Lie subgroup"]
domains = ["lie-groups"]
prerequisites = ["fiber-bundles/lie-group", "lie-groups/lie-subgroup", "lie-groups/conjugation-action-of-a-lie-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "lie-groups/normal-lie-subgroup.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]]. A [[lie-groups/lie-subgroup|Lie subgroup]] \(N\subseteq G\) is **normal** if
\[
gNg^{-1}=N\qquad\text{for every }g\in G.
\]
Thus \(N\) is invariant under the [[lie-groups/conjugation-action-of-a-lie-group|conjugation action]] of \(G\).

## Infinitesimal characterization
Let \(\mathfrak g=\operatorname{Lie}(G)\) and \(\mathfrak n=\operatorname{Lie}(N)\). If \(N\) is normal, then \(\mathfrak n\) is an [[lie-groups/ideal-lie-algebra|ideal]] in \(\mathfrak g\). Conversely, if \(G\) is connected and \(\mathfrak n\subseteq\mathfrak g\) is an ideal, then the connected Lie subgroup integrating \(\mathfrak n\) is normal in \(G\).

## Quotients
If \(N\) is closed and normal, then \(G/N\) is a [[lie-groups/quotient-lie-group|quotient Lie group]] whose Lie algebra is
\[
\operatorname{Lie}(G/N)\cong \mathfrak g/\mathfrak n.
\]

## Remarks
Normal Lie subgroups permit Lie-group quotients, while ideals play the corresponding infinitesimal role.
