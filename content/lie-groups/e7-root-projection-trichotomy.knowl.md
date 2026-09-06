+++
id = "lie-groups/e7-root-projection-trichotomy"
title = "E7 root-projection trichotomy"
kind = "theorem"
summary = "Projection of an E7 root to the generation plane is zero, a defining A2 weight up to sign, or a generation A2 root."
aliases = ["root projection trichotomy in E7", "generation-plane projection lemma"]
domains = ["lie-groups", "mathematical-physics"]
prerequisites = ["lie-groups/root-system", "lie-groups/generation-sl3-in-e7", "linear-algebra/orthogonal-projection"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\Phi\subset V\) be the \(E_7\) [[lie-groups/root-system|root system]], let \(A\subset\Phi\) be the \(A_2\) root system of the [[lie-groups/generation-sl3-in-e7|generation \(\mathfrak{sl}_3\)]], let \(P=\operatorname{span}_{\mathbb R}A\), and let \(\pi:V\to P\) be [[linear-algebra/orthogonal-projection|orthogonal projection]]. If \(w_1,w_2,w_3\) are the defining \(A_2\) weights, then every \(r\in\Phi\) satisfies
\[
\pi(r)\in
\{0\}\;\sqcup\;
\{\pm w_1,\pm w_2,\pm w_3\}\;\sqcup\;A.
\]
Moreover,
\[
\pi(r)\in A\quad\Longleftrightarrow\quad r\in A.
\]

## Why only these projections occur

For every \(\delta\in A\), integrality of Cartan integers gives
\(\langle\pi(r),\delta\rangle=\langle r,\delta\rangle\in\mathbb Z\). Hence \(\pi(r)\) lies in the [[lie-groups/weight-lattice|\(A_2\) weight lattice]]. With \(E_7\) roots normalized to squared length \(2\), orthogonal projection gives
\(\lVert\pi(r)\rVert^2\le 2\). The weight-lattice vectors within this bound are precisely zero, the six vectors \(\pm w_i\) of squared length \(2/3\), and the six roots of squared length \(2\).

Equality of lengths forces \(r=\pi(r)\in P\). The only rank-two [[lie-groups/simply-laced-root-system|simply laced]] [[lie-groups/root-subsystem|root subsystem]] containing \(A_2\) is \(A_2\), proving the final equivalence.

## The induced partition

Define
\[
\Phi_0=\{r\in\Phi:\pi(r)=0\},
\qquad
\Phi_k=\{r\in\Phi:\pi(r)=\pm w_k\}.
\]
Then
\[
\Phi=A\sqcup\Phi_0\sqcup\Phi_1\sqcup\Phi_2\sqcup\Phi_3,
\]
with \(|\Phi_0|=|\Phi_1|=|\Phi_2|=|\Phi_3|=30\). The set \(\Phi_0\) is an \(A_5\) root subsystem; the sets \(\Phi_k\) are not root systems but index the [[lie-groups/thirty-dimensional-generation-module-in-e7|30-dimensional generation modules]].

## Dependence on choices

The trichotomy is valid for any compatible generation-plane choice. The sets \(\Phi_k\) are permuted when the weights \(w_k\) are relabeled; no ordering of the three sets is intrinsic to the good Standard Model embedding alone.

## References

1. John C. Baez, “Three Generations in E7,” 2026, Lemmas 2–3. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
2. Benjamin Nasmith, “An Exceptional Combinatorial Sequence and Standard Model Particles,” 2020, Lemma 2.1. [arXiv:2012.03933](https://arxiv.org/abs/2012.03933).
3. P. J. Cameron, J. M. Goethals, J. J. Seidel, and E. E. Shult, “Line Graphs, Root Systems, and Elliptic Geometry,” *Journal of Algebra* 43 (1976), 305–327. [DOI record](https://doi.org/10.1016/0021-8693(76)90162-9).
