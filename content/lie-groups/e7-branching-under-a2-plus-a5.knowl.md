+++
id = "lie-groups/e7-branching-under-a2-plus-a5"
title = "E7 branching under A2 + A5"
kind = "theorem"
summary = "The adjoint E7 module branches under the mutually centralizing generation sl3 and standard sl6 as 8 + 35 + (3⊗15) + (3*⊗15*)."
aliases = ["E7 to A2 A5 branching", "e7 under sl3 plus sl6", "133 branching to 8 35 45 45"]
domains = ["lie-groups", "representation-theory", "mathematical-physics"]
prerequisites = ["lie-groups/branching-rule-for-lie-representations"]
dependency_review_count = 1
section_mode = "progressive"
+++

For the maximal mutually centralizing subalgebra
\[
\mathfrak{sl}_3^{\mathrm{gen}}
\oplus\mathfrak{sl}_6^{\mathrm{SM}}
\subset\mathfrak e_7,
\]
the adjoint representation has the [[lie-groups/branching-rule-for-lie-representations|branching rule]]
\[
\mathbf{133}\;\downarrow_{A_2+A_5}
=(\mathbf8,\mathbf1)
\oplus(\mathbf1,\mathbf{35})
\oplus(\mathbf3,\mathbf{15})
\oplus(\mathbf3^*,\mathbf{15}^*).
\]
Equivalently, as a module for \(\mathfrak{sl}_3^{\mathrm{gen}}\oplus\mathfrak{sl}_6^{\mathrm{SM}}\),
\[
\mathfrak e_7
\cong\mathfrak{sl}_3^{\mathrm{gen}}
\oplus\mathfrak{sl}_6^{\mathrm{SM}}
\oplus(\mathbf3\otimes\mathbf{15})
\oplus(\mathbf3^*\otimes\mathbf{15}^*).
\]

## What the decomposition means

This is a decomposition of the adjoint module and of the underlying [[linear-algebra/vector-space|vector space]]. The first two terms together form the [[lie-groups/lie-subalgebra|Lie subalgebra]]
\(\mathfrak{sl}_3^{\mathrm{gen}}\oplus\mathfrak{sl}_6^{\mathrm{SM}}\). The two \(45\)-dimensional tensor-product summands are irreducible modules; they are not asserted to be Lie subalgebras.

## Identification of the 15s

After choosing highest-weight conventions for [[lie-groups/complex-lie-algebra-sl6|\(\mathfrak{sl}_6\)]], one may take
\[
\mathbf{15}=\Lambda^2\mathbb C^6,
\qquad
\mathbf{15}^*=\Lambda^4\mathbb C^6.
\]
Under the standard \(\mathfrak{sl}_5\), these restrict to complementary pairs among
\(\Lambda^1\mathbb C^5,\ldots,\Lambda^4\mathbb C^5\), producing the three unlabeled generation modules without neutrino singlets.

## Choice independence

Unlike a decomposition into individually labeled generation spaces, this branching rule requires only the chosen good embedded \(\mathfrak g_{\mathrm{SM}}\): its generation \(\mathfrak{sl}_3\) and standard \(\mathfrak{sl}_6\) are intrinsic centralizers. [[lie-groups/dynkin-diagram-automorphisms-and-dual-representations|Diagram automorphisms]] exchange
\(\mathbf3\leftrightarrow\mathbf3^*\) and
\(\mathbf{15}\leftrightarrow\mathbf{15}^*\), so the naming of either dual pair is conventional while the paired decomposition is invariant.

## References

1. John C. Baez, “Three Generations in E7,” 2026, Theorem 11. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
2. R. Slansky, “Group Theory for Unified Model Building,” *Physics Reports* 79 (1981), 1–128, Table 52. [DOI record](https://doi.org/10.1016/0370-1573(81)90092-2).
3. E. B. Dynkin, “Semisimple Subalgebras of Semisimple Lie Algebras,” *American Mathematical Society Translations*, Series 2, 6 (1957), 111–244.
