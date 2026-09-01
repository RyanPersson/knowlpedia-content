+++
id = "harmonic-analysis/induction-in-stages-unitary-representations"
title = "Induction in stages for unitary representations"
kind = "theorem"
summary = "Unitary induction through an intermediate closed subgroup is equivalent to direct induction."
aliases = ["transitivity of unitary induction", "induction by stages"]
domains = ["harmonic-analysis", "representation-theory"]
prerequisites = ["topology/locally-compact-group", "lie-groups/strongly-continuous-unitary-representation", "harmonic-analysis/unitary-induced-representation", "lie-groups/homogeneous-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a second-countable
[[topology/locally-compact-group|locally compact Hausdorff group]], let
\(H\subseteq K\subseteq G\) be closed subgroups, and let \(\sigma\) be a
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of \(H\). **Induction in stages** is the natural
unitary equivalence
\[
\operatorname{Ind}_H^G\sigma
\ \simeq\
\operatorname{Ind}_K^G\bigl(\operatorname{Ind}_H^K\sigma\bigr).
\]
Here every induction is the
[[harmonic-analysis/unitary-induced-representation|unitary induction]]
constructed from the canonical quasi-invariant measure class on the relevant
[[lie-groups/homogeneous-space|homogeneous space]]. The equivalence is canonical up to the harmless choices
used to realize those measure classes and intertwines the \(G\)-actions.

## Geometric mechanism

The quotient map \(G/H\to G/K\) has fibers modeled on \(K/H\). Disintegrating
a measure in the class on \(G/H\) first over \(G/K\) and then over \(K/H\)
identifies an \(L^2\)-section over \(G/H\) with an \(L^2\)-section over
\(G/K\) whose values are themselves \(L^2\)-sections over \(K/H\). The
Radon–Nikodym and [[harmonic-analysis/modular-function|modular]] factors
combine exactly to give the direct-induction normalization.

## Consequences

The theorem permits a complicated inducing subgroup to be approached through
an intermediate subgroup without changing the resulting representation. In
real reductive groups it is the formal reason that induction from a parabolic
can be decomposed through a larger parabolic, with the appropriate normalized
induction at each step. It also makes the assignment of induction functors
coherent for longer chains of closed subgroups.

## Finite-group model and analytic content

For finite groups, the equivalence reduces to the associativity isomorphism
\[
\mathbb C[G]\otimes_{\mathbb C[K]}
\bigl(\mathbb C[K]\otimes_{\mathbb C[H]}V\bigr)
\cong
\mathbb C[G]\otimes_{\mathbb C[H]}V.
\]
For locally compact groups, tensor associativity alone does not prove the
Hilbert-space statement: quotient measures, completion, and modular
corrections are essential parts of the theorem.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Chapter 6, section “Pseudomeasures and Induction in Stages.”
2. George W. Mackey, *The Theory of Unitary Group Representations*, University of Chicago Press, 1976. [Library record](https://openlibrary.org/books/OL4887050M/The_theory_of_unitary_group_representations). Relevant: Chapter 3 on induced representations and induction in stages.
