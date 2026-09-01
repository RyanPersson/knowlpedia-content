+++
id = "harmonic-analysis/tempered-dual"
title = "Tempered dual of a locally compact group"
kind = "definition"
summary = "The part of a group's unitary dual represented by irreducible unitary representations weakly contained in the regular representation."
aliases = ["reduced dual", "Plancherel-supported dual"]
domains = ["harmonic-analysis", "lie-groups", "operator-algebras"]
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/unitary-dual", "harmonic-analysis/tempered-unitary-representation", "harmonic-analysis/regular-representations-locally-compact-group", "harmonic-analysis/weak-containment-unitary-representations", "harmonic-analysis/fell-topology", "topology/subspace-topology"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]], and
let \(\widehat G\) be its [[harmonic-analysis/unitary-dual|unitary dual]].
The **tempered dual** \(\widehat G_{\mathrm{temp}}\) is the set of classes
\([\pi]\in\widehat G\) for which \(\pi\) is
[[harmonic-analysis/tempered-unitary-representation|tempered]], equivalently
\[
\pi\prec\lambda_G,
\]
where \(\lambda_G\) is the
[[harmonic-analysis/regular-representations-locally-compact-group|left regular representation]] and \(\prec\) denotes
[[harmonic-analysis/weak-containment-unitary-representations|weak containment]]. It carries the topology inherited from the
[[harmonic-analysis/fell-topology|Fell topology]] on \(\widehat G\), hence
the [[topology/subspace-topology|subspace topology]].
This definition does not require \(G\) to be type I, although type I
hypotheses are important for measurable decomposition and Plancherel theory.

## Reduced-algebra interpretation

The class \([\pi]\) lies in \(\widehat G_{\mathrm{temp}}\) exactly when the
[[harmonic-analysis/integrated-form-unitary-representation|integrated form]]
of \(\pi\) factors through the
[[operator-algebras/reduced-group-cstar-algebra|reduced group \(C^*\)-algebra]] \(C_r^*(G)\). Thus the tempered dual is also called the
**reduced dual**: it is the [[algebra-representation-theory/irreducible-representation|irreducible representation]] spectrum seen by
\(C_r^*(G)\), rather than by the full group \(C^*\)-algebra.

## Role in Plancherel theory

For a second-countable unimodular
[[lie-groups/type-i-locally-compact-group|type I group]], the
[[harmonic-analysis/plancherel-measure-nonabelian|Plancherel measure]] is
supported on the tempered dual. The direct-integral decomposition of the
[[algebra-representation-theory/regular-representation|regular representation]] therefore detects only tempered irreducibles, even
when \(\widehat G_{\mathrm{temp}}\) is a [[shared-foundations/proper-subset|proper subset]] of \(\widehat G\).
For real reductive groups, this subset includes the discrete series and the
[[lie-groups/principal-series-representation|tempered principal series]].

## Conventions and scope

Some authors use “tempered dual” only for a specified class of reductive Lie
groups, while the weak-containment definition applies to every locally
compact group. “Plancherel-supported dual” can also mean the support of a
particular representative of Plancherel measure; the intrinsic object here is
the reduced dual, defined before any choice of
[[harmonic-analysis/haar-measure|Haar measure]].

## References

1. Jacques Dixmier, *\(C^*\)-Algebras*, North-Holland Mathematical Library 15, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: §18.8 on the reduced dual and Plancherel theory.
2. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter XIV on tempered representations and the Plancherel theorem.
