+++
id = "operator-algebras/full-to-reduced-group-cstar-quotient"
title = "Canonical quotient from full to reduced group C*-algebra"
kind = "definition"
summary = "The regular representation induces the canonical surjection from the full group C*-algebra onto the reduced group C*-algebra."
aliases = ["full-to-reduced quotient", "regular quotient of a group C*-algebra"]
domains = ["operator-algebras", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] and let \(\lambda\) be its left [[algebra-representation-theory/regular-representation|regular representation]]. Since the universal norm on \(C_c(G)\) dominates the norm \(f\mapsto\|\lambda(f)\|\), the assignment \(f\mapsto\lambda(f)\) extends uniquely from the [[operator-algebras/full-group-cstar-algebra|full group \(C^*\)-algebra]] to the [[operator-algebras/reduced-group-cstar-algebra|reduced group \(C^*\)-algebra]] as a surjective \(*\)-homomorphism
\[
q_G\colon C^*(G)\longrightarrow C_r^*(G).
\]
This map is the **canonical full-to-reduced quotient**. Its kernel is precisely the kernel of the integrated regular representation, so \(C_r^*(G)\cong C^*(G)/\ker\lambda\).

## Representation-theoretic meaning

A [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate representation]] of \(C^*(G)\) factors through \(q_G\) exactly when the corresponding unitary representation of \(G\) is [[harmonic-analysis/weak-containment-unitary-representations|weakly contained]] in \(\lambda\). Thus the reduced algebra records only those representations detected by the regular representation, whereas the full algebra records every [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]].

## When the quotient is an isomorphism

The map \(q_G\) is an isomorphism exactly when \(G\) is [[harmonic-analysis/amenable-locally-compact-group|amenable]]. Without that hypothesis, its kernel can be nonzero; consequently, the notation “the group \(C^*\)-algebra” should not be used to identify the full and reduced completions. For example, nonabelian [[algebra-groups/free-group|free groups]] give standard cases in which the quotient is not injective [Brown–Ozawa, Chapter 2](https://doi.org/10.1090/gsm/088).

## References

1. D. P. Williams, *Crossed Products of \(C^*\)-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: Section 2.5 on full and reduced group \(C^*\)-algebras.
2. N. P. Brown and N. Ozawa, *\(C^*\)-Algebras and Finite-Dimensional Approximations*, Graduate Studies in Mathematics 88, American Mathematical Society, 2008. [DOI record](https://doi.org/10.1090/gsm/088). Relevant: Chapter 2 on reduced group \(C^*\)-algebras and amenability.
