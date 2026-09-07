+++
id = "fiber-bundles/construction-adjoint-lie-algebra-bundle-ad"
title = "Adjoint Lie algebra bundle ad(P)"
kind = "knowl"
summary = "The Lie algebra bundle associated to a principal G-bundle via the adjoint representation on the Lie algebra."
aliases = ["construction-adjoint-lie-algebra-bundle-ad", "Adjoint Lie algebra bundle ad(P)"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/construction-adjoint-lie-algebra-bundle-ad.md"
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/lie-group", "lie-groups/lie-algebra", "fiber-bundles/associated-bundle", "lie-groups/adjoint-action-of-a-lie-group", "fiber-bundles/vector-bundle"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] with [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\). Let \(\pi:P\to M\) be a [[fiber-bundles/principal-g-bundle|principal G-bundle]]. The [[lie-groups/adjoint-action-of-a-lie-group|adjoint representation]] \(\mathrm{Ad}:G\to \mathrm{Aut}(\mathfrak g)\) gives a left action of \(G\) on \(\mathfrak g\) by \(g\cdot X := \mathrm{Ad}(g)X\).

**Construction (adjoint Lie algebra bundle).** Define
\[
\mathrm{ad}(P) := P\times_G \mathfrak g.
\]
This is a smooth [[fiber-bundles/vector-bundle|vector bundle]] over \(M\). Moreover, each fiber \(\mathrm{ad}(P)_x\) carries a Lie bracket induced from the [[lie-groups/lie-algebra|Lie algebra bracket]] on \(\mathfrak g\):
\[
[p,X]\ \text{ and }\ [p,Y] \ \mapsto\ [p,[X,Y]].
\]
This is well-defined because \(\mathrm{Ad}(g)\) is a Lie algebra automorphism.

## Remarks

Local sections \(s:U\to P\) identify \(\mathrm{ad}(P)|_U\) with \(U\times \mathfrak g\); changes of section act by \(\mathrm{Ad}\).

## Examples
1. If \(P\) is trivial, then \(\mathrm{ad}(P)\cong M\times \mathfrak g\) as a Lie algebra bundle.
2. If \(G\) is abelian, then \(\mathrm{Ad}\) is trivial and \(\mathrm{ad}(P)\cong M\times \mathfrak g\) for every principal \(G\)-bundle.
3. For a principal \(\mathrm{SO}(n)\)-bundle, \(\mathrm{ad}(P)\) is the bundle of skew-symmetric endomorphisms (locally identified with \(\mathfrak{so}(n)\)) transforming by conjugation under change of orthonormal frame.
