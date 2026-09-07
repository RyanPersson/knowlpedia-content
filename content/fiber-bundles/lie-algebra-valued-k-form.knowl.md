+++
id = "fiber-bundles/lie-algebra-valued-k-form"
title = "Lie-algebra-valued k-form"
kind = "knowl"
summary = "A differential form whose values lie in a fixed Lie algebra."
aliases = ["lie-algebra-valued-k-form", "Lie-algebra-valued k-form"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/lie-algebra-valued-k-form.md"
prerequisites = ["fiber-bundles/smooth-manifold", "lie-groups/lie-algebra", "fiber-bundles/differential-k-form", "fiber-bundles/section-of-a-fiber-bundle", "fiber-bundles/vector-bundle", "fiber-bundles/vector-bundle-valued-differential-form"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]] and fix a finite-dimensional real or complex [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\).

For \(k\ge0\), a **\(\mathfrak{g}\)-valued [[fiber-bundles/differential-k-form|differential k-form]]** on \(M\) is a [[fiber-bundles/section-of-a-fiber-bundle|smooth section]] of the [[fiber-bundles/vector-bundle|vector bundle]]
\[
\Lambda^k T^*M \otimes \mathfrak{g} \;\longrightarrow\; M.
\]

Here the constant coefficient space means the trivial bundle \(M\times\mathfrak g\); equivalently, this is a [[fiber-bundles/vector-bundle-valued-differential-form|form with values in that bundle]].

Concretely, choosing a basis \(\{e_a\}\) of \(\mathfrak{g}\), any \(\alpha\in\Omega^k(M;\mathfrak{g})\) can be written uniquely as
\[
\alpha = \sum_a \alpha^a \, e_a,
\]
with ordinary \(k\)-forms \(\alpha^a\in\Omega^k(M)\).

## Equivalent characterizations

Equivalently, it is a smoothly varying alternating multilinear map
\[
\alpha_x : (T_xM)^k \to \mathfrak{g}
\quad\text{for each }x\in M.
\]
The space of such forms is commonly denoted \(\Omega^k(M;\mathfrak{g})\).

## Examples
1. **Maurer–Cartan form.** On a Lie group \(G\), the left Maurer–Cartan form is a \(\mathfrak{g}\)-valued 1-form on \(G\).
2. **Connection form.** A [[fiber-bundles/principal-connection|principal connection]] on a principal bundle is encoded by a \(\mathfrak{g}\)-valued 1-form on the total space (the connection form).
3. **Curvature.** The [[fiber-bundles/curvature|curvature]] of a principal connection is a \(\mathfrak{g}\)-valued 2-form on the total space.
