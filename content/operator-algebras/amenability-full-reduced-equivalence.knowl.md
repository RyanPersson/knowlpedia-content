+++
id = "operator-algebras/amenability-full-reduced-equivalence"
title = "Amenability and equality of full and reduced group C*-algebras"
kind = "theorem"
summary = "A locally compact group is amenable exactly when its canonical full-to-reduced group C*-algebra quotient is injective."
aliases = ["Hulanicki theorem", "amenability criterion by group C*-algebras"]
domains = ["operator-algebras", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]]. The following are equivalent:

1. \(G\) is [[harmonic-analysis/amenable-locally-compact-group|amenable]];
2. the canonical quotient
   \[
   q_G:C^*(G)\longrightarrow C_r^*(G)
   \]
   is injective, hence is an isomorphism; and
3. the full and reduced \(C^*\)-norms agree on \(C_c(G)\).

Here \(q_G\) is the [[operator-algebras/full-to-reduced-group-cstar-quotient|full-to-reduced group \(C^*\)-algebra quotient]] induced by the left regular representation. Thus the notation \(C^*(G)=C_r^*(G)\) is justified canonically precisely in the amenable case.

## Representation-theoretic form

Injectivity of \(q_G\) is equivalent to every unitary representation of \(G\) being weakly contained in the left [[algebra-representation-theory/regular-representation|regular representation]]. Amenability is also equivalent to weak containment of the trivial representation in the regular representation. Fell absorption then supplies the bridge from the latter condition to all representations. This formulation is often called Hulanicki's criterion.

## Consequences and examples

Every abelian, compact, or solvable locally compact group is amenable, so its full and reduced group \(C^*\)-algebras coincide. By contrast, a nonabelian free group on finitely many generators is nonamenable, and its canonical quotient has nonzero kernel. Equality concerns the two completions of the same convolution \(*\)-algebra; it does not assert that either completion is commutative.

## Hypotheses and scope

The theorem holds for locally compact groups, with a choice of [[harmonic-analysis/haar-measure|Haar measure]] used to present \(C_c(G)\); the resulting completions and quotient are canonical up to the usual isomorphisms. For discrete groups the convolution algebra is the finitely supported group algebra. Analogous full-versus-reduced questions for groupoids, crossed products, and [[operator-algebras/fell-bundle|Fell bundles]] require their own amenability hypotheses and are not automatic consequences of this theorem.

## References

1. A. Hulanicki, “Means and Følner condition on locally compact groups,” *Studia Mathematica* 27 (1966), 87–104. [EuDML record](https://eudml.org/doc/217185). Relevant: equivalences among invariant means, Følner conditions, and regular-representation criteria.
2. A. L. T. Paterson, *Amenability*, Mathematical Surveys and Monographs 29, American Mathematical Society, 1988. [AMS DOI record](https://doi.org/10.1090/surv/029). Relevant: Chapters 1 and 4 on amenable locally compact groups and weak containment.
