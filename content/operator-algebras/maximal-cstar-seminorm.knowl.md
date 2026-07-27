+++
id = "operator-algebras/maximal-cstar-seminorm"
title = "Maximal C*-seminorm"
kind = "definition"
summary = "The maximal C*-seminorm of an involutive algebra is the supremum of the operator norms of an element over all bounded Hilbert-space representations."
aliases = ["universal C*-norm", "maximal representation seminorm", "Universal C*-seminorm"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be an [[operator-algebras/involutive-algebra|involutive algebra]]. For \(a\in A\), set
\[
\|a\|_{\max}=\sup_{\pi}\|\pi(a)\|,
\]
where \(\pi\) ranges over all [[operator-algebras/cstar-representation|bounded Hilbert-space \(*\)-representations]] of \(A\). If this supremum is finite for every \(a\), it is the maximal [[convex-analysis/seminorm|\(C^*\)-seminorm]] on \(A\): it satisfies \(\|a^*a\|_{\max}=\|a\|_{\max}^2\) and dominates the seminorm arising from every such representation. It can have a nonzero kernel, so “universal \(C^*\)-norm” is literally a norm only after the appropriate quotient.

## Enveloping completion

When \(\|\cdot\|_{\max}\) is finite, first form \(A/\ker\|\cdot\|_{\max}\), then complete it. The resulting [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(C^*(A)\) has the universal property that every bounded \(*\)-representation of \(A\) factors uniquely through a representation of \(C^*(A)\). The quotient and completion are separate steps and should not be folded into the seminorm's definition.

## Existence and failure

The supremum is automatically finite when algebraic relations impose uniform bounds on the images of generators, as happens for unitary generators. For a general involutive algebra it may be infinite on some element; then no enveloping \(C^*\)-algebra with all bounded \(*\)-representations has been defined by this formula. If there are no nonzero bounded representations, the seminorm is identically zero.

## Maximality and terminology

Every \(C^*\)-seminorm \(p\) on \(A\) is bounded above by \(\|\cdot\|_{\max}\): represent the \(C^*\)-completion of \(A/\ker p\) faithfully on a [[linear-algebra/hilbert-space|Hilbert space]] and compare norms. Some authors say “universal \(C^*\)-seminorm”; the adjective “maximal” emphasizes the supremum over all representations, not a chosen faithful one [Blackadar, section II.8](https://doi.org/10.1007/3-540-28517-2).

## References

1. Bruce Blackadar, *Operator Algebras: Theory of* \(C^*\)-*Algebras and von Neumann Algebras*, Encyclopaedia of Mathematical Sciences 122, Springer, 2006. [DOI record](https://doi.org/10.1007/3-540-28517-2). Relevant: section II.8 on universal \(C^*\)-algebras and maximal seminorms.
2. Jacques Dixmier, \(C^*\)-*Algebras*, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: section 2.7 on enveloping \(C^*\)-algebras.
