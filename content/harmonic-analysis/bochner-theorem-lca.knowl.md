+++
id = "harmonic-analysis/bochner-theorem-lca"
title = "Bochner's theorem for locally compact abelian groups"
kind = "theorem"
summary = "Bochner's theorem identifies continuous positive-definite functions on a locally compact abelian group with Fourier transforms of finite positive measures on its dual."
aliases = ["Bochner theorem", "positive-definite Fourier representation"]
domains = ["harmonic-analysis", "measure-theory"]
prerequisites = ["algebra-groups/abelian-group", "topology/locally-compact-group", "harmonic-analysis/pontryagin-dual", "harmonic-analysis/positive-definite-function", "probability/probability-measure"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be an [[algebra-groups/abelian-group|abelian]] [[topology/locally-compact-group|locally compact group]] and \(\widehat G\) its [[harmonic-analysis/pontryagin-dual|Pontryagin dual]]. **Bochner's theorem** states that a function \(\varphi:G\to\mathbb C\) is continuous and [[harmonic-analysis/positive-definite-function|positive definite]] if and only if there is a unique finite positive regular Borel measure \(\nu\) on \(\widehat G\) such that
\[
\varphi(x)=\int_{\widehat G}\gamma(x)\,d\nu(\gamma)
\qquad (x\in G).
\]
Moreover, \(\nu(\widehat G)=\varphi(e)\). The unique \(\nu\) is called the representing measure of \(\varphi\); no Haar normalization is involved. Thus normalized positive-definite functions, characterized by \(\varphi(e)=1\), correspond exactly to [[probability/probability-measure|probability measures]] on \(\widehat G\).

## Why positivity appears

If \(\nu\) is positive, then for \(x_1,\ldots,x_n\in G\) and \(c_1,\ldots,c_n\in\mathbb C\),
\[
\sum_{i,j}c_i\overline{c_j}\varphi(x_j^{-1}x_i)
=
\int_{\widehat G}\left|\sum_i c_i\gamma(x_i)\right|^2\,d\nu(\gamma)\geq0.
\]
The converse is deeper: positive definiteness produces a cyclic unitary representation, and abelian spectral theory represents its cyclic coefficient by a measure.

## Standard examples

The constant function \(1\) corresponds to the point mass at the trivial character. Every character \(\gamma_0\) corresponds to \(\delta_{\gamma_0}\). On \(G=\mathbb R^n\), the theorem is the classical statement that every continuous positive-definite function is the Fourier transform of a finite positive measure.

A continuous function with \(\varphi(e)=1\) but a non-positive semidefinite coefficient matrix is a near miss: normalization alone does not produce a positive measure.

## Conventions and scope

**Warning.** With the Fourier convention \(\widehat\nu(x)=\int\overline{\gamma(x)}\,d\nu(\gamma)\), the representing formula contains \(\overline{\gamma(x)}\) instead. The two forms are interchanged by pushing \(\nu\) forward under \(\gamma\mapsto\gamma^{-1}\). Positivity of the measure, finiteness, and continuity of \(\varphi\) are essential parts of the theorem.

## References

1. Walter Rudin, *Fourier Analysis on Groups*, Wiley-Interscience, 1962. [Wiley DOI record](https://doi.org/10.1002/9781118165621). Relevant: Chapter 1, positive-definite functions and Bochner's theorem.
2. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Chapter 4, positive-definite functions on locally compact abelian groups.
