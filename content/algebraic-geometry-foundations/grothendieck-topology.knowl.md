+++
id = "algebraic-geometry-foundations/grothendieck-topology"
title = "Grothendieck topology"
kind = "knowl"
summary = "A specification of covering sieves on each object of a category, stable under pullback and satisfying local character."
aliases = ["grothendieck-topology", "Grothendieck topology"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebra-category-theory/category", "algebraic-geometry-foundations/sieve", "algebra-category-theory/morphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\mathcal C\) be a [[algebra-category-theory/category|category]]. A **[[algebraic-geometry-foundations/sieve|sieve]]** \(S\) on an object \(U\) is a collection of [[algebra-category-theory/morphism|morphisms]] with codomain \(U\) that is closed under precomposition: if \(V\to U\) belongs to \(S\), then every composite \(W\to V\to U\) belongs to \(S\).

A **Grothendieck topology** \(J\) on \(\mathcal C\) assigns to every object \(U\) a collection \(J(U)\) of sieves, called **covering sieves**, such that:

1. the maximal sieve of all morphisms into \(U\) belongs to \(J(U)\);
2. if \(S\in J(U)\) and \(f:V\to U\), then the pullback sieve \(f^*S\) belongs to \(J(V)\);
3. if \(S\) is a sieve on \(U\), \(R\in J(U)\), and \(f^*S\in J(V)\) for every \(f:V\to U\) in \(R\), then \(S\in J(U)\).

Thus a Grothendieck topology specifies what it means to work locally on the objects of a category; it need not arise from a [[topology/topology|topology]] on a set of points.
