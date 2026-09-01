+++
id = "noncommutative-geometry/smooth-subalgebra-cstar-algebra"
title = "Smooth subalgebra of a C*-algebra"
kind = "definition"
summary = "A dense Fréchet *-subalgebra of a C*-algebra whose finer topology records regularity and which is closed under holomorphic functional calculus."
aliases = ["smooth dense *-subalgebra", "spectrally invariant subalgebra", "holomorphically closed subalgebra"]
domains = ["noncommutative-geometry", "operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "functional-analysis/holomorphic-functional-calculus-banach-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. In this knowl, a **smooth subalgebra** is a dense \(*\)-subalgebra \(\mathcal A\subseteq A\) with a complete Fréchet topology finer than the \(C^*\)-norm topology, continuous multiplication and involution, and spectral invariance: after adjoining identities when necessary,
\[
x\in\widetilde{\mathcal A}\text{ is invertible in }\widetilde A
\quad\Longrightarrow\quad
x^{-1}\in\widetilde{\mathcal A}.
\]
Under the standard complete locally convex hypotheses, this is equivalent to closure under [[functional-analysis/holomorphic-functional-calculus-banach-algebra|holomorphic functional calculus]] in \(\widetilde A\).

## Why spectral invariance matters

Holomorphic closure keeps spectral constructions inside the regular algebra. In particular, idempotents and invertibles used in \(K\)-theory can be deformed without leaving \(\mathcal A\), and the inclusion \(\mathcal A\hookrightarrow A\) induces the expected \(K\)-theory isomorphisms under the usual matrix-stable formulation. This is why a spectrally invariant [[noncommutative-geometry/pre-cstar-algebra|pre-\(C^*\)-algebra]] is often the preferred coordinate algebra in noncommutative geometry.

## Standard constructions

If a finite-dimensional [[fiber-bundles/lie-group|Lie group]] acts strongly continuously on \(A\) by \(*\)-automorphisms, the elements whose orbit maps are smooth form a dense Fréchet \(*\)-subalgebra \(A^\infty\); it is spectrally invariant. Classical examples include \(C^\infty(M)\subset C(M)\) for a compact [[fiber-bundles/smooth-manifold|smooth manifold]] and smooth noncommutative tori inside their \(C^*\)-completions. Schwartz-type convolution algebras provide further examples only when the relevant decay and spectral-invariance theorems are verified.

## Conventions and scope

**Warning.** “Smooth subalgebra” is not governed by one universal convention. Some authors mean only a dense locally convex \(*\)-subalgebra, while others build spectral invariance or regularity under specified derivations into the term. Spectral invariance is algebraic inverse-closedness; the finer Fréchet topology records differentiability or decay. Neither property gives \(\mathcal A\) the structure of a smooth manifold.

## References

1. Alain Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-hosted book](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Part IV on smooth algebras and spectral triples.
2. Bruce Blackadar, *K-Theory for Operator Algebras*, 2nd ed., Cambridge University Press, 1998. [Author-hosted text](https://bruceblackadar.com/Mathematics/book6.pdf). Relevant: §III.5 on dense subalgebras stable under holomorphic functional calculus.
