+++
id = "lie-groups/global-character-of-an-admissible-representation"
title = "Global character of an admissible representation"
kind = "definition"
summary = "The conjugation-invariant distribution obtained by tracing the integrated operators of an admissible representation."
aliases = ["Harish-Chandra character", "distribution character"]
domains = ["lie-groups", "harmonic-analysis"]
prerequisites = ["fiber-bundles/lie-group", "harmonic-analysis/haar-measure", "lie-groups/admissible-representation-real-reductive-group", "harmonic-analysis/integrated-operator-continuous-representation", "functional-analysis/distribution"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a real reductive [[fiber-bundles/lie-group|Lie group]] with a
fixed [[harmonic-analysis/haar-measure|Haar measure]], and let \(\pi\) be a
continuous, finite-length
[[lie-groups/admissible-representation-real-reductive-group|admissible
Hilbert globalization]] in the standard real-reductive category. For
\(f\in C_c^\infty(G)\), form the
[[harmonic-analysis/integrated-operator-continuous-representation|integrated
operator]]
\[
\pi(f)=\int_G f(g)\pi(g)\,dg.
\]
The Harish–Chandra trace-class theorem makes \(\pi(f)\) trace class for this
class of globalizations. The **global character**, or **Harish–Chandra
character**, of \(\pi\) is the [[functional-analysis/distribution|distribution]]
\[
\Theta_\pi(f)=\operatorname{Tr}\pi(f),\qquad f\in C_c^\infty(G).
\]
It replaces the usually undefined pointwise trace of the individual infinite-dimensional operators \(\pi(g)\).

This definition includes nonunitary admissible globalizations; it uses no
\(*\)-representation property of \(f\mapsto\pi(f)\).

## Invariance and additivity

The distribution \(\Theta_\pi\) is invariant under conjugation: translating a test function by \(g\mapsto xgx^{-1}\) does not change its value. Characters are additive in [[algebra-modules/short-exact-sequence|short exact sequences]] of finite-length [[lie-groups/admissible-representation-real-reductive-group|admissible representations]] and therefore depend only on the corresponding class in the Grothendieck group. For a finite-dimensional representation, the definition recovers integration against the ordinary trace function \(g\mapsto\operatorname{Tr}\pi(g)\).

## Infinitesimal eigencharacter

If \(\pi\) has [[lie-groups/infinitesimal-character|infinitesimal character]] \(\chi\), then its global character is a joint eigendistribution for the invariant differential operators arising from \(Z(U(\mathfrak g_\mathbb C))\). This connects the central algebraic invariant of the differentiated representation with a conjugation-invariant analytic object on \(G\).

## Regularity

The [[lie-groups/harish-chandra-regularity-theorem|Harish–Chandra regularity theorem]] represents \(\Theta_\pi\) by a locally integrable function that is real analytic on the regular semisimple set. The phrase “character value at \(g\)” refers to this representing function where it is defined, not to an operator trace of \(\pi(g)\).

## References

1. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986; reprint 2001. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter X on global characters.
2. Harish-Chandra, “Invariant Eigendistributions on a Semisimple Lie Group,” *Transactions of the American Mathematical Society* 119 (1965), 457–508. [DOI record](https://doi.org/10.1090/S0002-9947-1965-0180631-0). Relevant: invariant eigendistributions and character regularity.
