+++
id = "harmonic-analysis/invariant-mean"
title = "Invariant mean"
kind = "definition"
summary = "A normalized positive linear functional on a translation-invariant function space that is fixed by translations."
aliases = ["left-invariant mean", "translation-invariant mean"]
domains = ["harmonic-analysis", "functional-analysis", "topology"]
prerequisites = ["topology/topological-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[topology/topological-group|topological group]] and let
\(\mathcal A\) be a specified unital, self-adjoint, translation-invariant
space of bounded complex functions on \(G\). A **left-invariant mean** on
\(\mathcal A\) is a linear functional
\[
m:\mathcal A\longrightarrow\mathbb C
\]
such that \(m(f)\geq0\) whenever \(f\geq0\), \(m(1)=1\), and
\[
m(L_gf)=m(f),\qquad (L_gf)(x)=f(g^{-1}x),
\]
for all \(g\in G\). Thus a mean is a normalized positive averaging functional, while invariance says that translating the input does not change its average.
The domain is part of the notion: standard choices include
\(\operatorname{RUC}_b(G)\), the bounded right-uniformly continuous
functions, and, for locally compact \(G\), \(L^\infty(G)\) modulo null sets.

## Positivity and norm

Positivity and \(m(1)=1\) imply \(\lVert m\rVert=1\), so a mean is automatically continuous in the [[real-analysis/supremum-norm|supremum norm]]. It also satisfies \(\inf f\leq m(f)\leq\sup f\) for real-valued \(f\), and \(m(\overline f)=\overline{m(f)}\). Unlike evaluation at a point, an invariant mean need not be countably additive or represented by a [[probability/probability-measure|probability measure]] on \(G\).

## Amenability and examples

A standard definition calls \(G\) **amenable** when such a mean exists on
\(\operatorname{RUC}_b(G)\); for locally compact \(G\), this is equivalent
to existence on \(L^\infty(G)\). For a compact group, integration against
normalized [[harmonic-analysis/haar-measure|Haar measure]] gives an invariant
mean. Locally compact [[algebra-groups/abelian-group|abelian groups]] and solvable locally compact groups are
amenable, whereas the discrete [[algebra-groups/free-group|free group]] on
two generators is not.

## Conventions and function spaces

For a discrete group, \(\operatorname{RUC}_b(G)=\ell^\infty(G)\). For a [[topology/locally-compact-group|locally compact group]], amenability is also equivalent to the existence of an invariant mean on \(L^\infty(G)\), with translations understood modulo [[measure-theory/null-set|null sets]]. Authors may instead use left-uniformly continuous functions and [[lie-groups/right-translation|right translations]].

**Warning.** The spaces \(C_b(G)\), \(\operatorname{RUC}_b(G)\), and \(L^\infty(G)\) are not interchangeable in arbitrary topological-group settings. A statement about an invariant mean must specify both its function space and the side of translation.

## References

1. A. L. T. Paterson, *Amenability*, Mathematical Surveys and Monographs 29, American Mathematical Society, 1988. [AMS DOI record](https://doi.org/10.1090/surv/029). Relevant: Chapters 0–1 on invariant means and amenable groups.
