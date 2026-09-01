+++
id = "lie-groups/standard-sl6-in-e7"
title = "Standard sl6 in e7"
kind = "theorem"
summary = "The centralizer of the generation sl3 in e7 is a distinguished sl6, and the two subalgebras are mutual centralizers."
aliases = ["standard sl6", "Standard Model sl6 in e7", "sl6 SM"]
domains = ["lie-groups", "mathematical-physics"]
prerequisites = ["lie-groups/good-standard-model-embedding-in-e7", "lie-groups/generation-sl3-in-e7", "lie-groups/mutual-centralizers-in-a-lie-algebra", "lie-groups/maximal-lie-subalgebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Fix a [[lie-groups/good-standard-model-embedding-in-e7|good embedded]] \(\mathfrak g_{\mathrm{SM}}\subset\mathfrak e_7\) and let \(\mathfrak{sl}_3^{\mathrm{gen}}\) be its [[lie-groups/generation-sl3-in-e7|generation \(\mathfrak{sl}_3\)]]. Then
\[
C_{\mathfrak e_7}(\mathfrak{sl}_3^{\mathrm{gen}})
\cong\mathfrak{sl}_6(\mathbb C).
\]
This embedded algebra is the **standard \(\mathfrak{sl}_6\)**, denoted \(\mathfrak{sl}_6^{\mathrm{SM}}\). Moreover,
\[
C_{\mathfrak e_7}(\mathfrak{sl}_6^{\mathrm{SM}})
=\mathfrak{sl}_3^{\mathrm{gen}},
\]
so the two are [[lie-groups/mutual-centralizers-in-a-lie-algebra|mutual centralizers]], and
\[
\mathfrak{sl}_3^{\mathrm{gen}}\oplus\mathfrak{sl}_6^{\mathrm{SM}}
\subset\mathfrak e_7
\]
is a [[lie-groups/maximal-lie-subalgebra|maximal embedded Lie subalgebra]] of type \(A_2+A_5\).

## Root-system description

For a compatible [[lie-groups/generation-plane|generation plane]] \(P\), let
\[
\Phi_0=\{r\in\Phi(E_7):r\perp P\}.
\]
The [[lie-groups/e7-root-projection-trichotomy|projection analysis]] shows that \(\Phi_0\) has rank \(5\) and \(30\) roots, hence is of [[lie-groups/type-a-root-system|type \(A_5\)]]. Its Cartan subspace is \(P^\perp\), so there is no additional abelian centralizer summand; the associated regular algebra is [[lie-groups/complex-lie-algebra-sl6|\(\mathfrak{sl}_6\)]].

## Intrinsic status

Although the root-system proof uses a compatible [[lie-groups/cartan-subalgebra|Cartan subalgebra]], \(\mathfrak{sl}_6^{\mathrm{SM}}\) is intrinsically characterized as the centralizer of \(\mathfrak{sl}_3^{\mathrm{gen}}\). Thus it depends only on the chosen good embedded Standard Model algebra, not on the later choice that labels three generation root lines.

## Branching

Restriction of the adjoint \(\mathfrak e_7\)-module to this maximal \(A_2+A_5\) subalgebra gives the [[lie-groups/e7-branching-under-a2-plus-a5|\(A_2+A_5\) branching rule]]. The direct sum \(\mathfrak{sl}_3^{\mathrm{gen}}\oplus\mathfrak{sl}_6^{\mathrm{SM}}\) is a Lie-algebra direct sum; the other branching summands are modules, not [[lie-groups/lie-subalgebra|Lie subalgebras]].

## References

1. John C. Baez, “Three Generations in E7,” 2026, Proposition 6. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
2. E. B. Dynkin, “Semisimple Subalgebras of Semisimple Lie Algebras,” *American Mathematical Society Translations*, Series 2, 6 (1957), 111–244, especially the maximal-subalgebra tables.
