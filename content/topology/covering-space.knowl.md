+++
id = "topology/covering-space"
title = "Covering space"
kind = "definition"
summary = "A space locally homeomorphic to a fixed base through a continuous surjection whose fibers are evenly covered."
aliases = ["covering map", "covering space over X"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/topological-space", "topology/continuous-map", "topology/homeomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) and \(\widetilde X\) be topological spaces. A **covering space of \(X\)** is a topological space \(\widetilde X\), a continuous surjection
\[
p:\widetilde X\to X,
\]
and the following local condition: for every \(x\in X\), there is an open neighborhood \(U\subseteq X\) such that
\[
p^{-1}(U)=\coprod_{\alpha\in A}V_\alpha
\]
is a disjoint union of open subsets \(V_\alpha\subseteq\widetilde X\), and for every \(\alpha\) the restriction
\[
p|_{V_\alpha}:V_\alpha\xrightarrow{\cong}U
\]
is a [[topology/homeomorphism|homeomorphism]]. Such a \(U\) is evenly covered, and the \(V_\alpha\) are its sheets. The map \(p\) is the covering map.

## Fibers and sheets

Every fiber \(p^{-1}(x)\) is discrete in the subspace topology. A covering is **\(n\)-sheeted** if every fiber has \(n\) points. A one-sheeted covering is a homeomorphism, while a disconnected covering may have several connected components lying over the same base.

## Maps and examples

A map of covering spaces over \(X\) is a continuous map \(F:\widetilde X\to\widetilde Y\) satisfying \(p_Y\circ F=p_X\). The product projection \(X\times F\to X\), with \(F\) nonempty and discrete, is a covering space, and the projection \(\mathbb R\to S^1\), \(t\mapsto e^{2\pi i t}\), is an infinite-sheeted covering.

The evenly covered condition is stronger than being a local homeomorphism: it requires the full inverse image \(p^{-1}(U)\) to split into disjoint sheets, each mapping homeomorphically onto the same \(U\).

## References

1. Allen Hatcher, *Algebraic Topology*, Cambridge University Press, 2002, Chapter 1, §1.3, “Covering Spaces,” pp. 56–83. [Author-hosted PDF](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf).
