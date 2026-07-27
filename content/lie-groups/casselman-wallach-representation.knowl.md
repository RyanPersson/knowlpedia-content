+++
id = "lie-groups/casselman-wallach-representation"
title = "Casselman–Wallach representation"
kind = "definition"
summary = "A smooth admissible Fréchet representation of a real reductive group whose action has moderate growth."
aliases = ["smooth admissible Fréchet representation", "SAF representation"]
domains = ["lie-groups", "representation-theory", "functional-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a [[lie-groups/real-reductive-lie-group|real reductive group]] and \(K\) a [[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]]. A **Casselman–Wallach representation** is a continuous representation \((\pi,E)\) on a complex [[functional-analysis/frechet-space|Fréchet space]] such that the action is smooth, its [[lie-groups/k-finite-vector|\(K\)-finite part]] \(E_K\) is a [[lie-groups/harish-chandra-module|Harish–Chandra module]], and the action has moderate growth. The latter means that, for every continuous [[convex-analysis/seminorm|seminorm]] \(p\) on \(E\), there are a continuous seminorm \(q\) and \(N\geq0\) with
\[
p(\pi(g)v)\leq \lVert g\rVert^Nq(v)
\]
for all \(g\in G\) and \(v\in E\), where \(\lVert\cdot\rVert\) is any fixed algebraic scale on \(G\).

## The role of the three conditions

Smoothness requires every orbit map \(g\mapsto\pi(g)v\) to be smooth. Admissibility is algebraic: \(E_K\) has finite \(K\)-multiplicities and is finitely generated over \(U(\mathfrak g)\). Moderate growth controls every defining seminorm uniformly by a polynomial scale on \(G\). Replacing the algebraic scale by an equivalent one does not change the condition. Bernstein and Krötz formulate these objects as smooth admissible moderate-growth Fréchet representations, the objects of their category \(\mathcal{SAF}\) [Bernstein–Krötz, Introduction and §1.3](https://doi.org/10.1007/s11856-013-0056-1).

## Structure and consequences

The underlying Fréchet space of a Casselman–Wallach representation is nuclear, and continuous \(G\)-maps between such representations are controlled by their restrictions to \(K\)-finite vectors. The category is closed under kernels and cokernels in the form dictated by the corresponding exact operations on Harish–Chandra modules. Most importantly, the [[lie-groups/casselman-wallach-globalization-theorem|Casselman–Wallach globalization theorem]] says that taking \(K\)-finite vectors loses no categorical information.

## Examples and near-misses

If \(V\) is a Harish–Chandra module, its canonical smooth globalization \(V^\infty\) is the basic example. Smooth vectors in a Hilbert globalization also give a Casselman–Wallach representation once their \(K\)-finite part is \(V\) and moderate growth is verified [Bernstein–Krötz, §4.1](https://doi.org/10.1007/s11856-013-0056-1). A smooth Fréchet representation of moderate growth whose \(K\)-finite vectors have an infinite \(K\)-type multiplicity is a near-miss: it fails admissibility.

## Conventions and scope

The synonymous abbreviations “SAF” and “SF” are not completely uniform across sources. In Bernstein–Krötz, an SF-representation means a smooth Fréchet representation satisfying the relevant growth condition, while \(\mathcal{SAF}\) additionally imposes admissibility. Here “Casselman–Wallach representation” includes admissibility, so its \(K\)-finite part is a Harish–Chandra module. Nuclearity is a consequence in this setting, not an extra axiom in the core definition.

## References

1. Joseph Bernstein and Bernhard Krötz, “Smooth Fréchet Globalizations of Harish-Chandra Modules,” *Israel Journal of Mathematics* 199 (2014), 45–111. [DOI record](https://doi.org/10.1007/s11856-013-0056-1). Relevant: Introduction, §1.3 on moderate growth, and §4.1 on globalizations.
2. W. Casselman, “Canonical Extensions of Harish-Chandra Modules to Representations of \(G\),” *Canadian Journal of Mathematics* 41 (1989), 385–438. [DOI record](https://doi.org/10.4153/CJM-1989-019-5). Relevant: introduction and the smooth moderate-growth category.
