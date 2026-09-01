+++
id = "harmonic-analysis/amenability-trivial-representation-weak-containment"
title = "Amenability via weak containment of the trivial representation"
kind = "definition"
summary = "The representation-theoretic criterion that a locally compact group is amenable exactly when its regular representation weakly contains the trivial representation."
aliases = ["Hulanicki-Reiter criterion"]
domains = ["harmonic-analysis", "operator-algebras"]
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/regular-representations-locally-compact-group", "harmonic-analysis/weak-containment-unitary-representations", "algebra-representation-theory/regular-representation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]], let \(1_G\) denote its one-dimensional trivial unitary representation, and let \(\lambda_G\) be its left [[harmonic-analysis/regular-representations-locally-compact-group|regular representation]] on \(L^2(G)\). The **Hulanicki–Reiter criterion** states that
\[
G\text{ is amenable}\quad\Longleftrightarrow\quad
1_G\prec\lambda_G,
\]
where \(\prec\) denotes [[harmonic-analysis/weak-containment-unitary-representations|weak containment]]. Equivalently, there is a net of unit vectors \(\xi_i\in L^2(G)\) such that
\[
\sup_{g\in C}\lVert\lambda_G(g)\xi_i-\xi_i\rVert_2\longrightarrow0
\]
for every compact \(C\subseteq G\). Thus amenability is detected by almost invariant vectors in the [[algebra-representation-theory/regular-representation|regular representation]].

## Why the formulations agree

The almost-invariant-vector condition says that the constant coefficient \(1\) of \(1_G\) is uniformly approximated on [[topology/compact-set|compact sets]] by positive-definite coefficients of \(\lambda_G\), which is precisely weak containment for the trivial representation. Squaring [[real-analysis/absolute-value|absolute values]], \(\lvert\xi_i\rvert^2\), turns such vectors into approximately invariant \(L^1\)-probability densities; conversely, taking square roots of Reiter \(P_1\) densities yields almost invariant \(L^2\)-vectors. This is the Hulanicki–Reiter bridge between representation theory and [[harmonic-analysis/amenable-locally-compact-group|invariant-mean amenability]].

## Operator-algebraic consequence

Weak containment \(\pi\prec\sigma\) is equivalent to the associated [[harmonic-analysis/integrated-form-unitary-representation|integrated representations]] satisfying \(\ker\sigma\subseteq\ker\pi\) on the full group \(C^*\)-algebra. Applied to \(1_G\) and \(\lambda_G\), the criterion identifies amenability with continuity of the trivial representation for the reduced group-\(C^*\)-norm. This is one route to the equality of full and reduced group \(C^*\)-algebras for amenable groups.

## Examples and scope

For an abelian locally compact group, normalized functions supported on increasingly invariant sets provide the required almost invariant vectors. For the [[algebra-groups/free-group|free group]] on two generators, the trivial representation is not weakly contained in the regular representation. The criterion concerns the regular representation itself; weak containment in an arbitrary representation is not a definition of amenability.

## References

1. Bachir Bekka, Pierre de la Harpe, and Alain Valette, *Kazhdan's Property (T)*, Cambridge University Press, 2008. [Appendix G DOI record](https://doi.org/10.1017/CBO9780511542749.015). Relevant: §G.3 on weak containment and amenability.
2. Alan L. T. Paterson, *Amenability*, Mathematical Surveys and Monographs 29, American Mathematical Society, 1988. [AMS DOI record](https://doi.org/10.1090/surv/029). Relevant: Reiter conditions and amenability of locally compact groups.
