+++
id = "fiber-bundles/orthonormal-frame-bundle-reduction-of-the-frame-bundle"
title = "Orthonormal frame bundle"
kind = "knowl"
summary = "The principal O(n)-bundle of orthonormal frames determined by a bundle metric on a real rank-n bundle."
aliases = ["orthonormal-frame-bundle-reduction-of-the-frame-bundle", "Orthonormal frame bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/orthonormal-frame-bundle-reduction-of-the-frame-bundle.md"
+++

Let \(\pi:E\to M\) be a real rank-\(n\) vector bundle over a [[fiber-bundles/smooth-manifold|smooth manifold]], equipped with a [[fiber-bundles/bundle-metric|bundle metric]] \(\langle\cdot,\cdot\rangle\). Its **orthonormal frame bundle** is
\[
\mathrm{O}(E):=\{(e_1,\dots,e_n)\in \mathrm{Fr}(E)\ :\ \langle e_i,e_j\rangle = \delta_{ij}\ \text{fiberwise}\}.
\]

The right action of \(\mathrm{GL}(n,\mathbb R)\) on \(\mathrm{Fr}(E)\) restricts to a free transitive action of \(\mathrm O(n)\) on each fiber of \(\mathrm O(E)\). Thus \(\mathrm O(E)\to M\) is a [[fiber-bundles/principal-g-bundle|principal \(\mathrm O(n)\)-bundle]] and a reduction of the frame bundle's structure group.

## Examples
1. If \(E=TM\) with a Riemannian metric, then \(\mathrm O(TM)\) is the bundle of orthonormal tangent frames.

2. For \(E=M\times\mathbb R^n\) with its Euclidean metric, \(\mathrm O(E)\cong M\times\mathrm O(n)\).

3. If \(n=1\), then \(\mathrm O(1)=\{\pm1\}\), and \(\mathrm O(E)\to M\) is the bundle of unit vectors, a double cover.
