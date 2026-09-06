+++
id = "operator-algebras/enveloping-cstar-algebra"
title = "Enveloping C*-algebra"
kind = "definition"
summary = "The universal C*-completion of an involutive algebra in the maximal norm detected by bounded representations."
aliases = ["C*-completion", "universal C*-completion", "C*-envelope of a *-algebra", "full C*-completion"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/involutive-algebra", "operator-algebras/maximal-cstar-seminorm", "operator-algebras/cstar-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) be an [[operator-algebras/involutive-algebra|involutive algebra]]
whose [[operator-algebras/maximal-cstar-seminorm|maximal
\(C^*\)-seminorm]]
\[
\|a\|_{\max}=\sup_\pi\|\pi(a)\|
\]
is finite for every \(a\in A\), where \(\pi\) ranges over its bounded
Hilbert-space \(*\)-representations. The **enveloping \(C^*\)-algebra**
\(C^*(A)\) is the completion of
\(A/\ker\|\cdot\|_{\max}\) in this norm. Its canonical \(*\)-homomorphism
\(\iota:A\to C^*(A)\) has dense image, and every bounded
\(*\)-representation of \(A\) factors canonically and uniquely through a
[[operator-algebras/cstar-representation|representation]] of \(C^*(A)\).

## Universal property

If \(\pi:A\to B(H)\) is a bounded \(*\)-representation, there is a unique
\(*\)-representation \(\widetilde\pi:C^*(A)\to B(H)\) satisfying
\(\pi=\widetilde\pi\circ\iota\). This property determines \(C^*(A)\) up to
canonical \(*\)-isomorphism. The kernel of \(\iota\) is the intersection of
the kernels of all bounded \(*\)-representations, so \(\iota\) need not be
injective.

## Existence and examples

For the algebraic group algebra \(\mathbb C[\Gamma]\) of a discrete group,
unitarity of the group generators supplies uniform bounds, and the
enveloping completion is the full group \(C^*\)-algebra \(C^*(\Gamma)\).
For a general involutive algebra, the supremum can be infinite for some
element; then this construction does not produce an enveloping
\(C^*\)-algebra. If all bounded representations vanish, the completion is
the zero algebra.

## Terminology

The enveloping \(C^*\)-algebra is sometimes called the universal
\(C^*\)-completion. It must not be confused with the \(C^*\)-envelope of an
operator system or nonself-adjoint operator algebra, which is a minimal
boundary construction rather than the maximal completion over
representations. Nor is it the universal enveloping algebra of a Lie
algebra, which is purely algebraic.

## References

1. Jacques Dixmier, \(C^*\)-Algebras, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: §2.7 on enveloping \(C^*\)-algebras.
2. Bruce Blackadar, Operator Algebras: Theory of \(C^*\)-Algebras and von Neumann Algebras, Springer, 2006. [DOI record](https://doi.org/10.1007/3-540-28517-2). Relevant: §II.8 on maximal seminorms and universal completions.
