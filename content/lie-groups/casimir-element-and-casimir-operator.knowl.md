+++
id = "lie-groups/casimir-element-and-casimir-operator"
title = "Casimir element and Casimir operator"
kind = "definition"
summary = "A basis-independent central element of an enveloping algebra and the operator through which it acts in a representation."
aliases = ["quadratic Casimir", "Casimir invariant"]
domains = ["lie-groups", "algebra-representation-theory"]
section_mode = "progressive"
+++

Let \(\mathfrak g\) be a finite-dimensional [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]] over \(\mathbb R\) or \(\mathbb C\), let \(B\) be its [[lie-groups/killing-form|Killing form]], and choose bases \((X_i)\) and \((X^i)\) dual with respect to \(B\). The **Casimir element** in the [[lie-groups/universal-enveloping-algebra|universal enveloping algebra]] is
\[
\Omega_B=\sum_i X_iX^i\in U(\mathfrak g).
\]
\(\Omega_B\) is independent of the chosen dual bases and belongs to
[[lie-groups/center-of-universal-enveloping-algebra|the center of
\(U(\mathfrak g)\)]]. If a representation \(d\pi\) of \(\mathfrak g\) is
extended to \(U(\mathfrak g)\), then \(d\pi(\Omega_B)\) is its **Casimir
operator**.

## Centrality and normalization

The invariance of \(B\) makes the tensor corresponding to the identity map on \(\mathfrak g\) invariant under the adjoint action; multiplication into \(U(\mathfrak g)\) therefore makes \(\Omega_B\) central. Replacing \(B\) by \(cB\) replaces \(\Omega_B\) by \(c^{-1}\Omega_B\), so numerical Casimir eigenvalues depend on the normalization of the invariant form.

## Action in representations

Because the Casimir operator commutes with the \(\mathfrak g\)-action, it is a module endomorphism. On an irreducible complex representation in a setting where [[algebra-representation-theory/schurs-lemma|Schur's lemma]] gives scalar endomorphisms, it acts by a scalar. For highest-weight modules this scalar can be computed from the [[lie-groups/highest-weight|highest weight]] and the half-sum of [[lie-groups/positive-root|positive roots]]; the formula changes with the normalization of \(B\).

## Conventions and scope

For a real semisimple Lie algebra, one often forms the element after complexifying \(\mathfrak g\). More generally, any nondegenerate invariant symmetric [[linear-algebra/bilinear-form|bilinear form]] produces a quadratic Casimir element by the same construction. “Casimir invariant” may also refer to the scalar eigenvalue or to higher-degree central elements, so it is not always synonymous with this quadratic element.

## References

1. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002. [DOI record](https://doi.org/10.1007/978-1-4757-2453-0). Relevant: Chapter V, §5 on the center and Casimir element.
2. Jacques Dixmier, *Enveloping Algebras*, Graduate Studies in Mathematics 11, American Mathematical Society, 1996. [DOI record](https://doi.org/10.1090/gsm/011). Relevant: Chapters 2 and 7 on enveloping algebras and their centers.
