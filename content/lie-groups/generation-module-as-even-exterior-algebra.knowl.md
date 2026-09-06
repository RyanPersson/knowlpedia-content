+++
id = "lie-groups/generation-module-as-even-exterior-algebra"
title = "Generation module as an even exterior algebra"
kind = "theorem"
summary = "Adding two generation-root singlets to each 30-dimensional module gives Λeven C6, which restricts to ΛC5 and hence one full Standard Model generation."
aliases = ["32-dimensional generation module in e7", "generation module Lambda even C6", "V k generation module"]
domains = ["lie-groups", "representation-theory", "mathematical-physics"]
section_mode = "progressive"
prerequisites = ["lie-groups/even-and-odd-exterior-algebra", "linear-algebra/vector-space", "lie-groups/lie-subalgebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\Phi_k=\{r\in\Phi(E_7):\pi(r)=\pm w_k\}\) be the projection class from the [[lie-groups/e7-root-projection-trichotomy|E7 root-projection trichotomy]]. For \(k=1,2,3\), define the \(32\)-dimensional subspace
\[
V_k:=
\bigoplus_{r\in\{\pm\beta_k\}\sqcup\Phi_k}
(\mathfrak e_7)_r.
\]
Then \(V_k\) is an \(\mathfrak{sl}_6^{\mathrm{SM}}\)-submodule of the adjoint \(\mathfrak e_7\)-module, and
\[
V_k\cong
\Lambda^0\mathbb C^6
\oplus\Lambda^2\mathbb C^6
\oplus\Lambda^4\mathbb C^6
\oplus\Lambda^6\mathbb C^6
=\Lambda^{\mathrm{even}}\mathbb C^6,
\]
the [[lie-groups/even-and-odd-exterior-algebra|even exterior algebra]] of the defining module.

## Scope of the identification

This is an isomorphism of modules and [[linear-algebra/vector-space|vector spaces]]. The subspace \(V_k\) is not generally a [[lie-groups/lie-subalgebra|Lie subalgebra]] of \(\mathfrak e_7\).

## Restriction to sl5 and the Standard Model

For \(\mathbb C^6\cong\mathbb C^5\oplus\mathbb C\) as \(\mathfrak{sl}_5^{\mathrm{SM}}\)-modules, the [[lie-groups/exterior-algebra-of-a-direct-sum|direct-sum exterior-algebra formula]] gives
\[
\Lambda^{\mathrm{even}}(\mathbb C^5\oplus\mathbb C)
\cong
\Lambda^{\mathrm{even}}\mathbb C^5
\oplus
\Lambda^{\mathrm{odd}}\mathbb C^5
=\Lambda\mathbb C^5.
\]
Consequently \(V_k\cong\Lambda\mathbb C^5\) as an \(\mathfrak{sl}_5^{\mathrm{SM}}\)-module, and its restriction to \(\mathfrak g_{\mathrm{SM}}\) is the [[mathematical-physics/standard-model-exterior-algebra-representation|full one-generation Standard Model representation]].

## The two added singlets

The [[lie-groups/root-space|root spaces]] \((\mathfrak e_7)_{\pm\beta_k}\) commute with \(\mathfrak{sl}_6^{\mathrm{SM}}\), so they supply the trivial modules \(\Lambda^0\mathbb C^6\) and \(\Lambda^6\mathbb C^6\). Under \(\mathfrak g_{\mathrm{SM}}\) they model the [[mathematical-physics/right-handed-neutrino-gauge-singlet|right-handed neutrino gauge singlet]] and its antiparticle, completing the [[lie-groups/thirty-dimensional-generation-module-in-e7|30-dimensional module]].

## Dependence on choices and conventions

The spaces \(V_k\) require a compatible [[lie-groups/cartan-subalgebra|Cartan subalgebra]] and a labeling of the three root lines. Exchanging \(\beta_k\) with \(-\beta_k\) preserves \(V_k\) but swaps the two singlet root spaces and hence the conventional degree-zero/degree-six assignment. Particle and antiparticle labels are likewise conventional; the module isomorphism is the invariant statement.

## References

1. John C. Baez, “Three Generations in E7,” 2026, Theorem 12. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
2. John C. Baez and John Huerta, “The Algebra of Grand Unified Theories,” *Bulletin of the American Mathematical Society* 47 (2010), 483–552. [arXiv:0904.1556](https://arxiv.org/abs/0904.1556).
3. Benjamin Nasmith, “An Exceptional Combinatorial Sequence and Standard Model Particles,” 2020. [arXiv:2012.03933](https://arxiv.org/abs/2012.03933).
