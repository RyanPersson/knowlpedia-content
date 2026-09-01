+++
id = "supergeometry/supermanifold"
title = "Supermanifold"
kind = "definition"
summary = "A locally superringed space locally isomorphic to a finite-dimensional smooth real superdomain."
aliases = ["smooth supermanifold", "Berezin-Leites supermanifold", "Kostant supermanifold"]
domains = ["supergeometry", "differential-geometry"]
prerequisites = ["supergeometry/superspace", "supergeometry/superdomain", "algebra-rings/nilpotent-element"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A **smooth real supermanifold of dimension \(p|q\)** is a
[[supergeometry/superspace|superspace]] \(X=(|X|,\mathcal O_X)\) that is
locally isomorphic to a [[supergeometry/superdomain|superdomain]]
\(U^{p|q}\). Its morphisms are morphisms of locally superringed spaces.
These objects and morphisms form the category
\(\mathbf{SMan}_{\mathbb R}^{\mathrm{sm}}\).

Let \(\mathcal J_X\subseteq\mathcal O_X\) be the sheaf of [[algebra-rings/nilpotent-element|nilpotent elements]],
equivalently in this smooth model the ideal generated locally by odd
functions. Then
\[
\mathcal O_X/\mathcal J_X\cong C^\infty_{X_{\mathrm{red}}},
\]
where \(X_{\mathrm{red}}\) is an ordinary smooth \(p\)-manifold with
underlying topological space \(|X|\). The odd dimension \(q\) records the
rank of \(\mathcal J_X/\mathcal J_X^2\).

## Local versus global structure

Local coordinates are written
\((x^1,\ldots,x^p;\theta^1,\ldots,\theta^q)\), with even \(x^i\) and odd
\(\theta^\alpha\). Transition morphisms may mix the even coordinates with
even nilpotent expressions and the odd coordinates with odd expressions.
Consequently, being locally an exterior-algebra model does not itself choose
a global [[supergeometry/split-supermanifold|splitting]].

Ordinary [[fiber-bundles/smooth-manifold|smooth manifolds]] embed fully faithfully as supermanifolds of
dimension \(p|0\). Complex-analytic and algebraic supermanifolds use different
local function sheaves; unlike the smooth real case, they need not split.

## References

1. D. A. Leites, “Introduction to the theory of supermanifolds,” *Russian Mathematical Surveys* 35(1), 1980, 1–64. [Article](https://doi.org/10.1070/RM1980v035n01ABEH001545).
2. C. Carmeli, L. Caston, and R. Fioresi, *Mathematical Foundations of Supersymmetry*, EMS, 2011. [Publisher record](https://doi.org/10.4171/097). Relevant: Chapter 4.
