+++
id = "fiber-bundles/classifying-map-of-a-principal-bundle"
title = "Classifying map of a principal bundle"
kind = "knowl"
summary = "A map from the base into BG whose pullback of EG reproduces a given principal G-bundle."
aliases = ["classifying-map-of-a-principal-bundle", "Classifying map of a principal bundle"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/lie-group", "fiber-bundles/universal-principal-bundle-egbg", "fiber-bundles/smooth-manifold", "fiber-bundles/classification-theorem-principal-g-bundles-over-m-are-classified-by-homotopy-classes-mbg"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "fiber-bundles/classifying-map-of-a-principal-bundle.md"
+++

Fix a [[fiber-bundles/lie-group|Lie group]] \(G\) and a chosen [[fiber-bundles/universal-principal-bundle-egbg|universal principal bundle]] \(EG\to BG\). For a principal \(G\)-bundle \(P\to M\), a **classifying map** is a continuous map
\[
c\colon M \longrightarrow BG
\]
such that there is an isomorphism of principal \(G\)-bundles
\[
P \cong c^{*}(EG).
\]

If \(M\) is paracompact and has the homotopy type of a CW complex, as a standard [[fiber-bundles/smooth-manifold|smooth manifold]] does, then a classifying map exists and its homotopy class is uniquely determined by \(P\). Thus isomorphism classes of principal \(G\)-bundles correspond to homotopy classes of maps \(M\to BG\).

See [[fiber-bundles/classification-theorem-principal-g-bundles-over-m-are-classified-by-homotopy-classes-mbg|classification of principal bundles]].

## Examples
1. **Trivial bundle.** For \(P=M\times G\), a classifying map can be taken to be constant (and hence null-homotopic).
2. **Hopf fibration.** The principal \(U(1)\)-bundle \(S^3\to S^2\) is classified by a map \(S^2\to BU(1)\simeq \mathbb{C}P^\infty\) representing the generator of \(H^2(S^2;\mathbb{Z})\).
3. **Frame bundle viewpoint.** The oriented orthonormal frame bundle of a Riemannian \(n\)-manifold is a principal \(SO(n)\)-bundle; its classifying map \(M\to BSO(n)\) encodes characteristic classes such as the Stiefel–Whitney and Pontryagin classes.
