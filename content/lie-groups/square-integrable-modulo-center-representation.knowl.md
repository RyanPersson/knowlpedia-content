+++
id = "lie-groups/square-integrable-modulo-center-representation"
title = "Square-integrable representation modulo the center"
kind = "definition"
summary = "An irreducible unitary representation having a nonzero matrix coefficient that is square-integrable after quotienting by the center."
aliases = ["relative discrete series", "square-integrable modulo Z"]
domains = ["lie-groups", "harmonic-analysis"]
prerequisites = ["harmonic-analysis/unimodular-group", "lie-groups/irreducible-unitary-representation", "harmonic-analysis/coefficient-function", "algebra-representation-theory/schurs-lemma", "real-analysis/absolute-value"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a second-countable [[harmonic-analysis/unimodular-group|unimodular locally compact group]] with center \(Z\), and fix an invariant measure on \(G/Z\). An [[lie-groups/irreducible-unitary-representation|irreducible unitary representation]] \(\pi\) of \(G\) is **square-integrable modulo the center** if some nonzero [[harmonic-analysis/coefficient-function|matrix coefficient]] satisfies
\[
\int_{G/Z}\left|\langle \pi(g)u,v\rangle\right|^2\,d(gZ)<\infty.
\]
[[algebra-representation-theory/schurs-lemma|Schur's lemma]] gives a unitary central character \(\chi_\pi\) with \(\pi(z)=\chi_\pi(z)I\), so the [[real-analysis/absolute-value|absolute value]] of the coefficient is constant on central cosets and the integrand is well defined. Such representations are also called the **relative discrete series**.

## Equivalent formulations and orthogonality

For an irreducible unitary representation in this setting, existence of one nonzero square-integrable coefficient modulo \(Z\) implies the corresponding orthogonality relations for all coefficients. After a normalization of measure, these relations involve a positive formal degree. This is the central-quotient analogue of the coefficient criterion for the [[lie-groups/discrete-series-representation|discrete series]].

## Why the quotient is necessary

If \(Z\) is noncompact, every coefficient of an [[algebra-representation-theory/irreducible-representation|irreducible representation]] has constant modulus along \(Z\). A nonzero coefficient therefore cannot usually belong to \(L^2(G)\), even when it is square-integrable on \(G/Z\). For a real reductive group with noncompact center, relative discrete series is consequently the useful replacement for ordinary discrete series.

## Conventions and scope

**Warning.** Some authors build a fixed unitary central character into the ambient \(L^2\)-space and say “discrete series” for the resulting relative notion. Here ordinary discrete series means occurrence in \(L^2(G)\), whereas “modulo the center” always means integration over \(G/Z\). For nonunimodular groups the orthogonality relations require Duflo–Moore operators, so the uncomplicated scalar formal-degree formulation above is deliberately restricted to the unimodular case.

## References

1. Michel Duflo and Calvin C. Moore, *On the regular representation of a nonunimodular locally compact group*, Journal of Functional Analysis 21 (1976), 209–243. [DOI record](https://doi.org/10.1016/0022-1236%2876%2990079-3). Relevant: §§2–3 on square-integrable representations and orthogonality operators.
2. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [Author-maintained book record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter XII on discrete series and square integrability modulo the center.
