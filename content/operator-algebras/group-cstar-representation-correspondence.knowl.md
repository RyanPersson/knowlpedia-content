+++
id = "operator-algebras/group-cstar-representation-correspondence"
title = "Unitary representations and representations of the full group C*-algebra"
kind = "theorem"
summary = "Integrated form gives a natural correspondence between continuous unitary group representations and nondegenerate representations of the full group C*-algebra."
aliases = ["integrated-form correspondence", "universal representation correspondence"]
domains = ["operator-algebras", "harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["topology/locally-compact-group", "lie-groups/strongly-continuous-unitary-representation", "operator-algebras/nondegenerate-star-homomorphism", "operator-algebras/full-group-cstar-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]]. The **integrated-form correspondence** assigns to every [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] \(U\colon G\to\mathcal U(H)\) the unique [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate \(C^*\)-representation]] of the [[operator-algebras/full-group-cstar-algebra|full group \(C^*\)-algebra]]
\[
\widetilde U\colon C^*(G)\longrightarrow B(H)
\]
extending \(\widetilde U(f)=\int_G f(s)U_s\,ds\) for \(f\in C_c(G)\). Conversely, every nondegenerate representation of \(C^*(G)\) arises uniquely this way. The two constructions preserve intertwining operators, direct sums, invariant subspaces, and unitary equivalence.

## Recovering the group representation

The canonical map \(s\mapsto u_s\) takes \(G\) into the [[operator-algebras/unitary-element|unitary multipliers]] of \(C^*(G)\). If \(\pi\) is nondegenerate, its unique extension to the [[operator-algebras/multiplier-algebra|multiplier algebra]] gives \(U_s=\overline\pi(u_s)\). Nondegeneracy is essential here: it is what makes the multiplier extension and the recovered unitary representation canonical.

## Full versus reduced

This correspondence is universal for the **full** group \(C^*\)-algebra. The representation \(\widetilde U\) factors through the [[operator-algebras/full-to-reduced-group-cstar-quotient|canonical quotient]] onto \(C_r^*(G)\) exactly when \(U\) is [[harmonic-analysis/weak-containment-unitary-representations|weakly contained]] in the left [[algebra-representation-theory/regular-representation|regular representation]]. Therefore representations of the reduced algebra do not, in general, parameterize all unitary representations of \(G\).

## References

1. D. P. Williams, *Crossed Products of \(C^*\)-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: Sections 2.3–2.5 on integrated forms and group \(C^*\)-algebras.
2. J. M. G. Fell and R. S. Doran, *Representations of \(*\)-Algebras, Locally Compact Groups, and Banach \(*\)-Algebraic Bundles*, vol. I, Academic Press, 1988. [Publisher record](https://www.sciencedirect.com/bookseries/pure-and-applied-mathematics/vol/125/suppl/C). Relevant: the integration and disintegration of group representations.
