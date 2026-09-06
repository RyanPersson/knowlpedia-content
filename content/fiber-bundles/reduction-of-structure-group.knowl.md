+++
id = "fiber-bundles/reduction-of-structure-group"
title = "Reduction of structure group"
kind = "knowl"
summary = "A way to replace the structure group G of a principal bundle by a subgroup H by choosing compatible H-frames in each fiber."
aliases = ["reduction-of-structure-group", "Reduction of structure group"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/lie-group", "fiber-bundles/smooth-map", "fiber-bundles/principal-bundle-isomorphism", "fiber-bundles/principal-h-subbundle"]
dependency_review_count = 1
legacy_source_path = "fiber-bundles/reduction-of-structure-group.md"
+++

Let \(P\to M\) be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] and let \(H\subset G\) be a Lie subgroup of the [[fiber-bundles/lie-group|Lie group]] \(G\).

A **reduction of structure group of \(P\) from \(G\) to \(H\)** consists of a principal \(H\)-bundle \(\pi_H:Q\to M\) together with an injective [[fiber-bundles/smooth-map|smooth map]] \(i:Q\hookrightarrow P\) such that:
1. \(\pi\circ i=\pi_H\) (so \(i\) covers \(\mathrm{id}_M\)),
2. \(i(q\cdot h)=i(q)\cdot h\) for all \(q\in Q\) and \(h\in H\),
3. the induced map
   \[
   Q\times_H G \to P,\qquad [q,g]\mapsto i(q)\cdot g
   \]
   is a [[fiber-bundles/principal-bundle-isomorphism|principal bundle isomorphism]].

In this situation \(Q\) is called a [[fiber-bundles/principal-h-subbundle|principal H-subbundle]] of \(P\).

## Examples
1. **Orientation.** The frame bundle of an \(n\)-manifold reduces from \(GL(n)\) to \(GL^+(n)\) exactly when \(M\) is orientable.
2. **Riemannian metric.** A Riemannian metric determines a [[fiber-bundles/g-structure|reduction of the frame bundle]] to \(O(n)\), namely the orthonormal frame bundle.
3. **Almost complex structure.** An almost complex structure on a \(2n\)-manifold reduces the frame bundle from \(GL(2n,\mathbb{R})\) to \(GL(n,\mathbb{C})\) (and further to \(U(n)\) when compatible with a Hermitian metric).

## Equivalent characterizations
A standard equivalent characterization (useful in practice) is: a reduction to \(H\) exists if and only if the associated bundle with fiber \(G/H\) admits a global [[fiber-bundles/section-of-a-fiber-bundle|smooth section]] (here \(G\) acts on \(G/H\) by left multiplication).
