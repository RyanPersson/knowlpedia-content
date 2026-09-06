+++
id = "fiber-bundles/pullback-functoriality-pullback-of-a-principal-bundle-is-a-principal-bundle"
title = "Theorem: Pullback of a principal bundle is a principal bundle"
kind = "knowl"
summary = "The pullback construction sends principal bundles to principal bundles functorially in the base map."
aliases = ["pullback-functoriality-pullback-of-a-principal-bundle-is-a-principal-bundle", "Theorem: Pullback of a principal bundle is a principal bundle"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/smooth-map", "fiber-bundles/principal-g-bundle", "fiber-bundles/lie-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "fiber-bundles/pullback-functoriality-pullback-of-a-principal-bundle-is-a-principal-bundle.md"
+++

Let \(f:N\to M\) be a [[fiber-bundles/smooth-map|smooth map]] between smooth manifolds, and let \(\pi:P\to M\) be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with structure [[fiber-bundles/lie-group|Lie group]] \(G\).

## Theorem (pullback principal bundle)

Define the pullback total space
\[
f^*P := \{(n,p)\in N\times P \mid f(n)=\pi(p)\},
\]
with projection \(\pi_N:f^*P\to N\) given by \(\pi_N(n,p)=n\). Equip \(f^*P\) with the right \(G\)-action
\[
(n,p)\cdot g := (n,p\cdot g).
\]
Then \(\pi_N:f^*P\to N\) is a principal \(G\)-bundle, called the **pullback bundle** of \(P\) along \(f\).

Moreover, this construction is functorial: if \(g:L\to N\) is another smooth map, then \((f\circ g)^*P\) is canonically isomorphic to \(g^*(f^*P)\) as principal bundles.

## Examples

1. **Pullback of a trivial bundle.** If \(P\cong M\times G\), then \(f^*P\cong N\times G\) by the evident identification.

2. **Restriction to a submanifold.** If \(i:Z\hookrightarrow M\) is an embedding, then \(i^*P\) is the restriction of \(P\) to \(Z\); its total space is \(\pi^{-1}(Z)\subset P\).

3. **Pullback along a covering map.** If \(f:N\to M\) is a covering and \(P\to M\) is nontrivial, \(f^*P\to N\) may become trivial; for circle bundles this reflects the effect of the degree of \(f\) on the corresponding cohomology class.
