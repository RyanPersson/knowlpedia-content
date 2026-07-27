+++
id = "noncommutative-geometry/nonunital-spectral-triple"
title = "Nonunital spectral triple"
kind = "definition"
summary = "A nonunital spectral triple replaces global compact resolvent by compactness after multiplication by algebra elements."
aliases = ["locally compact spectral triple", "noncompact spectral triple"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
+++

In the locally compact convention, a **nonunital spectral triple** \((\mathcal A,H,D)\) consists of a nonunital [[operator-algebras/involutive-algebra|involutive algebra]] \(\mathcal A\) whose \(C^*\)-completion acts faithfully by a [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate representation]] on a [[linear-algebra/hilbert-space|Hilbert space]] \(H\), together with a densely defined [[functional-analysis/self-adjoint-unbounded-operator|self-adjoint operator]] \(D\). For every \(a\in\mathcal A\), one requires \(a\operatorname{Dom}(D)\subseteq\operatorname{Dom}(D)\), a [[functional-analysis/bounded-commutator|bounded extension]] of \([D,a]\), and the localizing operator below must be [[linear-algebra/compact-operator|compact]]:
\[
a(1+D^2)^{-1/2}\in K(H).
\]
The last condition is **local compactness**; it replaces the global compact-resolvent axiom of a [[noncommutative-geometry/spectral-triple|compact spectral triple]].

## Why local compactness is the right replacement

When \(\mathcal A\) is unital, substituting \(a=1\) recovers compactness of \((1+D^2)^{-1/2}\), hence [[functional-analysis/compact-resolvent|compact resolvent]]. In a genuinely nonunital example, multiplication by \(a\) localizes the resolvent before compactness is tested. The operator \((1+D^2)^{-1/2}\) itself may therefore be noncompact, as expected for a [[noncommutative-geometry/dirac-operator|Dirac operator]] on a noncompact manifold.

## Standard examples and conventions

For a complete noncompact spin manifold, a suitable dense smooth subalgebra of \(C_0(M)\) acts on \(L^2(M,S)\), and the Dirac operator gives the model example; local compactness follows from local elliptic compactness. Moyal planes provide genuinely noncommutative examples [Gayral et al., Sections 2–4](https://doi.org/10.1007/s00220-004-1057-z).

**Warning.** Terminology varies: some authors say “nonunital spectral triple” while retaining global compact resolvent. “Locally compact spectral triple” unambiguously signals the localized condition used here. Extra hypotheses such as summability, regularity, grading, or a preferred unitization are additional structure.

## References

1. A. L. Carey, V. Gayral, A. Rennie, and F. A. Sukochev, *Index Theory for Locally Compact Noncommutative Geometries*, Memoirs of the American Mathematical Society 231, no. 1085, 2014. [AMS record](https://bookstore.ams.org/memo-231-1085). Relevant: the nonunital locally compact framework and local index formula.
2. V. Gayral, J. M. Gracia-Bondía, B. Iochum, T. Schücker, and J. C. Várilly, “Moyal Planes Are Spectral Triples,” *Communications in Mathematical Physics* 246 (2004), 569–623. [DOI record](https://doi.org/10.1007/s00220-004-1057-z). Relevant: axioms and Moyal-plane examples.
