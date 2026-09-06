+++
id = "lie-groups/three-d6-subsystems-in-e7"
title = "Three D6 subsystems in E7"
kind = "theorem"
summary = "Each of the three generation root lines has a 60-root orthogonal complement of type D6, yielding a copy of so12 in e7."
aliases = ["three so12 subalgebras in e7", "D6 subsystem orthogonal to generation root", "so12 beta k"]
domains = ["lie-groups", "mathematical-physics"]
prerequisites = ["lie-groups/generation-sl2-subalgebras", "lie-groups/root-subsystem", "lie-groups/type-d-root-system", "lie-groups/regular-lie-subalgebra", "lie-groups/complex-lie-algebra-so12"]
dependency_review_count = 1
section_mode = "progressive"
+++

Use the generation-plane partition
\(\Phi=A\sqcup\Phi_0\sqcup\Phi_1\sqcup\Phi_2\sqcup\Phi_3\) and roots \(\pm\beta_k\) defining the three [[lie-groups/generation-sl2-subalgebras|generation \(\mathfrak{sl}_2\)'s]]. For each \(k\),
\[
\{r\in\Phi:r\perp\beta_k\}=\Phi_0\sqcup\Phi_k
\]
is a rank-six [[lie-groups/root-subsystem|root subsystem]] with \(60\) roots, hence is of [[lie-groups/type-d-root-system|type \(D_6\)]]. Its [[lie-groups/regular-lie-subalgebra|regular Lie subalgebra]] is denoted
\[
\mathfrak{so}_{12}(\beta_k)\subset\mathfrak e_7.
\]

The three \(D_6\) subsystems, and therefore the three embedded copies of [[lie-groups/complex-lie-algebra-so12|\(\mathfrak{so}_{12}(\mathbb C)\)]], are distinct.

## Orthogonality test

Projection to the [[lie-groups/generation-plane|generation plane]] reduces the condition \(r\perp\beta_k\) to \(\pi(r)\perp\beta_k\). In the [[lie-groups/e7-root-projection-trichotomy|projection trichotomy]], zero and \(\pm w_k\) are orthogonal to \(\beta_k\); the other four defining weights and all six \(A_2\) roots are not. This gives exactly \(\Phi_0\sqcup\Phi_k\).

## Centralizer statement

The regular subalgebras
\[
\mathfrak{sl}_2(\beta_k)
\quad\text{and}\quad
\mathfrak{so}_{12}(\beta_k)
\]
are mutual centralizers in \(\mathfrak e_7\). Their sum is therefore a [[lie-groups/maximal-rank-lie-subalgebra|maximal-rank]] embedded [[lie-groups/lie-subalgebra|Lie subalgebra]] of type \(A_1+D_6\). The associated [[lie-groups/e7-branching-under-a1-plus-d6|branching rule]] describes the complementary \(64\)-dimensional module.

## Dependence on choices

The unordered triple depends on a Cartan choice in \(\mathfrak{sl}_3^{\mathrm{gen}}\); labels depend on an ordering of its three root lines. The notation \(\mathfrak{so}_{12}(\beta_k)\) is insensitive to changing \(\beta_k\) to \(-\beta_k\).

## References

1. John C. Baez, “Three Generations in E7,” 2026, Lemma 4 and Proposition 5. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
2. E. B. Dynkin, “Semisimple Subalgebras of Semisimple Lie Algebras,” *American Mathematical Society Translations*, Series 2, 6 (1957), 111–244.
