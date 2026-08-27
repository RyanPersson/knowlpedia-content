+++
id = "complex-analysis/octonionic-affine-line"
title = "Affine octonionic line"
kind = "definition"
summary = "A translate in the octonionic plane of an eight-dimensional direction parametrized by the octonionic projective line."
aliases = ["octonionic line in O^2", "affine Cayley line", "AOP^1 line"]
domains = ["complex-analysis", "octonionic-analysis", "differential-geometry"]
section_mode = "progressive"
+++

An **affine octonionic line** in \(\mathbb O^2\) is a translate of one of the
eight-dimensional real linear subspaces parametrized by
[[differential-geometry/octonionic-projective-line|
\(\mathbb OP^1\)]]. The space of all such affine lines is denoted
\(\mathcal A\mathbb OP^1\).

## Symmetry

The [[algebra-groups/semidirect-product|semidirect product]]
\[
\mathbb O^2\rtimes\operatorname{Spin}(9)
\]
acts transitively on \(\mathcal A\mathbb OP^1\): translations move the affine
base point, while the [[lie-groups/spin9-spin-representation|spin action]]
rotates the octonionic direction.

## Analytic role

Affine octonionic lines are the test subspaces in the definition of an
[[complex-analysis/octonionic-plurisubharmonic-function|octonionic
plurisubharmonic function]]. They also form the integration family for the
[[complex-analysis/octonionic-radon-transform|octonionic Radon transform]].

## Nonassociativity warning

An octonionic line should not be treated naively as a free rank-one submodule
of \(\mathbb O^2\): scalar multiplication over \(\mathbb O\) is not
associative. The projective-line construction supplies the well-defined
eight-dimensional real subspaces needed here.

## References

1. Semyon Alesker, “Plurisubharmonic functions on the octonionic plane and \(\operatorname{Spin}(9)\)-invariant valuations on convex sets,” *Journal of Geometric Analysis* 18 (2008), 651–686. [arXiv record](https://arxiv.org/abs/0707.4385). Relevant: §§1.3 and 2.
