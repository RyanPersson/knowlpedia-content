+++
id = "lie-groups/dual-representation-lie"
title = "Dual (contragredient) representation"
kind = "knowl"
summary = "The dual representation acts on linear functionals by precomposition with the inverse group action; infinitesimally, it is the negative transpose."
aliases = ["dual-representation-lie", "Dual (contragredient) representation"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/representation-of-a-lie-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "lie-groups/dual-representation-lie.md"
+++

Let \(V\) be a finite-dimensional vector space. If \(\rho:G\to \mathrm{GL}(V)\) is a [[lie-groups/representation-of-a-lie-group|representation of a Lie group]] \(G\), its **dual**, or **contragredient**, representation on \(V^*\) is
\[
\rho^*:G\to \mathrm{GL}(V^*),\qquad
(\rho^*(g)\lambda)(v) := \lambda\bigl(\rho(g^{-1})v\bigr).
\]
In a chosen basis, \(\rho^*(g)\) is represented by \((\rho(g^{-1}))^{\mathsf T}\).

## Lie algebra version

If \(\pi:\mathfrak g\to \mathfrak{gl}(V)\) is a [[lie-groups/representation-of-a-lie-algebra|representation of a Lie algebra]] \(\mathfrak g\), its dual representation \(\pi^*:\mathfrak g\to\mathfrak{gl}(V^*)\) is defined by
\[
(\pi^*(X)\lambda)(v) := -\,\lambda\bigl(\pi(X)v\bigr).
\]
In matrix form, \(\pi^*(X)=-\pi(X)^{\mathsf T}\).

These definitions are compatible under differentiation: if \(\pi=d\rho_e\), then \(d(\rho^*)_e=\pi^*\).

## Remarks
Duals interact naturally with other constructions such as [[lie-groups/tensor-product-of-representations-lie|tensor products]]. In highest-weight theory, dualizing typically negates weights (compare [[lie-groups/weight-of-a-representation|weights]] and [[lie-groups/weights-in-dual-cartan|weights in the dual Cartan]]).
