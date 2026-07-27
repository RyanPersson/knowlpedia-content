+++
id = "operator-algebras/dual-action-von-neumann-crossed-product"
title = "Dual action on a von Neumann crossed product"
kind = "definition"
summary = "The canonical action of the dual group on a von Neumann crossed product by an abelian group."
aliases = ["von Neumann dual action", "W*-crossed-product dual action"]
domains = ["operator-algebras", "harmonic-analysis", "dynamical-systems"]
section_mode = "progressive"
+++

Let an [[topology/locally-compact-group|abelian locally compact group]] \(G\)
act point-ultraweakly continuously on a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\) by
\(\alpha\). The **dual action** on the
[[operator-algebras/von-neumann-crossed-product|von Neumann crossed product]]
is the point-ultraweakly continuous action of the
[[harmonic-analysis/pontryagin-dual|Pontryagin dual]] \(\widehat G\)
\[
\widehat\alpha:\widehat G\longrightarrow
\operatorname{Aut}(M\rtimes_\alpha G)
\]
determined by
\[
\widehat\alpha_\chi(\pi_\alpha(x))=\pi_\alpha(x),\qquad
\widehat\alpha_\chi(\lambda(t))
=\overline{\chi(t)}\,\lambda(t).
\]
Thus it fixes the coefficient algebra pointwise and multiplies the canonical
group unitary of \(t\) by its Fourier character.

## Existence and uniqueness

The displayed assignments preserve the covariance relation and therefore
extend from integrated covariant operators to normal automorphisms of the
generated von Neumann algebra. Character multiplication gives an action, and
ultraweak density of the integrated core gives uniqueness. When
\(G=\mathbb R\) and \(\chi_s(t)=e^{ist}\), the convention above reads
\(\widehat\alpha_s(\lambda(t))=e^{-ist}\lambda(t)\).

## Duality

Crossing again by \(\widehat G\) recovers \(M\), stabilized by
\(\mathcal B(L^2(G))\), through Takesaki duality. The corresponding
double-dual action remembers the original action up to the standard inner
correction. This makes the dual action structural data rather than an
arbitrary symmetry of the crossed product
[Nakagami–Takesaki, Chapters 1–2](https://doi.org/10.1007/BFb0069742).

## Relation to other dual actions

The formula resembles the
[[operator-algebras/dual-action-crossed-product|dual action on a
\(C^*\)-crossed product]], but the topology and ambient algebra differ:
point-ultraweak continuity and normal automorphisms are used here. For
nonabelian \(G\), the replacement is generally a dual coaction rather than an
action of a Pontryagin dual group.

## References

1. Yoshiomi Nakagami and Masamichi Takesaki, *Duality for Crossed Products of von Neumann Algebras*, Lecture Notes in Mathematics 731, Springer, 1979. [Publisher DOI record](https://doi.org/10.1007/BFb0069742). Relevant: Chapters 1–2 on actions, coactions, crossed products, and duality.
2. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [Publisher DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: Chapter X on dual actions and Takesaki duality.
