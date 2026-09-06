+++
id = "operator-algebras/reduced-group-cstar-algebra"
title = "Reduced group C*-algebra"
kind = "definition"
summary = "The operator-norm closure of the integrated left regular representation of a locally compact group."
aliases = ["regular group C*-algebra", "C_r*(G)"]
domains = ["operator-algebras", "harmonic-analysis"]
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/regular-representations-locally-compact-group", "harmonic-analysis/l1-group-algebra", "algebra-representation-theory/regular-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] and let
\(\lambda:G\to\mathcal U(L^2(G))\) be its
[[harmonic-analysis/regular-representations-locally-compact-group|left regular
representation]]. Integrating \(\lambda\) gives a \(*\)-representation of the
[[harmonic-analysis/l1-group-algebra|group convolution algebra]]
\(L^1(G)\) on \(L^2(G)\). The **reduced group \(C^*\)-algebra** is
\[
C_r^*(G)=\overline{\lambda(L^1(G))}^{\,\|\cdot\|}
\subseteq\mathcal B(L^2(G)).
\]
Equivalently, it is the completion of \(L^1(G)\) after quotienting by the
kernel of \(\lambda\) and using the reduced norm
\(\|f\|_r=\|\lambda(f)\|\). The construction therefore records exactly the
part of the group convolution algebra visible in the [[algebra-representation-theory/regular-representation|regular representation]].

## Discrete groups

If \(G\) is discrete, \(L^2(G)=\ell^2(G)\) and
\[
\lambda_s\delta_t=\delta_{st}.
\]
Then \(C_r^*(G)\) is the norm closure of the finite sums
\(\sum_{s\in G}a_s\lambda_s\). It is unital, with unit
\(\lambda_e\). For a nondiscrete locally compact group the Dirac mass at \(e\)
does not lie in \(L^1(G)\), and the reduced group \(C^*\)-algebra is generally
nonunital; in fact it is unital exactly when \(G\) is discrete.

## Relation to the full completion

The reduced norm is [[real-analysis/bounded-above|bounded above]] by the universal group \(C^*\)-norm, so
there is a canonical surjective \(*\)-homomorphism from
[[operator-algebras/full-group-cstar-algebra|\(C^*(G)\)]] onto the reduced
completion:
\[
C^*(G)\longrightarrow C_r^*(G).
\]
This map need not be injective. Its being an isomorphism is equivalent to
[[harmonic-analysis/amenable-locally-compact-group|amenability of \(G\)]], a
fact that separates regular-representation data from the totality of
unitary-representation data.

## Abelian and geometric perspectives

For a locally compact [[algebra-groups/abelian-group|abelian group]], the Fourier transform identifies
\(C_r^*(G)\) with \(C_0(\widehat G)\), where \(\widehat G\) is the
[[harmonic-analysis/pontryagin-dual|Pontryagin dual]], and the full and
reduced completions coincide. For general groups, properties of
\(C_r^*(G)\)—such as simplicity, exactness, and the existence of
traces—encode rigidity, approximation, and dynamical features of \(G\).
These properties are not determined merely by the abstract [[linear-algebra/vector-space|vector space]]
\(L^1(G)\); the reduced [[linear-algebra/operator-norm|operator norm]] is essential.

## References

1. Nathanial P. Brown and Narutaka Ozawa, *C*-Algebras and Finite-Dimensional Approximations*, American Mathematical Society, 2008. [DOI record](https://doi.org/10.1090/gsm/088). Relevant: Chapter 2 and Appendix D on reduced group \(C^*\)-algebras and amenability.
2. Dana P. Williams, *Crossed Products of C*-Algebras*, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: §2 on full and reduced group \(C^*\)-algebras.
