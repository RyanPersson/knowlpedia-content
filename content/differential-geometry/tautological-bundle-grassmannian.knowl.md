+++
id = "differential-geometry/tautological-bundle-grassmannian"
title = "Tautological bundle on a Grassmannian"
kind = "construction"
summary = "The rank-k vector bundle over a Grassmannian whose fiber over a k-plane is that plane itself."
aliases = ["universal subbundle", "tautological subbundle"]
domains = ["differential-geometry", "fiber-bundles"]
section_mode = "progressive"
prerequisites = ["linear-algebra/vector-space", "differential-geometry/grassmannian", "fiber-bundles/vector-bundle", "fiber-bundles/vector-subbundle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(V\) be a finite-dimensional real or complex [[linear-algebra/vector-space|vector space]] and let \(\operatorname{Gr}_k(V)\) be its [[differential-geometry/grassmannian|Grassmannian]]. The **tautological bundle** is
\[
\mathcal S=\{(W,v)\in\operatorname{Gr}_k(V)\times V:v\in W\},
\qquad \pi(W,v)=W.
\]
Its fiber \(\mathcal S_W\) over a \(k\)-plane \(W\) is canonically \(W\) itself. The graph charts on the Grassmannian give \(\mathcal S\) the structure of a rank-\(k\) [[fiber-bundles/vector-bundle|vector bundle]] and identify it as a [[fiber-bundles/vector-subbundle|vector subbundle]] of the trivial bundle \(\operatorname{Gr}_k(V)\times V\). The corresponding quotient bundle \(\mathcal Q=(\operatorname{Gr}_k(V)\times V)/\mathcal S\) has fiber \(\mathcal Q_W\cong V/W\).

## Universal property

Let \(E\subseteq X\times V\) be a rank-\(k\) vector subbundle of a trivial bundle over a [[fiber-bundles/smooth-manifold|smooth manifold]] \(X\). Sending \(x\) to the subspace \(E_x\subseteq V\) defines a smooth classifying map \(c:X\to\operatorname{Gr}_k(V)\), and there is a canonical [[fiber-bundles/bundle-isomorphism|bundle isomorphism]]
\[
E\cong c^*\mathcal S.
\]
Conversely, every pullback of \(\mathcal S\) is such a subbundle. This finite-dimensional universal property classifies subbundles equipped with an embedding into a fixed trivial bundle.

## Exact sequence and characteristic classes

The inclusion and quotient fit into the canonical [[algebra-modules/short-exact-sequence|short exact sequence]]
\[
0\longrightarrow\mathcal S\longrightarrow
\operatorname{Gr}_k(V)\times V\longrightarrow\mathcal Q\longrightarrow0.
\]
The [[fiber-bundles/characteristic-class|characteristic classes]] of \(\mathcal S\) and \(\mathcal Q\) generate much of the cohomology used in Grassmannian and Schubert calculus. Their relation follows from the triviality of the middle bundle.

## Standard examples and conventions

On \(\operatorname{Gr}_1(\mathbb R^n)=\mathbb{RP}^{n-1}\), \(\mathcal S\) is the real tautological [[fiber-bundles/line-bundle|line bundle]]. On \(\operatorname{Gr}_1(\mathbb C^n)=\mathbb{CP}^{n-1}\), it is the complex tautological line bundle, commonly denoted \(\mathcal O(-1)\). The word “canonical bundle” should not be used here without qualification, because in complex geometry it usually denotes the top exterior power of the [[differential-geometry/holomorphic-cotangent-bundle|holomorphic cotangent bundle]].

## References

1. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: §5, Grassmannians, universal bundles, and complementary bundles.
2. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: chapters on Grassmannians and universal vector bundles.
