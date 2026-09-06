+++
id = "harmonic-analysis/harish-chandra-schwartz-space"
title = "Harish-Chandra Schwartz space"
kind = "definition"
summary = "A Fréchet space of smooth functions on a real reductive group whose invariant derivatives decay relative to the Harish-Chandra Xi-function."
aliases = ["Harish-Chandra space", "Harish-Chandra Schwartz functions"]
domains = ["harmonic-analysis", "lie-groups", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["lie-groups/real-reductive-lie-group", "lie-groups/maximal-compact-subgroup-real-reductive-group", "lie-groups/universal-enveloping-algebra", "lie-groups/lie-algebra", "harmonic-analysis/harish-chandra-xi-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a
[[lie-groups/real-reductive-lie-group|real reductive Lie group]] in the
Harish-Chandra class, choose a
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact
subgroup]] \(K\), and let \(\sigma:G\to[0,\infty)\) be a standard proper
\(K\)-bi-invariant length function. The **Harish-Chandra Schwartz space**
\(\mathcal C(G)\) is the space of smooth functions \(f:G\to\mathbb C\) such
that, for every \(D_1,D_2\) in the
[[lie-groups/universal-enveloping-algebra|universal enveloping algebra]] of
the complexified [[lie-groups/lie-algebra|Lie algebra]] and every integer \(N\geq0\),
\[
\sup_{g\in G}(1+\sigma(g))^N\Xi(g)^{-1}
\lvert (L_{D_1}R_{D_2}f)(g)\rvert<\infty.
\]
Here \(\Xi\) is the [[harmonic-analysis/harish-chandra-xi-function|Harish-Chandra Xi-function]], and \(L_{D_1}\), \(R_{D_2}\) are the corresponding left- and right-invariant differential operators.

## Topological algebra structure

The displayed seminorms make \(\mathcal C(G)\) a [[functional-analysis/frechet-space|Fréchet space]], independently of the standard choices up to equivalent seminorms. It is closed under [[harmonic-analysis/convolution-on-locally-compact-group|convolution]] and under the involution \(f^*(g)=\overline{f(g^{-1})}\), because real reductive groups are unimodular. With these operations it is a Fréchet \(*\)-algebra and a basic test algebra for tempered harmonic analysis on \(G\).

## Comparison with ordinary rapid decay

On an abelian vector group, ordinary Schwartz seminorms use polynomial weights and constant-coefficient derivatives. On a noncompact reductive group, Haar volume grows exponentially. The factor \(\Xi(g)^{-1}\) compensates for the characteristic decay of spherical [[harmonic-analysis/coefficient-function|matrix coefficients]], while \((1+\sigma(g))^N\) enforces additional rapid polynomial decay. Omitting \(\Xi^{-1}\) therefore gives the wrong scale for harmonic analysis on \(G\).

## Conventions and scope

Some sources define \(L_{D_1}R_{D_2}\) with an antipode or reverse-order convention; these choices yield the same space. The notation \(\mathcal C(G)\) is conventional but can be confused with continuous functions. This definition concerns smooth scalar-valued functions on a real reductive group, not the [[harmonic-analysis/schwartz-bruhat-space-lca|Schwartz–Bruhat space]] of an arbitrary locally compact [[algebra-groups/abelian-group|abelian group]].

## References

1. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter VII on spherical functions, estimates, and the Harish-Chandra Schwartz space.
2. Harish-Chandra, “Harmonic analysis on real reductive groups I: The theory of the constant term,” *Journal of Functional Analysis* 19 (1975), 104–204. [DOI record](https://doi.org/10.1016/0022-1236%2875%2990034-8). Relevant: the Schwartz space and constant-term theory.
