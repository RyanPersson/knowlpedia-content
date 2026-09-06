+++
id = "differential-geometry/maslov-class-lagrangian-submanifold"
title = "Maslov class of a Lagrangian submanifold"
kind = "definition"
summary = "The pullback of the universal Maslov class along the Lagrangian Gauss map of a Lagrangian immersion."
aliases = ["Lagrangian Maslov class"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/symplectic-vector-space", "differential-geometry/lagrangian-gauss-map", "differential-geometry/maslov-class-lagrangian-grassmannian", "differential-geometry/symplectic-manifold"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(f:L^n\to(V^{2n},\omega)\) be a Lagrangian immersion into a real [[differential-geometry/symplectic-vector-space|symplectic vector space]]. Its **Maslov class** is
\[
\mu_L=\gamma_f^*\mu_\Lambda\in H^1(L;\mathbb Z),
\]
where \(\gamma_f:L\to\Lambda(V)\) is the [[differential-geometry/lagrangian-gauss-map|Lagrangian Gauss map]] and \(\mu_\Lambda\) is the [[differential-geometry/maslov-class-lagrangian-grassmannian|universal Maslov class]]. More generally, the same formula applies after choosing a symplectic trivialization of \(f^*TM\) for an immersion into a [[differential-geometry/symplectic-manifold|symplectic manifold]] \(M\), or after supplying equivalent Maslov-covering data. For a loop \(c:S^1\to L\), the integer \(\langle\mu_L,[c]\rangle\) is the Maslov index of the loop of tangent Lagrangian planes \(df_{c(t)}(T_{c(t)}L)\).

## Geometric interpretation

Fix a reference Lagrangian plane \(L_0\subset V\). For a generic immersion and loop, the Maslov number counts, with signs, the points where the tangent plane \(\gamma_f(c(t))\) fails to be transverse to \(L_0\). In other words, it is the intersection number of \(\gamma_f\circ c\) with the [[differential-geometry/maslov-cycle|Maslov cycle]]. This is the characteristic-class interpretation of the Maslov class.

## Examples

An affine Lagrangian plane has constant Gauss map, hence zero Maslov class. The [[fiber-bundles/zero-section|zero section]] in a [[fiber-bundles/cotangent-bundle|cotangent bundle]] likewise has zero class in its canonical local model. For a Lagrangian curve in \(\mathbb R^2\), the class records the winding of the unoriented tangent line: one positive half-turn of the tangent line evaluates to \(1\) under the normalization used here.

## Ambient-manifold caveat

For a general \((M,\omega)\), the canonical Gauss map is a section of the Lagrangian-Grassmannian bundle, not automatically a map to one fixed \(\Lambda(n)\). An integral grading obstruction can therefore depend on an ambient Maslov covering or on a trivialization such as one induced by a chosen squared canonical-volume form. Omitting this datum can make the phrase “the Maslov class in \(H^1(L;\mathbb Z)\)” ambiguous.

## Distinction from disk indices

The class \(\mu_L\) evaluates on loops in \(L\). The [[differential-geometry/maslov-index|Maslov index]] of a relative disk \(u:(D,\partial D)\to(M,L)\) instead measures the loop of Lagrangian boundary conditions \(T_{u(e^{it})}L\) after trivializing \(u^*TM\). It defines a homomorphism on \(\pi_2(M,L)\) and need not be determined by \(\mu_L\) alone in a nontrivial ambient manifold. These invariants agree only after the relevant trivializations and boundary-loop identifications are specified.

## References

1. V. I. Arnol'd, “On a characteristic class entering into conditions of quantization,” *Functional Analysis and Its Applications* 1 (1967), 1–14. [DOI record](https://doi.org/10.1007/BF01079201). Relevant: the Gauss-map definition of the Maslov characteristic class.
2. Paul Seidel, “Graded Lagrangian submanifolds,” *Bulletin de la Société Mathématique de France* 128 (2000), 103–149. [arXiv record](https://arxiv.org/abs/math/9903049). Relevant: §2, Maslov coverings, gradings, and their obstruction classes.
