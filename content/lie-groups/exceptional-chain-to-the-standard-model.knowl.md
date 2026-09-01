+++
id = "lie-groups/exceptional-chain-to-the-standard-model"
title = "Exceptional chain to the Standard Model Lie algebra"
kind = "construction"
summary = "A chain of regular semisimple subalgebras obtained by deleting simple roots, terminating in the semisimple part of the Standard Model Lie algebra."
aliases = ["exceptional chain to gSM", "E7 E6 D5 A4 A2+A1 chain", "en chain to the Standard Model"]
domains = ["lie-groups", "mathematical-physics"]
prerequisites = ["lie-groups/cartan-subalgebra", "lie-groups/simple-root", "lie-groups/removing-a-simple-root", "lie-groups/regular-lie-subalgebra", "lie-groups/maximal-levi-subalgebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For a compatible choice of [[lie-groups/cartan-subalgebra|Cartan subalgebra]] and [[lie-groups/simple-root|simple roots]] in \(\mathfrak e_7\), repeated [[lie-groups/removing-a-simple-root|simple-root removal]] gives a chain of [[lie-groups/regular-lie-subalgebra|regular semisimple Lie subalgebras]]
\[
\mathfrak{sl}_3\oplus\mathfrak{sl}_2
\subset \mathfrak{sl}_5
\subset \mathfrak{so}_{10}
\subset \mathfrak e_6
\subset \mathfrak e_7.
\]
Equivalently, its root-system types are
\[
A_2+A_1\subset A_4\subset D_5\subset E_6\subset E_7.
\]
Inside the \(A_4\) stage, delete the node that leaves \(A_2+A_1\) but retain the full \(A_4\) Cartan. This produces the [[lie-groups/maximal-levi-subalgebra|maximal Levi subalgebra]]
\[
(\mathfrak{sl}_3\oplus\mathfrak{sl}_2)\oplus\mathbb C
\cong \mathfrak g_{\mathrm{SM}}.
\]

Every displayed inclusion is a Lie-algebra inclusion. This chain is not a direct-sum decomposition of \(\mathfrak e_7\).

## Root-system construction

Given simple roots \(\alpha_1,\ldots,\alpha_n\), retain the roots in the integer span of \(\alpha_1,\ldots,\alpha_{n-1}\) and the corresponding smaller Cartan subspace. Iterating the operation along the selected \(E_7\) diagram produces the [[lie-groups/exceptional-e-root-systems|exceptional \(E_n\) chain]]
\[
E_7\supset E_6\supset E_5=D_5\supset E_4=A_4\supset E_3=A_2+A_1.
\]
The last equality is an equality of root-system types and hence of the associated complex [[lie-groups/semisimple-lie-algebra|semisimple Lie algebras]].

## Role in the E7 construction

The chain supplies a concrete [[lie-groups/good-standard-model-embedding-in-e7|good embedding]] of \(\mathfrak g_{\mathrm{SM}}\) in \(\mathfrak e_7\). It also exhibits the familiar \(\mathfrak{sl}_5\), \(\mathfrak{so}_{10}\), and \(\mathfrak e_6\) enlargements in one regular-subalgebra framework.

## Dependence on choices

The literal embedded chain depends on a Cartan subalgebra, a simple-root system, and an ordering of the deleted nodes. Its automorphism class is the invariant relevant here. The abelian \(\mathbb C\) in \(\mathfrak g_{\mathrm{SM}}\) is a Levi-center direction; it is not an extra simple factor in the semisimple root-system chain.

## References

1. John C. Baez, “Three Generations in E7,” 2026, §2 and Table 2. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
2. E. B. Dynkin, “Semisimple Subalgebras of Semisimple Lie Algebras,” *American Mathematical Society Translations*, Series 2, 6 (1957), 111–244.
3. John C. Baez and John Huerta, “The Algebra of Grand Unified Theories,” *Bulletin of the American Mathematical Society* 47 (2010), 483–552. [arXiv:0904.1556](https://arxiv.org/abs/0904.1556).
