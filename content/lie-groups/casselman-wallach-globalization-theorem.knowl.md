+++
id = "lie-groups/casselman-wallach-globalization-theorem"
title = "Casselman–Wallach globalization theorem"
kind = "theorem"
summary = "Taking maximal-compact-subgroup-finite vectors is an equivalence from smooth admissible moderate-growth representations to Harish–Chandra modules."
aliases = ["unique smooth globalization theorem"]
domains = ["lie-groups", "representation-theory", "functional-analysis"]
prerequisites = ["lie-groups/real-reductive-lie-group", "lie-groups/maximal-compact-subgroup-real-reductive-group", "lie-groups/casselman-wallach-representation", "lie-groups/harish-chandra-module", "algebra-category-theory/equivalence-of-categories"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[lie-groups/real-reductive-lie-group|real reductive group]] with [[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]] \(K\). The **Casselman–Wallach globalization theorem** states that the functor
\[
E\longmapsto E_K
\]
from [[lie-groups/casselman-wallach-representation|Casselman–Wallach representations]] with continuous \(G\)-maps to [[lie-groups/harish-chandra-module|Harish–Chandra modules]] with \((\mathfrak g,K)\)-maps is an [[algebra-category-theory/equivalence-of-categories|equivalence of categories]]. Thus every Harish–Chandra module \(V\) has a smooth admissible moderate-growth Fréchet globalization \(V^\infty\), unique up to a unique continuous \(G\)-isomorphism compatible with the identification \((V^\infty)_K\cong V\). Moreover, every \((\mathfrak g,K)\)-map between Harish–Chandra modules extends uniquely to a continuous \(G\)-map between their globalizations.

## What uniqueness means

A Harish–Chandra module can be completed in many inequivalent Banach or Hilbert norms. The theorem does not identify all such completions. It says that after passing to the smooth Fréchet, moderate-growth category, the globalization is canonical up to the categorical uniqueness stated in the core. In Casselman’s formulation, a finitely generated Harish–Chandra module has exactly one smooth representation of moderate growth with the prescribed underlying \((\mathfrak g,K)\)-module, up to canonical topological isomorphism.

## Consequences

Submodules, quotients, extensions, and morphisms may be studied algebraically and then globalized. In particular, irreducibility and finite length correspond across the equivalence. If \(V^\infty\) denotes the globalization, Bernstein and Krötz identify it as
\[
V^\infty=\pi(\mathcal S(G))V,
\]
the span obtained by acting on \(V\) with the Harish–Chandra Schwartz algebra. Their proof also shows that minimal and maximal smooth Fréchet globalizations coincide.

## Boundary of the theorem

**Warning.** Uniqueness depends on the full Casselman–Wallach conditions. If smoothness, admissibility, or moderate growth is discarded, the same Harish–Chandra module can underlie different topological representations. Likewise, a general \((\mathfrak g,K)\)-module outside the Harish–Chandra category need not possess a globalization covered by this theorem.

## References

1. W. Casselman, “Canonical Extensions of Harish-Chandra Modules to Representations of \(G\),” *Canadian Journal of Mathematics* 41 (1989), 385–438. [DOI record](https://doi.org/10.4153/CJM-1989-019-5). Relevant: introduction and the canonical smooth extension.
2. Joseph Bernstein and Bernhard Krötz, “Smooth Fréchet Globalizations of Harish-Chandra Modules,” *Israel Journal of Mathematics* 199 (2014), 45–111. [DOI record](https://doi.org/10.1007/s11856-013-0056-1). Relevant: Introduction, §§5–8, especially §8.3.
