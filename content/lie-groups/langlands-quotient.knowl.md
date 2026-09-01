+++
id = "lie-groups/langlands-quotient"
title = "Langlands quotient"
kind = "definition"
summary = "The Langlands quotient is the unique irreducible quotient of a standard module with its inducing parameter in the chosen positive chamber."
aliases = ["unique irreducible quotient of a standard module", "Langlands subquotient"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/standard-module-real-reductive-group", "lie-groups/real-reductive-lie-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(I(P,\sigma,\nu)\) be a
[[lie-groups/standard-module-real-reductive-group|standard module]] of a
[[lie-groups/real-reductive-lie-group|real reductive group]], with
\(\operatorname{Re}\nu\) in the chosen open positive chamber. The Langlands
classification theorem gives this module a unique
irreducible quotient. That quotient,
\[
J(P,\sigma,\nu),
\]
is its **Langlands quotient**. The term applies to the irreducible admissible
\((\mathfrak g,K)\)-module and, after choosing a compatible globalization, to
the corresponding representation of \(G\). It is not required to be unitary:
unitarity is an additional property of particular Langlands parameters.

## Classification statement

Every irreducible [[lie-groups/admissible-representation-real-reductive-group|admissible representation]] of \(G\) is the Langlands quotient
of some standard module. With a fixed positive system, the inducing data are
unique up to the standard conjugacies and equivalences on the Levi factor.
This makes the quotient construction a parametrization theorem, not merely a
way to manufacture examples.

## Example

For a real rank-one group, a positive-parameter [[lie-groups/principal-series-representation|principal series]] can be
reducible at special parameters. Its composition series may contain both a
finite-dimensional constituent and an infinite-dimensional constituent, but
the chosen chamber and quotient orientation select exactly one as
\(J(P,\sigma,\nu)\). Replacing the positive parameter by its negative can
exchange which constituent appears as a quotient rather than a submodule.

## Conventions and scope

**Warning.** Some authors formulate the classification using a unique
irreducible subrepresentation of an oppositely normalized or oppositely
ordered induced module. “Langlands subquotient” emphasizes the invariant
irreducible object, while “Langlands quotient” depends on the positive chamber
and induction convention. One should not infer that every irreducible
subquotient of a standard module is its Langlands quotient.

## References

1. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton Mathematical Series 36, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter XIV on standard modules, uniqueness of the irreducible quotient, and the Langlands classification.
2. Robert P. Langlands, *On the Classification of Irreducible Representations of Real Algebraic Groups*, Institute for Advanced Study, 1973. [Author PDF](https://publications.ias.edu/sites/default/files/classification-algebraic-groups_rpl_7.pdf). Relevant: §3, Lemmas 3.13–3.14 on the irreducible quotient and uniqueness, and §4, Lemma 4.2 on exhaustion.
