+++
id = "algebraic-geometry-foundations/galois-tensor-product-identity"
title = "Galois tensor-product identity"
kind = "theorem"
summary = "For a finite Galois extension, the self-tensor product splits into one copy for each automorphism."
aliases = ["Galois tensor-product identity", "Galois tensor identity", "K tensor K decomposition"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebra-fields-galois/galois-extension", "algebra-modules/tensor-product"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Base-changing \(\operatorname{Spec}K\to\operatorname{Spec}F\) along itself should reveal one sheet for every \(F\)-automorphism of \(K\). On coordinate rings, that geometric splitting is exactly the following identity.

Let \(K/F\) be a finite [[algebra-fields-galois/galois-extension|Galois extension]] and \(G=\operatorname{Gal}(K/F)\). The \(K\)-algebra homomorphism

\[
\Phi:K\otimes_F K\longrightarrow\prod_{\sigma\in G}K,
\qquad
\Phi(a\otimes b)=\bigl(a\,\sigma(b)\bigr)_{\sigma\in G}
\]

is an isomorphism. Taking spectra reverses products and arrows, giving

\[
\operatorname{Spec}K\times_{\operatorname{Spec}F}\operatorname{Spec}K
\cong
\coprod_{\sigma\in G}\operatorname{Spec}K
\cong
\operatorname{Spec}K\times G.
\]

This is the affine form of the [[algebraic-geometry-foundations/torsor-condition|torsor condition]] and proves that a [[algebraic-geometry-foundations/galois-extension-as-etale-torsor|Galois extension is an étale torsor]].

**Warning.** The formula depends on both separability and normality. For a finite separable but nonnormal extension, its embeddings do not all land back in \(K\); for a purely inseparable extension, \(K\otimes_F K\) can contain nilpotents instead of splitting as a product.
