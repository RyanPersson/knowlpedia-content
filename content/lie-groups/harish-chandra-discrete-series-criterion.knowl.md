+++
id = "lie-groups/harish-chandra-discrete-series-criterion"
title = "Harish–Chandra's discrete-series criterion"
kind = "theorem"
summary = "A connected semisimple real group with finite center has discrete series exactly when it has a compact Cartan subgroup."
aliases = ["equal-rank criterion", "compact Cartan criterion"]
domains = ["lie-groups", "harmonic-analysis"]
prerequisites = ["fiber-bundles/lie-group", "lie-groups/maximal-compact-subgroup-real-reductive-group", "lie-groups/discrete-series-representation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a connected semisimple real [[fiber-bundles/lie-group|Lie group]] with finite center, and let
\(K\) be a
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]]. **Harish–Chandra's discrete-series criterion** states that the
following are equivalent:

1. \(G\) has a [[lie-groups/discrete-series-representation|discrete series representation]];
2. \(G\) has a compact Cartan subgroup; and
3. \(\operatorname{rank}G=\operatorname{rank}K\).

Here \(\operatorname{rank}G\) is the complex rank of
\(\mathfrak g_{\mathbb C}\), while \(\operatorname{rank}K\) is the dimension
of a maximal torus of \(K\). Under equality, such a maximal torus is a Cartan
subgroup of \(G\).

## Meaning of the rank condition

Every maximal torus \(T\subseteq K\) is compact. Equality of the two ranks
means that its complexified [[lie-groups/lie-algebra|Lie algebra]] is already a
[[lie-groups/cartan-subalgebra|Cartan subalgebra]] of
\(\mathfrak g_{\mathbb C}\); equivalently, \(T\) is a compact Cartan subgroup
of \(G\). The criterion converts an analytic question about square-integrable
matrix coefficients into this finite-dimensional structural condition.

## Examples

The group \(\operatorname{SL}(2,\mathbb R)\) has
\(K=\operatorname{SO}(2)\), and both ranks are \(1\), so it has discrete
series. For \(\operatorname{SL}(3,\mathbb R)\), the complex rank is \(2\)
while \(\operatorname{SO}(3)\) has rank \(1\), so no discrete series exists.
Compact connected semisimple groups satisfy the condition automatically,
with \(K=G\).

## Scope of the finite-center hypothesis

**Warning.** The finite-center assumption is essential for this formulation.
An infinite central direction prevents nonzero matrix coefficients with a
fixed unitary central character from being square-integrable over \(G\).
One then studies representations square-integrable modulo the center rather
than ordinary discrete series. Broader real reductive formulations replace
the semisimple finite-center hypotheses by the corresponding Harish–Chandra
class conditions.

## Historical significance

Harish–Chandra did more than prove existence: he constructed and classified
the discrete series and determined their characters. The compact Cartan
provides the regular integral parameters, while quotienting by the relevant
Weyl-group action removes equivalent parametrizations.

## References

1. Harish–Chandra, “Discrete Series for Semisimple Lie Groups I: Construction of Invariant Eigendistributions,” *Acta Mathematica* 113 (1965), 241–318. [DOI record](https://doi.org/10.1007/BF02391779). Relevant: construction and existence of the discrete series.
2. Harish–Chandra, “Discrete Series for Semisimple Lie Groups II: Explicit Determination of the Characters,” *Acta Mathematica* 116 (1966), 1–111. [DOI record](https://doi.org/10.1007/BF02392813). Relevant: classification and character formulas.
3. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter XII, especially the equal-rank existence criterion.
