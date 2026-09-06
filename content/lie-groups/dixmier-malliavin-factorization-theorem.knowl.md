+++
id = "lie-groups/dixmier-malliavin-factorization-theorem"
title = "Dixmier–Malliavin factorization theorem"
kind = "theorem"
summary = "Every compactly supported smooth function on a Lie group is a finite sum of convolutions of such functions, and every smooth representation vector is a finite sum of smoothed vectors."
aliases = ["smooth-vector factorization theorem", "Dixmier–Malliavin theorem"]
domains = ["lie-groups", "harmonic-analysis", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group", "harmonic-analysis/convolution-on-locally-compact-group", "functional-analysis/frechet-space", "lie-groups/garding-subspace"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a finite-dimensional [[fiber-bundles/lie-group|Lie group]]. The **Dixmier–Malliavin factorization theorem** states that every \(f\in C_c^\infty(G)\) is a finite sum of [[harmonic-analysis/convolution-on-locally-compact-group|convolutions]]:
\[
f=\sum_{j=1}^{N}a_j*b_j,\qquad a_j,b_j\in C_c^\infty(G).
\]
Consequently, if \(G\) acts continuously on a [[functional-analysis/frechet-space|Fréchet space]] \(E\), every smooth vector is a finite sum
\[
v=\sum_{j=1}^{N}\pi(f_j)v_j
\]
with \(f_j\in C_c^\infty(G)\) and \(v_j\in E\). Hence the smooth-vector space equals the [[lie-groups/garding-subspace|Gårding subspace]], not merely its closure.

## Support control

The function factorization is local in one factor: a neighborhood \(U\) of the identity may be fixed in advance and the factors chosen so that one factor in each convolution has support in \(U\), while the other has support controlled by that of \(f\). This strengthened statement is Theorem 3.1 of the original paper.

## From functions to vectors

The vector form is a direct part of the Dixmier–Malliavin theorem: the
smooth vectors of a continuous Fréchet representation are the finite sums
of vectors \(\pi(f)w\), with \(f\in C_c^\infty(G)\) and \(w\in E\).
It does not require an individual compactly supported \(f\) satisfying
\(\pi(f)v=v\), which need not exist. Associativity for the
[[harmonic-analysis/integrated-operator-continuous-representation|integrated
operator]], \(\pi(a*b)=\pi(a)\pi(b)\), is compatible with factorization once
the vector theorem has been established. In a unitary representation it gives
\[
\mathcal H^\infty=\operatorname{span}\{\pi(f)w:f\in C_c^\infty(G),\ w\in\mathcal H\}.
\]

## Distinction from density

Gårding's argument only shows that smoothed vectors form a dense smooth subspace. Dixmier–Malliavin identifies every smooth vector as a finite algebraic sum of smoothed vectors. It does not assert that every test function is a single convolution; finite sums are indispensable in general.

## References

1. Jacques Dixmier and Paul Malliavin, *Factorisations de fonctions et de vecteurs indéfiniment différentiables*, Bulletin des Sciences Mathématiques 102 (1978), 307–330. [Academic-hosted scan](https://www.math.ubc.ca/~cass/research/pdf/Dixmier-Malliavin.pdf). Relevant: Theorem 3.1 and the representation-vector consequences.
2. Michael D. Francis, *A Dixmier–Malliavin theorem for Lie groupoids*, Journal of Lie Theory 32 (2022), 879–898. [Publisher record](https://www.heldermann.de/JLT/JLT32/JLT323/jlt32041.htm). Relevant: Theorem 1.1 restates the classical Lie-group theorem with support control.
