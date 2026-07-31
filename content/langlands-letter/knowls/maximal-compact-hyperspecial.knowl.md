+++
id = "langlands-letter/knowls/maximal-compact-hyperspecial"
title = "Maximal Compact and Hyperspecial Subgroup"
kind = "definition"
summary = "A compact open subgroup arising as the integral points of a reductive model at an unramified place."
aliases = ["maximal-compact-hyperspecial", "Maximal Compact and Hyperspecial Subgroup"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/maximal-compact-hyperspecial.md"
+++

Let \(k\) be a nonarchimedean local field with ring of integers
\(\mathcal O_k\), and let \(G\) be a connected reductive group over \(k\).

A **maximal compact subgroup** of \(G(k)\) is a compact subgroup maximal under inclusion. Such subgroups are open in the standard \(p\)-adic topology.

A compact open subgroup \(K\subseteq G(k)\) is **hyperspecial** if there is a smooth affine reductive group scheme
\(\mathcal G\) over \(\mathcal O_k\), together with an identification of its generic fiber with \(G\), such that
\[
K=\mathcal G(\mathcal O_k).
\]
The reductivity of the entire integral model, including its special fiber, is the condition that distinguishes hyperspecial subgroups from general parahoric subgroups.

## Existence and maximality

A connected reductive \(k\)-group admits a hyperspecial subgroup exactly when it is **unramified**: it is quasi-split over \(k\) and splits over an unramified extension. Every hyperspecial subgroup is maximal compact, but not every maximal compact subgroup is hyperspecial.

## Examples

- \(\mathrm{GL}_n(\mathcal O_k)\subset \mathrm{GL}_n(k)\) is hyperspecial.

## Spherical Hecke algebra

For hyperspecial \(K\), the [[langlands-letter/knowls/spherical-hecke-algebra-satake|spherical Hecke algebra]] admits the unramified Satake description. The subgroups denoted \(G_{\mathbb Z_p}\) in the letter play this role at almost all primes.
